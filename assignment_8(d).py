import os
import random
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from gensim.models import Word2Vec

if os.path.exists("cbow.model"):
    print("Loading CBOW model...")
    model = Word2Vec.load("cbow.model")
else:
    raise FileNotFoundError("No trained model found! Train your CBOW model first.")

# Pick 50 random words
vocab = list(model.wv.index_to_key)
words = random.sample(vocab, 50)

# Get vectors
vectors = [model.wv[w] for w in words]

# Reduce dimensions with PCA
pca = PCA(n_components=2)
reduced = pca.fit_transform(vectors)

# Plot
plt.figure(figsize=(12, 8))
for i, word in enumerate(words):
    x, y = reduced[i]
    plt.scatter(x, y, color="blue")
    plt.annotate(word, (x+0.02, y+0.02), fontsize=9)
plt.title("Word Embeddings Visualization (PCA)")
plt.show()
