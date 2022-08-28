stuff = {"Airtel":70, "Jio":99, "Vi":49}
print(stuff.items())

new_item = {"BSNL":94}
stuff.update(new_item)
print(stuff)

new_item = {"Airtel Xtream":499, "Jio Fiber":799}
stuff.update(new_item)
print(stuff)

new_update = {"BSNL Broadband":599}
stuff.update(new_update)
print(stuff)

stuff.update(Jio = 555)
print(stuff)

