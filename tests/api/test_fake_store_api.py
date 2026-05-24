import pytest
from jsonschema import validate

from api.fake_store_api import FakeStoreAPI

from utils.api_assertions import (
    assert_status_code,
    assert_response_not_empty
)

from utils.logger import logger

from data.test_data import (
    PRODUCT_ID,
    CATEGORY
)

# =========================
# JSON SCHEMAS
# =========================

product_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "title": {"type": "string"},
        "price": {"type": "number"},
        "description": {"type": "string"},
        "category": {"type": "string"},
        "image": {"type": "string"}
    },
    "required": [
        "id",
        "title",
        "price",
        "description",
        "category",
        "image"
    ]
}


category_schema = {
    "type": "string"
}


# =========================
# TEST CLASS
# =========================

@pytest.mark.api
class TestFakeStoreAPI:

    @pytest.fixture(scope="class")
    def api(self):

        logger.info("Initializing FakeStore API client")

        return FakeStoreAPI()

    # =========================
    # GET ALL PRODUCTS
    # =========================

    def test_get_all_products(self, api):

        logger.info("Testing GET all products")

        response = api.get_all_products()

        assert_status_code(response, 200)
        assert_response_not_empty(response)

        products = response.json()

        assert len(products) > 0

        for product in products:
            validate(instance=product, schema=product_schema)

        logger.info("GET all products test passed")

    # =========================
    # GET SINGLE PRODUCT
    # =========================

    def test_get_single_product(self, api):

        logger.info(f"Testing GET single product: {PRODUCT_ID}")

        response = api.get_single_product(PRODUCT_ID)

        assert_status_code(response, 200)
        assert_response_not_empty(response)

        product = response.json()

        validate(instance=product, schema=product_schema)

        assert product["id"] == PRODUCT_ID

        logger.info("GET single product test passed")

    # =========================
    # GET CATEGORIES
    # =========================

    def test_get_categories(self, api):

        logger.info("Testing GET categories")

        response = api.get_categories()

        assert_status_code(response, 200)
        assert_response_not_empty(response)

        categories = response.json()

        assert len(categories) > 0

        for category in categories:
            validate(instance=category, schema=category_schema)

        logger.info("GET categories test passed")

    # =========================
    # GET PRODUCTS BY CATEGORY
    # =========================

    def test_get_products_in_category(self, api):

        logger.info(f"Testing GET products in category: {CATEGORY}")

        response = api.get_products_in_category(CATEGORY)

        assert_status_code(response, 200)
        assert_response_not_empty(response)

        products = response.json()

        assert len(products) > 0

        for product in products:
            validate(instance=product, schema=product_schema)
            assert product["category"] == CATEGORY

        logger.info("GET products by category test passed")