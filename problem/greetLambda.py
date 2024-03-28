loud=lambda s:s.upper()
quiet=lambda s:s.lower()
reverse=lambda s:s[::-1]
repeat=lambda s:s+" "+s

def greet(time,name,fn):
    if time>=0 and time<12:
        return "Good Morning "+fn(name)
    elif time>=12 and time<18:
        return "Good Afternoon "+fn(name)
    else:
        return "Good Evening "+fn(name)



print(greet(1, "John", loud))
print(greet(2, "John", quiet))
print(greet(13, "John", reverse))
print(greet(19, "John", repeat))
print(greet(13, "Leslie Emmanuel Beadon", loud))
print(greet(19, "Leslie Emmanuel Beadon", quiet)) 
print(greet(5, "Leslie Emmanuel Beadon", reverse))
print(greet(1, "Leslie Emmanuel Beadon", repeat))
