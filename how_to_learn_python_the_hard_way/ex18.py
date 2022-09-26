def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_two_again(arg1, arg2):
    print(f"arg1: {arg1} arg2: {arg2}")


def print_none():
    print("I got nothing \\ dosent work this way")


print_two("einar", "steinar")
print_two_again("einar", "steinar")
print_none()