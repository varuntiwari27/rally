#!flask/bin/python
class Animal:

  legs = 0

  def walk(self):
      print ("walking")

  def count_legs(self):
      print("number of legs %s" %self.legs)


puppy = Animal()
puppy.legs = 4

Kangaroo = Animal()
Kangaroo.legs = 2

puppy.count_legs()
