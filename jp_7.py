import sys

if len(sys.argv) <= 1:
    print("Error: No scores passed. Provide scores like: python jp_7.py 10 20 30")
    sys.exit(1)

scores = [float(num) for num in sys.argv[1:]]

total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print(f"Sum of scores = {total}")
print(f"Average score = {average:.2f}")
print(f"Maximum score = {maximum}")
print(f"Minimum score = {minimum}")
