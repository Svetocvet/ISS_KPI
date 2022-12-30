import json


def append_entry(docs, document, keywords):
    if document not in docs:
        docs[document] = keywords

    elif document in docs:
        # add new and remove duplicates
        docs[document] += keywords
        docs[document] = list(set(docs[document]))


def print_dict(docs):
    print(json.dumps(docs, sort_keys=False, indent=2))


def search(index, query):
    pages = []
    for key in index.keys():
        if query in index[key]:
            pages.append(key)
    return pages
