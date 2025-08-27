import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers={"Content-Type": "application/json"})

def post_new_client_kit(kit_body, auth_token):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers={"Content-Type": "application/json",
                                  "Authorization": f"Bearer {auth_token}"})

def get_new_user_token():
    # Crear un nuevo usuario usando los datos del archivo data.py
    user_response = post_new_user(data.user_body)
    # Extraer y devolver el authToken de la respuesta
    return user_response.json()["authToken"]