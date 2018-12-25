#checking for inequality

# requested_toppings = 'mushrooms'

# if requested_toppings != 'anchovies':
#     print("Hold the anchovies!")

#testing multiple conditions

# requested_toppings = ['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")
# print("\nFinished making your pizza!")

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we're out of green peppers.")
#     else:
#         print("Adding " + requested_topping + ".")

# print("\nFinished making your pizza.")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza.")
else:
    print("Are you sure you want a plain pizza?")
