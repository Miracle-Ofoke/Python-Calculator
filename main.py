#CALCULATOR BY OFOKE MIRACLE

#I CREATED A WHILE LOOP 

while  True:
#CREATED ALL THE VARIABLE AND RECIEVED ALL THE INPUT I NEED
        while True:
            calc_type = int(input("""           Type Of Calculation 
                1) Multiplication
                2) Addition
                3) Subtraction
                4) Division
                PICK BY INPUTING THE NUMBER : """))
            if calc_type > 4 : 
                print("""           PICK FROM TH OPTION GIVEN""")
                continue
            else: 
                break
                
        first_num = int(input("First Number : "))
        second_num = int(input("Second Number : "))
        answer = f"Your Answer Is : "
#I CREATED A CLASS TO PREVENT REPITITION OF CODE
        class Calculation():
            def Multiply(num1,num2):
                print(f"{answer} {num1*num2}")
            def Addition(num1,num2):
                print(f"{answer} {num1 +num2}")
            def Subtractiion(num1,num2):
                print(f"{answer} {num1-num2}")  
            def Division(num1,num2):
                print(f"{answer} {num1 /num2}")  
#USED CONDITION OPERATORS TO ADD LOGIC TO THE CALCULATOR
        if calc_type == 1 :
            Calculation.Multiply(first_num,second_num)
            sign = " * "
        elif calc_type == 2:    
            Calculation.Addition(first_num,second_num)
            sign = " + "
        elif calc_type == 3:    
            Calculation.Subtractiion(first_num,second_num)
            sign = " - "
        elif calc_type == 4:    
            Calculation.Division(first_num,second_num)
            sign = " / "
        print(f"""          EQUATION
            {first_num}{sign}{second_num} 
              """)    
#ADDED THIS TO BE ABLE TO EXIT FROM THE CODE AT ALL TIMES
        stop = input("Do you want to CONTINUE Y for YES an N for NO : ").capitalize()
        if stop == "Y" :
            continue
        else:
            break   