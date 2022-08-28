def user_info_1(name, age, city):
    print("{} is {} years old and lives in {}".format(name, age, city))

user_info_1("Alex", 25, "California")

def user_info_2(name, age=0, city="Delhi"):
    print("{} is {} years old and lives in {}".format(name, age, city))

user_info_2("Alex")
user_info_2(age=21, city="Bengaluru", name="Rahul")