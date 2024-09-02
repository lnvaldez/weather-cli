import csv
import io
import json
from typing import Dict, List, Union, Any

nl_nl = "\n\n"


def format_as_json(data: Union[Dict[str, Any], List[Any]]) -> str:
    return json.dumps(data, indent=4)


# The parameter 'data' can be either a Dict, or a List
def format_as_csv(data: Union[Dict[str, Any], List[Any]]) -> str:
    output = io.StringIO()
    if isinstance(data, Dict):
        writer = csv.DictWriter(output, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)
    else:
        fieldnames = [
            "date",
            "temp",
            "sensation",
            "description",
            "humidity",
            "pressure",
            "wind_speed",
            "visibility",
        ]
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        for d in data:
            writer.writerow(d)
    return output.getvalue()


def format_as_txt(data: Union[Dict[str, Any], List[Any]]) -> str:
    if isinstance(data, Dict):
        return "\n".join(f"{key.capitalize()}: {value}" for key, value in data.items())
    else:
        return nl_nl.join(
            "\n".join(f"{key.capitalize()}: {value}" for key, value in item.items())
            for item in data
        )
