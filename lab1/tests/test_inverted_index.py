from lab1.src.inverted_index import InvertedIndex
from lab1.src import docworks as dw

# test inverted
# append, search

text1 = "You cannot just go in there blazing"
text2 = "We grab the choppers, go in guns blazing - simple as that"
text3 = "Do you really expect to just grab some choppers and go guns blazing?"

doc1 = dw.remove_stop_words(dw.tokenize(dw.clean_text(text1)))
doc2 = dw.remove_stop_words(dw.tokenize(dw.clean_text(text2)))
doc3 = dw.remove_stop_words(dw.tokenize(dw.clean_text(text3)))

ivt = InvertedIndex()

ivt.append_entry("doc1", doc1)
ivt.append_entry("doc2", doc2)
ivt.append_entry("doc3", doc3)

ivt.print()


def test_ivt_append():
    assert any(ivt.dict["simple"])
    assert ivt.dict["simple"] == ["doc2"]

    assert "doc3" in ivt.dict["expect"]

    assert "doc1", "doc2" in ivt.dict["blazing"]
    assert "doc3" in ivt.dict["blazing"]

    assert "ludicrous" not in ivt.dict


def test_ivt_search():
    assert ivt.search('blazing')

    assert 'doc1', 'doc2' in ivt.search('blazing')
    assert 'doc3' in ivt.search('blazing')

    assert 'doc1', 'doc2' not in ivt.search('ludicrous')


test_ivt_append()
test_ivt_search()
