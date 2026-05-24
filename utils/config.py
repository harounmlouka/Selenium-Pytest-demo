import os

BASE_URL = os.getenv("BASE_URL", "https://www.wikipedia.org/")
BROWSER = os.getenv("BROWSER", "chrome")
TIMEOUT = int(os.getenv("TIMEOUT", 10))