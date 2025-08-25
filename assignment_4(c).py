from collections import Counter
from nltk import ngrams

# Function to generate n-gram counts
def get_ngram_counts(tokens, n):
    return Counter(ngrams(tokens, n))

# Function: P(w2 | w1) using bigrams
def bigram_prob(w1, w2, tokens):
    bigram_counts = get_ngram_counts(tokens, 2)
    unigram_counts = get_ngram_counts(tokens, 1)
    
    numerator = bigram_counts[(w1, w2)]
    denominator = unigram_counts[(w1,)]
    
    if denominator == 0:
        return 0
    return numerator / denominator

# Function: P(w3 | w1, w2) using trigrams
def trigram_prob(w1, w2, w3, tokens):
    trigram_counts = get_ngram_counts(tokens, 3)
    bigram_counts = get_ngram_counts(tokens, 2)
    
    numerator = trigram_counts[(w1, w2, w3)]
    denominator = bigram_counts[(w1, w2)]
    
    if denominator == 0:
        return 0
    return numerator / denominator

# Example corpus tokens
tokens = [
    "in", "the", "middle", "of", "the", "night",
    "in", "the", "forest", "of", "the", "dark",
    "the", "light", "in", "the", "sky"
]

# Example usage
print("P('the' | 'in') =", bigram_prob("in", "the", tokens))
print("P('middle' | 'in', 'the') =", trigram_prob("in", "the", "middle", tokens))
print("P('dark' | 'of', 'the') =", trigram_prob("of", "the", "dark", tokens))
