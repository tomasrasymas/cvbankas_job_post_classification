import json
import os
import string


def load_json(file_path):
    with open(file_path, "r", encoding="utf8") as file_obj:
        json_data = json.load(file_obj)

    return json_data


def clean_punctuation(text):
    table = str.maketrans("", "", string.punctuation)

    return " ".join([word.translate(table) for word in text.split()]).lower()


def clean_stop_words(text):
    stop_words_path = os.path.join("data", "stopwords-lt.json")
    stop_words = load_json(stop_words_path)

    return " ".join([word for word in text.split() if not word in stop_words])


if __name__ == "__main__":
    posts_path = os.path.join("data", "posts.json")
    posts = load_json(posts_path)

    classification_text = [(post["responsibilities_text"] if post["responsibilities_text"] else "") + " " + (post["qualifications_text"] if post["qualifications_text"] else "") for post in posts]
    classification_category = [post["category"] for post in posts]

    classification_text = [clean_punctuation(c_text) for c_text in classification_text]
    classification_text = [clean_stop_words(c_text) for c_text in classification_text]