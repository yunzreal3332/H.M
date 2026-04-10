import os
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.groq.com/openai/v1"
)

print("Welcome to your Smart Fitness Assistant!")

#  More accurate calorie calculation (Mifflin-St Jeor)
def calculate_calories(weight, height, age, activity, goal):
    bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5  # assuming male

    activity_levels = {
        "low": 1.2,
        "medium": 1.55,
        "high": 1.75
    }

    maintenance = bmr * activity_levels[activity]

    if goal == "gain weight":
        return int(maintenance + 400)
    elif goal == "lose weight":
        return int(maintenance - 400)
    else:
        return int(maintenance)

def calculate_protein(weight):
    return int(weight * 1.8)

def parse_foods(food_input):
    food_input = food_input.lower().replace("and", ",")
    return [f.strip() for f in food_input.split(",") if f.strip()]

def get_user_data():
    while True:
        try:
            weight = float(input("Enter your weight (kg): "))
            break
        except:
            print("Invalid input.")

    while True:
        try:
            height = float(input("Enter your height (cm): "))
            break
        except:
            print("Invalid input.")

    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except:
            print("Invalid input.")

    activity_options = ["low", "medium", "high"]
    while True:
        activity = input("Enter activity level (low / medium / high): ").lower()
        if activity in activity_options:
            break
        print("Invalid activity level.")

    goal_options = ["lose weight", "gain weight", "fitness"]
    while True:
        goal = input("Enter your goal (lose weight / gain weight / fitness): ").lower()
        if goal in goal_options:
            break
        print("Invalid goal.")

    foods_input = input("Enter available foods in your fridge: ")
    foods = parse_foods(foods_input)

    return weight, height, age, activity, goal, foods

def generate_plan(messages):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.7
    )
    return response.choices[0].message.content

#  Start
weight, height, age, activity, goal, foods = get_user_data()

calories = calculate_calories(weight, height, age, activity, goal)
protein = calculate_protein(weight)

messages = [
    {
        "role": "system",
        "content": """You are a strict professional fitness trainer and nutrition expert.

Rules:
- Only use foods provided by the user
- Do not add new foods
- Calculate protein correctly
- Meals must match target calories
- Keep plans simple and realistic
"""
    },
    {
        "role": "user",
        "content": f"""
User Data:
- Weight: {weight} kg
- Height: {height} cm
- Age: {age}
- Activity level: {activity}
- Goal: {goal}
- Available foods: {', '.join(foods)}
- Target calories: {calories}
- Required protein: {protein} g

Tasks:
1. Create a workout plan
2. Create a meal plan using ONLY available foods
3. Ensure calories are close to target
4. Add daily water reminders
5. Keep it clear and structured
"""
    }
]

while True:
    user_input = input("Type 'plan' or 'exit': ").lower()

    if user_input == "exit":
        print("Goodbye!")
        break

    elif user_input == "plan":
        print("\nGenerating your plan...\n")

        reply = generate_plan(messages)
        print(reply)

        messages.append({"role": "assistant", "content": reply})

    else:
        print("Invalid command.")