
scores_input = input("Enter scores separated by spaces: ")
scores = [float(num) for num in scores_input.split()]

total = sum(scores)
average = total / len(scores)

maximum = max(scores)
minimum = min(scores)

print(f"Sum of scores = {total}")
print(f"Average score = {average:.2f}")
print(f"Maximum score = {maximum}")
print(f"Minimum score = {minimum}")
