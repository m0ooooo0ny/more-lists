"""Goal: Practice with lists
Follow the directions to create a list that will pass the automated testing
If you're correct, you'll get a message in the terminal saying "Your string_list appears to be correct"."""

# On the line below, create a list named string_list containing 7 strings
string_list = ["potato", "tomato", "celery", "carrots", "green beans", "onion", "garlic"]




# DON'T EDIT BELOW THIS LINE #
# I have code here that will help you know if your answer works
# Don't just copy and paste the list - that is NOT a valid answer
# Don't change the name of the list above or the error checking will not work correctly

def check_string_list_exists():
    try:
        print(f"string_list contains {string_list}\n")
        return True
    except NameError:
        print("It looks like string_list doesn't exist. Did you forget to create it or name it wrong?\n")
        return False


def check_string_list_length():
    if len(string_list) == 7:
        print("String_list contains 7 items as requested.\n")
        return True
    else:
        print(f"Oops, string_list contains {len(string_list)} items instead of 7.\n")
        return False


def check_string_list_contents():
    for n in range(len(string_list)):
        if type(string_list[n]) is str:
            print(f"Item {n + 1} is a string, as it should be.")
        else:
            print(f"Ooops, {string_list[n]} at index {n} is a {type(string_list[n])}")
            return False
    print("\n\nYour string_list appears to be correct\n\n")
    print("Try the fibonacci exercise now")
    return True

if check_string_list_exists():
    if check_string_list_length():
        check_string_list_contents()