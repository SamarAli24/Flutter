

record_list=[]
def input_record(record_list):
    while True:
        name=input("enter the Bakery Item Name:")
        number=input("enter the Bakery Item Number:")
        price=input("enter the Bakery Item Price:Rs ")
        date=input("enter the Date of Manufacture (dd-mm-yyyy):")
        record_list.append([name,number,price,date])
        choice=input("Press y/Y to enter another record esle press any key to exit")
        if choice!="y" and choice!="Y":
            break

def display_record(record_list):
    serial=1
    for record in record_list:
        print("serial no.",serial)
        print("Bakery Item Name:",record[0])
        print("Bakery Item Number:",record[1])
        print("Bakery Item Price:Rs ",record[2])
        print("Date of Manufacture:",record[3])
        date=record[3]
        
        print("Date of Expiry:",expiry_date(date))           #expired after 1 week of manufacture
        serial+=1

def save_record(record_list):
    f=open("bakery.txt","w")
    for record in record_list:
        f.write(record[0]+",")
        f.write(record[1]+",")
        f.write(record[2]+",")
        f.write(record[3]+"\n")
    f.close()

def load_record(record_list):
    f=open("bakery.txt","r")
    x=(f.read()).split("\n")
    for record in x:
        if record!='':
            r=record.split(",")
            r[-1]==r[-1][0:-2]
            record_list.append(r)
            
def expiry_date(date):
    date_contents=date.split("-")
    max_days=0
    exp_date=""
    if int(date_contents[1])in [1,3,5,7,8,10,12]:
        max_days=31
    elif int(date_contents[1])in [4,6,9,11]:
        max_days=30
    elif int(date_contents[1])==2:
        max_days=28
    if (int(date_contents[0])+7)>max_days:
        remainder=int(date_contents[0])+7-max_days
        if int(date_contents[1])+1>12:
            date_contents[2]=str(int(date_contents[2])+1)
            exp_date=str(remainder)+"-"+str(int(date_contents[1])-12+1)+"-"+date_contents[2]
        else:
            exp_date=str(remainder)+"-"+str(int(date_contents[1])+1)+"-"+date_contents[2]
    else:
        remainder=int(date_contents[0])+7
        exp_date=str(remainder)+date[2:]
    return (exp_date)

#main program
while True:
    print("1.input records")
    print("2.save records")
    print("3.load records")
    print("4.display records")
    print("5.exit")
    choice=input("=>")
    if choice=="1":
        input_record(record_list)
    elif choice=="2":
        save_record(record_list)
    elif choice=="3":
        load_record(record_list)
    elif choice=="4":
        display_record(record_list)
    elif choice=="5":
        break
    else:
        print("wrong choice entered")
