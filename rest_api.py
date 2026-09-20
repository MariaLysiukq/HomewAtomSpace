import requests
import json
from requests.exceptions import RequestException

def get_users() -> dict:
    """Get all users."""
    response = requests.get(f"{BASE_URL}/users")
    response.raise_for_status()
    return {"status_code": response.status_code,"data": response.json()}

def get_user(user_id: int) -> dict:
    """Get user from ID."""
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    response.raise_for_status()
    return {"status_code": response.status_code,"data": response.json()}
    
    
def create_user(user_data: dict) -> dict:
    """Create new user"""
    response = requests.post(f"{BASE_URL}/users", json=user_data)
    response.raise_for_status()
    return {"status_code": response.status_code,"data": response.json()}
    
    
def modify_user(user_id: int, user_data: dict) -> dict:
    """modify user data."""
    response = requests.patch(f"{BASE_URL}/users/{user_id}", json=user_data)
    response.raise_for_status()
    return {"status_code": response.status_code,"data": response.json()}


def remove_user(user_id: int) -> dict:
    """delete user from ID."""
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    response.raise_for_status()
    return {"status_code": response.status_code,"data": response.json()}


def main():
    while True:
        print("WELCOME")
        print("1. Переглянути всіх користувачів\n2. Переглянути користувача за ID")
        print("3. Створити користувача\n4. Оновити користувача\n5. Видалити користувача\n0. Вийти")    
        action = input("Enter your choice: ").strip()
    
        try:
            if action == "1":
                dict_respons = get_users()
                users = dict_respons["data"]
                print(f"Get {len(users)} users:")
                for user in users:
                    print(user["name"])
            elif action == "2":    
                user_id = int(input("Enter user ID: "))
                dict_respons = get_user(user_id)
                user = dict_respons["data"]
                print(f"ID: {user.get('id')}")
                print(f"Name: {user.get('name')}")
                print(f"Username: {user.get('username')}")
                print(f"Email: {user.get('email')}")
            elif action == "3":
                name = input("Enter user name: ")
                email = input("Enter user email: ")
                payload = {"name": name, "email": email}
                created = create_user(payload)
                print("\nUser created:", created)
            elif action == "4":
                user_id = int(input("Enter user ID: "))
                key = input("What you wanna change? (name, email): ")
                val = input("New value: ")
                updated = modify_user(user_id, {key: val})
                print("Modified:", updated)
            elif action == '5':
                user_id = int(input("Enter user ID: "))
                remove_user(user_id)
                print(f"\nUser {user_id} deleted ")
            elif action == "0":
                print("Bye")
                return
            else:
                print("Cannot do your action. ")
                
        except ValueError:
            print("Error, id must be an integer")
        except RequestException as error:
            print(f"Something went wrong during the request: {error}")
            
            
main()
