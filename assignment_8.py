from nltk.stem import WordNetLemmatizer
from collections import Counter
import nltk

# Download WordNet data if not already done
nltk.download('wordnet')
nltk.download('omw-1.4')

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Apply lemmatization to tokenized words
lemmatized_words = [lemmatizer.lemmatize(word) for word in words_only]

# Count frequency
lemmatized_freq = Counter(lemmatized_words)

# Print top 20 lemmatized words
print("Top 20 lemmatized words and their frequencies:")
for word, freq in lemmatized_freq.most_common(20):
    print(f"{word}: {freq}")
