from api.base_api import BaseAPI

class FakeStoreAPI(BaseAPI):

    BASE_URL = "https://fakestoreapi.com"

    # =====================
    # GET
    # =====================
    def get_all_products(self):
        return self.get("/products")

    def get_single_product(self, product_id):
        return self.get(f"/products/{product_id}")

    def get_categories(self):
        return self.get("/products/categories")

    def get_products_in_category(self, category):
        return self.get(f"/products/category/{category}")

    # =====================
    # POST
    # =====================
    def create_product(self, payload):
        return self.post("/products", json=payload)

    # =====================
    # PUT
    # =====================
    def update_product(self, product_id, payload):
        return self.put(f"/products/{product_id}", json=payload)

    # =====================
    # DELETE
    # =====================
    def delete_product(self, product_id):
        return self.delete(f"/products/{product_id}")