from items import *

def add_device():
    name = input("What do you want to name your light?\n>>")
    device=Items(name)
    print("{} has been successfully created".format(device.name))
    return device
