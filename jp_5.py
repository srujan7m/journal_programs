import sys


if len(sys.argv) == 4:
    script_name = sys.argv[0]
    principle = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])
else:
    
    script_name = sys.argv[0]
    principle = 1000.0
    rate = 5.0
    time = 2.0

simple_interest = (principle * rate * time) / 100

print(f"Simple Interest = {simple_interest:.2f}")
