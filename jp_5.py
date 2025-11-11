import sys


if len(sys.argv) == 4:
    script_name = sys.argv[0]
    principal = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])
else:
    
    script_name = sys.argv[0]
    principal = 1000.0
    rate = 5.0
    time = 2.0

simple_interest = (principal * rate * time) / 100

print(f"Simple Interest = {simple_interest:.2f}")
