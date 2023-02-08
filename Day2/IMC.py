#Calculo IMC
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

first = float((height))
second = int((weight))
result = (second / (first * first))

print("\nsee the interpretation of BMI\nBMI")
print("Menor que 18 | thinness | obesity(grau) 0")
print("Entre 18 e 24.9 | normal | obesity(grau) 0")
print("Entre 25 e 29.9 | overweight | obesity(grau) I")
print("Entre 30 e 39.9 | obesity | obesity(grau) II")
print("Maior que 40 | severe obesity | obesity(grau) III")

print(f"resultado: {round(result, 1)}")