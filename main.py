# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array): 
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)
'''
How does this solution ensure data immutability?
  #its immutable because the original array is being changed, the flatten/sorted array is being appended to the "arr" array

Is this solution a pure function? Why or why not?
  #this is pure because "flatten_and_sort" doesnt alter the array value

Is this solution a higher order function? Why or why not
  #yes because it returns the function sorted()

Would it have been easier to solve this problem using a different programming style?
  #No I thing functional is the best style because of the stipulations of 
  creating an immutable and pure function

Why in particular is functional programming a helpful paradigm when solving this problem? 
  #it avoids mutable data
'''

#Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. 
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  # Define a repair() method that will update the condition of the podracer to "repaired".
  def repair(self):
    self.condition = "repaired"
    
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def boost(self):
    self.max_speed *= 2
    
# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def flame_jet(self,other):
    other.condition = "trashed"

'''
How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
  #Encapsulate: solution consist of multiple objects that controls their on state
  #Inheritance: allows you to inherit properties and methods of the other objects
  #Polymorphism:solutions allows you to update/override methods of the other objects

Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
  #Not easier because this problem requires you to reuse code. OOP allows you to reuse code without rewriting the code each time.

How in particular did Object Oriented Programming assist in the solving of this problem?
  #The ability to reuse code 
'''