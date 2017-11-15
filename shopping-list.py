shopping_list = []
master_opts = ["exit", "'exit'", "Exit", "'Exit'", "EXIT", "'EXIT'", "view", "'view'", "View", "'View'", "VIEW", "'VIEW'", "add", "'add'", "Add", "'Add'", "ADD", "'ADD'", "help", "'help'", "Help", "'Help'", "HELP", "'HELP'", "delete", "'delete'", "Delete", "'Delete'", "DELETE", "'DELETE'"]
exit_opts = ["exit", "'exit'", "Exit", "'Exit'", "EXIT", "'EXIT'"]
view_opts = ["view", "'view'", "View", "'View'", "VIEW", "'VIEW'"]
add_opts = ["add", "'add'", "Add", "'Add'", "ADD", "'ADD'"]
help_opts = ["help", "'help'", "Help", "'Help'", "HELP", "'HELP'"]
delete_opts = ["delete", "'delete'", "Delete", "'Delete'", "DELETE", "'DELETE'"]

cont = True
print("""If you wish to add items to your list, type in 'add'.\nIf you wish to delete items from your list, type in 'delete'.\nIf you wish to stop adding items, type in 'exit'.\nIf you wish to see what you have added, type in 'view'.\nIf you wish to see available commands, type in 'help'.\n""")

def shopping():
    global cont
    global opt
    while cont == True:
        opt = input("What would you like to do?: ")
        if opt in exit_opts:
            exit_mode()
        elif opt in view_opts:
            view_mode()
        elif opt in help_opts:
            help_mode()
        elif opt in delete_opts:
            delete_mode()
        elif opt in add_opts:
            add_mode()
        else:
            print("\nI am sorry, but that is not an acceptable answer. Please try again.")

def exit_mode():
    global cont
    if len(shopping_list) == 0:
        print("""\nYou have exited the program.\nYou have no items on your shopping list.""")
    else:
        print("""\nYou have exited the program.\nYour finalized shopping list is:""")
        print(shopping_list[:])
    cont = False

def view_mode():
    print("""\nYou are now in view mode.""")
    if len(shopping_list) == 0:
        print("""\nYou have no items in your shopping list right now.
        """)
    else:
        print("""\nYour current shopping list is:""")
        print(shopping_list[:],"\n")

def help_mode():
    print("""\nYou are now in help mode.\nIf you wish to exit the program, type 'exit'.\nIf you wish to add more items, type 'add'.\nIf you wish to delete items, type 'delete'.\nIf you wish to ask for help, type 'help' (but you should already know that if\n    you're here, you dingus.)\nIf you wish to view your current list, type 'view'.\n""")

def add_mode():
    print("""\nYou are currently in add mode.\nType in what items you would like to add.\nIf you would like to exit add mode, type in 'end'.\nYou will not be prompted to type in 'end'.\n""")
    cont1 = True
    while cont1 == True:
        item = input("What item would you like to add?: ")
        if item in master_opts:
            print("""\nYou cannot access any other commands before exiting add mode.\nPlease type 'end' if you wish to access other commands.\n""")
        elif item in shopping_list:
            print("""\nThat item is already in your list!\n""")
        elif item == "end":
            print("""\nYou have exited add mode.
            """)
            cont1 = False
        else:
            shopping_list.append(item)

def delete_mode():
    global cont3
    if len(shopping_list) == 0:
        print("""\nYou currently have no items to remove.
        """)
    else:
        print("""\nYou are currently in delete mode.\nType in what items you would like to delete.\nIf you would like to exit delete mode, type in 'end'.\nYou will not be prompted to type in 'end'.\n""")
        cont3 = True
        cont2 = input("Would you like to view your list before continuing? [Y/N]: ")
        while cont2 not in ["Y", "y"] and cont2 not in ["N", "n"]:
            print("""\nThat is unacceptable. Please choose another answer.\n""")
            cont2 = input("Would you like to view your list before continuing? [Y/N]: ")
        if cont2 in ["Y","y"]:
            print("""\nYour current list is:""")
            print(shopping_list[:],"""
            """)
        while cont3 == True:
            if cont2 == "end":
                print("""\nYou have exited delete mode.
                """)
                cont3 = False
            else:
                item = input("What item would you like to delete? Please type one item at a time.: ")
                if item == "end":
                    print("""\nYou have exited delete mode.
                    """)
                    cont3 = False
                elif item in master_opts:
                    print("""\nYou cannot access any other commands before exiting delete mode. \nPlease type 'end' if you wish to access other commands.\n""")
                elif item not in shopping_list:
                    print("""\nThat item is not in your list.\nPlease check to make sure your spelling is correct.\n""")
                else:
                    shopping_list.remove(item)

shopping()