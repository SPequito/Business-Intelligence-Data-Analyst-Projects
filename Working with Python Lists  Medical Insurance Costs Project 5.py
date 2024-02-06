names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here

#inserting new values at the end 
names.append("Priscilla")
insurance_costs.append(8320.0)

print("Names")
print(names)
print("Insurance costs")
print(insurance_costs)
# create 2d array with zip, and use list to read wend i print
print()
medical_records = list(zip(insurance_costs, names))
print(medical_records)
# see the leght from medical_record
print()
num_medical_records = len(medical_records)
print("There are " + str(num_medical_records)  + " medical records.")
#see the 1º value (1º "array")
print()
first_medical_record = medical_records[0]
print("Here is the first medical record:" + str(first_medical_record))
# i sort the mediucal record from the cheapest to expensive
print()
medical_records.sort()
print(medical_records)
# at the sort list i only see the 3 firts one (cheapest)
print()
cheapest_three = medical_records[:3]
print("Here are three cheapest insurance costs in our medical records " + str(cheapest_three))
# at the sort list i only see the 3 last one (expense)
print()
cheapest_three = medical_records[-3:]
print("Here are three most expensive insurance costs in our medical records " + str(cheapest_three))
# i look for how maney "pauls" exist 
print()
occurrences_paul = names.count("Paul")
print("There are " + str(occurrences_paul) + " individuals with the name Paul in our medical records")

