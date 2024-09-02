from enum import Enum


class OutputFormat(str, Enum):
    json = "json"
    csv = "csv"
    txt = "txt"


class Target(str, Enum):
    file = "file"
    terminal = "terminal"
