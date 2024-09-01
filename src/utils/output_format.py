import csv
import io
import json
from typing import Dict, Any


def format_as_json(data: Dict[str, Any]) -> str:
    return json.dumps(data, indent=4)


def format_as_csv(data: Dict[str, Any]) -> str:
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=data.keys())
    writer.writeheader()
    writer.writerow(data)
    return output.getvalue()


def format_as_txt(data: Dict[str, Any]) -> str:
    return "\n".join(f"{key.capitalize()}: {value}" for key, value in data.items())


def output_format(data: Dict[str, Any], format_type: str):
    if format_type == "json":
        return format_as_json(data)
    elif format_type == "csv":
        return format_as_csv(data)
    elif format_type == "txt":
        return format_as_txt(data)
    else:
        raise TypeError("Supported formats are: (json, csv, txt)")
