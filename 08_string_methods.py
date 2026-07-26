name = "vipul"
age = 20

text = "saloni,longdistance,vipul"
fruits = ["Apple", "Banana", "Mango"]

print(len(name)) 
print(name.upper()) 
print(name.lower()) 
print(name.capitalize()) 
print(text.title()) 
print(text.strip()) 
print(text.lstrip())
print(text.rstrip())
print(text.replace("saloni", "vipul"))
print(text.find("saloni"))
print(text.count("a"))
print(text.startswith("sa"))
print(text.endswith("on"))
print(text.split(","))
print(",".join(fruits))
print("python".isalpha())
print("12345".isdigit())
print("python123".isalnum())
print("  ".isspace())
print(text.swapcase())
print("python".center(20))
print("15".zfill(5))
print("My name is {} and I am {} year old.".format(name,age))
print("py" in text)
print("java" not in "python")
