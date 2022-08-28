print('Enter a 4 digit pin :: ')
pin = input()

# isdigit() method is to check whether the String is digit or not

pin_is_digit = pin.isdigit()
length_of_pin = (len(pin) == 4)

if (pin_is_digit and length_of_pin):
    print('Valid pin')
else:
    print('Invalid pin')