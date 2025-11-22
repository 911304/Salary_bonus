import sys

def calculate_bonus(salary):
    """Calculates 10% bonus and total salary."""
    bonus_rate = 0.10
    bonus_amount = salary * bonus_rate
    total_salary = salary + bonus_amount
    return bonus_amount, total_salary

if _name_ == "_main_":
    # In a real Jenkins job, the salary might be passed as an environment variable or argument
    # For this example, we'll assume a hardcoded value or one passed via command line
    try:
        if len(sys.argv) > 1:
            employee_salary = float(sys.argv[1])
        else:
            # Example hardcoded salary if no argument is provided
            employee_salary = 50000 
        
        bonus, total = calculate_bonus(employee_salary)
        print(f"Employee Salary: ${employee_salary:,.2f}")
        print(f"Bonus amount (10%): ${bonus:,.2f}")
        print(f"Total salary after adding bonus: ${total:,.2f}")
    except ValueError:
        print("Invalid salary input. Please provide a numeric value.")
