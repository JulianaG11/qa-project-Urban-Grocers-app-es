import sender_stand_request
import data

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def positive_assert(kit_body):
    auth_token = sender_stand_request.get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    auth_token = sender_stand_request.get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 400

def test_create_kit_empty_name_get_bad_request_response():
    kit_body = get_kit_body("")
    print("Enviando al servidor:", kit_body)  # Debug line
    auth_token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    print("Respuesta del servidor:", response.status_code)  # Debug line
    assert response.status_code == 201