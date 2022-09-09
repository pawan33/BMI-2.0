# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi=float(int(weight) / float(height)**2)
final_bmi=round(bmi,2)

if final_bmi<18.5:
  print(f"Your BMI is {final_bmi}. You are underweight")
elif final_bmi<25:
  print(f"Your BMI is {final_bmi}. You have normal weight")
elif final_bmi<30:
  print(f"Your BMI is {final_bmi}. You slightly overweight")
elif final_bmi<35:
  print(f"Your BMI is {final_bmi}. You are obese")
else:
  print(f"Your BMI is {final_bmi}. You are clinically obese")
  



