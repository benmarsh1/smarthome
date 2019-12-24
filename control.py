from add import *

device=add_device()

def change_colour():
    device.Light.r = int(input("What red value do you want?\n>>"))
    device.Light.g = int(input("What green value do you want?\n>>"))
    device.Light.b = int(input("What blue value do you want?\n>>"))



