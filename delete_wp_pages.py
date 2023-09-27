"""
This is a Python script that deletes random WordPress pages.
"""

import os
import sys
import requests

# required Environment Variables
# WP_USERNAME
# WP_KEY

# Get the value of the "WP_USERNAME" environment variable
WP_USERNAME = os.environ.get("WP_USERNAME")

# Check if the variable is set
if WP_USERNAME is None:
    print("WP_USERNAME environment variable is not set.")
    sys.exit(1)
else:
    print("WP_USERNAME: found")

# Get the value of the "WP_KEY" environment variable
WP_KEY = os.environ.get("WP_KEY")

# Check if the variable is set
if WP_KEY is None:
    print("WP_KEY environment variable is not set.")
    sys.exit(1)
else:
    print("WP_KEY: found")

# Get the value of the "STUDENT_ASSIGNED_NUMBER" environment variable
STUDENT_ASSIGNED_NUMBER = os.environ.get("STUDENT_ASSIGNED_NUMBER")

# Check if the variable is set
if STUDENT_ASSIGNED_NUMBER is None:
    print("STUDENT_ASSIGNED_NUMBER environment variable is not set.")
    sys.exit(1)

# Define base URL
BASE_URL = "https://toddbooth.com/wp-json/wp/v2"

# Define the headers
headers = {
    "Content-Type": "application/json"
}

# retrive some the WordPress posts
NUMBER=5
TIMEOUT_SECONDS = 5
response = requests.get(
    f"{BASE_URL}/pages?per_page={NUMBER}",
    headers=headers,
    timeout=TIMEOUT_SECONDS
)

pages = response.json()

# print the number of items
print(f"Number of pages: {len(pages)}")

# Delete the pages
TIMEOUT_SECONDS = 5
for page in pages:
    title = page['title']['rendered']
    print(f"Deleting page: {title}")
    response = requests.delete(
        f"{BASE_URL}/pages/{page['id']}",
        auth=(WP_USERNAME, WP_KEY),
        headers=headers,
        timeout=TIMEOUT_SECONDS
    )
    print(f"status_code: {response.status_code}")
    if response.status_code == 200:
        print("Page deleted successfully!")
    else:
        print("Error:")
        print(response.text)
        sys.exit(1)
