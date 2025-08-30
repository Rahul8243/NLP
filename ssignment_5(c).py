from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

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

# Train/test split
train = emails[:8]
test  = emails[8:]

X_train_texts, y_train = zip(*train)
X_test_texts,  y_test  = zip(*test)

# Vectorize text
vectorizer = CountVectorizer(stop_words="english")
X_train = vectorizer.fit_transform(X_train_texts)
X_test  = vectorizer.transform(X_test_texts)

# Train Naive Bayes
nb = MultinomialNB()
nb.fit(X_train, y_train)

# Predict
y_pred = nb.predict(X_test)

# Evaluate
print("Predictions:", list(y_pred))
print("True labels:", list(y_test))
print("Accuracy:", accuracy_score(y_test, y_pred))
    