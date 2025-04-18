band = { "vocals":"Plants", "Guitar": "Page"}
band2 = dict(vocals="Plant", Guitar="Page")


print(band)
print(band2)
print(type(band))
print(len(band))


print(band["vocals"])
print(band.get("Guitar"))

print(band.values())
print(band.items())
print("Triangle" in band)

band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)

print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)


band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

band2 = band #not to be used
print(band)

band["drums"] = "Dave"
print(band)

band2 = band.copy()
band2["drums"] = "Dave"
print(band)

member1 = {"name": "Plant", "instrument": "Vocals"} 
member2 = {"name": "Page", "instrument": "Guitar"}

band = {"member1": member1, "member2": member2}
print(band)
print(band["member1"]["name"])

nums = {1, 2, 3, 4}
nums = set((1, 2, 3, 4))

nums.add(8)
print(nums)

morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

A = {1, 2, 3}
B = {2, 3, 4}

mynewset = A.union(B)
print(mynewset)

A.intersection_update(B)
print(A)

A = {1, 2, 3}
B = {2, 3, 4}

A.symmetric_difference_update(B)
print(A)

newset = A.intersection(B)
print(newset)
