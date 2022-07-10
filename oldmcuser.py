import requests
import sys




def fetch_old_users(uuid):
    old_user = requests.get(f"https://api.mojang.com/user/profile/{uuid}/names")
    list_names = old_user.json()
    return list_names

def if_uuid(user):
    old_names = fetch_old_users(user)
    for name in old_names:
        print(f"User: {name['name']}")
    old_userget()



def old_userget():
    user = input(">")
    if user == "oldnames":
        user = input("Who do you wanna search: ")
        old = requests.get(f"https://api.mojang.com/users/profiles/minecraft/%s" % (user))
        if len(user) > 16:
            if_uuid(user)

        js = old.json()
        old_names = fetch_old_users(js['id'])
        for name in old_names:
            print(f"User: {name['name']}")
        old_userget()

    if user == "exit":
        sys.exit()
    else:
        print("Invalid input")
        old_userget()










old_userget()