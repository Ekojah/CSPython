ch = int(input("Choose a number between 1-4\t"))
match ch:
    case 1:
        print("You will have a discomboulatingly extravagant day")
    case 2:
        print("You will have an average day")
    case 3:
        print("Your day may be suboptimal")
    case 4:
        print("Just stay home lil bro")
    case _:
        print("Invalid choice")

