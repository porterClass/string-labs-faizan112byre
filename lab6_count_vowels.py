"""

6. Count Vowels
Write a function count_vowels() that takes a string as a parameter and returns the number of vowels (a, e, i, o, u) in the string.

count_vowels("hello")  # returns 2
count_vowels("world")  # returns 1
count_vowels("Python")  # returns 1
"""

#CODE 
#YOUR
#FUNCTION BELOW HERE
def count_vowels(string):
  ans = 0
  for let in string:
    if let == "a":
      ans += 1
    elif let == "e":
      ans += 1
    elif let == "i":
      ans += 1
    elif let == "o":
      ans += 1
    elif let == "u":
      ans += 1
  return ans 














"""
++++++++++++++++++++
don't code below here
++++++++++++++++++++++
"""
if __name__ == "__main__":
  x = input("Enter in a string to count the vowels of: \n")
  print(count_vowels(x))