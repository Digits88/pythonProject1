"""
Ushtrim 01
"""
# Jepet 1 metode me 2 parametra qe printon vleren e parametrave:
def funksion1(name, age):
    print(name, age)

#TODO: Me poshte gjeni cila nga alternativat e sakte per te thirrur metoden:

# funksion1("Emma", age=23)  # Alternativa 1

# funksion1(age=23, name="Emma")   # Alternativa 2

# funksion1(name="Emma", 23)   # Alternativa 3

# funksion1(age=23, "Emma")   # Alternativa 4

funksion1("Emma", 23) # Alternativa 5

# funksion1(23, "Emma") # Alternativa 6
#
# """
# Ushtrim 02
# """
# # Jepet 1 metode me 2 parametra qe printon vleren e parametrave dhe me pas therrasim metoden:
# def funksion2(name, age=20):
#     print(name, age)
#
# funksion2('Emma', 25)
#
# # //TODO Cili eshte rezultati i sakte nga 2 alternativat e meposhtme:
# #Alternativa 01:
# # Emma 25
#
# #Alternativa 02:
# # Emma 20
#
#
# """
# Ushtrim 03
# """
# # Jepet 1 metode me 1 parameter qe kthen vleren e shumes se parametrit me numrin 25:
# def funksion3(num):
#     return num + 25
#
# funksion3(5) # Therrasim metoden
#
# print(num) # Printojme vleren
#
# # //TODO Cili eshte rezultati i sakte nga alternativat e meposhtme:
# #Alternativa 01:
# # 25

#Alternativa 02:
# 5

#Alternativa 03:
# NameError

"""
Functions can be called only by its name, as it is defined independently. 
But methods can't be called by its name only, 
we need to invoke the class by a reference of that class in which it is defined, 
i.e. method is defined within a class and hence they are dependent on that class.
"""