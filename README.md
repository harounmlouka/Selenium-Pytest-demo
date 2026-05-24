This project was built to practice and demonstrate modern Quality Assurance automation engineering concepts using Python, Selenium, Pytest, and API testing.
I tried to structure the project to be as close to a real-world professional QA automation framework as possible.

The framework was built using Selenium WebDriver for browser automation andPytest as the testing framework.

I used a Page Object Model (POM) an industry-standard design pattern that: improves maintainability, reduces duplicated code, and makes large automation suites easier to scale.

The project is seperated into two distinct parts.

First an UI test on the wikipedia website that:

    1.Opens Wikipedia.
    2.Searches for a keyword.
    3.Validates the results page title.

Second is a CRUD API automation test on fakestoreapi.com.

I tested GET, PUT, POST, and DELETE operations and implemented response validation, JSON validation, status code assertions.

Some miscellaneous added to bring the project up to professional standards:

I externalized test data into JSON files to seprate data from logic.
I implemented automatic screenshot capture when UI tests fail.
I created reusable API assertion helper functions to reduce duplication and improve readabilit.
I also included execution logs, HTML test reports, and structured test output.

