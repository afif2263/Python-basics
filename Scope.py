
count = 1
def another(name):
    colour= "Blue"
    global count
    count += 1
    print(count)
    
    def greeting(name):
        nonlocal colour
        color = "red"
        print(color)
        print(name)

    greeting(name)

another("afif")

