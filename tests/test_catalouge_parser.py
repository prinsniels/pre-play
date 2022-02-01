import pytest
from pre_play.catalouge import extract_document_year


@pytest.mark.parametrize("inp,exp", [
    ("gebieden in nederland 2018", 2018),
    ("Gebieden in nederland 2018", 2018),
    ("Gebieden in nederland 2018 2018", None),
    ("Gebieden in nederland ", None),
    ("Wrong gebieden in nederland 2018", None)
])
def test_year_from_title(inp, exp):
    assert extract_document_year(inp) == exp
