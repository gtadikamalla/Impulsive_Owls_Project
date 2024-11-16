import os
from Data import Create_db, Create_Tables, Insert_Data
import POPS_Functions


outer_Break=False
while not outer_Break:
    print('______________________')
    print('D for Database access.')
    print('U for User access.')
    print('Q for quit.')
    choice=input('Enter D or U or Q:')
    if choice is not None and choice and choice in 'Dd':
        while True:
            print('_______________')
            print('C for create DB')
            print('T for Create Tables')
            print('I for Insert Tables.')
            print('B for Back to Main Menu.')
            print('Q for Quit the process.')
            choice=input('Enter C or T or I or B or Q:')
            if choice is not None and choice and choice in 'cC':
                DB=input('Enter the Database name to create:')
                Create_db.create_sqlite_database(DB)
            elif choice is not None and choice and choice in 'Tt':
                DB=input('Enter the DB name to create tables:')
                Create_Tables.creating_tables(DB)
            elif choice is not None and choice and choice in 'iI':
                db=input('Enter the DB name to insert data:')
                Insert_Data.insert_data_into_tables(db)
                
            elif choice is not None and choice and choice in 'Bb':
                break
            elif choice is not None and choice and choice in 'qQ':
                outer_Break = True
                break
            elif choice.lower() not in 'ctib':
                print('Invalid input.')
                print('--------------')
                continue
    elif choice is not None and choice and choice in 'uU':
        while True:
            print('C for Clerck Access.')
            print('W for Warehouse Manager Access.')
            print('B for Back to Main Menu.')
            print('Q for Quit the process.')
            choice=input('Enter your role for access:')
            
            if choice is not None and choice and choice in 'cC':
                print('R for Registering the New Customer.')
                print('T for Take Order and keep status is open.')
                print('A for Assign Order to Sales Person.')
                print('B for Back to Main Menu.')
                print('Q for Quit the process.')

                Clerk_choice=input('Enter R or T or A B or Q to perform action:')
                if Clerk_choice is not None and Clerk_choice and Clerk_choice in 'rR':
                    POPS_Functions.Register_Customer()
                elif Clerk_choice is not None and Clerk_choice and Clerk_choice in 'tT':
                    POPS_Functions.Customer_Order()
                elif Clerk_choice is not None and Clerk_choice and Clerk_choice in 'aA':
                    POPS_Functions.Assigned_Orders()
                elif Clerk_choice is not None and Clerk_choice and Clerk_choice in 'bB':
                    break
                elif Clerk_choice is not None and Clerk_choice and Clerk_choice in 'qQ':
                    outer_Break = True
                    break
                elif Clerk_choice is not None and Clerk_choice and Clerk_choice.lower() not in 'rtabq' :
                    print('Invalid input.')
                    continue

            elif choice is not None and choice and choice in 'wW':
                while True:
                    Read_Order=input('Enter (R) to read all the Orders:')
                    if Read_Order is not None and Read_Order and Read_Order in 'rR':
                        POPS_Functions.warehouse_Manager()
                        break
                    else:
                        break
            elif choice is not None and choice and choice in 'Bb':
                break
            elif choice is not None and choice and choice in 'qQ':
                outer_Break = True
                break
            elif choice is not None and choice and choice.lower() not in 'cwbq':
                print('Invalid input.')
                print('--------------')
                continue

                


    elif choice is not None and choice and choice in 'qQ':
        break
    else:
        print('Invalid input. Please enter valid input.')
        continue



