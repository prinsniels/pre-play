from dataclasses import dataclass

from pendulum import datetime

from datetime import date


@dataclass(frozen=True)
class Document:
    title: str
    identifier: str

