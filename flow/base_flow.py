from typing import Any, List

import prefect


from pre_play.catalouge import gebieden_in_nederland_year
from pre_play.gebieden_in_nederland import load_document, to_pandas, strip_all_strings
from pre_play.models import Document
from prefect import Flow, task
import pandas as pd
from time import sleep

LOG = prefect.context.get("logger")

@task(name="Get documents from catalouge")
def get_documents() -> List[Document]:
    return [
        entry[1] for entry in gebieden_in_nederland_year() if entry and entry[0] > 2020
    ]


@task(name="Load table")
def load_table(doc: Document) -> pd.DataFrame:
    return to_pandas(load_document(doc), [])


@task(name="Parse dataframe input")
def parse_table(df: pd.DataFrame) -> pd.DataFrame:
    return strip_all_strings(df)


@task(name="echo")
def echo(v: pd.DataFrame):
    LOG.info(v.describe())

@task(name="echo")
def shout(v: Any):
    LOG.info(v)


@task(name="useless")
def massive():
    LOG.info("useless process to enable paralism")
    sleep(5)



def compose_flow() -> Flow:
    with Flow("CBS test flow") as f:
        documents = get_documents()
        data_table = load_table.map(documents)
        cleaned = parse_table.map(data_table)
        echo.map(cleaned).set_upstream(massive())
        # just here to enable parallel processing

    return f

def compose_alter_flow() -> Flow:
    with Flow("CBS test flow") as f:
        res1 = massive()
        res2 = massive()
        shout("FOO BAR").set_upstream(res1).set_upstream(res2)
        # just here to enable parallel processing

    return f