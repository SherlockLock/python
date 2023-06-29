############## Strings ##############
#     KEYWORD:          str

str = "a sequence of characters"
len(str) #Returns an int of the number of characters in the string
str.capitalize() #first letter is capitalized and the rest remain the same
str.count('e') #Returns an integer representing the number of times the element of substring appears in the string
str.find('')  #Returns the index of the first occurence of the substring
str.lower() #converts all chars to lowercase
str.upper() #converts all chars to uppercase
str.replace("old", "new")
str.replace("old", "new", "count")
' '.join(["some", "cool", "message"]) # A function that can be used with any iterable containing all strings and concatenate them using the string the function has been called on as a separator
# ^ returns -> "some cool message"

msg = "Hey {name}, my favorite number is {num}"
msg.format(name = "Epsilon", num = 8)

