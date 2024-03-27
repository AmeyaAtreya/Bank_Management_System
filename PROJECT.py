import mysql.connector as driver
import sys



#-------------MAIN MENU --------------------


def menu():
    loop='y'
    while(loop=='y' or loop=='Y'):
        print("........MENU.......")
        print("1. CREATE DATABASE")
        print("2. CREATE TABLE")
        print("3. SHOW TABLES")
        print("4. INSERT RECORD")
        print("5. DELETE RECORD")
        print("6. SEARCH RECORD")
        print("7. DISPLAY RECORD")
        print()
        print()
        choice=int(input("Enter the choice (1-7) : "))
        if(choice==1):
            create_database()
        elif(choice==2):
            create_table()
        elif(choice==3):
            show_tables()
        elif(choice==4):
            insert_record()
        elif(choice==5):
            delete_record()
        elif(choice==6):
            search_record()
        elif(choice==7):
            display_record()
        else:
            print("Wrong Choice.")
        loop=input("Do you want more try? Press 'y' to continue...")
    else:
        sys.exit()


#-------------CREATE DATABASE --------------------


        
def create_database():
    con=driver.connect(host='localhost',user='root', passwd='tiger', charset='utf8')
    if con.is_connected():
        print("Successfully Connected")
    cur=con.cursor()
    cur.execute('create database if not exists customer')
    print()
    print("Database Created")
    con.close()
        




#-------------CREATE TABLE --------------------


    
def create_table():
    con=driver.connect(host='localhost',user='root',passwd='tiger',charset='utf8',database='customer')
    if con.is_connected():
        print("Successfully Connected")
    cur=con.cursor()
    cur.execute('create table if not exists cus(id integer primary key, name varchar(15), total float)')
    cur.execute('create table if not exists bill(id integer primary key, BFS integer, ESP integer, IC integer, LAT integer, PAS integer)')
    print()
    print("Table Created")
    con.close()



#-------------SHOW TABLES --------------------


    
def show_tables():
    con=driver.connect(host='localhost',user='root',passwd='tiger',charset='utf8',database='customer')
    if con.is_connected():
        print("Successfully Connected")
    cur=con.cursor()
    cur.execute('show tables')
    for i in cur:
        print(i)
    con.close()



#-------------INSERT RECORD --------------------



def insert_record():
    con=driver.connect(host='localhost',user='root',passwd='tiger',charset='utf8',database='customer')
    if con.is_connected():
        print("Successfully Connected")
        cur=con.cursor()
        ID=int(input("ENTER CUSTOMER ID : "))
        NAME=input("ENTER NAME OF CUSTOMER : ")
        global BFS
        BFS=0
        global ESP
        ESP=0
        global IC
        IC=0
        global LAT
        LAT=0
        global PAS
        PAS=0
        while True:
         print("Select Order :")
         print()
         print("1. Breakfast Sandwich  (Rs 40))")
         print("2. Espresso  (Rs 20)")
         print("3. Iced Coffee  (Rs 30)")
         print("4. Latte  (Rs 35)")
         print("5. Pastries  (Rs 35) ")
         print('6. Done')
         print()
         print()
         choice=int(input("Enter the choice (1-5) : "))
         if(choice==1):
            a=int(input('Enter Quantity :'))
            BFS=a
         elif(choice==2):
            b=int(input('Enter Quantity :'))
            ESP=b
         elif(choice==3):
            c=int(input('Enter Quantity :'))
            IC=c
         elif(choice==4):  
            d=int(input('Enter Quantity :'))
            LAT=d
         elif(choice==5):
            e=int(input('Enter Quantity :'))
            PAS=e
         elif(choice==6):
            break
         else:
            print("Wrong Choice.")
         total=(BFS*40+ESP*20+IC*30+LAT*35+PAS*35)
        print("Total Cost =",total)
        query1="INSERT INTO cus(id,name,total) VALUES({},'{}',{})".format(ID,NAME,total)
        query2="INSERT INTO bill(id,BFS,ESP,IC,LAT,PAS) VALUES({},{},{},{},{},{})".format(ID,BFS,ESP,IC,LAT,PAS)
        cur.execute(query1)
        cur.execute(query2)
        con.commit()
        print('Record Inserted')
        con.close()
    else:
        print("Error : Not Connected")




#-------------DELETE RECORD --------------------



def delete_record():
    con=driver.connect(host='localhost',user='root',passwd='tiger',charset='utf8',database='customer')
    cur=con.cursor()
    d=int(input("Enter CUSTOMER ID for deleting record : "))
    query1="delete from cus where id=%s" %(d)
    query2="delete from bill where id=%s" %(d)
    cur.execute(query1)
    cur.execute(query2)
    con.commit()
    print("Record Deleted")
    con.close()



#-------------SEARCH RECORD --------------------


def search_record():
    con=driver.connect(host='localhost',user='root',passwd='tiger',charset='utf8',database='customer')
    cur=con.cursor()
    print()
    d=int(input("Enter Customer ID which you want to search : "))
    query1="select * from cus where id=%s" %(d)
    query2="select * from bill where id=%s" %(d) 
    cur.execute(query1)
    rec=cur.fetchall()
    print("+----------|--------------|-----------+")
    print("+    ID    |     Name     |   Total   |")
    print("+----------|--------------|-----------+")
    for i in rec:
        print('|{0:<9} | {1:12} | {2:10}|'.format(i[0],i[1],i[2])) 
    cur=con.cursor()
    cur.execute(query2)       
    rec1=cur.fetchall()
    print()
    print()
    print("+----------|-----------|-----------|-----------|-----------|-----------+")
    print("+    ID    |    BFS    |    ESP    |     IC    |    LAT    |    PAS    |")
    print("+----------|-----------|-----------|-----------|-----------|-----------+")
    for i in rec1:
        print("|{0:<9} |{1:<10} |{2:<10} |{3:<10} |{4:<10} |{5:<10} |".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    print("Record Searched")
    con.close()

#-------------DISPLAY RECORD --------------------

def display_record():
    con=driver.connect(host='localhost',user='root',passwd='tiger',charset='utf8',database='customer')
    if con.is_connected():
        cur=con.cursor()
        cur.execute('select * from cus')
        rec=cur.fetchall()
        count=cur.rowcount
        print("+----------|--------------|-----------+")
        print("+    ID    |     Name     |   Total   |")
        print("+----------|--------------|-----------+")
        for i in rec:
            print('|{0:<9} | {1:12} | {2:10}|'.format(i[0],i[1],i[2])) 
        print("+----------|--------------|-----------+")
        print("+   Total no. of records are : ",count,"    |")
        print("+-------------------------------------+")
        print()
        print()
        cur=con.cursor()
        cur.execute('select * from bill')       
        rec1=cur.fetchall()
        print("+----------|-----------|-----------|-----------|-----------|-----------+")
        print("+    ID    |    BFS    |    ESP    |     IC    |    LAT    |    PAS    |")
        print("+----------|-----------|-----------|-----------|-----------|-----------+")
        for i in rec1:
         print("|{0:<9} |{1:<10} |{2:<10} |{3:<10} |{4:<10} |{5:<10} |".format(i[0],i[1],i[2],i[3],i[4],i[5]))

    


        con.close()
    else:
        print("Error : Database Connection is not success" )
    

#-------------MAIN BLOCK---------------------------


menu()
