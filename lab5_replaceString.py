"""

5. Replace String
Write a function replaceString() that takes an original string, a target string, and a replacement string as parameters and returns a new string with the first instance of the target string replaced with the replacement string.

replaceString("Computer science is fun.", "science", "programming")
# returns "Computer programming is fun."

replaceString("Python is difficult.", "difficult", "really easy")
# returns "Python is really easy."

"""

#CODE 
#YOUR
#FUNCTION BELOW HERE
def replaceString(org, target, replace):
  first_tar = org.find(target)
  last_char_tar = target[-1]
  last_tar = org.find(last_char_tar)
  first = org[0 : first_tar]
  last = org[last_tar + 1 :]
  ans = first + replace + last
  return ans
print(replaceString("Hello World!", "Hello", "Goodbye"))










"""

++++++++++++++++++++
don't code below here
++++++++++++++++++++++
"""
if __name__ == "__main__":
  x = input("Enter in a string: \n")
  y = input("Enter in a target string: \n")
  z = input("Enter in a replacement string: \n")
  print(replaceString(x, y, z))   
