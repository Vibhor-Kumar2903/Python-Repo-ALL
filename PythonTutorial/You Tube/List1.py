mobile = ["Apple","One+", "Redmi", "Oppo", "Vivo"]

print(mobile)
for cell in mobile:
    print(cell)

telecom = ["Jio", "Airtel", "Vi"]

print(telecom)
for comms in telecom:
    print(comms)

mobile.append("Samsung")
telecom.append("BSNL")

mobile.extend(telecom)

print(mobile)