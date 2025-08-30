import re
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

# ----------------------
# 1. Preprocessing
# ----------------------
stopwords = set(["the","is","at","how","are","you","a","an","to","for","of","and"])

def tokenize(text):
    tokens = re.findall(r"[a-z']+", text.lower())
    return [t for t in tokens if t not in stopwords]

# Split dataset (simple: first 8 train, last 2 test)
train = emails[:8]
test = emails[8:]

# Build vocab
all_words = []
for text, label in train:
    all_words.extend(tokenize(text))
vocab = set(all_words)
V = len(vocab)

# ----------------------
# 2. Feature extraction
# ----------------------
spam_words = []
ham_words = []
for text, label in train:
    if label == "Spam":
        spam_words.extend(tokenize(text))
    else:
        ham_words.extend(tokenize(text))

spam_count = len(spam_words)
ham_count = len(ham_words)
spam_ctr = Counter(spam_words)
ham_ctr = Counter(ham_words)

# Priors
p_spam = sum(1 for _, l in train if l=="Spam") / len(train)
p_ham  = sum(1 for _, l in train if l=="Ham") / len(train)

# ----------------------
# 3. Naive Bayes function
# ----------------------
def predict(text):
    words = tokenize(text)
    log_spam = math.log(p_spam)
    log_ham = math.log(p_ham)
    for w in words:
        # Laplace smoothing
        log_spam += math.log((spam_ctr.get(w,0)+1)/(spam_count+V))
        log_ham  += math.log((ham_ctr.get(w,0)+1)/(ham_count+V))
    return "Spam" if log_spam > log_ham else "Ham"

# ----------------------
# 4. Evaluate
# ----------------------
correct = 0
for text,label in test:
    pred = predict(text)
    print(f"Email: {text} | True: {label} | Pred: {pred}")
    if pred == label:
        correct += 1

accuracy = correct / len(test)
print("Accuracy =", accuracy)
