"""
1. Concatenate Strings
Write a function concat() that takes as parameters two strings and returns the two strings concatenated together. Concatenate means to join two strings together.

concat("hello", "world")  # returns "hello world"
concat("jim", "bob")      # returns "jim bob"

"""

#CODE 
#YOUR
#FUNCTION BELOW HERE
def concat(String1, String2):
  String3 = String1 + " " + String2
  return String3
concat("Hello", "World")













"""
++++++++++++++++++++
don't code below here
++++++++++++++++++++++
"""
if __name__ == "__main__":
  x = input("Enter in a string: \n")
  y = input("Enter in another string: \n")
  print(concat(x,y))