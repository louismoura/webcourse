print(5)
print("Hello World")


weight = 81
height = 190
age = 23

bmr = 66.5 + (13.75 * weight) + (5 * height) - (6.755 * age)
bmr = round(bmr)
print("%s Calories/day" % bmr)