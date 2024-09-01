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
