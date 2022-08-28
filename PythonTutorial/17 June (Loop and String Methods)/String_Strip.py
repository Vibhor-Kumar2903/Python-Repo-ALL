mobile_no = "   8920097461   "
# strip() method will remove extra spaces from start(Leading) and end(Trailing)
print(mobile_no.strip())

mobile_no = "   89200    97461   "
# strip() method will not remove extra spaces from middle
print(mobile_no.strip(" "))

name = ".vibhor."
# strip() method will remove extra dot from start and end
print(name.strip("."))

name = ".V.Kumar."
# strip() method will not remove extra dot from middle
print(name.strip("."))

msg = " , . ,,, .. , String.,....   ,, "
print(msg.strip("., "))

