import random
from game_data import data
from art import logo, vs

# Taking all numbers of data
random_number = []
for index, element in enumerate(data):
    random_number.append(index)
stops = 0
score = 0
while stops == 0:
    # Taking randomly influencers
    compare_a = random.randint(min(random_number), max(random_number))
    random_number.remove(compare_a)

    compare_b = random.randint(min(random_number), max(random_number))
    random_number.remove(compare_b)

    proof_1 = f"Compare A: {data[compare_a]["name"]}, {data[compare_a]["description"]}, from {data[compare_a]["country"]}."

    proof_2 = f"Against B: {data[compare_b]["name"]}, {data[compare_b]["description"]}, from {data[compare_b]["country"]}."
    print(f"{proof_1} \n {vs} {proof_2}")

    # Comparing

    your_answer = input("Who has more followers? Type 'A' or 'B': ")

    if your_answer == "A":
        if data[compare_a]["follower_count"] > data[compare_b]["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            stops = 1
    elif your_answer == "B":
        if data[compare_a]["follower_count"] < data[compare_b]["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            stops = 1