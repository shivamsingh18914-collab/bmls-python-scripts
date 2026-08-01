#creating a program with 3 random patient name and data for diabetes

laboratory_database = [ {"id" : "p_01" ,"name" : "jignesh" , "blood_glucose" : 110 },
                        {"id" : "p_02" , "name" : "rajesh" , "blood_glucose" : 92 },
                        {"id" : "p_03" , "name" : "lavish" , "blood_glucose" : 175},]


print("----NAMS LAB AUTOMATION REPORT----")

for patient in laboratory_database:

    p_id = patient["id"]