import requests

response = requests.get("https://api.github.com/users/apoorvareddy")

data = response.json()

print("Username:", data["login"])
print("Name:", data["name"] if data["name"] else "Not Provided")
print("Followers:", data["followers"])
print("Following:", data["following"])
print("Public Repos:", data["public_repos"])