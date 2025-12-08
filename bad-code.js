# Code très mauvais pour SonarQube
password = "123456"   # secret exposé

def add(a, b):
    return a + b

def add(a, b):  # duplication
    return a + b

if True == "True":     # bug logique
   print("Bad code")

