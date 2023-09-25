"""
This is a Python script that demonstrates basic usage of the Canvas API.
"""

import json
import os
import sys
import requests

# network programming
BASE_URL = "https://canvas.ltu.se/api/v1"
COURSE_ID = 19899

# required Environment Variables
# CANVAS_TOKEN

# Get the value of the "token" environment variable
CANVAS_TOKEN = os.environ.get("CANVAS_TOKEN")

# Check if the variable is set
if CANVAS_TOKEN is None:
    print("CANVAS_TOKEN environment variable is not set.")
    sys.exit(1)
else:
    print("CANVAS_TOKEN: found")

headers = {
    "Authorization": "Bearer " + CANVAS_TOKEN,
}

TIMEOUT_SECONDS = 5
response = requests.get(
    f"{BASE_URL}/courses/{COURSE_ID}/users",
    headers=headers,
    timeout=TIMEOUT_SECONDS
)

print(response.status_code)

# Check if the response status code is 200 (OK) before attempting to parse the JSON response
if response.status_code != 200:
    print(f"Request failed with status code {response.status_code}")
    sys.exit(1)

users_data = response.json()

for user in users_data:

    # Pretty print the JSON data
    # print(json.dumps(user, indent=4))

    # Access the 'name' key within each user dictionary
    # print(user['name'])
    name=user['name']
    print (f"name: {name}")

    # Access the 'name' key within each user dictionary and verify that it is "maharg-3"
    if name == "Alrub Ahmad Ibrahim Abu":
        print(name)
        sys.exit(0)

print("No user with sys_user_id 'Alrub Ahmad Ibrahim Abu' found.")
sys.exit(1)
