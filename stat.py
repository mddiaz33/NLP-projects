
#program performs common stats
#takes a list of numbers as a parameter and returns the average

def avg(List):
  return sum(List)/ len(List)


#takes a list of numbers as a parameter and returns a list with the corresponding values squared
def l_sqr(List):
  squared = []
  for num in List:
     squared.append(num**2)
  return squared


# takes list of numbers and computes variance
def var(List):
  var = 0
  currAvg = avg(List)
  for i in (List):
    var +=  (List[i]- currAvg)**2

  #not sure if you said to divide the total sum by the number of items.....but I believe we did so in class
  return var / len(List)


