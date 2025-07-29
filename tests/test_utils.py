from src.utils import get_operations, convertation
from unittest.mock import Mock, patch


def test_get_operations(input_file, list_of_transactions_json):
    assert get_operations(input_file) == []


@patch('requests.get')
def test_convertation(mock_get, operation_usd, response_usd, operation_rub):
    # настройка mock_response
    mock_response = Mock()
    mock_response.json.return_value = response_usd

    # установка mock_get
    mock_get.return_value = mock_response

    assert convertation(operation_rub) == 31957.58
    assert convertation(operation_usd) == 665930.9700000001
