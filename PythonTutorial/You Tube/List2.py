mobile = ["Vivo", "Apple","One+", "Redmi", "Oppo", "Vivo"]
print(mobile)

telecom = ["Jio", "Airtel", "Vi"]
print(telecom)

mobile.remove("Oppo")
print(mobile)

telecom.pop(0)
print(telecom)

telecom.pop(-1)
print(telecom)

mobile.sort()
print(mobile)

print("Apple" in mobile) # To check membership of an entity in the list
print("Vivo" in mobile)

print(mobile.count("Vivo"))
print(mobile.count("Apple"))