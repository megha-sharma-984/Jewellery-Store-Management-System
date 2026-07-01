import mysql.connector as sqlcon
from tabulate import tabulate
conn= sqlcon.connect(host='localhost',user='root',password='Mesh#524')
cur=conn.cursor()
cur.execute("create database if not exists Jewellery_Mall;")
cur.execute("use Jewellery_Mall;")
# cur.execute('create table if not exists userid_pass(user_name varchar(20),password varchar(20));')
# cur.execute("create table if not exists TANISHQ(JewelNo varchar(15) primary key,JewelType varchar(30),JewelMaterial varchar(40),Jewelsize varchar(40),JewelPriceRange varchar(40),Occasion varchar(50));")
# cur.execute("create table if not exists MALABAR(JewelNo varchar(15) primary key,JewelType varchar(30),JewelMaterial varchar(40),Jewelsize varchar(40),JewelPriceRange varchar(40),Occasion varchar(50));")
# cur.execute("create table  if not exists YOUBELLE(JewelNo varchar(15) primary key,JewelType varchar(30),JewelMaterial varchar(40),Jewelsize varchar(40),JewelPriceRange varchar(40),Occasion varchar(50));")
# cur.execute("create table if not exists KALYANJEWELLERS(JewelNo varchar(15) primary key,JewelType varchar(30),JewelMaterial varchar(40),Jewelsize varchar(40),JewelPriceRange varchar(40),Occasion varchar(50));")
# cur.execute("create table if not exists PCJEWELLERS(JewelNo varchar(15) primary key,JewelType varchar(30),JewelMaterial varchar(40),Jewelsize varchar(40),JewelPriceRange varchar(40),Occasion varchar(50));")
# cur.execute("alter table TANISHQ modify JewelPriceRange varchar(50);")
# cur.execute("alter table MALABAR modify JewelPriceRange varchar(50);")
# cur.execute("alter table YOUBELLE modify JewelPriceRange varchar(50);")
# cur.execute("alter table KALYANJEWELLERS modify JewelPriceRange varchar(50);")
# cur.execute("alter table PCJEWELLERS modify JewelPriceRange varchar(50);")
# cur.execute("insert into TANISHQ values('8685479','Chain','Platinum,Gold','41-61cm','Rs.3,000-2,00,000','partywear'),('8685470','Necklace','Gold','41-76cm','Rs.5,000-1,50,000','Bridal collections,Casualwear'),('5326837','Bracelet','Gold','13.5-21.5cm','Rs.10,000-25,000','Partywear'),('8735323','Earrings','Platinum,Gold,Gemstone','4-55mm','Rs.25,000-1,00,000','Any occasion'),('7613268','Noserings','Gold,Diamond','4.8-13mm','Rs.1,000-50,000','Any occasion'),('7863537','Anklet','Gold,Silver','12.8-30.5cm','Rs.3,000-30,000','Wedding'),('6732765','Rings','Gold,Platinum','3-22.6mm','Rs.16,000-40,000','Any occasion');")
# cur.execute("insert into MALABAR values('8685478','Chain','Platinum,Gold','41-61cm','Rs.5,000-2,10,000','partywear'),('8685479','Necklace','Gold','41-76cm','Rs.10,000-2,75,000','Bridal collections,Casualwear'),('5326836','Bracelet','Gold','13.5-21.5cm','Rs.7,000-25,000','Partywear'),('8735322','Earrings','Platinum,Gold,Gemstone','4-55mm','Rs.20,000-1,50,000','Any occasion'),('7613267','Noserings','Gold,Diamond','4.8-13mm','Rs.1,000-25,000','Any occasion'),('7863536','Anklet','Gold,Silver','12.8-30.5cm','Rs.5,000-45,000','Wedding'),('6732763','Rings','Gold,Platinum','3-22.6mm','Rs.15,000-45,000','Any occasion');")
# cur.execute("insert into YOUBELLE values('8685477','Chain','Platinum,Gold','41-61cm','Rs.7,000-1,90,000','partywear'),('8685478','Necklace','Gold','41-76cm','Rs.7,500-2,55,000','Bridal collections,Casualwear'),('5326835','Bracelet','Gold','13.5-21.5cm','Rs.9,800-30,000','Partywear'),('8735325','Earrings','Platinum,Gold,Gemstone','4-55mm','Rs.16,000-1,20,000','Any occasion'),('7613266','Noserings','Gold,Diamond','4.8-13mm','Rs.1,000-45,000','Any occasion'),('7863535','Anklet','Gold,Silver','12.8-30.5cm','Rs.3,000-45,000','Wedding'),('6732764','Rings','Gold,Platinum','3-22.6mm','Rs.10,000-50,000','Any occasion');")             
# cur.execute("insert into KALYANJEWELLERS values('8685476','Chain','Platinum,Gold','41-61cm','Rs.10,000-2,00,000','partywear'),('8685477','Necklace','Gold','41-76cm','Rs.11,500-2,80,000','Bridal collections,Casualwear'),('5326834','Bracelet','Gold','13.5-21.5cm','Rs.5,000-30,000','Partywear'),('8735324','Earrings','Platinum,Gold,Gemstone','4-55mm','Rs.18,000-1,00,000','Any occasion'),('7613269','Noserings','Gold,Diamond','4.8-13mm','Rs.800-30,000','Any occasion'),('7863530','Anklet','Gold,Silver','12.8-30.5cm','Rs.2,500-40,000','Wedding'),('6732762','Rings','Gold,Platinum','3-22.6mm','Rs.11,000-35,000','Any occasion');")            
# cur.execute("insert into PCJEWELLERS values('8685475','Chain','Platinum,Gold','41-61cm','Rs.9,000-1,80,000','partywear'),('8685476','Necklace','Gold','41-76cm','Rs.7,000-2,50,000','Bridal collections,Casualwear'),('5326833','Bracelet','Gold','13.5-21.5cm','Rs.9,500-30,000','Partywear'),('8735326','Earrings','Platinum,Gold,Gemstone','4-55mm','Rs.15,000-1,10,000','Any occasion'),('7613265','Noserings','Gold,Diamond','4.8-13mm','Rs.1,000-40,000','Any occasion'),('7863534','Anklet','Gold,Silver','12.8-30.5cm','Rs.5,000-35,000','Wedding'),('6732761','Rings','Gold,Platinum','3-22.6mm','Rs.9,000-50,000','Any occasion');")
conn.commit()

