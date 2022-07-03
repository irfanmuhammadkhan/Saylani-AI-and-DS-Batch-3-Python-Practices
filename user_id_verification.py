user_info = [['irfan', 'abc123'], ['asad', 'xyz987'], ['saleem', 'ghq555'], ['faheem', 'pqr852]']]
user_name = input("Enter your name: ").lower().strip()
user_password = input("Enter your password: ").strip()

for i in user_info:
    if user_name == i[0] and user_password == i[1]:
        print("valid user")
        break
    else:
        continue
else:
    print("Invalid user")