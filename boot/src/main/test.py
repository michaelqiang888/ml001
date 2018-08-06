print("hello world")

username = "xiang"

print(username)

# define a named function, this function return an anonymous function
def fun1(n):
    temp = lambda a:a*n
    return temp

mynum = fun1(2)
print(mynum(11))
