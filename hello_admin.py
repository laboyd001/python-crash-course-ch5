#make a list of 5 user names.  admin is one and will get a special greeting.  Otherwise there will be a generic greeting printed.

# user_names = ['admin', 'lesley', 'jenn', 'kathy', 'bt']

user_names = []

for user_name in user_names:
    if user_name == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user_name.title() + ", welcome back!" )
if len(user_names) < 1:
        print("There are no users!")