import nltk
from nltk.corpus import brown, stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist

# Download required data
nltk.download('brown')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Load text from 'news' category
news_text = brown.words(categories='news')
text = " ".join(news_text)

# Tokenize
words = word_tokenize(text)

# Remove stopwords & non-alphabetic
stop_words = set(stopwords.words('english'))
filtered_words = [w.lower() for w in words if w.isalpha() and w.lower() not in stop_words]

# Apply WordNet Lemmatizer
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(w) for w in filtered_words]

# Frequency Distribution
fdist_lemmatized = FreqDist(lemmatized_words)

# Show top 20
print("\nTop 20 lemmatized words (with frequency):")
for word, freq in fdist_lemmatized.most_common(20):
    print(word, ":", freq)
