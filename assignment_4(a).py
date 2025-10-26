import nltk
from nltk.corpus import brown
from nltk.tokenize import sent_tokenize, word_tokenize
import re


# 1) Load news category
news_words_list = brown.words(categories='news')
news_sents_list = brown.sents(categories='news')  

# 2) Make RAW text (keep punctuation for sentence tokenizer)
raw_text = " ".join(news_words_list)

# 3) Sentence tokenization on RAW
sentences = sent_tokenize(raw_text)
total_sentences = len(sentences)

# 4) Clean text (lower + remove punctuation) for word-level processing
clean_text = raw_text.lower()
clean_text = re.sub(r'[^\w\s]', '', clean_text)    # remove punctuation
clean_text = re.sub(r'\s+', ' ', clean_text).strip()

# 5) Word tokenization on CLEAN text
words = word_tokenize(clean_text)
total_words = len(words)

# 6) Vocabulary size
vocab_size = len(set(words))

# 7) Report
print("===== REPORT (Brown: news) =====")
print(f"Total Sentences      : {total_sentences}")
print(f"Total Words          : {total_words}")
print(f"Vocabulary Size      : {vocab_size}")

