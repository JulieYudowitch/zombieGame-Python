import random

class Zombie:
  contagiousness = 10  
  def __init__(self, name, level, health):
    self.name = name
    self.level = level
    self.health = health
  def __repr__(self):
    rep = "My name is " + self.name + ". I am a level " + str(self.level) + " zombie.  I currently have " + str(self.health) + " health and I want to eat your braiiiiiins!"
    return rep  
  def walk(self):
    print(self.name + " wanders aimlessly groaning incoherently about brains.")  
  def eatBrains(self, target):
    if (target.immunity < self.contagiousness):
      target.infected = True
      self.contagiousness -= 1
      self.level += 1
      self.health += 1
      print(target.name + ", you are now infected and will be a zombie with me!")
    else:
      target.immunity -= 1
      self.health -= 1
  def incubateSickness(self):
    self.contagiousness += 1
    print("My contagiousness level is now " + str(self.contagiousness) + ".")  

class Paladin:
  holyWater = 5
  infected = False
  immunity = 10
  def __init__(self, name, level, health):
    self.name = name
    self.level = level
    self.health = health
  def __repr__(self):
    return "My name is " + self.name + " I am currently at level " + str(self.level) + " with " + str(self.health) + " health. I am a righteous paldin of the light."
  def cureZombieInfection(self, target):
    if (self.holyWater > 0 and target.infected):
      target.infected = False
      self.holyWater -= 1
      print(target.name + ", You are healed good citizen!")  
  def swordFight(self, target):
    self.power = random.randint(0,10)
    target.power = random.randint(0,10)
    if (self.power > target.power):
      target.health -= 2
      self.level += 1
    else:
      self.health -= 1  
  def heal(self):
    self.health += 1
  

class Mage:
  infected = False
  immunity = 10
  def __init__(self, name, level, health):
    self.name = name
    self.level = level
    self.health = health
  def __repr__(self):
    return "My name is " + self.name + " I am currently at level " + str(self.level) + " with " + str(self.health) + " health. I am a powerful mage."
  def fireball(self, target):
    self.power = random.randint(0,10)
    target.power = random.randint(0,10)
    if (self.power > target.power):
      target.health -= 3
    else:
      self.health -= 2   
  def magicBlast(self, target):
    self.power = random.randint(0,10)
    target.power = random.randint(0,10)
    if (self.power > target.power):
      target.health -= 4
      self.level += 1
    else:
      self.health -= 3    
  def iceCage(self, target):
    self.power = random.randint(0,10)
    target.power = random.randint(0,10)
    if (self.power > target.power):
      print(target.name + ", You are frozen and incapable of acting for 10 seconds!")

walker = Zombie("Walker", 5, 10)
creep = Zombie("Creep", 8, 5)
astirii = Paladin("Astirii", 10, 10)
nilua = Paladin("Nilua", 12, 8)
zara = Mage("Zara", 9, 6)
celicii = Mage("Celicii", 8, 10)
print(repr(walker))
print(repr(creep))
print(repr(astirii))
print(repr(nilua))
print(repr(zara))
print(repr(celicii))
walker.walk()
creep.walk()
creep.eatBrains(astirii)
creep.eatBrains(astirii)
walker.eatBrains(celicii)
walker.eatBrains(celicii)
walker.eatBrains(celicii)
walker.incubateSickness()
creep.incubateSickness()
astirii.cureZombieInfection(celicii)
astirii.swordFight(walker)
astirii.heal()
nilua.cureZombieInfection(zara)
nilua.swordFight(creep)
nilua.heal()
zara.fireball(creep)
zara.magicBlast(walker)
zara.iceCage(creep)
celicii.fireball(walker)
celicii.magicBlast(walker)
celicii.iceCage(walker)