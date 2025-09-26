from collections import Counter
from nltk import ngrams

# --- Helper functions ---
def get_ngram_counts(tokens, n):
    return Counter(ngrams(tokens, n))

def bigram_prob(w1, w2, tokens):
    bigram_counts = get_ngram_counts(tokens, 2)
    unigram_counts = get_ngram_counts(tokens, 1)
    numerator = bigram_counts[(w1, w2)]
    denominator = unigram_counts[(w1,)]
    return numerator / denominator if denominator > 0 else 0

def trigram_prob(w1, w2, w3, tokens):
    trigram_counts = get_ngram_counts(tokens, 3)
    bigram_counts = get_ngram_counts(tokens, 2)
    numerator = trigram_counts[(w1, w2, w3)]
    denominator = bigram_counts[(w1, w2)]
    return numerator / denominator if denominator > 0 else 0

# --- Sentence Probability ---
def sentence_prob_bigram(sentence, tokens):
    words = sentence.split()
    prob = 1.0
    for i in range(1, len(words)):
        p = bigram_prob(words[i-1], words[i], tokens)
        prob *= p
    return prob

def sentence_prob_trigram(sentence, tokens):
    words = sentence.split()
    prob = 1.0
    if len(words) < 3:
        return sentence_prob_bigram(sentence, tokens)  # fallback
    for i in range(2, len(words)):
        p = trigram_prob(words[i-2], words[i-1], words[i], tokens)
        prob *= p
    return prob

# --- Example Corpus ---
tokens = [
    "the", "president", "of", "the", "company",
    "the", "manager", "of", "the", "company",
    "the", "company", "is", "big"
]

# --- Test Sentence ---
sentence = "the president of the company"

print("Sentence:", sentence)
print("Bigram Model Probability =", sentence_prob_bigram(sentence, tokens))
print("Trigram Model Probability =", sentence_prob_trigram(sentence, tokens))
