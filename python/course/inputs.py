# Basal Metabolic Rate Calculator

weight = int(input("Enter your weight in kg: \n"))
height = int(input("Enter your height in cm: \n"))
age = int(input("Enter your age: \n"))

# Mifflin St. Jeor Equation for males
bmr = 66.5 + (13.75 * weight) + (5 * height) - (6.755 * age)
bmr = round(bmr)
print("%s calories/day" % bmr)

