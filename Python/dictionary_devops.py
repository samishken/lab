# Storing configuration Setting: DevOps use dictionaries to store application or server
# configuration settings.

config = {
    "hostname": "server1.example.com",
    "port": 8080,
    "username": "admin",
    "password": "<PASSWORD>"
}
print(config["hostname"])  # Accessing value using a key

# Output:
# server1.example.com

environment = {
    "DATABASE_URL": "postgres://user:password@localhost:5432/mydb",
    "API_KEY": "abc1234secret",
    "DEBUG": True
}
print(environment["DATABASE_URL"])

api_response = {
    "status": "success",
    "data": {
        "server": "192.168.1.1",
        "uptime": "24 hours"
    }
}
print(api_response["data"]["server"])

