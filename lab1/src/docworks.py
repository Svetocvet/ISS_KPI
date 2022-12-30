from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = stopwords.words()


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def clean_text(text):
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~\n'''
    for char in text:
        if char in punc:
            text = text.replace(char, " ")
    text = text.lower()
    return text


def tokenize(text):
    tokens = word_tokenize(text)
    return tokens


def remove_stop_words(tokens):
    filtered_tokens = [word for word in tokens if not word in stop_words]
    return filtered_tokens


def process_document(path):
    doc = read_file(path)
    cleaned = clean_text(doc)
    tokenized = tokenize(cleaned)
    filtered_tokens = remove_stop_words(tokenized)
    return filtered_tokens
