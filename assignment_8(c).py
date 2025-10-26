import os
import nltk
import string
from nltk.corpus import movie_reviews, stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from gensim.models import Word2Vec

def preprocess():
    stop_words = set(stopwords.words('english'))
    punctuations = set(string.punctuation)

    # Load dataset
    documents = [movie_reviews.raw(fileid) for fileid in movie_reviews.fileids()]
    text = " ".join(documents).lower()

    # Tokenize into sentences → tokens → clean
    sentences = sent_tokenize(text)
    processed_sentences = []
    for sent in sentences:
        tokens = word_tokenize(sent)
        tokens_clean = [t for t in tokens if t not in stop_words and t not in punctuations and t.isalpha()]
        if tokens_clean:
            processed_sentences.append(tokens_clean)
    return processed_sentences


def load_or_train_model():
    if os.path.exists("cbow.model"):
        print("Loading existing CBOW model (cbow.model)...")
        model = Word2Vec.load("cbow.model")
    else:
        print("No saved model found. Training a new CBOW model...")
        sentences = preprocess()
        model = Word2Vec(
            sentences=sentences,
            vector_size=100,
            window=5,
            min_count=2,
            sg=0,   # CBOW
            epochs=5
        )
        model.save("cbow.model")
        print("Model trained and saved as cbow.model")
    return model


def explore_embeddings(model):
    print("\n=== Similarity Tests ===")
    for word in ["king", "education", "football"]:
        if word in model.wv:
            print(f"\nTop 10 words similar to '{word}':")
            for sim_word, score in model.wv.most_similar(word, topn=10):
                print(f"{sim_word:15} {score:.4f}")
        else:
            print(f"\nWord '{word}' not found in vocabulary!")

    print("\n=== Analogy Tests ===")
    try:
        result = model.wv.most_similar(positive=["king", "woman"], negative=["man"], topn=5)
        print("Analogy: king - man + woman = ?")
        for word, score in result:
            print(f"{word:15} {score:.4f}")
    except KeyError:
        print("Words not found for analogy (king, man, woman).")

    try:
        result = model.wv.most_similar(positive=["paris", "italy"], negative=["france"], topn=5)
        print("\nAnalogy: paris - france + italy = ?")
        for word, score in result:
            print(f"{word:15} {score:.4f}")
    except KeyError:
        print("Words not found for analogy (paris, france, italy).")

    print("\n=== Cosine Similarity ===")
    try:
        sim_score = model.wv.similarity("king", "queen")
        print(f"Cosine similarity (king, queen): {sim_score:.4f}")
    except KeyError:
        print("Either 'king' or 'queen' not found in vocabulary.")


if __name__ == "__main__":
    model = load_or_train_model()
    explore_embeddings(model)
