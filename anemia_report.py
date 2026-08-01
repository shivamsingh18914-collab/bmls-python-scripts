#documenting data of 3 patients for anemia report

laboratory_database = [ {"id" : "p_01" ,"name": "Raj" , "blood_group" :"B+","hb_level" : 11.2},
                     {"id" : "p_02" ,"name": "shami" ,"blood_group" : "O+" ,"hb_level" : 17.2},
                       {"id" : "p_03" , "name" : "shraddha" ,"blood_group" :"AB+" ,"hb_level": 12.0}
                       ]

#processing data of 3 patients to flag anemia

print("-----VNSGU AUTOMATION LAB ANEMIA REPORT----")

for patient in laboratory_database:

    #extraction of data from dictionary

    p_id = patient["id"]

    p_name = patient["name"]

    hb = patient["hb_level"]

    #using if elif operator to flag condition of patient

    if hb < 12.0:

           status  = "anemia(flag:low)"


    elif hb > 16.0:

           status = "polycythemia(flag:high)"

    else:

        status = "Normal"


    print(f" patient ID : {p_id} | Name :{p_name} | Hb :{hb} g/dl | status :{status}")

    print("---------")


