# Add your code here
medical_costs = {"Mariana" : 6607.0, "Vinay" : 3225.0 }

medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0,"Valentina": 6420.0})

print(medical_costs)
print()

medical_costs["Vinay"] = 3325.0

print(medical_costs)
print()

total_cost = 0

for cost in medical_costs.values():
  total_cost += cost

average_cost = total_cost / len(medical_costs)
print("Average Insurance Cost : " + str(average_cost))
print()

names = {"Marina", "Vinay", "Connie","Isaac","Valentina"}
ages = {27, 24, 43, 35 , 52}

zipped_ages = list(zip(names,ages)) 
print(zipped_ages)
print()

names_to_ages = {key:value for key, value in zipped_ages}
print(names_to_ages)
print()

mariana_age = names_to_ages.get("Marina")
print("Marina's age is " + str(mariana_age))
print()

medical_records = {}

medical_records["Mariana"] = {"Age":27, "Sex": "Female", "BMI":31.1, "Childre":2, "Smoker": "Non_smoker","Insurance_cost": 6607.0}

medical_records["Vinay"] = {"Age":24, "Sex": "Male", "BMI":26.9, "Childre":0 ,"Smoker": "Non_smoker","Insurance_cost": 3225.0}

medical_records["Connie"] = {"Age":43, "Sex": "Female", "BMI":25.3, "Childre":3, "Smoker": "Non_smoker","Insurance_cost": 8886.0}

medical_records["Isaac"] = {"Age":35, "Sex": "Male", "BMI":20.6, "Childre":4, "Smoker": "Smoker","Insurance_cost": 16444.0}

medical_records["Valentina"] = {"Age":52, "Sex": "Female", "BMI":18.7, "Childre":1, "Smoker": "Non_smoker","Insurance_cost": 6420.0
}

print(medical_records)
print()

connie_cost = medical_records["Connie"]["Insurance_cost"]
print("Connie's insurance cost is " + str(connie_cost) + " dollars.")
print()

medical_records.pop("Vinay")
print(medical_records)
print()

for name, record in medical_records.items():
  print(name + " is a " + str(record["Age"]) + " years old " + record["Sex" ]+ " " +record["Smoker"]+ " with a BMI of " + str(record["BMI"]) + " and insurance cost of "+ str(record["Insurance_cost"]) + ".")
  print()





