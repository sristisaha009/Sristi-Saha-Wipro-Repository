from behave import given, when, then
import requests


@given("the API endpoint is available")
def check_endpoint(context):
    response = requests.get(
        context.base_url + "/users/1",
        timeout=15
    )

    assert response.status_code == 200

    print("API endpoint is accessible")
    print("Status code:", response.status_code)

    input(
        "SCREENSHOT 1: Capture the API setup "
        "and terminal output. Press ENTER."
    )


@when("I send a GET request for user {user_id:d}")
def get_user(context, user_id):
    url = f"{context.base_url}/users/{user_id}"

    context.response = requests.get(
        url,
        timeout=15
    )

    print("\nRequest URL:", url)
    print("HTTP Method: GET")
    print("Response Status:", context.response.status_code)
    print("Response Body:", context.response.text)

    input(
        "SCREENSHOT 2: Capture the API response "
        "in the terminal. Press ENTER."
    )


@then("the response status should be {status:d}")
def verify_status(context, status):
    assert context.response.status_code == status

    print(
        f"PASS: Expected status {status}, "
        f"received {context.response.status_code}"
    )


@then("the response should contain the expected user ID {user_id:d}")
def verify_user_id(context, user_id):
    data = context.response.json()

    assert data["id"] == user_id
    assert "name" in data
    assert "email" in data

    print("PASS: User ID verified:", data["id"])
    print("User Name:", data["name"])
    print("User Email:", data["email"])

    input(
        "SCREENSHOT 3: Capture the validation "
        "and user details. Press ENTER."
    )