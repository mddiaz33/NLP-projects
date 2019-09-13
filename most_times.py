#asks the user for an integer number ”n”, then asks the user for ”n” integers. 
#Once the user is done entering integers, your program outputs the one that is repeated the most. 

def most_times(nInts): 
  # max times a number has been repeated starting of as 0 times 
  mostTimes = 0
  #the number that has been repeated the most times, start off as the first number in the list 
  num = nInts[0]
  # loop through each number and check number of times that number is found in list using List.count
  for number in nInts: 
        numTimes = nInts.count(number) 
        if(numTimes > mostTimes): 
            mostTimes = numTimes 
            num = number
  
  return num 
nInts = []
#Ask user for number n 
n = int(input("Enter a number n: ") )
# prompt user of n integers and add them to a list 
for i in range(0, n): 
    x = int(input("Enter an Int: "))
  
    nInts.append(x) 
      
print(most_times(nInts))

