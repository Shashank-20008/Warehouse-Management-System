'''
   field = ['stockid','stockname','amount of stock','total price','price for each','email','phone number']
   0: quit
   1: Add
   2: View
   3: Search
   4: Update


   stock_details = []
   stock_file = ""
'''


import csv
from datetime import datetime
import pandas as pd

stock_details = ['stockname','amount of stock','total price','price for each','date','email','phone number']
stock_file = "stock2.csv"
stock_index = "sindex.csv"


#Data of Stock Bought from the market 
def stock_bought():

   def display_menu():
      print("--------------------------------")
      print("Welcome to Acharya Bakery Enterprise")
      print("--------------------------------")
      print("0: Quit")
      print("1. Add the name of stock item")
      print("2. View Stock item")
      print("3. Search stock item")
      print("4. Update stock item")
      print("5. Return to home")


   def add_stock():
      print("----------------------------")
      print("Add the details of stock")
      print("-----------------------------")

      global stock_details
      global stock_file

      stock_data = {}
      
      from uuid import uuid4
      stock_data['stockid'] = str(uuid4())

      for detail in stock_details:
         value = input("Enter "+ detail +" :")
         stock_data[detail] = [value]

      # with open(stock_file, "a", encoding="utf-7") as f:
      #    writer = csv.writer(f)
      #    writer.writerows([stock_data])
      stock_df = pd.DataFrame.from_dict(stock_data)
      stock_df.to_csv('stock2.csv', mode='a', index=False, header=False)

      with open(stock_index,"a",encoding="utf-7") as f:
         writer = csv.writer(f)
         writer.writerow([stock_data['stockid']])


      print("Data saved successfully")
      input("Press any key to continue")
      return



   def view_stock():
      global stock_details
      global stock_file
      global stock_index

      print("--------Records Of Stock Bought-----------")

      # with open(stock_index,"r",encoding="utf-7") as f:
      #    reader = csv.reader(f)
      #    with open(stock_file,"r",encoding="utf-7") as d:
      #       reader = csv.reader(d)
      df = pd.read_csv("stock2.csv")
            # df.to_csv("stock2.csv",header=stock_details,index=False)
      print(df.to_string())
      print("\n-----------------------------")

      input("Press any key to continue")


   def search_stock():
      global stock_details
      global stock_file

      print("----------Search Stock Bought-----------")
      name = input("Enter the stock name you want to search\n")

      stock = pd.read_csv('stock2.csv')
      search_stock = stock[stock['stockname'] == name]
      if not search_stock.empty:
         print(search_stock.to_string())

      else:
         print(f'Stock with {name} not found') 

      # with open(stock_index,"r",encoding="utf-8") as f:
      #    reader = csv.reader(f)
      #    for row in reader:
      #       if len(row) > 0:
      #          if id == row[0]:
      #             print("---------Stock Record found---------")
      #             with open(stock_file,"r",encoding="utf-8") as d:
      #                reader = csv.reader(d)
      #                for row1 in reader:
      #                   print("stock id: ",row1[0])
      #                   print("stock name: : ",row1[1])
      #                   print("Amount of stock purchased: ",row1[2])
      #                   print("Total Price: ",row1[3])
      #                   print("Price of each:",row1[4])
      #                   print("Date of purchasing:",row1[5])
      #                   print("Email of the dealer where stock is purchased: ",row1[6])
      #                   print("Phone number of the dealer: ",row1[7])
      #                   break
      #          else:
      #             print("Stock record not found for this id")
      
      input("Press any key to continue")
            
      
   def update_stock():
      global stock_details
      global stock_file

      print("-----------Update stock from available-------------")
      print(pd.read_csv('stock2.csv').to_string())

      id = input("Enter the stock id you want to update:\n")
      index_stock = None
      updated_data = []
      with open(stock_file,"r",encoding="utf-8") as f:
         reader = csv.reader(f)
         counter = 0
         for row in reader:
            if len(row) > 0:
               if id == row[0]:
                  index_stock = counter
                  print("Stock Data found in index:",index_stock)
                  stock_data = []
                  stock_data.append(id)
                  for field in stock_details:
                     value = input("Enter "+field+": ")
                     stock_data.append(value)
                  updated_data.append(stock_data)
               else:
                  updated_data.append(row)
                  counter += 1

      # Check if the record is found or not
      if index_stock is not None:
         with open(stock_file,"w",encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
      else:
         print("Stock Record not found")
      
      input("Press any key to continue")



   while True:
      display_menu()
      choice = int(input("Enter the choice:\n"))
      if choice == 0:
         exit()
      elif choice == 1:
         add_stock()
      elif choice == 2:
         view_stock()
      elif choice == 3:
         search_stock()
      elif choice == 4:
         update_stock()
      elif choice == 5:
         main()
      else:
         print("Wrong choice entered reenter the correct one\n")

   print("------------------------")
   print("Thank You")
   print("------------------------\n")



      


#Stock sold from the warehouse

''' fields: 
1. Stock sold to
2. Rupees 
3. amount of stock
4. phne number'''

sale_file = "sale.csv"
sale_index = "saleindex.csv"
sale_details = ["stockid","stocksoldto",'date',"price","amount of stock","phone number"]

def stock_sold():
   def display_menu():
      print("--------------------------------")
      print("Welcome to Acharya Bakery Enterprise")
      print("--------------------------------")
      print("0: Quit")
      print("1. Add the sale details")
      print("2. View sale deails")
      print("3. Search")
      print("5. Return to home")


   def add_sale():
      print("-------------------------")
      print("------Stock sale Details--------")
      print("--------------------------")

      global sale_file
      global sale_details

      sale_data = []

      df = pd.read_csv("stock2.csv")
      print(df.to_string())

      print("From above stock details enter the sale details\n ")

      for detail in sale_details:
         value = input("Enter "+ detail +" :")
         sale_data.append(value)

      with open(sale_file, "a", encoding="utf-7") as f:
         writer = csv.writer(f)
         writer.writerows([sale_data])

      stock = pd.read_csv('stock2.csv')

      def update_stock(s):
         if s['stockid'] == sale_data[0]:
            s['amount of stock'] -= int(sale_data[-2])
         return s

      updated_stock = stock.apply(update_stock, axis=1)
      updated_stock.to_csv('stock2.csv', index=False)

      
      
      print("Data saved successfully")
      input("Press any key to continue")
      return


   def view_sale():
      global sale_details
      global sale_file
      global sale_index

      print("--------Records Of Stocks Sold-----------")

      # with open(sale_index,"r",encoding="utf-7") as f:
      #    reader = csv.reader(f)
      #    with open(sale_file,"r",encoding="utf-7") as d:
      #       reader = csv.reader(d)
      #       for x in sale_details:
      #          print(x,end = "\t |")

      #       for row in reader:
      #             for ite-----------------------------")m in row:
      #                print(item, end="\t |")
      #             print("\n
      df = pd.read_csv("sale.csv")
      df.to_csv("sale.csv",header=sale_details,index=False)
      print(df.to_string())

      input("Press any key to continue")

   def search_sale():
      global sale_details
      global sale_file
      global sale_index

      print("----------Search Stocks Sold-----------")
      name = input("Enter the bakery name you want to search\n")

      sale = pd.read_csv('sale.csv')
      search_sale = sale[sale['stocksoldto'] == name]
      if not search_sale.empty:
         print(search_sale.to_string())

      else:
         print(f'Bakery with {name} not found')

      # with open(sale_file,"r",encoding="utf-8") as f:
      #    reader = csv.reader(f)
      #    for row in reader:
      #       if len(row) > 0:
      #          if id == row[0]:
      #             print("---------Sale Record found---------")
      #             with open(sale_file,"r",encoding="utf-8") as d:
      #                reader = csv.reader(d)
      #                for row1 in reader:
      #                   print("stock id: ",row1[0])
      #                   print("stock sold to: ",row1[1])
      #                   print("Date of sale",row1[2])
      #                   print("Amount of stock purchased: ",row1[3])
      #                   print("Price of the stock: ",row1[4])
      #                   print("Phone number of the dealer: ",row1[5])
      #                   break
      #          else:
      #             print("Stock record not found for this id")
      
      input("Press any key to continue")


   # def update_sale():
   #    global sale_details
   #    global sale_file

   #    print("-----------Update sale details-------------")
   #    print(pd.read_csv('sale.csv').to_string())

   #    id = input("Enter the stock id you want to update:\n")
   #    index_stock = None
   #    updated_data = []
   #    with open(sale_file,"r",encoding="utf-8") as f:
   #       reader = csv.reader(f)
   #       counter = 0
   #       for row in reader:
   #          if len(row) > 0:
   #             if id == row[0]:
   #                index_stock = counter
   #                print("Stock Data found in index:",index_stock)
   #                stock_data = []
   #                for field in sale_details:
   #                   value = input("Enter "+field[1]+": ")
   #                   stock_data.append(value)
   #                updated_data.append(stock_data)
   #             else:
   #                updated_data.append(row)
   #                counter += 1
      
   #    stock = pd.read_csv('stock2.csv')

   #    def update_stock(s):
   #       if s['stockid'] == updated_data[0]:
   #          s['amount of stock'] -= int(updated_data[-2])
   #       return s

   #    updated_stock = stock.apply(update_stock, axis=1)
   #    updated_stock.to_csv('stock2.csv', index=False)

   #    # Check if the record is found or not
   #    if index_stock is not None:
   #       with open(sale_file,"w",encoding="utf-8") as f:
   #          writer = csv.writer(f)
   #          writer.writerows(updated_data)
   #    else:
   #       print("Stock Record not found")
      
   #    input("Press any key to continue")


   while True:
      display_menu()
      choice = int(input("Enter the choice\n"))
      if choice == 0:
         exit()
      elif choice == 1:
         add_sale()
      elif choice == 2:
         view_sale()
      elif choice == 3:
         search_sale()
      elif choice == 5:
         main()
      else:
         print("Wrong choice entered!! Try Again")




#Main Fuction
def main():
   if __name__ == '__main__':
      print("---------------------------")
      print("Welcome to Acharya Enterprise")
      print("---------------------------")
      print("Home".center(25,'-'))
      ch = int(input("The details to be stored:\n 0. Quit\n 1. Stock Bought\n 2. Stock sold\n"))

      while True:
         if ch == 0:
            exit()
         elif ch == 1:
            stock_bought()
         elif ch == 2:
            stock_sold()
         else:
            print("Wrong choice entered!!")



#Calling main fuction
main()
