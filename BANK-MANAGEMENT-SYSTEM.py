print("""\n     ╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
     ╟═══════════════════════════════════════ TOPIC : BANK MANGEMENT SYSTEM ════════════════════════════════════════════╣
     ║══════════════════════════════════════════════════════════════════════════════════════════════════════════════════║
     ╟═══════════════════════════════════════ MADE BY : AMEYA ATREYA ═══════════════════════════════════════════════════╣
     ║════════════════════════════════════════════════      AND      ═══════════════════════════════════════════════════║
     ║════════════════════════════════════════════════   GYAN DUBEY  ═══════════════════════════════════════════════════║
     ║══════════════════════════════════════════════════════════════════════════════════════════════════════════════════║
     ╟═══════════════════════════════════════ SUBMITTED TO : MS. SARITA CHAUHAN ════════════════════════════════════════╣
     ╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝ """)

print("\n *-----------------------------------------------------* WELCOME *------------------------------------------------------------* ")

#Importing modules 
import csv
import random
import datetime

#Field Names
Bank_fields = ["Account No.","Account Holder", "Account type","Current Balance","Contact No.","Email","Address","Account Opening Date","Account Status","Pin"]

#Name of the csv file
Bank_database = "bankrecord.csv"

#Defining functions
def add_account():
    print("\n-------------------------")
    print("     Open Bank Account   ")
    print("-------------------------")
    global Bank_fields
    global Bank_database
    
    with open(Bank_database,'w') as f:
        Customer_data = []
        b_w = csv.writer(f)
        b_w.writerow(Bank_fields)
        ch = "y"
        t_date = datetime.datetime.now()
        while ch == "y":
            acc_no = random.randrange(100000,999999)
            print("The Account Number :",acc_no)
            hol = input("Enter Account Holder Name: ").upper()
            acc_typ = input("Enter Account type: ").upper()
            bal = float(input("Enter Total Balance: \u20B9"))
            con_no = int(input("Enter contact number: +91 "))
            email = input("Enter Email Address: ")
            add = input("Enter Address: ").upper()
            op_date = t_date
            op_date1 = print("Account Opening Date/Time(YYYY-MM-DD HH:MM:SS):",t_date)
            acc_sat = "ACTIVE"
            pin = random.randrange(1000,9999)
            pn = print("Pin number: ",pin)
            L = [acc_no,hol,acc_typ,float(bal),con_no,email,add,op_date,acc_sat,pin]
            Customer_data.append(L)
            Customer_data.sort()
            print("Customer Data Added Succesfully")
            ch = input("Do you want to add more record Y/N: ").lower()
        b_w.writerows(Customer_data)
    
def search():
    print("\n-----------------------")
    print("    Customer Enquiry   ")
    print("-----------------------")

    Name = input("Enter Customer Name You Want To Search: ").upper()
    with open(Bank_database,'r') as f:
        b_r = csv.reader(f)
        count = 0
        for i in b_r:
            if len(i) > 1:
                if str(i[1])== Name:
                    print(i[0:9])
                    count+=1
        if count == 0:
            print('No Customer Data Found!')
            input('\nPress any key to continue')
    return

def bal_en():
    print("\n------------------------")
    print("     Balance Enquiry    ")
    print("------------------------")

    name = input("Enter Customer Name for Balance Enquiry: ").upper()
    with open(Bank_database,'r') as f:
        b_r = csv.reader(f)
        count = 0
        l=[]
        for i in b_r:
            next(b_r)
            if len(i) > 1:
                if i[1] == name:
                    print("Bank Balance: \u20B9",i[3])
                
                    count+=1
        if count==0:
            print('No Customer Data Found!')
            input('\nPress any key to continue')
    return

def credit():
    print("\n----------------------")
    print("        Deposit       ")
    print("----------------------")

    name = input("Enter Customer Name for deposit: ").upper()
    amd = float(input("Enter amount to be credited : \u20B9"))
    with open(Bank_database,'r+') as f:
        l=[]
        b_r = csv.reader(f)
        count = 0
        for i in b_r:
            next(b_r)
            if len(i) > 1:
                if i[1] == name:
                    i[3] = float(i[3])+amd
                    print('\u20b9',amd,'has been succesfully credited to your account')
                    print("Current Balance: \u20B9",i[3])
                    count+=1
                    l.append(i)
                else:
                    l.append(i)
        update(l)           
        if count==0:
            print('No Customer Data Found!')
            input('\nPress any key to continue')
    return

def update(a):
     with open(Bank_database,'w') as f:
        b_w = csv.writer(f)
        b_w.writerows(a)

def debit():
    print("\n-----------------------")
    print("        Withdraw       ")
    print("-----------------------")

    name = input("Enter Customer Name for withdrawal: ").upper()
    amw = float(input("Enter amount to be debited : \u20B9"))
    with open(Bank_database,'r+') as f:
        l=[]
        b_r = csv.reader(f)
        count = 0
        for i in b_r:
            if len(i) > 1:
                if i[1] == name:
                    i[3] = float(i[3])-amw
                    print('\u20b9',amw,'has been succesfully debited from your account')
                    print("Current Balance: \u20B9", i[3])
                    count+=1
                    l.append(i)
                else:
                    l.append(i)
        update(l)   
        if count==0:
            print('No Customer Data Found!')
            input('\nPress any key to continue')
    return

