d = {}

with open("activities.txt") as f:
    for line in f:
        (key, val) = line.split()
        d[str(key)] = val
    # print(d)

    # this value should be inputted by the user 
    accepted_value = input("What intensity level are you looking for? ") 
    for key, value in list(d.items()):
        if value != accepted_value:
            del d[key]

    print(d.keys())


# intensity_level = input("What intensity level are you looking for today? ")
