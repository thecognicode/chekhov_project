import os
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt


print("Текущая рабочая директория:", os.getcwd())
print("Содержимое папки 'texts':", os.listdir("texts"))


def load_texts(folder_path):
    texts = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                texts.append(f.read())
    return texts


def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zа-яё\s]", "", text)
    tokens = text.split()
    return tokens


def get_bigrams(tokens):
    return list(zip(tokens, tokens[1:]))


def plot_wordcloud(tokens, title):
    if not tokens:
        print("Внимание: нет токенов для облака слов.")
        return
    text = " ".join(tokens)
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(title)
    plt.savefig("images/Chekhov_The_Bet_1.png")
    plt.show()


def compute_tfidf(texts):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    feature_names = vectorizer.get_feature_names_out()
    for i, row in enumerate(tfidf_matrix.toarray()):
        print(f"\nКлючевые слова для текста {i+1}:")
        top_indices = row.argsort()[-5:][::-1]
        for idx in top_indices:
            print(f"{feature_names[idx]}: {row[idx]:.3f}")


if __name__ == "__main__":
    folder = "texts"
    texts_raw = load_texts(folder)
    print("Загружено текстов:", len(texts_raw))

    processed_texts = [preprocess_text(text) for text in texts_raw]
    for i, tokens in enumerate(processed_texts):
        print(f"Пример токенов для текста {i+1}: {tokens[:10]}")
        if not tokens:
            print("Внимание: после предобработки текст стал пустым!")

    
    for i, tokens in enumerate(processed_texts[:2]):
        plot_wordcloud(tokens, title=f"Облако слов для текста {i+1}")

    
    for i, tokens in enumerate(processed_texts[:2]):
        bigrams = get_bigrams(tokens)
        top_bigrams = Counter(bigrams).most_common(5)
        print(f"\nТоп-5 биграмм для текста {i+1}:")
        for bigram, count in top_bigrams:
            print(f"{bigram}: {count}")

    
    compute_tfidf([" ".join(tokens) for tokens in processed_texts])
