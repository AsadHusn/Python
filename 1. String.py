# strings are immutable in python

s = "HELLO WORLD"

s.upper()
s.lower()

# remove whitespace
s.strip()

# Replace String
s.replace("H", "J")

# returns a list where the text between the specified separator becomes the list items
s.split(',')

# Slicing
s[2:5]
# from start
s[:5]
# to end
s[2:]
# Negative Indexing
s[-5:-2]

# return index of searched letter
print(s.index("R"))

# Format String
txt = "My name is John, and I am {}"
print(txt.format(36))

myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(25, 30, 35))

# multiline string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

# Check String
# if a certain phrase or character is present in a string with 'in'
txt = "The best things in life are free!"
if "free" in txt:
    print("ok")