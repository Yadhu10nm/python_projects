# """""<<<<  THIS IS A PROGRAM THAT SHOWS VARIOUS FUNCTIONS OF A RESTURANT
#             *THIS PROGRAM CONTAIN 2 CLASSES ...ADMIN CLASS AND USER CLASS
#                   -ADMIN CLASS HAVE THE FUNCTIONS --> UPDATE_MENU , LATEST_ORDER , REMOVE_ORDERS
#                   -USER CLASS HAVE FUNCTION --> MENU , ADD_ORDERS , DELETE_ORDERS
#
#           THS PROGRAM CONTAINS 4 LIBRARIES --> OS , MYSQL.CONNECTOR , PANDAS , TABULATE  >>>>>"""
import os
import mysql.connector as mc
import pandas as pd
from tabulate import tabulate

"""<<<<USER CLASS BEGINS HERE >>>>"""
class Food_Booking_user:
    def __init__(self):
        self.mydb=mc.connect(host="localhost",user="root",password="1234",database="k")
        self.mycursor=self.mydb.cursor()
        self.menu=[]
    def Menu(self):
        self.query="select * from menu"
        self.mycursor.execute(self.query)
        for i in self.mycursor:
            self.menu.append(list(i))
        df=pd.DataFrame(self.menu)
        data=tabulate(df,headers=["FOOD_ID","FOOD_NAME","PRICE"],tablefmt ='grid')
        print(data)
    def Add_orders(self):
        self.total_amt=0
        self.price_list={}
        try:
            self.n=int(input("Enter how many food items you want : "))
            self.name=input("Enter your name : ")
            self.address=input("Enter you address : ")
            self.phn=input("Enter your mobile number : ")
            for i in range(self.n):
                 self.food=input("Enter the food name you want to buy : ")
                 self.qty=int(input(f"Enter the quantity of  {self.food} : "))
                 self.query1="INSERT INTO `order` (cname,caddress,cphn,fname,quantity) VALUES (%s, %s, %s,%s,%s)"
                 self.values=(self.name,self.address,self.phn,self.food,self.qty)
                 self.mycursor.execute(self.query1,self.values)
                 self.mydb.commit()
                 self.query2 = "select fprice from menu where fname=(%s)"
                 self.mycursor.execute(self.query2, (self.food,))
                 for i in self.mycursor:
                     key=i[0]
                     self.price_list[key]=self.qty
            for key in self.price_list:
                    self.total_amt=self.total_amt+(key*self.price_list[key])

            print(f"Dear {self.name} your order is accepted by the resturant !")
            print(f"Dear {self.name} your Bill amount is {self.total_amt} ")

        except Exception as e:
            print(f"Error : {e}")
        finally:
            print("thank you..!")
    def delete_order(self):
        try:
            self.name=input("Enter your name : ")
            self.query="delete from `order` where cname=%s"
            self.ch=input("Are you sure , you want to delete order ? (yes/no) :")
            if self.ch.lower()=="yes":
                   self.mycursor.execute(self.query,(self.name,))
                   self.mydb.commit()
                   print(f"Dear {self.name} your order has been cancelled ...!")
        except Exception as e:
            print(f"Error : {e}")
        finally:
            print("Thank you...!")

"""<<<<ADMIN CLASS BEGINS HERE >>>>"""
class Food_Booking_admin(Food_Booking_user):
    def __init__(self):
        super().__init__()
    def update_menu(self):
        def mod_price():
            try:
              self.fname=input("enter the food name you want to change the price : ")
              self.fprice=int(input("enter the new price : "))
            except Exception as e:
                print(f"Error : {e}")
            self.query="update menu set fprice=%s where fname=%s"
            self.mycursor.execute(self.query,(self.fprice, self.fname,))
            self.mydb.commit()
            print(f"successfullly updated the price of {self.fname} to {self.fprice}")

        def add_new_items():
            self.nl=[]
            self.n=int(input("how many items you want to add to menu ? "))
            self.mycursor.execute("select * from menu")
            for i in self.mycursor:
                self.l = []
                self.l.append(list(i))

            for i in self.l:
                for j in i:
                    self.nl.append(j)
            for i in range(self.n):
                try:
                     self.fid = int(input("enter food id : "))
                     self.fname = input("enter the food name : ")
                     if self.fname in self.nl or self.fid in self.nl:
                         print(f"{self.fname} or id: {self.fid}) is already in the menu ")
                     else:
                        self.fprice = int(input("enter the price : "))
                        self.query="insert into menu(fid,fname,fprice) values(%s,%s,%s)"
                        self.value=(self.fid,self.fname,self.fprice,)
                        self.mycursor.execute(self.query,self.value)
                        self.mydb.commit()
                        print(f"{self.fname} has benn added ..")
                except Exception as e:
                    print(f"Error : {e}")
        print("press\n1-modify the price\n2-add new items")
        self.choice=int(input("enter your choice :"))
        if self.choice==1:
            mod_price()
        elif self.choice==2:
            add_new_items()
        else:
            print("invalid entry...")
    def latest_order(self):
              self.order=[]
              self.query="select * from `order` order by id desc"
              self.mycursor.execute(self.query)
              for i in self.mycursor:
                  self.order.append(list(i))
              df = pd.DataFrame(self.order)
              data = tabulate(df, headers=["ORDER_ID", "CUSTOMER_NAME", "CUSTOMER_ADDRESS","CUSTOMER_PHN_NO","FOOD_NAME","QTY"], tablefmt='grid')
              print(data)
    def remove_item(self):
        self.id = int(input("enter the id to remove from database"))
        self.query="delete from `order` where id=(%s)"
        self.mycursor.execute(self.query,(self.id,))
        self.mydb.commit()
        print(f"ID number -> {self.id} has been deleted ")
        self.latest_order()

"""<<<< MAIN() WHICH CONTAINS OBJECT CREATION FUNCTION CALLS  >>>>"""
def main():
    Food_user_Obj = Food_Booking_user()
    Food_admin_obj=Food_Booking_admin()

    def clear():
        ch=input()
        if ch=="c":
            os.system('cls')
    def admin():
      while True:

            print("1-update menu\n2-menu\n3-latest orders\n4-removing the accepted items\n5-exit")
            choice=int(input("enter your choice : "))
            if choice==1:
                    Food_admin_obj.update_menu()
            elif choice==2:
                    Food_user_Obj.Menu()
            elif choice==3:
                    Food_admin_obj.latest_order()
            elif choice==4:
                    Food_admin_obj.remove_item()
            elif choice==5:
                    break
            else:
                    print("invalid entry ....")
            clear()
    def user():
         while True:
               print("1-menu\n2-order food\n3-cancel order\n4-exit")
               try:
                  choice=int(input("enter your choice : "))
               except ValueError as v:
                   print(f"Error : {v}")
               if choice==1:
                    Food_user_Obj.Menu()
               elif choice==2:
                    Food_user_Obj.Add_orders()
               elif choice==3:
                    Food_user_Obj.delete_order()
               elif choice==4:
                     break
                     print("thank you !")
               else:
                     print("invalid entry...!")
               clear()

    users = {"yadhu": 123, "ammu": 123}
    try:
       name = input("enter your name :")
       pass_ = int(input("enter the password : "))
    except ValueError as v:
        print(f"Error : {v}")
    if name == "root" and pass_ == 123:
        admin()
    for key in users:
        if name == key and pass_ == users[key]:
            user()
            break
"""<<<< THE PROGRAM STARTS FROM HERE  >>>>"""
if __name__=="__main__":
     main()