import time
import random
from random import randint
import csv
from csv import DictWriter, writer
from csv import DictReader



def Bank_service():
    # Generate 14-digit random Account Number for 
    def N_digit_random_number(n):
        start=10**(n-1)
        end=(10**n)-1
        return randint(start,end)

    # function to create account if not exit 
    def create_acc():
        with open("Bank_custumer_info.csv","a", newline="") as write:
            myFile=csv.writer(write)
            myFile.writerow(["Name","Address","AccountNumber","PhoneNo"])

            print("\nCreate Your New Bank Acount...")
            global userName
            userName=input("\nEnter Your Full Name: ").capitalize()
            if(userName== userName.isdigit()):
                print("Please Enter Only Name.")
                choice=input("Do You want to continue (Y/N)? : ")
                if(choice.isalpha()):
                    if(choice=="y"or choice=="Y"):
                        create_acc()
                    elif(choice=="n"or choice=="N"):
                        print("Thank YOU ...")
                        exit()
                    else:
                        print("INVALID INPUT")
                else:
                    print("System Terminated !!!")          


            global address
            address=input("Please Enter Your Full Address : ")
            

            global phoneNo 
            phoneNo=input("Enter Your Phone Number : ")
            if(phoneNo.isdigit()):
                print("Wait.......")
                time.sleep(1)
                print(f"\nYour Account Number is generating.....................\nDon't press Anything.")
                time.sleep(3)      
                accountNumber=N_digit_random_number(14)
                time.sleep(2)
                print("****************************")
                print(f"Your A/C No. : {accountNumber}")
                print("****************************")   
                time.sleep(2)
                print("\nAccount Number Generated Successfully........... . \nDon't share A/C No. with Anyone!") 
                time.sleep(3)

                global userBalance  
                userBalance=(input("\nEnter How Much You Want To Deposite In Your Account : "))
                if (userBalance.isalpha()):
                    print("Please Enter Only Amount.")
                    choice=input("Do You want to continue (Y/N)? : ")
                    if(choice.isalpha()):
                        if(choice=="y"or choice=="Y"):
                            create_acc()
                        elif(choice=="n"or choice=="N"):
                            print("Thank YOU ...")
                            exit()
                        else:
                            print("INVALID INPUT")    


                myFile.writerow([userName,address,accountNumber,phoneNo])
            else:
                time.sleep(1)
                print("INVALID INPUT !!! INPUT NUMBERS ONLY ....")
                choice =input("System Terminated... Do You Want To Try Again (Y/N)?: ")
                if(choice.isalpha()):
                    if(choice=="y"or choice=="Y"):
                        create_acc()
                    elif(choice=="n"or choice=="N"):
                        print("Thank YOU ...")
                        exit()
                    else:
                        print("INVALID INPUT")
                else:
                    print("System Terminated !!!")
        
        print()
        print(f"Welcome {userName} in National Indian Bank.") 
        time.sleep(1.7)

        while True:
            print("\nYour Transaction Numbers are : \n1) Check Amount \t2) Withdraw Amount \n3) Deposite Amount \t4) Exit")
            option=int(input("\nEnter the Transaction Number: "))
            
            if (option in  [1,2,3,4]):
                userBalance=int(userBalance)
                match option:
                        case (1):
                            print("***********************")
                            print(f"Total Amount: {userBalance} ₹")
                            print("***********************")
                        case (2):
                            withdraw=int(input("Enter the withdraw Amount: "))
                            if(userBalance<withdraw):
                                print("You dno't have sufficient Balance!")
                            else:
                                userBalance=userBalance-withdraw
                                print("*****************************")
                                print(f"You Current Balance is {userBalance} ₹")
                                print("*****************************")
                        case (3):
                            deposite=int(input("Enter the Deposite Amount: "))
                            userBalance=userBalance+deposite
                            print("******************************")
                            print(f"your Current Balance is {userBalance} ₹")
                            print("******************************")
                        case (4):
                            if (option==4):
                                print("Thanks for Comming in National Indian Bank...")
                                break
                        case (_):
                            print("Something Went Wrong")
            else:
                print("Please Enter The Only Transaction Number \nLike 1, 2, 3, 4 ")
            


    print("\n----- WELCOME TO INTERNATION INDIAN BANK -----")
    newCustumer=input("\nYou Have Account In Internation Indian Bank. \nPress Y for Yes OR N for No. (y/n) : ")


    if (newCustumer=="y"or newCustumer=="Y"):
        while True:
            userPhoneNo=input("Enter Your 10-digit Phone Number : ")
            if (len(userPhoneNo)==10):
                break
            print("Enter 10 digits no. only")
        
        if userPhoneNo in open("Bank_custumer_info.csv").read():
            print("Account is Exist")
        else:
            print("Account is Not Exits") 
            userInput=input("Do You Want To Open New Account (Y/N)? : ")
            if (userInput=='y' or userInput=='Y'):
                create_acc()
            else:
                print("Thank You.. \n\tHave a Nice day")

        

    elif (newCustumer=="n" or newCustumer=="N" ):
        create_acc()

    else:
        print("Invalid Input!!!")

    input("Press Enter To Exit...")

if __name__ =="__main__":
    Bank_service()
