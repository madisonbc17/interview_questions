#function parameters: user's name
#function output: user name with greeting
#for testing purposes, I would do something like the test_function()
def test_function():
    name = "Madison"
    result = username_greeting(name)
    if result == "Hello " + str(name):
        print("Success!")
    else:
        print("Fail")

#while this could all be done outside of a function, I prefer to use functions in case scope increases
def username_greeting(user_name):
    personal_greeting = "Hello " + str(user_name)
    return personal_greeting
    
#Here would be an example of a "main" code. I know there is another fancy way of doing something like
#main__init().. but I think this would do for this situation
test_function()
name = "John Doe"
result = username_greeting(name)
print(result)