def display():
    print("\n------------------------")
    print("        Bank Data       ")
    print("------------------------")

    with open(Bank_database,'r') as f:
        b_r = csv.reader(f)
        for i in b_r:
            print(i)

def up_con():
    print("\n--------------------------------------")
    print("         Contact Number Updation      ")
    print("--------------------------------------")

    name = input("Enter Customer Name for contact Number Updation : ").upper()
    cn = int(input("Enter contact number: "))
    with open(Bank_database,'r+') as f:
        l=[]
        b_r = csv.reader(f)
        count = 0
        for i in b_r:
            if len(i) > 1:
                if i[1] == name:
                    i[4] = cn
                    print("Contact Number has been successfully updaated")
                    count+=1
                    l.append(i)
                else:
                    l.append(i)
        update(l)   
        if count==0:
            print('No Customer Data Found!')
            input('\nPress any key to continue')
    return

def up_email():
    print("\n-------------------------------------")
    print("         Email Address Updation      ")
    print("-------------------------------------")

    name = input("Enter Customer Name for Email Updation : ").upper()
    em = input("Enter Email Address: ")
    with open(Bank_database,'r+') as f:
        l=[]
        b_r = csv.reader(f)
        count = 0
        for i in b_r:
            if len(i) > 1:
                if i[1] == name:
                    i[5] = em
                    print("Email Address has been successfully updaated")
                    count+=1
                    l.append(i)
                else:
                    l.append(i)
        update(l)   
        if count==0:
            print('No Customer Data Found!')
            input('\nPress any key to continue')
    return

def up_add():
    print("\n-------------------------------")
    print("         Address Updation      ")
    print("-------------------------------")

    name = input("Enter Customer Name for Address Updation : ").upper()
    add = input("Enter Residential Address: ")
    with open(Bank_database,'r+') as f:
        l=[]
        b_r = csv.reader(f)
        count = 0
        for i in b_r:
            if len(i) > 1:
                if i[1] == name:
                    i[6] = add
                    print("Address has been successfully updaated")
                    count+=1
                    l.append(i)
        update(l)   
        if count==0:
            print('No Customer Data Found!')
            input('\nPress any key to continue')
    return

def deln():
    print("\n-------------------------------")
    print("         Account Deletion      ")
    print("-------------------------------")

    name = input("Enter Customer Name for Account Deletion : ").upper()
    with open(Bank_database,'r+') as f:
        l=[]
        b_r = csv.reader(f)
        count = 0
        for i in b_r:
            if len(i) > 1:
                if i[1] != name:
                    count+=1
                    l.append(i)
        update(l)
        if count==0:
            print('No Customer Data Found!')
            input('\nPress any key to continue')
    return

#Creating Admin and Customer Window
while True:
    print("\n1.Admin Login")
    print("2.Customer Login\n")

    ch = input("Enter your choice: ")
    if (ch == "1"):
        print("\nEnter User-id and Password")
        us = "admin@123"
        pss = "abg"
        us_id = input("User-ID: ")
        pas = input("Password: ")
        if (us==us_id) and (pss==pss):
            while True:
                print("\n ----- Welcome Admin ----- ")
                print("\n1. Add Bank account to database")
                print("2. Search Customer")
                print("3. Display all records")
                print("4. Update Contact Number")
                print("5. Update Email Address")
                print("6. Update Residential Address")
                print("7. Delete Customer Record")
                print("8. Logout")
                print("\n")
                ch1 = int(input("Enter your choice: "))
                if (ch1==1):
                    add_account()
                elif (ch1==2):
                    search()
                elif (ch1==3):
                    display()
                elif (ch1==4):
                    up_con()
                elif (ch1==5):
                    up_email()
                elif (ch1==6):
                    up_add()
                elif (ch1==7):
                    deln()
                elif (ch1==8):
                    print("You have successfully loged out")
                    break
                else:
                    print("You have chosen invalid option")
        else:
            print("Invalid credential")
        
    elif (ch=="2"):
        while True:
            print("\n1. Balance Enquiry")
            print("2. Credit")
            print("3. Debit")
            print("4. Update Contact Number")
            print("5. Update Email Address")
            print("6. Update Residential Address")
            print("7. Search Details")
            print("8. Exit")
            print("\n")
            ch2 = int(input("Enter your choice: "))
            if (ch2==1):
                bal_en()
            elif (ch2==2):
                credit()
            elif (ch2==3):
                debit()
            elif (ch2==4):
                up_con()
            elif (ch2==5):
                up_email()
            elif (ch2==6):
                up_add()
            elif (ch2==7):
                search()
            elif (ch2==8):
                break
            else:
                print("Invalid Option")
    else:
            print(" Invalid Option ")
