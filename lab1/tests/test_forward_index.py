from lab1.src.forward_index import ForwardIndex
from lab1.src import docworks as dw

# test forward
# append, search

text1 = "You cannot just go in there blazing"
text2 = "We grab the choppers, go in guns blazing - simple as that"
text3 = "Do you really expect to just grab some choppers and go guns blazing?"

doc1 = dw.remove_stop_words(dw.tokenize(dw.clean_text(text1)))
doc2 = dw.remove_stop_words(dw.tokenize(dw.clean_text(text2)))
doc3 = dw.remove_stop_words(dw.tokenize(dw.clean_text(text3)))

fwd = ForwardIndex()

fwd.add_document("doc1", doc1)
fwd.add_document("doc2", doc2)
fwd.add_document("doc3", doc3)


def test_fwd_append():
    assert any(fwd.dict["doc1"])
    assert fwd.dict["doc1"] == ['blazing']

    assert 'choppers' in fwd.dict["doc2"]
    assert 'guns', 'blazing' in fwd.dict["doc2"]
    assert 'guns', 'blazing' in fwd.dict["doc3"]


def test_fwd_search():
    assert fwd.search('blazing')

    assert 'doc1', 'doc2' in fwd.search('blazing')
    assert 'doc3' in fwd.search('blazing')

    assert 'doc1', 'doc2' not in fwd.search('ludicrous')
    assert 'doc3' not in fwd.search('ludicrous')

    assert not fwd.search('ludicrous')


test_fwd_append()
test_fwd_search()
