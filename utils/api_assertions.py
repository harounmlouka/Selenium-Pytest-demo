def assert_status_code(response, expected_code):
    assert response.status_code == expected_code


def assert_response_not_empty(response):
    assert len(response.json()) > 0