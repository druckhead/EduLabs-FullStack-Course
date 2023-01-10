import requests
import json

BORED_URL = "https://www.boredapi.com/api/activity"
response = requests.get(BORED_URL)
print(response)
print(type(response))

print()

print(response.status_code)
print(response.text)

print()

res = json.loads(response.text)
print(type(res))
print(res)

response_as_json = response.json()

print(response_as_json["activity"])


response = requests.get("https://www.google.com")
print(response.status_code)
print(response.text)

# ####################
print()

#
# GENDER_BASE_URL = "https://api.genderize.io/"
# response = requests.get(GENDER_BASE_URL, params={"name": "daniel"})
# print(response.status_code, response.text, sep="\n")

if __name__ == '__main__':
    name = input("Enter your name: ")
    GENDER_BASE_URL = "https://api.genderize.io/"
    response = requests.get(GENDER_BASE_URL, params={"name": name})
    if response.status_code == 200:
        name_dict = response.json()
        print(f"Your name is {name_dict.get('gender')} with prob: {name_dict.get('probability')}")
    else:
        print(f"There was an error, status code: {response.status_code}")


