from collections import Counter
from nltk import ngrams

def generate_ngrams(tokens, n):
    return list(ngrams(tokens, n))

# Function to print most common n-grams
def print_top_ngrams(ngrams_list, top_n=20):
    freq_dist = Counter(ngrams_list)
    for ngram, count in freq_dist.most_common(top_n):
        print(f"{ngram}: {count}")

tokens = [
    "in", "the", "middle", "of", "the", "night", "in", "the", "forest",
    "of", "the", "dark", "the", "light", "in", "the", "sky"
]

# Generate unigrams, bigrams, trigrams
unigrams = generate_ngrams(tokens, 1)
bigrams = generate_ngrams(tokens, 2)
trigrams = generate_ngrams(tokens, 3)

print("Top 20 Bigrams:")
print_top_ngrams(bigrams)

print("\nTop 20 Trigrams:")
print_top_ngrams(trigrams)
