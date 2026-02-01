class User:
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role


class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, email):
        self.users = [user for user in self.users if user.email != email]

    def update_user(self, email, name=None, role=None):
        user = self._find_user_by_email(email)
        if user:
            if name:
                user.name = name
            if role:
                user.role = role

    def _find_user_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None

if __name__ == "__main__":
    manager = UserManager()
    user1 = User("Нұртілеу", "nurtileu@mail.com", "admin")
    user2 = User("Айгерім", "aigerim@mail.com", "user")

    manager.add_user(user1)
    manager.add_user(user2)

    
    for u in manager.users:
        print(u.name, u.email, u.role)

    
    manager.remove_user("aigerim@mail.com")
    print("Өшіруден кейін:")
    for u in manager.users:
        print(u.name, u.email, u.role)
