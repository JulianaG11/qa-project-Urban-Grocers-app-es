import sender_stand_request
import data

def get_kit_body(name):
    current_body = data.kit_body_nine.copy()
    current_body["name"] = name
    return current_body

def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body_nine)
    return user_response.json()["authToken"]

def positive_assert(kit_body):
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 400

def test_create_kit_number_type_name_get_error_response():
    kit_body_nine = get_kit_body(123)
    negative_assert_code_400(kit_body_nine)



