from typing import Any
from dataclasses import dataclass
import json

@dataclass
class Booking:
    id: int
    occurrenceId: int
    resourceId: int
    start: str
    end: str
    title: str
    rate: str
    status: str
    isCasual: bool

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _id = int(obj.get("id"))
        _occurrenceId = int(obj.get("occurrenceId"))
        _resourceId = int(obj.get("resourceId"))
        _start = str(obj.get("start"))
        _end = str(obj.get("end"))
        _title = str(obj.get("title"))
        _rate = str(obj.get("rate"))
        _status = str(obj.get("status"))
        _isCasual = bool(obj.get("isCasual"))
        return Booking(_id, _occurrenceId, _resourceId, _start, _end, _title, _rate, _status, _isCasual)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
