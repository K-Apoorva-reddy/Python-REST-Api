# REST API Development using Python and JSON

A Python project that demonstrates how to consume a REST API using the `requests` library. The application retrieves public GitHub user information through the GitHub REST API and displays the response in a readable format. This project was developed as Task 4 of my Python Internship.

# Project Overview

This project connects to the GitHub REST API, sends an HTTP GET request, receives JSON data, and extracts useful information such as username, name, followers, following, and public repositories.

It demonstrates how Python applications interact with web services using REST APIs and JSON data.


# Features

- Connects to the GitHub REST API
- Sends HTTP GET requests
- Reads JSON responses
- Extracts user information
- Displays formatted output in the terminal
- Simple REST API client implementation


# Technologies Used

- Python 3.x
- Requests Library
- JSON
- GitHub REST API

# Project Structure

```
T-4 REST API Development/
│
├── main.py
├── README.md
└── Screenshots/
```

# How to Run

#Clone Repository

```bash
git clone https://github.com/K-Apoorva-reddy/Python-rest-api.git
```

## Install Requests

```bash
pip install requests
```

## Run the Program

```bash
python main.py
```


# API Used

GitHub Users API

```
https://api.github.com/users/{username}
```

Example:

```
https://api.github.com/users/apoorvareddy
```

---

# Sample Output

```text
Username: apoorvareddy
Name: Not Provided
Followers: 5
Following: 2
Public Repos: 10
```

> Note: The follower count, following count, and public repositories will change over time as your GitHub profile changes.



# Project Screenshots

###  Project Structure

https://github.com/K-Apoorva-reddy/Python-REST-Api/blob/main/Project-structure.png


###  Terminal Output

https://github.com/K-Apoorva-reddy/Python-REST-Api/blob/main/Terminal-output.png

---

###  GitHub API Response

![API Response](Screenshots/api-response.png)


# Learning Outcomes

- Understanding REST APIs
- Working with HTTP GET requests
- Using the Requests library
- Parsing JSON responses
- Accessing public web APIs
- Error-free API integration

---

# Future Enhancements

- Accept GitHub username as user input
- Handle API errors gracefully
- Display additional profile information
- Save API responses to a JSON file
- Build a GUI for API requests

# Acknowledgement

This project was developed as part of my Python Internship to understand REST API communication, JSON data handling, and web service integration using Python.
