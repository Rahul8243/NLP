import nltk
from nltk.corpus import brown, stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# Download required data
nltk.download('brown')
nltk.download('punkt')
nltk.download('stopwords')

# Load text from 'news' category
news_text = brown.words(categories='news')
text = " ".join(news_text)

# Tokenize into words
words = word_tokenize(text)

# Remove stopwords & keep only alphabetic words
stop_words = set(stopwords.words('english'))
filtered_words = [w.lower() for w in words if w.isalpha() and w.lower() not in stop_words]

# Frequency Distribution
fdist = FreqDist(filtered_words)

# Top 20 words
print("\nTop 20 most frequent words (without stopwords):")
for word, freq in fdist.most_common(20):
    print(word, ":", freq)
