# Using match-case

status = 2

match status:
    case 1:
        print("Pending")
    case 2:
        print("Approved")
    case 3:
        print("Rejected")
    case _:
        print("Unknown status")
