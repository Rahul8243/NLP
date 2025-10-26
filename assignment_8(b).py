import time
import nltk
from nltk.corpus import movie_reviews, stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import string
from gensim.models import Word2Vec
import multiprocessing
import os

def preprocess():
    stop_words = set(stopwords.words('english'))
    punctuations = set(string.punctuation)
    documents = [movie_reviews.raw(fileid) for fileid in movie_reviews.fileids()]
    text = " ".join(documents).lower()
    sentences = sent_tokenize(text)
    processed_sentences = []
    for sent in sentences:
        tokens = word_tokenize(sent)
        tokens_clean = [t for t in tokens if t not in stop_words and t not in punctuations and t.isalpha()]
        if tokens_clean:
            processed_sentences.append(tokens_clean)
    return processed_sentences

def train_and_report(processed_sentences, embedding_dim=100, window_size=5, min_count=2, epochs=5):
    cores = multiprocessing.cpu_count()
    print(f"Using {cores} cores for training (gensim will use workers={max(1, cores-1)})")

    # CBOW (sg=0)
    start = time.time()
    cbow_model = Word2Vec(
        sentences=processed_sentences,
        vector_size=embedding_dim,
        window=window_size,
        min_count=min_count,
        sg=0,
        workers=max(1, cores-1),
        epochs=epochs
    )
    end = time.time()
    cbow_time = end - start
    print("=== CBOW Model ===")
    print(f"Training time: {cbow_time:.2f} seconds")
    print(f"Vocabulary size: {len(cbow_model.wv.index_to_key)}")
    print(f"Embedding dimension: {cbow_model.vector_size}")
    cbow_model.save("cbow.model")

    # Skip-Gram (sg=1)
    start = time.time()
    sg_model = Word2Vec(
        sentences=processed_sentences,
        vector_size=embedding_dim,
        window=window_size,
        min_count=min_count,
        sg=1,
        workers=max(1, cores-1),
        epochs=epochs
    )
    end = time.time()
    sg_time = end - start
    print("\n=== Skip-Gram Model ===")
    print(f"Training time: {sg_time:.2f} seconds")
    print(f"Vocabulary size: {len(sg_model.wv.index_to_key)}")
    print(f"Embedding dimension: {sg_model.vector_size}")
    sg_model.save("sg.model")

    return cbow_model, sg_model

if __name__ == "__main__":
    print("Preprocessing data...")
    sents = preprocess()
    print("Training Word2Vec models (this may take a while)...")
    cbow_model, sg_model = train_and_report(sents, embedding_dim=100, window_size=5, min_count=2, epochs=5)
    print("\nSaved CBOW model to cbow.model and Skip-Gram model to sg.model")
