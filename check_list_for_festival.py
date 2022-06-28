reg_name_list = ["abdullah", "ali", "usama", "irfan", "zain", "usman", "faheem", "umer", "waqas", "qasim"]
name = input("Enter your name: ").lower()

if name in reg_name_list:
    print("Welcome to festival")

else:
    print("Register yourself first, then come")