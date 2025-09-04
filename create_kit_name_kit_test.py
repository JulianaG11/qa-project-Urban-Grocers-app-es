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

def test_create_kit_with_name_empty_get_error_response():
    kit_body_eight = get_kit_body({ })
    negative_assert_code_400(kit_body_eight)

def test_create_kit_with_numbers_in_name_get_success_response():
    kit_body_seven = get_kit_body("123")
    positive_assert(kit_body_seven)


def test_create_kit_with_spaces_in_name_get_success_response():
    kit_body_six = get_kit_body(" A Aaa ")
    positive_assert(kit_body_six)


def test_create_kit_special_symbol_in_name_get_success_response():
    kit_body_five = get_kit_body("#$%")
    positive_assert(kit_body_five)


def test_create_kit_512_characters_in_name_bad_request_response():
    kit_body_four = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(kit_body_four)


def test_create_kit_has_empty_name_get_bad_request_response():
    kit_body_three = get_kit_body("")
    negative_assert_code_400(kit_body_three)


def test_create_kit_511_characters_name_success_response():
    kit_body_two = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(kit_body_two)


def test_create_kit_1_characters_in_name_success_response():
    kit_body_one = get_kit_body("a")
    positive_assert(kit_body_one)
