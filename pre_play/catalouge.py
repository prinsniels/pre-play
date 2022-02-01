import re
from typing import Dict, List, Optional, Tuple

from cbsodata import get_table_list

from pre_play.models import Document


def get_gebieden_in_nederland():
    return [
        d
        for d in get_table_list()
        if d["Title"].lower().startswith("gebieden in nederland")
    ]


def gebieden_in_nederland_parser(document: Dict[str, str]) -> Optional[Document]:
    title = document.get("Title", None)
    identifier = document.get("Identifier", None)

    if not (title and identifier):
        return None
    else:
        return Document(title, identifier)


def extract_document_year(title: str) -> Optional[int]:
    pattern = re.compile(r"^gebieden in nederland (\d{4})$", flags=re.I)
    res = pattern.match(title)
    if res:
        return int(res.group(1))
    else:
        return None


def gebieden_in_nederland_year() -> List[Tuple[int, Document]]:
    acc = []
    for document in get_gebieden_in_nederland():
        parsed_document = gebieden_in_nederland_parser(document)
        if not parsed_document:
            continue
        parsed_year = extract_document_year(parsed_document.title)
        if not parsed_year:
            continue
        acc.append((parsed_year, parsed_document))
    return acc
