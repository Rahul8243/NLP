import nltk
from nltk.corpus import brown, stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.probability import FreqDist

# Download required data
nltk.download('brown')
nltk.download('punkt')
nltk.download('stopwords')

# Load text from 'news' category
news_text = brown.words(categories='news')
text = " ".join(news_text)

# Tokenize
words = word_tokenize(text)

# Remove stopwords & non-alphabetic
stop_words = set(stopwords.words('english'))
filtered_words = [w.lower() for w in words if w.isalpha() and w.lower() not in stop_words]

# Apply Snowball Stemmer
stemmer = SnowballStemmer("english")
stemmed_words = [stemmer.stem(w) for w in filtered_words]

# Frequency Distribution
fdist_stemmed = FreqDist(stemmed_words)

# Show top 20
print("\nTop 20 stemmed words (with frequency):")
for word, freq in fdist_stemmed.most_common(20):
    print(word, ":", freq)
