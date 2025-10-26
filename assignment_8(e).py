# task5_pretrained_glove.py
import os
from gensim.models import Word2Vec, KeyedVectors
import gensim.downloader as api

if os.path.exists("cbow.model"):
    cbow_model = Word2Vec.load("cbow.model")
    print("Loaded CBOW model.")
else:
    raise FileNotFoundError("No trained CBOW model found! Run Task 2 first.")

# Step 2: Load small pretrained GloVe model
print("Loading pretrained GloVe embeddings (~128MB)...")
glove_model = api.load("glove-wiki-gigaword-100")  # smaller and fast
print("Pretrained GloVe model loaded.")

words_to_test = [("king", "queen"), ("man", "woman"), ("paris", "france")]

print("\n--- CBOW Model Similarities ---")
for w1, w2 in words_to_test:
    if w1 in cbow_model.wv and w2 in cbow_model.wv:
        sim = cbow_model.wv.similarity(w1, w2)
        print(f"Similarity({w1}, {w2}) = {sim:.4f}")
    else:
        print(f"Words ({w1}, {w2}) not in CBOW vocabulary.")

print("\n--- Pretrained GloVe Similarities ---")
for w1, w2 in words_to_test:
    if w1 in glove_model and w2 in glove_model:
        sim = glove_model.similarity(w1, w2)
        print(f"Similarity({w1}, {w2}) = {sim:.4f}")
    else:
        print(f"Words ({w1}, {w2}) not in pretrained vocabulary.")

print("\n--- CBOW Model Analogy ---")
try:
    result = cbow_model.wv.most_similar(positive=["king", "woman"], negative=["man"], topn=5)
    print("king - man + woman =", [(w, f"{s:.4f}") for w, s in result])
except KeyError:
    print("Analogy words not found in CBOW model.")

print("\n--- Pretrained GloVe Analogy ---")
try:
    result = glove_model.most_similar(positive=["king", "woman"], negative=["man"], topn=5)
    print("king - man + woman =", [(w, f"{s:.4f}") for w, s in result])
except KeyError:
    print("Analogy words not found in pretrained model.")
