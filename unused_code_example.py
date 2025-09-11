
# Real-world style example with unused code
import requests  # Unused import

def fetch_user_data(user_id):
    # Simulate fetching user data
    return {"id": user_id, "name": "Alice"}

def process_user_data(data):
    # Only this function is used
    print(f"Processing user: {data['name']}")

def unused_helper():
    # This function is never called
    print("This is an unused helper function.")

unused_constant = 12345  # Unused variable

if __name__ == "__main__":
    user = fetch_user_data(1)
    process_user_data(user)
