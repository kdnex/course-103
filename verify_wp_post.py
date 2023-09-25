"""
This is a Python script that verifies that a student created a WordPress post.
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

# Create the HTTP Basic Authentication string
auth_string = f"{WP_USERNAME}:{WP_KEY}"

# retrive all the WordPress posts

TIMEOUT_SECONDS = 5
response = requests.get(
    f"{BASE_URL}/posts",
    headers=headers,
    timeout=TIMEOUT_SECONDS
)

posts = response.json()

# Print the titles of all posts
for post in posts:
    title = post['title']['rendered']
    print(f"post title: {title}")
    # check if the string STUDNET_ASSIGNED_NUMBER is in the title
    if STUDENT_ASSIGNED_NUMBER in title:
        print(f"Found STUDENT_ASSIGNED_NUMBER: {STUDENT_ASSIGNED_NUMBER}")
        print(f"post id: {post['id']}")
        # post_id = post['id']
        sys.exit(0)

print(f"Did not find STUDENT_ASSIGNED_NUMBER: {STUDENT_ASSIGNED_NUMBER}")
sys.exit(1)

print(response.status_code)

# Define the post data as a dictionary
post_data = {
    "title": f"Just A Random Post Title - (STUDENT_ASSIGNED_NUMBER: {STUDENT_ASSIGNED_NUMBER})",
    "content": "This is the content of the new post.",
    "status": "publish"
}

# Send the POST request using the requests library
TIMEOUT_SECONDS = 5
response = requests.post(
    f"{BASE_URL}/posts/",
    auth=(WP_USERNAME, WP_KEY),
    headers=headers,
    json=post_data,
    timeout=TIMEOUT_SECONDS
)

# Check the response
if response.status_code == 201:
    print("Post created successfully!")
    sys.exit(0)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
    sys.exit(1)
