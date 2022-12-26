import re


# Find all the israeli cell phone numbers in the text.
# In this exercise, israeli cell phone number answers the following:
# format: <000-0000000>
# starts from 05

def find_phone_numbers(text: str):
    return re.findall("05[0234578][0-9]{7}", text)


if __name__ == '__main__':
    find_phone_numbers([])