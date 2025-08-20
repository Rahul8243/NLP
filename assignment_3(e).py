import nltk
from nltk.corpus import brown, stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Download required datasets (only the first time)
nltk.download('brown')
nltk.download('punkt')
nltk.download('stopwords')

# 1. Load text from 'news' category
news_text = brown.words(categories='news')
text = " ".join(news_text)

# 2. Tokenize into words
words = word_tokenize(text)

# 3. Join words back into string (before stopword removal)
text_before = " ".join(words)

# 4. Remove stopwords & keep only alphabetic words
stop_words = set(stopwords.words('english'))
filtered_words = [w.lower() for w in words if w.isalpha() and w.lower() not in stop_words]

# 5. Join filtered words into string (after stopword removal)
text_after = " ".join(filtered_words)

# 6. Generate Word Clouds
wc_before = WordCloud(width=800, height=400, background_color='white').generate(text_before)
wc_after = WordCloud(width=800, height=400, background_color='white').generate(text_after)

# 7. Plot both side by side
plt.figure(figsize=(16, 8))

plt.subplot(1, 2, 1)
plt.imshow(wc_before, interpolation="bilinear")
plt.title("Before Stopword Removal", fontsize=16)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(wc_after, interpolation="bilinear")
plt.title("After Stopword Removal", fontsize=16)
plt.axis("off")
plt.savefig("wordclouds.png")
plt.show()
