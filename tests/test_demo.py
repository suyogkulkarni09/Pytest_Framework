from apilayer.apiclient import PetStoreApiClient
import allure


def test_find_pets_by_status(api_client):
    allure.step("Test HTML Log")
    pet_store = PetStoreApiClient()

    status = 'sold'
    response = pet_store.find_pets_by_status(status)

    # Assert the response code
    assert response.status_code == 200

    # Assert other response details as needed
    response_json = response.json()
    # print("Response is")
    # print(response_json)
    # print(response_json[0]['name'])


def test_add_new_pet(api_client):
    pet_store = PetStoreApiClient()
    response = pet_store.add_new_pet()
    allure.step("Test HTML Log")
    # Assert the response code
    assert response.status_code == 200
    response_json = response.json()
    print("Response is")
    print(response_json)
