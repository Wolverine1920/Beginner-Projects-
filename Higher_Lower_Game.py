game_data = [
    {"name": "China", "population": 1444216107},
    {"name": "India", "population": 1393409038},
    {"name": "United States", "population": 331893745},
    {"name": "Indonesia", "population": 273523621},
    {"name": "Pakistan", "population": 225199937},
    {"name": "Brazil", "population": 213993437},
    {"name": "Nigeria", "population": 211400708},
    {"name": "Bangladesh", "population": 166303498},
    {"name": "Russia", "population": 145912025},
    {"name": "Mexico", "population": 130262216}
]
x = []
y = []
for i in range(len(game_data)):
    x.append(game_data[i]["name"])
    y.append(game_data[i]["population"])
print(x)
print(y)


def comparison(x, y):
    score = 0
    for i in range(len(x) - 1):
        print(f"{x[i]} has a population of {y[i]} ")
        answer = input(f"Does {x[i + 1]} has a population higher than {x[i]} ")
        if answer == "y":
            if y[i + 1] > y[i]:  # Corrected comparison for "higher"
                score += 1
                print(f"Correct! Score: {score}")
            else:
                print("Wrong! Game over.")
                break
        elif answer == "n":
            if y[i + 1] < y[i]:  # Corrected comparison for "lower"
                score += 1
                print(f"Correct! Score: {score}")
            else:
                print("Wrong! Game over.")
                break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
            break
    return score


user_input = input("Do u want to play a game of Higher or Lower Y/N")
if user_input.lower() == "y":
    final_score = comparison(x, y)
print(f"Final Score = {final_score}")