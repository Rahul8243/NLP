import nltk
from nltk.corpus import brown, stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.probability import FreqDist

nltk.download('brown')
nltk.download('punkt')
nltk.download('stopwords')

news_text = brown.words(categories='news')
text = " ".join(news_text)

words = word_tokenize(text)

stop_words = set(stopwords.words('english'))
filtered_words = [w.lower() for w in words if w.isalpha() and w.lower() not in stop_words]

stemmer = SnowballStemmer("english")
stemmed_words = [stemmer.stem(w) for w in filtered_words]

fdist_stemmed = FreqDist(stemmed_words)


print("\nTop 20 stemmed words (with frequency):")
for word, freq in fdist_stemmed.most_common(20):
    print(word, ":", freq)
