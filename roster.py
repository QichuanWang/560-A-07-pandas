import pandas as pd

player = {"Last Name": ["Bacot", "Davis", "Cadeau", "Evans", "High", "Brown", "Dixon", "Young", "Denis", "Davis"],
          "First Name": ["Armando", "RJ", "Elliot", "Kyan", "Zayden", "James", "Derek", "Jaydon", "Isaiah", "Elijah"],
          "height": [83, 72, 73, 74, 82, 82, 77, 76, 76, 75],
          "weight": [240, 180, 180, 175, 230, 240, 200, 200, 180, 205]}
data = pd.DataFrame(player)

# BMI = weight in kg / height in meters squared
data["BMI"] = round((data ["weight"] / 2.205) / ((data ["height"] / 39.37) ** 2), 2)

print(data)
data.to_csv("bmi.csv")