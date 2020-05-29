print("********Welcome to Mr Robot Game********")

def Error():
    print("[x]Invalid Try again[x]")
    exit()

#dec is decison
dec = input("You're trap in dungeon with your friend.\nyou see a barrel.What do you do?\n(move barrel or stay)\n")
if (dec == "move barrel"):
    dec = input("the barrel roll aside and you found a tunnel.\nWhat do you do? (enter tunnel or stay)\n")
    if (dec == "enter tunnel"):
        dec = input("You found an Escape but your fiend is too weak to go.\nThey hand you a Note.What do you do? (read note or leave)\n")
        if (dec == "read note"):
            dec = input("its too dark to read the note.\nWhat do you do? (lite match or leave)\n")
            if (dec == "lite match"):
                dec = input("The Note says \"don't leave me here\".\ndo you leave your friend or stay? (leave or stay)\n")
                if (dec == "stay"):
                    print("Everything Ends here\n")
                elif (dec == "leave"):
                    dec = input("You Crawl through the tunnel.it leads you to the beach.\nWhat do you do? (look out or wait)\n")
                    if (dec == "look out" or dec == "wait"):
                        dec = input("There you saw a boat in water.\nWhat do you do? (get on boat or stay)\n")
                        if (dec == "get on boat" or dec == "stay"):
                            print("Congratulations!\nYou're Heading to the new World.")
                else:
                    Error()
            elif (dec == "leave"):
                dec = input("You Crawl through the tunnel.it leads you to the beach.\nWhat do you do? (look out or wait)\n")
                if (dec == "look out" or dec == "wait"):
                    dec = input("There you saw a boat in water.\nWhat do you do? (get on boat or stay)\n")
                    if (dec == "get on boat" or dec == "stay"):
                        print("Congratulations!\nYou're Heading to the new World.")
            else:
                Error()
        elif (dec == "leave"):
                dec = input("You Crawl through the tunnel.it leads you to the beach.\nWhat do you do? (look out or wait)\n")
                if (dec == "look out" or dec == "wait"):
                    dec = input("There you saw a boat in water.\nWhat do you do? (get on boat or stay)\n")
                    if (dec == "get on boat" or dec == "stay"):
                        print("Congratulations!\nYou're Heading to the new World.")
        else:
            Error()
    elif (dec == "stay"):
        dec = input("You're friend hand you a Note.What do you do? (lite match or read)\n")
        if (dec == "lite match" or dec == "read"):
            dec = input("The Note says \"don't leave me here\".\ndo you leave your friend or stay? (leave or stay)\n")
            if (dec == "stay"):
                print("Everything Ends here\n")
            elif (dec == "leave"):
                dec = input("You Crawl through the tunnel.it leads you to the beach.\nWhat do you do? (look out or wait)\n")
                if (dec == "look out" or dec == "wait"):
                    dec = input("There you saw a boat in water.\nWhat do you do? (get on boat or stay)\n")
                    if (dec == "get on boat" or dec == "stay"):
                        print("Congratulations!\nYou're Heading to the new World.")
            else:
                Error()
    else:
        Error()

elif (dec == "stay"):
    dec = input("You're friend hand you a Note.What do you do? (lite match or read)\n")
    if (dec == "lite match" or dec == "read"):
        dec = input("The Note says \"don't leave me here\".\ndo you leave your friend or stay? (leave or stay)\n")
        if (dec == "stay"):
            print("Everything Ends here\n")
        elif (dec == "leave"):
                    dec = input("You Crawl through the tunnel.it leads you to the beach.\nWhat do you do? (look out or wait)\n")
                    if (dec == "look out" or dec == "wait"):
                        dec = input("There you saw a boat in water.\nWhat do you do? (get on boat or stay)\n")
                        if (dec == "get on boat" or dec == "stay"):
                            print("Congratulations!\nYou're Heading to the new World.")
        else:
            Error()

else:
    Error()
