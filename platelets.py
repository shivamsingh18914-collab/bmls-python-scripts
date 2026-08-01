def evaluate_platelets():

    #ask user about their name and greet them

    user_name = input("what is your name")

    print( f"\n Hello, {user_name}")

    #ask user for platelets count in cells/mcl

    platelets_input = input(" what is your platelets count ?")

    #convert string into float

    platelets_count = float(platelets_input)

    if platelets_count < 150000:

        print( f" Result :{platelets_count} cells/mcl , Thrombocytopenia (low platelets count)")

    elif platelets_count <= 450000:


        print(f" Result :{platelets_count} cells/mcl , Normal")

    else:

        print(f"Result : {platelets_count} cells/mcl , thrombocytosis (high platelets count )")

    if __name__=="__main__":
        evaluate_platelets()

