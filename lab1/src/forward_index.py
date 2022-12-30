# Document  Keywords
# doc1       hello, sky, morning
# doc2       tea, coffee, hi
# doc3       greetings, sky

import json


class ForwardIndex:
    def __init__(self):
        self.dict = {}

    def add_document(self, document, keywords):
        if document not in self.dict:
            self.dict[document] = keywords

        elif document in self.dict:
            # add new and remove duplicates
            self.dict[document] += keywords
            self.dict[document] = list(set(self.dict[document]))

    def print(self):
        print(json.dumps(self.dict, sort_keys=False, indent=2))

    def search(self, keyword):
        pages = []
        for key in self.dict.keys():
            if keyword in self.dict[key]:
                pages.append(key)
        return pages
