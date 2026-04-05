import numpy as np

# Original Lists
age_list = [25, 30, 35, 40]
salary_list = [40000, 50000, 60000, 70000]
experience_list = [2, 5, 7, 10]

# 1. Convert all into numpy arrays
age = np.array(age_list)
salary = np.array(salary_list)
experience = np.array(experience_list)


# 2. Convert all arrays into column format
age_col = age.reshape(-1, 1)
salary_col = salary.reshape(-1, 1)
experience_col = experience.reshape(-1, 1)



# 3. Combine all features into a dataset (as float)
dataset = np.hstack((age_col, salary_col, experience_col)).astype(int)

print(dataset)

# 4. Increase all salaries by 10%
# The salary is in the second column (index 1)
dataset[:, 1] = dataset[:, 1] * 1.1

print(dataset)

# 5. Normalize salary (divide by max salary)
max_salary = np.max(dataset[:, 1])
dataset_normalise = dataset[:, 1] / max_salary

print(f"--- Step 5: Normalized Salaries (Divided by max: {max_salary}) ---")
print(dataset_normalise)
print()

# 6. Extract all ages, first employee record
all_ages = dataset[:, 0]
first_employee = dataset[0, :]

print("All Ages:", all_ages)
print("First Employee Record:", first_employee)
print()

# 7. Calculate mean salary, median experience and std dev of age
mean_salary = np.mean(dataset[:, 1])
median_exp = np.median(dataset[:, 2])
std_age = np.std(dataset[:, 0])

print(f"Mean Salary (Normalized): {mean_salary:.4f}")
print(f"Median Experience: {median_exp}")
print(f"Std Dev of Age: {std_age:.2f}")
print()

# 8. Iterate through dataset and print each row
for row in dataset: 
    print(row)