signs=["Κριός - Aries", "Ταύρος - Taurus", "Δίδυμοι - Gemini", "Καρκίνος - Cancer", "Λέων - Leo", "Παρθένος - Virgo", "Ζυγός - Libra" , "Σκορπιός - Scorpio", "Τοξότης - Sagittarius", "Αιγόκερως - Capricorn","Υδροχόος - Aquarius", "Ιχθείς - Pisces"]
months=[1,2,3,4,5,6,7,8,9,10,11,12]
month=int(input("Enter your month of birth: "))
if (month in months):
    if (month==1)|(month==3)|(month==5)|(month==7)|(month==8)|(month==10)|(month==12):
        days=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    elif (month==4)|(month==6)|(month==9)|(month==11):
        days=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    elif (month==2):
        year=int(input("Enter your year of birth: "))
        if (year%4==0):
            days=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
        else:
            days=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
else:
    print("Enter a valid month.")
    month=int(input("Enter your month of birth: "))
day=int(input("Enter your day of birth: "))
if(day in days):
    if((month==3)&(day>20))|((month==4)&(day<21)):
        sign=signs[0]
    elif ((month==4)&(day>20))|((month==5)&(day<21)):
        sign=signs[1]
    elif ((month==5)&(day>20))|((month==6)&(day<21)):
        sign=signs[2]
    elif ((month==6)&(day>20))|((month==7)&(day<21)):
        sign=signs[3]
    elif ((month==7)&(day>20))|((month==8)&(day<21)):
        sign=signs[4]
    elif ((month==8)&(day>20))|((month==9)&(day<21)):
        sign=signs[5]
    elif ((month==9)&(day>20))|((month==10)&(day<21)):
        sign=signs[6]
    elif ((month==10)&(day>20))|((month==11)&(day<21)):
        sign=signs[7]
    elif ((month==11)&(day>20))|((month==12)&(day<21)):
        sign=signs[8]
    elif ((month==12)&(day>20))|((month==1)&(day<21)):
        sign=signs[9]
    elif ((month==1)&(day>20))|((month==2)&(day<21)):
        sign=signs[10]
    elif ((month==2)&(day>20))|((month==3)&(day<21)):
        sign=signs[11]
    else:
        sign=signs[12]    
else:
    print("Enter a valid day of the month.")
    day=int(input("Enter your day of birth: "))
print(f"Your sign is: {sign}")

"""ΑΘΑΝΑΣΙΑ ΤΖΑΝΙΔΗ 3Δ-ΠΛΠ01 20/11/2026"""
