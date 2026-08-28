"""RBAC and Authentication App"""

# Users and their assigned roles.
# Can Add new users here if you want to give them access too.
USERS = {
    "kyle": "admin",
    "kole": "user",
}


def login(username):
    """Check whether the username exists and return a session."""

    if username in USERS:
        role = USERS[username]

        print("\nLogin successful!")
        print(f"You are logged in as: {role}")

        return {"username": username, "role": role}

    # any username not in USERS is treated as unknown.
    print(f"\nUnknown user: {username}")
    return None


def admin(check):
    """Only admins can access this """

    if check is None:
        print("You are not logged in. You cannot access the admin panel")
        return

    if check["role"] == "admin":
        print("ADMIN ACTION: You can manage system settings.")
    else:
        print(
            f"You are logged in as a {check['role']}. "
            "You cannot access the admin panel."
        )


def user(check):
    """Only regular users can access this panel."""

    if check is None:
        print("You are not logged in. You cannot access the user panel.")
        return

    if check["role"] == "user":
        print("USER ACTION: You can view your personal dashboard.")
    else:
        print(
            f"You are logged in as a {check['role']}. "
            "You cannot access the user panel."
        )


def app():
    print("=== RBAC Authentication ===")
    print("Available registered users: kyle, kole\n")

    # Ask the person to enter ANY username.
    username = input("Enter username: ")

    # Try to log in.
    check = login(username)

    # If the username isn't registered
    if check is None:
        print(
            "\nYou are not logged in. "
            "You cannot access any thing make an account."
        )
        return

    print("\n--- Checking Access ---")

    # Check both.
    admin(check)
    user(check)


if __name__ == "__main__":
    app()


# CIA TRIAD NOTE:
# This app demonstrates CONFIDENTIALITY. Role checks prevent users from
# accessing actions that are not intended for their role. Only authorized
# users can access the protected actions associated with their role.