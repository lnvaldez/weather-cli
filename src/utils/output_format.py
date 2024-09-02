from typing import Dict, Any
from src.utils.format import format_as_json, format_as_csv, format_as_txt
from src.utils.file_writer import (
    write_to_json_file,
    write_to_csv_file,
    write_to_txt_file,
)


def output_format(data: Dict[str, Any], format_type: str, target_output: str):
    if target_output == "terminal":
        if format_type == "json":
            return format_as_json(data)
        elif format_type == "csv":
            return format_as_csv(data)
        else:
            return format_as_txt(data)

    else:
        if format_type == "json":
            write_to_json_file(data)
        elif format_type == "csv":
            write_to_csv_file(data)
        else:
            write_to_txt_file(data)
