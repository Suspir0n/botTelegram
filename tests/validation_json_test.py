
"""from jsonmix.validate import validate_json
from datetime import datetime


receive_mock_request_data = {
    "uid": 1,
    "data": {
        "name": "Teste",
        "phone": "71983620502",
        "text": "Hello my friend"
    },
    "date": 1621085772
}

model_mock_request_data = {
    "uid": int,
    "data": {
        "name": str,
        "phone": str,
        "text": str
    },
    "date": int
}
response_field_mock_request_data = {
      "code": "BTERR-001",
      "data": {
          "error": "inconsistency on JSON structure",
          "message": "Missing required JSON field"
      },
      "date": str(datetime.now().timestamp()),
}
response_type_mock_request_data = {
      "code": "BTERR-002",
      "data": {
          "error": "inconsistency on JSON structure",
          "message": "JSON field type is incorrect"
      },
      "date": str(datetime.now().timestamp())
}

def test_validate_json():
    sort = dict
    got = type(validate_json(receive=receive_mock_request_data, model=model_mock_request_data, response_field=response_field_mock_request_data, response_field_type=response_type_mock_request_data)),
    assert verification_condition((got != sort)) is True

    @validate_json(receive=receive_mock_request_data, model=model_mock_request_data, response_field=response_field_mock_request_data, response_field_type=response_type_mock_request_data, operation='decorator')
    def hello():
        _message = 'hello word'
        return _message

    assert verification_condition(type(hello()) != sort) is True


def verification_condition(condition):
    if condition is True:
        return True
    else:
        return False"""