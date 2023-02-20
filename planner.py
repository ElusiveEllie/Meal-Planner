min_cal_budget = ""
while type(min_cal_budget) != int:
  try:
    min_cal_budget = int(input("Set minimum daily calorie budget: "))
  except:
    print("Please input an integer.")

max_cal_budget = ""
while type(max_cal_budget) != int:
  try:
    max_cal_budget = int(input("Set maximum daily calorie budget: "))
    if max_cal_budget < min_cal_budget:
      max_cal_budget = ""
      print("Please enter a number greater than or equal to the minimum calorie budget.")
  except:
    print("Please input an integer.")

food_dictionary = {
    "overnight_oats": 440,
    "huevos_rancheros_tostadas": 543, 
    "burrito_bowl": 840,
    "chopped_cheese": 870,
    "green_goddess_salad": 548,
    "katsu_curry": 1158,
    "gochujang_fried_rice": 486,
    "chicken_salad_sandwich": 390,
    "pesto_ceasar_chicken_wrap": 705,
    "parmesean_nut_crusted_salmon": 761,
    "quest_bar": 190,
    "soylent_protein_drink": 250,
    "truffle_mushroom_burger_w/fries": 1623
}

def daily_meal_planning(food_dictionary):
  possible_meal_plans = find_meal_plans(food_dictionary)
  num_meal_plans = len(possible_meal_plans)
  print(f"there are {num_meal_plans} possible meal plans you can make with your current food supply")

def find_meal_plans(food_dictionary):
  ### your code here ###
  meal_plans = []
  food_list = food_dictionary.items()
  queue = []
  for food in food_list:
    queue.append({food})
  while queue:
    current_meal = queue.pop(0)
    calorie_count = 0
    for item in current_meal:
      calorie_count += item[1]
    for food in food_list:
      if food in current_meal or current_meal.union((food,)) in meal_plans:
        continue
      if calorie_count + food[1] <= max_cal_budget:
        new_meal = current_meal.union((food,))
        queue.append(new_meal)
        if calorie_count + food[1] >= min_cal_budget:
          meal_plans.append(new_meal)
  for i in range(len(meal_plans)):
    total_calories = 0
    for item in meal_plans[i]:
      total_calories += item[1]
    meal = list(meal_plans[i])
    meal.append(f"Total calorie count: {total_calories}")
    meal_plans[i] = meal

  for meal in meal_plans:
    print(meal)


  return meal_plans

run = "Y"
while run == "Y":
  daily_meal_planning(food_dictionary)
  run = input("Press enter to close.")
