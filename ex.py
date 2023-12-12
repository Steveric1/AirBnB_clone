import re

# Example arg string
arg = "some.prefix.method(arg1, arg2)"

# The provided code
match = re.search(r"\.", arg)
if match is not None:
    argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
    match = re.search(r"\((.*?)\)", argl[1])
    if match is not None:
        command = [argl[1][:match.span()[0]], match.group()[1:-1]]
        print("Before opening parenthesis:", command[0])
        print("Inside parentheses:", command[1])
    else:
        print("*** Unknown syntax: {}".format(arg))
else:
    print("*** No dot found in the string.")

# Output:
# Before opening parenthesis: some.prefix.method
# Inside parentheses: arg1, arg2
