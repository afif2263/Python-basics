# value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# value = 1
# while value <= 10:
#     value +=1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value now equal to " + str(value))

# names = ["Saniat", "Emad", "Sabbir"]
# for x in names:
#     print(x)

# for x in "Mississippi":
#     print(x)

# for x in names:
#     if x == "Emad":
#         break
#     print(x)

# for x in names:
#     if x == "Emad":
#         continue
    # print(x)

# for x in range(4):
#     print(x)

# for x in range(2,4):
#     print(x)

# for x in range(5, 101, 5):
#     print(x)
# else:
#     print("Glad that\'s over!")

names = ["Emad", "Sabbir", "Saniat"]
actions = ["reads", "paints", "oils"]

for name in names:
    for action in actions:
        print( name + " " + action)
