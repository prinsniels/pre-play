from cbsodata import get_data
from typing import Dict, List
from pre_play.models import Document
import pandas as pd
import numpy as np

def load_document(document: Document) -> List[Dict[str, str]]:
    return get_data(document.identifier)

def to_pandas(entries: List[Dict[str, str]], colums: List[str]) -> pd.DataFrame:
    # TODO: Add columns to take from the database
    return pd.DataFrame(entries)

def strip_all_strings(df: pd.DataFrame) -> pd.DataFrame:
    return df.applymap(lambda x: x.strip() if isinstance(x, str) else x)