import nltk
nltk.download('brown')
nltk.download('punkt_tab')

from nltk.corpus import brown
from nltk.tokenize import sent_tokenize, word_tokenize

# Download (only if not already done)
nltk.download('brown')
nltk.download('punkt')

# Load text from 'news' category
news_text = brown.words(categories='news')
text = " ".join(news_text)

# Sentence Tokenization
sentences = sent_tokenize(text)
print("First 3 Sentences:\n")
for s in sentences[:3]:
    print(s)

# Word Tokenization of first sentence
words = word_tokenize(sentences[0])
print("\nTokenized Words of First Sentence:\n", words)
