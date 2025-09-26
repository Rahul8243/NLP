import nltk
from nltk.corpus import movie_reviews, stopwords
from nltk.tokenize import word_tokenize
import string
from nltk import FreqDist
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.stem import PorterStemmer
from collections import Counter
from nltk.stem import WordNetLemmatizer
import numpy as np

# Download required NLTK data
# nltk.download('movie_reviews')
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

# Step 1: Load and Preprocess
documents = [movie_reviews.raw(fileid) for fileid in movie_reviews.fileids()]
text = " ".join(documents).lower()
tokens = word_tokenize(text)
stop_words = set(stopwords.words('english'))
words_only = [word for word in tokens if word.isalpha() and word not in stop_words]

print("Number of tokens after preprocessing:", len(words_only))
print("First 20 tokens:", words_only[:20])
print("Vocabulary size:", len(set(words_only)))

# Step 2: Frequency Distribution
freq_dist = FreqDist(words_only)
top20 = freq_dist.most_common(20)
print("Top 20 words:", top20)

# Step 3: Visualization
# Bar chart
words_bar, counts = zip(*top20)
plt.figure(figsize=(12,6))
plt.bar(words_bar, counts, color='skyblue')
plt.xticks(rotation=45)
plt.title("Top 20 Word Frequencies")
plt.ylabel("Frequency")
plt.show()

# Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color='white') \
            .generate_from_frequencies(dict(top20))
plt.figure(figsize=(15,7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Top 20 Words")
plt.show()

# Step 4: Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words_only]
stemmed_freq = Counter(stemmed_words)

print("\nTop 20 stemmed words and their frequencies:")
for word, freq in stemmed_freq.most_common(20):
    print(f"{word}: {freq}")

# Step 5: Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in words_only]
lemmatized_freq = Counter(lemmatized_words)

print("\nTop 20 lemmatized words and their frequencies:")
for word, freq in lemmatized_freq.most_common(20):
    print(f"{word}: {freq}")

# -------------------------------
# Step 6: Compare Stemming vs Lemmatization (Top 15 words)
# -------------------------------
top15_words = [word for word, freq in freq_dist.most_common(15)]
stemmed_counts = [stemmed_freq[stemmer.stem(word)] for word in top15_words]
lemmatized_counts = [lemmatized_freq[lemmatizer.lemmatize(word)] for word in top15_words]

x = np.arange(len(top15_words))
width = 0.35

plt.figure(figsize=(14,6))
plt.bar(x - width/2, stemmed_counts, width, label='Stemmed', color='skyblue')
plt.bar(x + width/2, lemmatized_counts, width, label='Lemmatized', color='salmon')
plt.xticks(x, top15_words, rotation=45)
plt.ylabel("Frequency")
plt.title("Comparison: Stemming vs Lemmatization (Top 15 Words)")
plt.legend()
plt.tight_layout()
plt.show()
