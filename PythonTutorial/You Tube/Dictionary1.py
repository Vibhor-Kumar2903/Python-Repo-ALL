stuff = {"Airtel":70, "Jio":99, "Vi":49}

print(stuff.get("Airtel"))

print(stuff.items())

print(stuff.keys())

print(stuff.setdefault("Jio"))
print(stuff)

print(stuff.setdefault("Amazon prime", 123))
print(stuff)

print(stuff.popitem())      # it will remove the last item from the dictionary
print(stuff)