def login():
    print('1.REGISTER')
    print('2.LOGIN')
    n=int(input('Enter your choice: '))
    if n==1:
        name=input('Enter your user name: ')
        p=input('Enter your password: ')
        r=input('Confirm your password: ')
        while p!=r:
            print("Password's Did not match")
            print('Please Re-enter again')
            p=input('Enter your password: ')
            r=input('Confirm your password: ')
        if p==r:
            a="insert into userid_pass(user_name,password) values('%s','%s')"%(name,p)
            cur.execute(a)
            conn.commit()
            print("User created succesfully")
            login()

    if n==2:
        n=input('Enter your username: ')
        p=input('Enter your password: ')
        a="select * from userid_pass where user_name='"+n+"' and password='"+p+"'  "
        cur.execute(a)
        if cur.fetchone() is None:
            print('Invalid username or password')
            login()
        else:
             
            print("               WELCOME TO JEWELLRY STORE")

def add():
    bb='y'
    while bb=='y':
        bsp=input('enter the brand you want to add the item to:')
        head2=['JewelNo','JewelType','JewelMaterial','Jewelsize','JewelPriceRange','Occasion']
        cur.execute("select * from %s "%(bsp))
        ht2=cur.fetchall()
        print(tabulate(ht2,headers=head2,tablefmt='fancy_grid'))
        bbb='y'
        while bbb=='y':
            bi=int(input('Enter the Jewel number:'))
            bn=input('enter the Jewel type:')
            br=input('enter the Jewel material:')
            bt=input('Enter the Jewel size:')
            bs=input('enter the Jewel price:')
            bo=input('Enter the occasion:')
            cur.execute("insert into %s values('%d','%s','%s','%s','%s','%s')"%(bsp,bi,bn,br,bt,bs,bo))
            conn.commit()
            print('Succesfully added')
            bbb=input('do you want to continue adding in the same brand\n y/n')
        bb=input('do you want to continue adding \n y/n')

def update():
    ab='y'
    while ab=='y':
        g=input('Enter the brand you want to update')
        head=['JewelNo','JewelType','JewelMaterial','Jewelsize','JewelPriceRange','Occasion']
        cur.execute("select * from %s "%(g))
        ht=cur.fetchall()
        print(tabulate(ht,headers=head,tablefmt='fancy_grid'))
        ch='y'
        while ch=='y':
                k=input('Enter the jewelno you want to update')
                i=input('Enter the Field You want to change')
                j=input('Enter the correct value to be entered')
                update_query = "UPDATE %s  set %s='%s' WHERE JewelNo = '%s'"%(g,i,j,k)
                cur.execute(update_query )
                conn.commit()
                ch=input('Do You Want To Continue updating in the same table y/n:')
        ab=input('do you want to continue updating y/n:')

def delete():
    aa='y'
    while aa=='y':
        sp=input('enter the brand you want to delete the jewel from:')
        head=['JewelNo','JewelType','JewelMaterial','Jewelsize','JewelPriceRange','Occasion']
        cur.execute("select * from %s"%(sp))
        ht1=cur.fetchall()
        print(tabulate(ht1,headers=head,tablefmt='fancy_grid'))
        aid=int(input('enter the jewelno you want to delete:'))
        cur.execute("delete from %s where JewelNo='%d';"%(sp,aid))
        conn.commit()
        print('Succesfully Deleted')
        aa=input('do you want to continue Deleting more jewels y/n:')

def display():
    A=input('Enter the brand you want to checkout')
    cur.execute("select * from %s"%(A))
    headd=['JewelNo','JewelType','JewelMaterial','Jewelsize','JewelPriceRange','Occasion']
    xyz=cur.fetchall()
    print(tabulate(xyz,headers=headd,tablefmt='fancy_grid'))

print("                     WELCOME TO JEWELLERY STORE")
while True:
    d=int(input('Welcome do you want to:\n 1:Register/Login \n 2:add\n 3:update\n 4:delete\n 5:display\n 6:exit enter your choice:'))
    if d==1:
        login()
    elif d==2:
        add()
    elif d==3:
        update()
    elif d==4:
        delete()
    elif d==5:
        display()
    elif d==6:
        exit()
    else:
        print('enter related input')