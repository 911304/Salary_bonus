import sys

if len(sys.argv) != 2:
    print("Usage: python salary.py <salary>")
    sys.exit(1)

salary = float(sys.argv[1])

bonus = salary * 0.10
total_salary = salary + bonus

print("Bonus Amount:", bonus)
print("Total Salary after Bonus:", total_salary)
