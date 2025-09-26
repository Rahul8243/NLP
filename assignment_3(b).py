import nltk
from nltk.corpus import brown, stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

news_text = brown.words(categories='news')
text = " ".join(news_text)

words = word_tokenize(text)

stop_words = set(stopwords.words('english'))
filtered_words = [w.lower() for w in words if w.isalpha() and w.lower() not in stop_words]

fdist = FreqDist(filtered_words)

print("\nTop 20 most frequent words (without stopwords):")
for word, freq in fdist.most_common(20):
    print(word, ":", freq)
