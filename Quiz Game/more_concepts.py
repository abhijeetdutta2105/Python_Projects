# __init__(self) is a constructor, here self refers to the object being created or initialized
class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.follower = 0
        self.following = 0

    def get_details(self):
        print(f"User ID : {self.user_id}")
        print(f"User Name : {self.user_name}")
        print(f"User follower count : {self.follower}")
        print(f"User following count : {self.following}")

    def follow(self,user):
        user.follower += 1
        self.following += 1


user_1 = User('001', 'Roshan')
user_2 = User('002', 'Parekh')
user_1.follow(user_2)
user_1.get_details()
user_2.get_details()

# user_2 = user_1
# user_2.get_details()

# This means user_2 just refers to user_1, it is shallow copy
# print(id(user_1))
# print(id(user_2))


