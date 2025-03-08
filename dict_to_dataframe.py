import pandas as pd

# Sample nested dictionary
student = {
    "Employee": [
        {"name": "Pratik", "age": 22, "department": "IT"},
        {"name": "Dipak", "age": 21, "department": "HR"},
        {"name": "Sohail", "age": 21, "department": "Finance"}
    ]
}

# Converting dictionary to dataframe
df = pd.DataFrame(student["Employee"])
print(df)

"""
     name  age department
0  Pratik   22         IT
1   Dipak   21         HR
2  Sohail   21    Finance
"""
