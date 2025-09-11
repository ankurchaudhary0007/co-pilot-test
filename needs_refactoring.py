# Example: Function that can be split into smaller functions for better debugging

def process_user_data(user_data):
    # Validate user data
    if not isinstance(user_data, dict):
        print("Invalid data format")
        return None
    if "name" not in user_data or "age" not in user_data:
        print("Missing required fields")
        return None
    # Clean name
    name = user_data["name"].strip().title()
    # Check age
    age = user_data["age"]
    if not isinstance(age, int) or age < 0:
        print("Invalid age")
        return None
    # Generate greeting
    greeting = f"Hello, {name}! You are {age} years old."
    # Log user info
    print(f"User processed: {name}, Age: {age}")
    # Return result
    return greeting

# Example usage
user = {"name": " alice ", "age": 30}
print(process_user_data(user))
