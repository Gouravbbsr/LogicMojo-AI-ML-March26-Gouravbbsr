input_data = [
    (101, "Rahul", 80000, "India", "Fraud"),
    (102, "Amit", 30000, "India", "Safe"),
    (103, "John", 90000, "USA", "Fraud"),
    (101, "Rahul", 80000, "India", "Fraud"),
    (104, "Sara", 40000, "USA", "Safe"),
    (105, "Mike", 120000, "USA", "Fraud")
]

unique_data= list(dict.fromkeys(input_data))
customers =[]
countries = set()
fraud_count: int = 0
results = []
for row in unique_data:
    cust_id, name, income, country, status = row
    if income < 40000:
        continue
    if income > 100000:
        print("Very high value customer")
        continue
    customer = {"id": cust_id, "name": name, "country": country, "status": status}
    customers.append(customer)
    countries.add(country)
    if status == "Fraud":
        fraud_count += 1    # pyre-ignore
    if income > 80000:
        if status == "Fraud":
            label = "High risk and high value"
        else:
            label = "high value safe"
    else:
        label = "Normal"
    output = (cust_id, label)
    results.append(output)
print("Unique Data: ", unique_data)
print("Customers: ", customers)
print("Countries: ", countries)
print("Fraud count: ", fraud_count)
print("Result: ", results)


