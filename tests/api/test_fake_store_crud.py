import pytest
from api.fake_store_api import FakeStoreAPI
from utils.api_assertions import assert_status_code


@pytest.mark.api
class TestFakeStoreCRUD:

    def test_create_product(self):

        api = FakeStoreAPI()

        payload = {
            "title": "QA Automation Product",
            "price": 99.99,
            "description": "Created by automation test",
            "image": "https://i.pravatar.cc",
            "category": "electronics"
        }

        response = api.create_product(payload)

        assert_status_code(response, 201)

        data = response.json()

        assert "id" in data
        assert data["title"] == payload["title"]


    def test_update_product(self):

        api = FakeStoreAPI()

        payload = {
            "title": "Updated Product",
            "price": 120
        }

        response = api.update_product(1, payload)

        assert_status_code(response, 200)

        data = response.json()

        assert data["title"] == "Updated Product"


    def test_delete_product(self):

        api = FakeStoreAPI()

        response = api.delete_product(1)

        assert_status_code(response, 200)

        data = response.json()

        # FakeStore returns deleted object or {} depending on version
        assert data is not None