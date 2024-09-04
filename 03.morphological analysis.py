import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

text = "The quick brown fox jumps over the lazy dog."

tokens = word_tokenize(text)

lemmas = [lemmatizer.lemmatize(token) for token in tokens]

print("Tokens:", tokens)
print("Lemmas:", lemmas)
