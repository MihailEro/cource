import pytest

@pytest.fixture
def test_data():
        return [
            {
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
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {
                    "amount": "67314.70",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657"
            },
            {
                "id": 172864002,
                "state": "EXECUTED",
                "date": "2018-12-28T23:10:35.459698",
                "operationAmount": {
                    "amount": "49192.52",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Открытие вклада",
                "to": "Счет 96231448929365202391"
            },
    ]
