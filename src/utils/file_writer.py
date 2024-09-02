import os
from typing import Union, Dict, List, Any
from src.utils.format import format_as_json, format_as_csv, format_as_txt


json_file = os.path.join("data", "data.json")
csv_file = os.path.join("data", "data.csv")
txt_file = os.path.join("data", "data.txt")


def write_to_json_file(data: Union[Dict[str, Any], List[Any]]):
    formatted_data = format_as_json(data)
    with open(json_file, "a+") as file:
        file.write(formatted_data)


def write_to_csv_file(data: Union[Dict[str, Any], List[Any]]):
    formatted_data = format_as_csv(data)
    with open(csv_file, "a+") as file:
        file.write(formatted_data)


def write_to_txt_file(data: Union[Dict[str, Any], List[Any]]):
    formatted_data = format_as_txt(data)
    with open(txt_file, "a+") as file:
        file.write(formatted_data)