import pytest

import json

from utils.utils import get_file_operations, get_last_operations, get_fixed_data, get_formatted_data

def test_get_file_operations():
    data = get_file_operations()
    assert isinstance(data, list)

def test_get_last_operations(test_data):
    assert get_fixed_data(test_data[:2]) == [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
    ]

