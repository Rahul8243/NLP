from collections import Counter
import math

# Dataset
emails = [
    ("Win money now", "Spam"),
    ("Lowest price guaranteed", "Spam"),
    ("Cheap meds available", "Spam"),
    ("Hello friend how are you", "Ham"),
    ("Let’s have lunch tomorrow", "Ham"),
    ("Meeting schedule attached", "Ham"),
    ("Win a free lottery ticket", "Spam"),
    ("See you at the conference", "Ham"),
    ("Project deadline reminder", "Ham"),
    ("Cheap loans available", "Spam")
]

# Preprocessing
def tokenize(text):
    return text.lower().split()

spam_words, ham_words = [], []
for text, label in emails:
    if label == "Spam":
        spam_words.extend(tokenize(text))
    else:
        ham_words.extend(tokenize(text))

spam_count = len(spam_words)
ham_count = len(ham_words)
vocab = set(spam_words + ham_words)
V = len(vocab)

# Laplace smoothed probability
def word_prob(word, word_list, total_count):
    return (word_list.count(word) + 1) / (total_count + V)

# Test email
test_email = ["cheap", "price", "now"]

# Likelihoods
p_spam = 1
p_ham = 1
for w in test_email:
    p_spam *= word_prob(w, spam_words, spam_count)
    p_ham *= word_prob(w, ham_words, ham_count)

# Priors
p_spam *= 0.5
p_ham *= 0.5

# Normalize
p_total = p_spam + p_ham
print("P(Spam|Email) =", p_spam/p_total)
print("P(Ham|Email)  =", p_ham/p_total)
