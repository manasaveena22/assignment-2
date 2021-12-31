#list methods

string_list = [1,2,3,4,5]
string_list2=[6,7,8,9,10]
string_list3=['a','d','c','b']
#append
string_list.append(6)
print(string_list)
#pop
string_list.pop()
print(string_list)
#copy
string_list.copy()
print(string_list)
#count
string_list.count(5)
print(string_list)
#index
string_list.index(5)
print(string_list)
#remove
string_list.remove(5)
print(string_list)
#extend
string_list.extend(string_list2)
print(string_list)
#insert
string_list.insert(0,'0')
print(string_list)
#reverse
string_list.reverse()
print(string_list)
#clear
string_list.clear()
print(string_list)
#sort
string_list3.sort()
print(string_list3)

#changing value in tuple

x = ("a", "b", "c")
y = list(x)
y[1] = " "
x = tuple(y)

print(x)

#set
thisset = {"a", "b", "c"}
print(thisset)

#dictionary methods

student = {
  "name": "xyz",
  "branch": "ece",
  "roll": 12
}

#copy
x = student.copy()
print(x)
#get
x = student.get("roll")
print(x)
#items
x = student.items()
print(x)
#keys
x = student.keys()
print(x)
#pop
student.pop("branch")
print(student)
#popitem
student.popitem()
print(student)
#setdefault
x = student.setdefault("name", "ABC")
print(x)
#update
student.update({"year": "3"})
print(student)
#values
x = student.values()
print(x)
#clear
student.clear()
print(student)
#from key
x = ('a', 'b', 'c')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

#string methods

#capayalize
txt = "hello world."
x = txt.capitalize()
print (x)
#casefold
txt = "Hello World!"
x = txt.casefold()
print(x)
#count
txt = "hello world."
x = txt.count("world")
print(x)
#encode
txt = "My name is abc"
x = txt.encode()
print(x)
#endswitch
txt = "Hello world."
x = txt.endswith(".")
print(x)
#expandtabs
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(0)
print(x)
#find
txt = "Hello world."
x = txt.find("world")
print(x)
#format
txt = "For only {price:.2f} ruppes!"
print(txt.format(price = 49))
#index
txt = "Hello world."
x = txt.index("world")
print(x)
#isalnum
txt = "hello123"
x = txt.isalnum()
print(x)
#isalpha
txt = "world456"
x = txt.isalpha()
print(x)
#isdecimal
txt = "\u0033" 
x = txt.isdecimal()
print(x)
#isdigit
t = "789"
x = txt.isdigit()
print(x)
#isidentifier
txt = "D"
x = txt.isidentifier()
print(x)
#islower
txt = "hello world!"
x = txt.islower()
print(x)
#isnumeric
txt = "135"
x = txt.isnumeric()
print(x)
#isprintable
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)
#is space
txt = " "
x = txt.isspace()
print(x)
#istitle
txt = "Hello World!"
x = txt.istitle()
print(x)
#isupper
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)
#join
my = ("a", "b", "c")
x = "#".join(my)
print(x)
#1just
txt = "hello"
x = txt.ljust(2)
print(x, "world.")
#lower
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)
#lstrip
txt = "   hello    "
x = txt.lstrip()
print(" ", x, "world")
#maketrans
txt = "Hello S!"
mytable = txt.maketrans("S", "w")
print(txt.translate(mytable))
#partition
txt = "hello world"
x = txt.partition("world")
print(x)
#replace
txt = "hello world"
x = txt.replace("world", "friends")
print(x)
#rfind
txt = "a b,c b."
x = txt.rfind("casa")
print(x)
#rindex
x = txt.rindex("b")
print(x)
#rjust
txt = "hello"
x = txt.rjust(2)
print(x, "world.")
#rpartition
txt = "hello world"
x = txt.rpartition("world")
print(x)
#rsplit
txt = "a, b, c"
x = txt.rsplit(", ")
print(x)
#rstrip
txt = "   hello   "
x = txt.rstrip()
print(" ", x, "world")
#split
txt = "welcome to python"
x = txt.split()
print(x)
#splitlines
txt = "hello\nWorld"
x = txt.splitlines()
print(x)
#startswith
txt = "Hello world."
x = txt.startswith("Hello")
print(x)
#strip
txt = "    hello    "
x = txt.strip()
print("  ", x, "world")
#swapcase
txt = "Hello World"
x = txt.swapcase()
print(x)
#title
txt = "Hello world"
x = txt.title()
print(x)
#translate
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))
#upper
txt = "Hello my friends"
x = txt.upper()
print(x)
#zfill
txt = "50"
x = txt.zfill(30)
print(x)












