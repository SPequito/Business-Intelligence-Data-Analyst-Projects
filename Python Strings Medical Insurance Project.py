medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,  #7045.0"""

# Add your code here
print(medical_data)
print()

# replace # tp $
update_medical_data = medical_data.replace("#", "$")
print(update_medical_data)
print()

# count the medical records

num_record = 0

for i in update_medical_data:
  if i == "$":
    num_record += 1
print("There are " + str(num_record) + " medical records in the data.")
print()

#lets slip update_medical  slipt at ;

medical_data_split = update_medical_data.split(";")
print(medical_data_split) 
print()
#lets separate better

medical_records = []

for i in medical_data_split:
  medical_records.append(i.split(","))
print(medical_records)
print()
#lets clean record

medical_record_clean = []

for i in medical_records:
  record_clean = []
  for j in i:
    record_clean.append(j.strip())
  medical_record_clean.append(record_clean)

print(medical_record_clean)
print()

#lets analise our data 

for record in medical_record_clean:
  record[0] = record[0].upper()
  print(record[0])
print()

#lets divide data in diferentes arrays

names = []
ages = []
bmis = []
insurances_costs = []

for record in medical_record_clean:
  names.append(record[0])
  ages.append(record[1])
  bmis.append(record[2])
  insurances_costs.append(record[3])

print("names")
print(names)
print("ages")
print(ages)
print("bmis")
print(bmis)
print("insurances_costs")
print(insurances_costs)

#now see the total and avg from bmis
total_bmi = 0

for bmi in bmis:
  total_bmi += float(bmi)

average_bmi = total_bmi / len(bmis)

print("Average BMI: " + str(average_bmi))