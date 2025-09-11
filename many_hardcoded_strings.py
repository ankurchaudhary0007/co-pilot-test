# Example Python file with many hardcoded strings
import os
def get_config():
    api_url = "https://api.example.com/v1/"  # Hardcoded API URL
    api_key = os.environ.get("API_KEY")      # API key loaded from environment variable
    timeout = 30
    print(f"Connecting to {api_url} with key {api_key} and timeout {timeout}s")


def greet_user():
    greeting = "Hello, user!"                 # Hardcoded greeting
    print(greeting)


def send_notification():
    title = "System Alert"                    # Hardcoded notification title
    message = "Your process has completed."   # Hardcoded notification message
    print(f"Notification: {title} - {message}")


def database_connect():
    host = "localhost"                       # Hardcoded DB host
    port = "5432"                            # Hardcoded DB port
    user = "admin"                           # Hardcoded DB user
    password = "password123"                 # Hardcoded DB password
    print(f"Connecting to DB at {host}:{port} as {user}")


def display_menu():
    menu = [
        "1. Start",
        "2. Stop",
        "3. Restart",
        "4. Exit"
    ]
    for item in menu:
        print(item)


def main():
    get_config()
    greet_user()
    send_notification()
    database_connect()
    display_menu()
    print("Program finished.")

if __name__ == "__main__":
    main()
