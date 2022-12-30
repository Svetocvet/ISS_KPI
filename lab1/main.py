import os
from lab1.src import docworks
from lab1.src.inverted_index import InvertedIndex
from lab1.src.forward_index import ForwardIndex

inverted = InvertedIndex()
forward = ForwardIndex()

path = os.getcwd() + "/documents"
documents = []

for file in os.listdir(path):
    if file.endswith(".txt"):
        file_path = f"{path}/{file}"
        tokens = docworks.process_document(file_path)
        doc_name = file[:-4]

        forward.add_document(doc_name, tokens)
        inverted.append_entry(doc_name, tokens)

forward.print()
inverted.print()

print(forward.search("existence"))
print(inverted.search("existence"))

print(forward.search("neglected"))
print(inverted.search("neglected"))
