#import the input list from the day1Input file
from day1Input import input

#Takes in the input array and determines if there's a combination that sums up to 2020 and returns the result of multiplying the 3 numbers together
def partTwo(entries):
  #creates a list of all the possible combination of the input array and groups them in 3s
  possibleCombinations = list(combinations(entries, 3))
  
  #Only accepting the unique combinations so there's no repeats of the same combination
  unq = set(possibleCombinations)

  #for each list in the set add the elements together and check if they equal 2020 if they are return the result of multiplying them together
  for a in unq:
    s = sum(a)
    if s == 2020:
      return a[0] * a[1] * a[2]


print(partTwo(input))