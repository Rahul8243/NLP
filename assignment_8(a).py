import nltk
from nltk.corpus import movie_reviews, stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import string
import sys

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
    flat_tokens = [t for sent in processed_sentences for t in sent]
    vocab = set(flat_tokens)

    print("===== Task 1: Preprocessing Results =====")
    print(f"Number of sentences: {len(processed_sentences)}")
    print(f"Number of tokens after preprocessing: {len(flat_tokens)}")
    print(f"Vocabulary size: {len(vocab)}")
    print(f"First 20 tokens: {flat_tokens[:20]}")
    print()
    print("Example tokenized sentence (first):", processed_sentences[0][:30])
    return processed_sentences

if __name__ == "__main__":
    _ = preprocess()
