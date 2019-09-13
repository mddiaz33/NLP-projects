#Create a program that reads a filename from the command line 
# tells me the number of words (types), characters and lines in that file.
# A sample ouput of the program looks like types:345, chars:1034, lines:43.
import sys 
import re

#uses system arguments as file name 
with open(sys.argv[1], 'r') as f:
	# matches non white space  ,  or new lines 
	alltypes = re.findall(r'\S+|\n',f.read())

#counts number of lines 
lines = 0 
#count num chars 
chars = 0 
#empty dictionary
typeDic= {}
#loop thru all words and lines found
for t in alltypes:
#count lines and avoid adding them to dict or counting them as char 
  if t == '\n':
    lines += 1 
#counts chars and adds unique types to dictionary 
  else:
    chars += len(t)
    #get rid of non alphanumeric char
    cleant = re.sub("[^a-zA-Z0-9]+", "", t)
    #check if clean key already in dictionary/ lower and upper case types will count as same time 
    if cleant.lower() not in typeDic:
      typeDic.update({cleant.lower() : 1})
#calculates num of types
types = len(typeDic)

print ("types:{}, chars:{}, lines:{}".format(types,chars,lines))