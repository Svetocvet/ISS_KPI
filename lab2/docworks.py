import string

import inverted_index


def read_text_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def format_document(text):
    rawarr = text.split()
    arr = []
    for term in rawarr:
        newterm = term.strip(string.punctuation)
        newterm = newterm.lower()
        if len(newterm) > 0:
            arr.append(newterm)
    return arr


# first line of each file is a title
def get_title(text):
    return text.partition('\n')[0]


def create_index(filenames, index, file_titles):
    for file in filenames:
        text = read_text_file(file)
        file_titles[file] = get_title(text)
        terms = format_document(text)
        inverted_index.append_entry(index, file, terms)


def print_index(index):
    inverted_index.print_dict(index)
