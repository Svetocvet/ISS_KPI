import json


def append_entry_singular(docs, keyword, document):
    if keyword not in docs:
        docs[keyword] = [document]
    elif keyword in docs:
        if document not in docs[keyword]:
            docs[keyword].append(document)


def append_entry(docs, document, keywords):
    for key in keywords:
        append_entry_singular(docs, key, document)


def print_dict(docs):
    print(json.dumps(docs, sort_keys=False, indent=2))


def search(index, query):
    if query in index:
        return index[query]
    return []
