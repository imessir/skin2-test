import json
import requests

baseurl = "https://opm-website.iot-asm-test1.insitech.live/"


def user_info():
    return {
        "id": -1,
        "userName": "Войти",
        "email": "anonymous@email.com",
        "phone": None,
        "bonusPoints": None,
        "preOrderNumber": "1-1",
        "secondName": None,
        "firstName": None,
        "patronymic": None,
        "birthDay": None,
        "countCartItems": None,
        "countOrders": None,
        "anonymous": True
    }


def verify_response(request: requests, expected_status_code: int, expected_data: dict):
    actual_status_code = request.status_code
    actual_data = json.loads(request.content)
    assert actual_status_code == expected_status_code, \
        f"Error! Status code does not match expected.\n" \
        f"Actual status code: {actual_status_code}.\n" \
        f"Expected status code: {expected_status_code}.\n" \
        f"Error: {json.loads(request.content).get('errors') if isinstance(request.text, dict) else '<empty>'}."
    assert actual_data == expected_data, \
        f"Error! Content does not match expected.\n" \
        f"Actual content: {actual_data}.\n" \
        f"Expected status code: {expected_data}.\n"


def get_user() -> requests.Response:
    """
    GET /api/strapi/user \n
    Get user info. \n
    :return: returns response result as object response.
    """
    with requests.get(
            f"{baseurl}/api/strapi/user"
    ) as response:
        return response


def test_send_request():
    test_data = user_info()
    tested_response = get_user()
    verify_response(tested_response, 200, test_data)
