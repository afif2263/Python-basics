users = ['Jawad', 'Zadid', 'Tahsin']
data = ['Jawad', 21, True]

emptylist = []

print("Jawad" in emptylist)
print(users[0])
print(users[-2])

print(users.index("Zadid"))

print(len(data))

users.append('Adnan')
users += ['Shadik']
users.extend(['Nader', "Rijon"])
print(users)


users.insert(0, 'Naim')
print(users)


users[1:3] = [ 'Hassan', 'Safal']
print(users)

users.remove('Hassan')
print(users)

data.clear()
print(data)

users[1:2] = ['kushal']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

print(sorted(nums, reverse=True))

nums.sort(reverse=True)
print(nums)


numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

