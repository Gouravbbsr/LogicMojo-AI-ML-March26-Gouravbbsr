import numpy as np

# Initial salary
salary = np.array([20000, 30000, 40000])
print("Original Salaries:", salary)

# 1. Add bonus 10%
salary_with_bonus = salary * 1.10
print("Salaries with 10% Bonus:", salary_with_bonus)

# 2. Reshape
# Reshaping to (3, 1) to prepare for horizontal stacking
salary_reshaped = salary_with_bonus.reshape(3, 1)
print("\nReshaped Salary (3, 1):\n", salary_reshaped)

# 3. Combine with experience
experience = np.array([2, 5, 8]).reshape(3, 1)
# Combining experience (column 1) and salary (column 2)
employee_data = np.hstack((experience, salary_reshaped))
employee_data = employee_data.astype(int)

print("\nCombined Data (Experience, Salary):\n", employee_data)



age = [25,30,35,45]
salary_new = [40000, 50000,60000,70000]
experience_new = [2,5,7,10]

