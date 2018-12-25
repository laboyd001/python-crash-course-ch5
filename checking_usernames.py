#simulating checking for unique usernames

current_users = ['admin', 'lesley', 'jenn', 'kathy', 'bt']

new_users = ['lesley', 'Jenn', 'austin', 'jessica', 'sam']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("That username is taken")
    else:
        print("That username is available")