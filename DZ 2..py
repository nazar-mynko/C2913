class Student:
  def __init__(self, name = Nope):
    self.name = name
  def __str__(self):
    return f"My name si {self.name}"
nick = Student(name = "Bob")
print(nick.test()) 



import random



class Student:
  def __init__(self, name):
    self.name = name
    self.gladness = 50
    self.progress = 0
    self.money = 500
    self.alive = True
  def to_study(self):
    print("Time to study")
    self.progress +- 0.12
    self.glandess -= 5
  def to_sleep(self):
    print("I will sleep")
    self.glandess += 3
  def to_chill(self):
    print("Time to rest")
    self.glandess += 5
    self.progress -= 0.1
    self.monty -= 60
   def to_work(self):
       print("NA ROBOTY")
       self.money += 50
       self.glandes -=5
       self.progres += 0.05
   def is_alive(self):
    if self.progress < -0.5:
      print("OTCHOSLENO")
      self.alive = False
    elif self.glandess <=0:
      print("UMER OT DEPRESII")
      self.alive = False
    elif self.progress > 5:
      print("Extern")
      self.alive = False
    elif salf.monty <= -200:
       print("NETU DENEG")
  def end_of_day(self):
    print(f"Gladness = {self.gladness}")
    print.(f"Progress = {round(self.progress, 2)}")
  def live(self, day):
      day = "Day" + str(day) + "of" + self.name + "life"
    print(f"{day:=^50}}")
    live_cube = random.randit(1, 3)
    if live_cube == 1:
      self.to_study()
elif live_cube == 2:
       self.to study()
elif live_cube == 3:
       self.to chill()
       self.end_of_day()
       self.is alive()
elif live_cube == 4:
     self.to_work()


nick = Student(name = "Anatolii")
for day in range(365):
  if nick.alive == False:
    break
  nick.live(day)
