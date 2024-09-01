from enum import Enum


class OutputFormat(str, Enum):
    json = "json"
    csv = "csv"
    txt = "txt"
