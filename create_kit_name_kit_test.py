import sender_stand_request
import data

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = user_response.json()["authToken"]
    return auth_token

def positive_assert(kit_body):
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

def test_create_kit_511_character_name_get_success_response():
    long_name = "a" * 511
    kit_body = get_kit_body(long_name)
    positive_assert(kit_body)