import requests
import logging

logging.basicConfig(filename="errors.log", level=logging.ERROR)

url_get = "https://httpbin.org/get"
url_post = "https://httpbin.org/post"

try:
    get_response = requests.get(url_get)
    print("GET Status:", get_response.status_code)
    print("GET Headers:", get_response.headers)
    print("GET Body:", get_response.text)
except Exception as e:
    logging.error(f"GET request failed: {e}")

try:
    post_response = requests.post(url_post, json={"title": "foo", "body": "bar", "userId": 1})
    print("POST Status:", post_response.status_code)
    print("POST Headers:", post_response.headers)
    print("POST Body:", post_response.text)
except Exception as e:
    logging.error(f"POST request failed: {e}")
