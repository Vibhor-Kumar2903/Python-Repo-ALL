# both start_index and end_index
msg1 = "Hey vibhor"
part1 = msg1[0:3]
print(part1)

# only end_index
msg2 = "Hey vibhor"
part2 = msg2[:3]
print(part2)

# only start_index
msg3 = "Hey vibhor"
part3 = msg3[4:]
print(part3)

# both index are blank
msg4 = "Hey vibhor"
part4 = msg4[:]
print(part4)

# both index with variable
msg5 = "Hey vibhor"
start_index = 4
end_index = 10
part5 = msg5[start_index:end_index]
print(part5)

# both index with variable
msg6 = "Hey vibhor"
start_index = 4
end_index = 9       # end_index is not includede
part6 = msg6[start_index:end_index]
print(part6)
