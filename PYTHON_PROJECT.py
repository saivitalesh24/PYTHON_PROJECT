import datetime
class Sbi:
    bank_name='SBI'
    bank_loc='Chaitanyapuri'
    IFSC_CODE='SBI12456'
    bank_manager='Rahul'
    pincode=500060

    no_of_cust=0
    cust_det={}
    transaction_details={}


    def __init__(self,name,phone,age,aadhar,address,balance,pin):
        self.name=name
        self.phone=self.validate_phone(phone)
        self.age=self.validate_age(age)
        self.aadhar=self.validate_aadhar(aadhar)
        self.address=address
        self.balance=balance
        self.pin=pin
        
        # self.info_cust()
        Sbi.no_of_cust+=1
        print(f'no of customers: {self.no_of_cust}')
        acc_num=1000 + Sbi.no_of_cust
        self.store_cust_data(acc_num,self)



    # @classmethod
    # def info_cust(cls):
    #     cls.no_of_cust+=1
    #     print(f'No of customers are : {cls.no_of_cust}')
    #     print('-'*40)

    @classmethod
    def store_cust_data(cls,acc_num_data,data):
        cls.cust_det[acc_num_data]=data
    

    @staticmethod
    def validate_phone(num):
        if len(str(num))==10 and str(num).isdigit():
            return num
        else:
            raise Exception('ENTER VALID PHONE NUMBER')
        
    
    @staticmethod
    def validate_age(age1):
        if age1>=18:
            return age1
        else:
            raise Exception('NOT ELIGIBLE TO CREATE ACCOUNT')
        
    @staticmethod
    def validate_aadhar(aadhar1):
        if len(str(aadhar1)) ==12 and str(aadhar1).isdigit():
            return aadhar1
        else:
            raise Exception('ENTER VALID AADHAR')
    
    @staticmethod
    def validate_pin(pin1):
        if len(str(pin1)) == 4 and str(pin1).isdigit():
            return pin1
        else:
            raise Exception('ENTER VALID PIN')
        
    @classmethod
    def check_bal(cls):
        user_acc=int(input('ENTER ACCOUNT NUMBER :'))
        user_pin=int(input('ENTER YOUR PIN :'))
        if user_acc in cls.cust_det and user_pin== cls.cust_det[user_acc].pin :
            print(f'YOUR CURRENT BALANCE IS :{cls.cust_det[user_acc].balance}')
        elif user_acc in cls.cust_det and user_pin != cls.cust_det[user_acc].pin:
            print('ENTER VALID PIN')
        else:
            print('ENTER VALID USER')

    @classmethod
    def deposit_amount(cls):
        print('\n-----------DEPOSIT PAGE-----------\n')
        user_acc=int(input('ENTER ACCOUNT NUMBER :'))
        user_pin=int(input('ENTER YOUR PIN :'))
        if user_acc in cls.cust_det and user_pin== cls.cust_det[user_acc].pin:
            amount=int(input('ENTER THE AMOUNT: '))
            if amount>0:
                cls.cust_det[user_acc].balance+=amount
                print(f'{amount} has been credited '
                      f'YOUR CURRENT BALANCE IS {cls.cust_det[user_acc].balance}')
                if user_acc not in cls.transaction_details:
                    cls.transaction_details[user_acc]=[{'time':datetime.datetime.now(),
                                                        'Type':'credited',
                                                        'amount':amount,
                                                        'balance':cls.cust_det[user_acc].balance
                                                        }]
                else:
                    cls.transaction_details[user_acc]+=[{'time':datetime.datetime.now(),
                                                        'Type':'credited',
                                                        'amount':amount,
                                                        'balance':cls.cust_det[user_acc].balance
                                                        }]
                
            else:
                print('ENTER VALID AMOUNT')

        elif user_acc in cls.cust_det and user_pin!= cls.cust_det[user_acc].pin :
            print('ENTER VALID PIN')

        else:
            print('ENTER SUFFICIENT DETAILS')
    

    @classmethod
    def withdraw_amount(cls):
        print('\n----------  WITHDRAW PAGE --------------\n')
        user_acc=int(input('ENTER ACCOUNT NUMBER :'))
        user_pin=int(input('ENTER YOUR PIN :'))
        if user_acc in cls.cust_det and user_pin== cls.cust_det[user_acc].pin:
            amount=int(input())
            if amount>0 and amount<cls.cust_det[user_acc].balance:
                cls.cust_det[user_acc].balance-=amount
                print(f'RS.{amount} has been withdrawn from your account '
                      f'your current balance is RS.{cls.cust_det[user_acc].balance}')
                if user_acc not in cls.transaction_details:
                    cls.transaction_details[user_acc]=[{'time':datetime.datetime.now(),
                                                        'Type':'debited',
                                                        'amount':amount,
                                                        'balance':cls.cust_det[user_acc].balance
                                                        }]
                else:
                    cls.transaction_details[user_acc]+=[{'time':datetime.datetime.now(),
                                                        'Type':'debited',
                                                        'amount':amount,
                                                        'balance':cls.cust_det[user_acc].balance
                                                        }]
            else:
                print('ENTER VALID AMOUNT')

        elif user_acc in cls.cust_det and user_pin!= cls.cust_det[user_acc].pin :
            print('ENTER VALID PIN')

        else:
            print('ENTER SUFFICIENT DETAILS')
    
    @classmethod
    def modify_user_acc(cls):
        print('\n------------- MODIFY PAGE ----------------\n')
        user_acc=int(input('ENTER ACCOUNT NUMBER :'))
        user_pin=int(input('ENTER YOUR PIN :'))
        if user_acc in cls.cust_det and user_pin== cls.cust_det[user_acc].pin:
            while True:
                print('\nselect 1 to modify name\n','select 2 to modify address\n' 'select 3 to modify mobile\n',
                  'select 4 to exit\n')
                select=int(input())
                match select:
                    case 1:
                        print('\n--------- PAGE TO MOMODIFY NAME ---------\n')
                        new_name=input()
                        confirm_name=input()
                        if new_name == cls.cust_det[user_acc]:
                            print('NAME ALREADY EXISTS')
                        elif new_name==confirm_name:
                            cls.cust_det[user_acc]=new_name
                            print('MODIFIED YOUR NAME SUCCESSFULLY')
                        else:
                            print('NEW_NAME AND CONFIRM_NAME DID NOT MATCHED')
                    
                    case 2:
                        print('\n--------- PAGE TO MOMODIFY ADDRESS ---------\n')
                        new_address=input()
                        confirm_address=input()
                        if new_address == cls.cust_det[user_acc].address:
                            print('ADDRESS ALREADY EXISTS')
                        elif new_name==confirm_address:
                            cls.cust_det[user_acc].address=new_address
                            print('MODIFIED YOUR ADDRESS SUCCESSFULLY')
                        else:
                            print('NEW_ADDRESS AND CONFIRM_ADDRESS DID NOT MATCHED')
                        
                    case 3:
                        print('\n----------- PAGE TO MODIFY MOBILE ---------\n')
                        new_mobile=int(input())
                        confirm_mobile=int(input())
                        if new_mobile == cls.cust_det[user_acc].phone:
                            print('MOBILE NUMBER ALREADY EXISTS')
                        elif new_mobile==confirm_mobile:
                            cls.validate_phone(new_mobile)
                            cls.cls.cust_det[user_acc].phone=new_mobile
                            print('MODIFIED YOUR MOBILE SUCCESSFULLY')
                        else:
                            print('NEW_MOBILE AND CONFIRM_MOBILE DID NOT MATCHED')
                    case 4:
                        print('MODIFICATION SUCESSFYLLY COMPLETED')
                        break
                    case _:
                        print('YOU NEED TO SELECT FROM 1,2,3,4')
        
        elif user_acc in cls.cust_det and user_pin!= cls.cust_det[user_acc].pin :
            print('ENTER VALID PIN')

        else:
            print('ENTER SUFFICIENT DETAILS')

            


    @classmethod
    def change_pin(cls):
        print('\n--------- PIN CHANGE PAGE ----------\n')
        user_acc=int(input('ENTER ACCOUNT NUMBER :'))
        user_pin=int(input('ENTER YOUR PIN :'))
        if user_acc in cls.cust_det and user_pin== cls.cust_det[user_acc].pin :
            new_pin=int(input())
            confirm_pin=int(input())
            if new_pin==confirm_pin:
                cls.validate_pin(new_pin)
                cls.cust_det[user_acc].pin=new_pin
                print('PIN GENERATED')
            elif new_pin==cls.cust_det[user_acc].pin:
                print('PLEASE ENTER NEW PIN')

            else:
                print('NEW PIN AND CONFIRM PIN SHOULD BE SAME')
        elif user_acc in cls.cust_det and user_pin!= cls.cust_det[user_acc].pin :
            print('ENTER VALID PIN')

        else:
            print('ENTER SUFFICIENT DETAILS')
    @classmethod
    def all_details(cls):
        for i in cls.cust_det:
            print(f'name:{cls.cust_det[i].name}\n'
                  f'phone:{cls.cust_det[i].phone}\n'
                  f'age:{cls.cust_det[i].age}\n'
                  f'aadhar:{cls.cust_det[i].aadhar}'
                  'address,balance,pin')
            print('***********')

    def loc(self):
        print(self.address)



c1=Sbi('Monty',1234567892,25,234567891346,'Banglore',50000,1234)
c2=Sbi('Yasin',2345678912,28,123456789678,'Raichur',40000,3456)
# Sbi.check_bal()
# print(Sbi.cust_det)
# Sbi.deposit_amount()
# print(Sbi.transaction_details)
# Sbi.deposit_amount()
# print(Sbi.transaction_details)
# Sbi.modify_user_acc()
# Sbi.withdraw_amount()
Sbi.all_details()