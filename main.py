


def sec_in_year():
    age = int(input("Enter your age: "))
    days = 365
    hours = 24
    min = 60
    sec = 60
    final_num = 0



    days = age * days
    hours = hours * days
    min = min * hours
    sec = sec * min

    final_num = days + hours + min + sec






    print(final_num)


sec_in_year()
