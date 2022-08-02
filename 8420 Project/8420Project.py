# 8420 Project - SWAP APP
# Ecommerce System
# Group: MIC
# Group Members: Yuhang Li, Julia(Yazheng Guo), Edison(Keyao Wang).

import sqlite3
import pandas as pd

# Password encryption rules:
alphabet_user = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'  # Normal password table
alphabet_system = 'TIMEODANSFRBCGHJKLPQUVWXYZtimeodansfrbcghjklpquvwxyz9876543210'  # Cryptographic comparison table

# SQLITE3 Database connection:
connection = sqlite3.connect('swap.db')
cursor = connection.cursor()

# Define Global Variables:
current_email = None   #Record current login email as a global variable.
search = None

# Database creation:
def CreateDatabase_InsertData():
    # 1. Create 3 tables
    connection = sqlite3.connect('swap.db')
    cursor = connection.cursor()
    #cursor.execute("DROP TABLE Product")
    connection.commit()

    #Create table Product:
    cursor.execute("""CREATE TABLE Product (
                    ProductID integer primary key not null,
                    Year integer not null,
                    Brand text null,
                    Name text not null,
                    Size text not null,
                    Price real not null,
                    Stock integer not null,
                    SalesHistory integer null DEFAULT 0
                    )""")
    connection.commit()

    #Create table Orders:
    cursor.execute("""CREATE TABLE Orders (
                    OrderID integer primary key,
                    ProductID integer not null,
                    CustomerID integer not null,
                    Price real not null,
                    DateTime text
                    )""")
    connection.commit()

    #Create table Users:
    cursor.execute("""CREATE TABLE Users (
                    UserID integer primary key,
                    Name text not null,
                    Gender text null,
                    Phone text null,
                    Email text not null,
                    Street text null,
                    Province text null,
                    PostalCode text null,
                    PurchaseHistory integer DEFAULT 0,
                    TotalSales real not null DEFAULT 0,
                    UserType text not null DEFAULT "Regular",
                    Enc_Password text not null
                    )""")
    connection.commit()

    # Step2: INSERT INITIAL VALUES INTO DATABASE:
    # Product Table:
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO Product VALUES
                       (1, 2015,    'Nike',    'AJ1 Chicago', '9.5', 1025,  5, 10),
                       (2,  2022,  'Nike',    'AF1 Low White',   '10',  120,   125,   95),
                       (3,  1998,  'Nike',    'AJ1 Bred Toe',    '11',  250,   245,   55),
                       (4,  2021,  'Nike',    'Dunk SB Cherry',  '8',   450,   13,    8),
                       (5,  2000,  'Nike',    'Dunk SB Paris',   '9',   8500,  2, 0),
                       (6,  2004,  'Nike',    'Dunk SB Heineken',    '9',   1045,  30,    3),
                       (7,  2015,  'Nike',    'Dunk SB Cherry',  '9',   500,   8, 6),
                       (8,  2016,  'Nike',    'Dunk SB Cherry',  '10',   550,   8, 12),
                       (9,  2017,  'Nike',    'AF1 Low White',   '10',  120,   100,   110),
                       (10,    2018,    'Nike',    'AF1 Low White',   '8',   120,   100, 75),
                       (11, 2019,  'Nike',    'AF1 Low White',   '8',   120,   100,   78),
                       (12, 2020,  'Nike',    'AF1 Low White',   '9',   120,   100,   98),
                       (13, 2021,  'Nike',    'AF1 Low White',   '9.5', 120,   100,   90),
                       (14, 2022,  'Nike',    'AF1 Low White',   '12',  120,   100,   95),
                       (15, 2018,  'Nike',    'AF1 Low Black',   '11',  120,   100,   105),
                       (16, 2019,  'Nike',    'AF1 Low Black',   '8',   120,   100,   105),
                       (17, 2020,  'Nike',    'AF1 Low Black',   '10',  120,   100,   105),
                       (18, 2021,  'Nike',    'AF1 Low Black',   '11',  120,   100,   105),
                       (19, 2022,  'Nike',    'AF1 Low Black',   '11.5',  120,   100,   105),
                       (20, 2011,  'Adidas',  'Orignal Low',     '9',   135,   50,    35),
                       (21, 2012,  'Adidas',  'Orignal Low',     '9.5',   135,   40,    30),
                       (22, 2013,  'Adidas',  'Orignal Low',     '10',  135,   50,    32),
                       (23, 2014,  'Adidas',  'Orignal Low',     '8.5', 135,   75,    75),
                       (24, 2015,  'Adidas',  'NBHD Black',  '9',   275,   15,    8),
                       (25, 2016,  'Adidas',  'NBHD Black',  '12',  270,   10,    8),
                       (26, 2021,  'LV',  'Bumbag',  'O/S', 5050,  2, 1),
                       (27, 2008,  'Supreme', 'Boxlogo Tee',     'M',   850,   1, 0),
                       (28, 2020,  'Supreme', 'Boxlogo Hood',    'L',   1050,  6, 13),
                       (29, 2021,  'Palace',  'Tri Logo Tee',    'M',   150,   25,    10),
                       (30, 2019,  'Palace',  'Tank Tee',    'M',   120,   20,    45),
                       (31, 2019,  'Jordan',  'Pro Strong',    '8.5',   180,   15,    10),
                       (32, 2020,  'Jordan',  'Retro 13',    '7',   175,   20,    45),
                       (33, 2022,  'Jordan',  'Retro 16',    '11.5',   260,   40,    35),
                       (34, 2021,  'Jordan',  'AJ1 Mid',  '6.5',  120,   10,    8),
                       (35, 2021,  'Jordan',  '6 ring',  '7', 150,  15, 25),
                       (36, 2021,  'Jordan', 'Air Jordan XXXVI Low',     '8.5',   250,   1, 0),
                       (37, 2022,  'Jordan', 'Air Jordan XXXVI Low',     '7.5',   260,   1, 1),
                       (38, 2020,  'Vans',  'Sk8-Hi',    '6.5',   90,   25,    10),
                       (39, 2021,  'Vans',  'Sk8-Hi',    '9',   100,   20,    45),
                       (40, 2019,  'Vans',  'Ultrarange Hi GTX',    '8.5',   200,   30,    30),
                       (41, 2019,  'Vans',  'Ultrarange EXO',    '7.5',   125,   20,    45),
                       (42, 2016,  'Vans',  'Old Skool',  '11',  90,   10,    10),
                       (43, 2021,  'New Balance',  '327',  '5.5', 130,  2, 1),
                       (44, 2019,  'New Balance', 'Rebel TR',     '12',   160,   1, 0),
                       (45, 2020,  'New Balance', 'Rebel TR',    '11',   160,  6, 13),
                       (46, 2021,  'New Balance',  '574 Classic',    '9',   85,   25,    15),
                       (47, 2018,  'Birkenstock',  'Arizona',    '6.5',   120,   20,    45),
                       (48, 2019,  'Birkenstock',  'Arizona',    '7',   140,   10,    5),
                       (49, 2020,  'Birkenstock',  'Boston',    '6.5',   200,   25,    35),
                       (50, 2021,  'Birkenstock',  'Super Birki',    '8',   120,   10,    40);""")

    connection.commit()

    # Orders Table:
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO Orders VALUES
                       (1,  6, 6, 1045, datetime('now')),
                       (2,  3, 7, 250, datetime('now')),
                       (3,  1, 10,    1025, datetime('now')),
                       (4,  2, 9,  120, datetime('now')),
                       (5,  2, 8, 120, datetime('now')),
                       (6,  4, 8, 450, datetime('now')),
                       (7,  6, 6, 1045, datetime('now')),
                       (8,  11,    10,    120, datetime('now')),
                       (9,  12,    5, 120, datetime('now')),
                       (10, 6, 4, 1045, datetime('now'));""")
    connection.commit()

    # Users Table:
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO Users VALUES
                       (1, "Yuhang", "M", "226-355-4325", "li@conestoga.ca", "25 Hazel St", "ON", "N2D 5D8", 2, 3000, "Admin", "112233"), 
                       (2, "Edison", "M", "226-877-3888", "Ed@conestoga.ca", "168 Hazel St", "ON", "N2D 4F8", 0, 0, "Admin", "112233"),
                       (3, "Julia", "F", "226-345-7857", "Guo@conestoga.ca", "132 Albert St", "ON", "N4K 4H8", 3, 1250, "Admin", "112233"),
                       (4, "Tom", "M", "226-355-4675", "Tom@conestoga.ca", "131 Albert St", "ON", "N5E 7K9", 5, 3000, "Regular", "112233"),
                       (5, "Jack", "M", "226-785-5425", "Jack@conestoga.ca", "255 University Ave", "ON", "N2Z 4D6", 4, 5000, "Regular", "112233"),
                       (6, "Dave", "M", "226-689-6925", "Dave@conestoga.ca", "68 Hope Rd", "ON", "N7K 5D8", 2, 6000, "Regular", "112233"),
                       (7, "James", "M", "226-323-4385", "James@conestoga.ca", "30 Hazelnut St", "ON", "N3E 5D9", 2, 3000, "Regular", "112233"), 
                       (8, "Luke", "M", "226-422-3800", "Luke@conestoga.ca", "22 Hazel St", "ON", "N2D 4F0", 0, 0, "Regular", "112233"),
                       (9, "Matthew", "M", "226-452-7907", "Matthew@conestoga.ca", "55 Albert St", "ON", "N4K 3I9", 3, 1300, "Regular", "112233"),
                       (10, "Emma", "F", "226-967-1342", "Emma@conestoga.ca", "22 University Ave", "ON", "N3P 0E1", 5, 3000, "Regular", "112233"),
                       (11, "Jackson", "M", "226-333-6660", "Jackson@conestoga.ca", "60 Parks Ave", "ON", "N2F 3E1", 4, 4500, "Regular", "112233"),
                       (12, "Henry", "F", "226-744-2592", "Henry@conestoga.ca", "25 University Ave", "ON", "N3P 0E4", 5, 2400, "Regular", "112233"),
                       (13, "Eva", "F", "226-907-1932", "Eva@conestoga.ca", "198 Charlies Ave", "ON", "N3P 0S2", 5, 3500, "Regular", "112233"),
                       (14, "Carol", "M", "226-300-4005", "Carol@conestoga.ca", "24 Sheppard Ave", "ON", "N6F 4R3", 5, 2500, "Regular", "112233"),
                       (15, "Jade", "F", "226-555-5433", "Jade@conestoga.ca", "52 Farms St", "ON", "N2A 4T9", 4, 5600, "Regular", "112233"),
                       (16, "Ariana", "F", "226-521-4525", "Ariana@conestoga.ca", "12 Hopeland Rd", "ON", "N3E 5A5", 3, 1400, "Regular", "112233"),
                       (17, "Austin", "M", "226-632-4413", "Austin@conestoga.ca", "98 Albert St", "ON", "N5L 4D0", 2, 4800, "Regular", "112233"), 
                       (18, "Nicholas", "M", "226-263-4510", "Nicholas@conestoga.ca", "155 Charlies St", "ON", "N4D 4S6", 0, 0, "Regular", "112233"),
                       (19, "Sophie", "F", "226-521-6250", "Sophie@conestoga.ca", "62 Atlas St", "ON", "N2L 5K9", 4, 1800, "Regular", "112233"),
                       (20, "Ruby", "F", "226-423-9524", "Ruby@conestoga.ca", "99 King St", "ON", "N7A 2P6", 2, 3000, "Regular", "112233");""")
    connection.commit()


# Define functions:
def update_csv(TableName,csv_path):
    sql = '''
        select * from {}
    '''
    sql_update = sql.format(TableName)
    allinfo = cursor.execute(sql_update)
    result = allinfo.fetchall()
    columnDes = cursor.description
    columnNames = [columnDes[i][0] for i in range(len(columnDes))]
    df = pd.DataFrame([list(i) for i in result], columns=columnNames)
    df.to_csv(csv_path, sep=',', header=True, index=False)

def asc_id(Id,TableName):       # Incrementing the ID and getting the new ID
    sql_last_data = '''select {} from {} order by {} desc LIMIT 1;'''
    sql_last_id = sql_last_data.format(Id,TableName,Id)
    get_id = cursor.execute(sql_last_id)
    result = get_id.fetchall()  # Return all rows of sql statement
    columnDes = cursor.description  # Gets the description of the connection object
    columnNames = [columnDes[i][0] for i in range(len(columnDes))]  # get column names
    df = pd.DataFrame([list(i) for i in result], columns=columnNames)  # Convert to data frame format
    row = df.iloc[0].values.tolist()
    id = row[0]
    id += 1
    return id

def encode(original_password):      # Encrypts the password entered by the user
    global alphabet_user, alphabet_system       # Calling an external table
    encrypted_user = ''
    for single_char in original_password:       # Iterate over every character in the password
        if single_char in alphabet_user:        # Check every single character if it's in the normal table
            index = alphabet_user.index(single_char)        # Record the index of each character in the normal table
            encrypted_user = encrypted_user + alphabet_system[index]        # Convert
        else:
            encrypted_user = encrypted_user + single_char       # Remain the same
    return encrypted_user

def decode(Database_password):      # Decode the password in the database (for testing purposes, enter the password which was already set)
    global alphabet_user, alphabet_system
    decrypted_user = ''
    for single_char in Database_password:
        if single_char in alphabet_system:      # Check
            index = alphabet_system.index(single_char)      # Record the index of each character in the crptographic comparison table
            decrypted_user = decrypted_user + alphabet_user[index]
        else:
            decrypted_user = decrypted_user + single_char
    return decrypted_user

def check_useremail(useremail):     #Check whether the mailbox already exists
    sql_whole_table = '''select count(*) from Users where Email = '{}' limit 1;'''       #Check whether the user's mailbox column already contains input information
    sql_all = sql_whole_table.format(useremail)     #Adds user input information to the SQL statement
    allinfo = cursor.execute(sql_all)        #Store information after execution
    result = allinfo.fetchall()     #Return all rows of sql staement
    columnDes = cursor.description       # Gets the description of the connection object
    columnNames = [columnDes[i][0] for i in range(len(columnDes))]      #get columnnames
    df = pd.DataFrame([list(i) for i in result], columns=columnNames)       #Convert to data frame format
    row = df.iloc[0].values.tolist()
    repeatnum = row[0]      #Get the data in the Dataframe
    if repeatnum != 0:
        return 0
    else:
        return 1

def create_account():
    enter_email = input('Please enter your email (Compulsive): ')
    if check_useremail(enter_email) == 1:
        print("Next we need some personal information about you: ")
        user_id = asc_id('UserID','Users')
        user_name = input('Please enter your name: ')
        user_gender = input('Please enter your gender(M/F): ')
        user_phone = input('Please enter your phonenumber: ')
        user_street = input('Please enter your street number and name: ')
        user_province = input('Please enter your province: ')
        user_postalcode = input('Please enter your postalcode: ')
        user_pd = input('Please input your password: ')
        sys_pd = encode(user_pd)
        sql_new_user = '''
        insert into Users (UserID,Name,Gender,Phone,Email,Street,Province,Postalcode,Enc_Password)
         values ('{}','{}','{}','{}','{}','{}','{}','{}','{}');
        '''
        sql_insert_new = sql_new_user.format(user_id,user_name,user_gender,user_phone,enter_email,user_street,user_province,
        user_postalcode,sys_pd)
        cursor.execute(sql_insert_new)
        connection.commit()
        update_csv('Users','./user.csv')
        print("Congratulations on creating a new account!")
    else:
        print("This email address has been registered, please log in instead.")

def check_userpassword(useremail,enter_password):     #C heck whether the mailbox already exists
    sys_password = encode(enter_password)       # Encrypts user input passwords into database format
    sql_whole_table = '''select Enc_password from Users where Email = '{}' limit 1;'''       # Check whether the user's mailbox column already contains input information
    sql_all = sql_whole_table.format(useremail)     # Adds user input information to the SQL statement
    allinfo = cursor.execute(sql_all)        # Store information after execution
    result = allinfo.fetchall()     # Return all rows of sql staement
    columnDes = cursor.description       # Gets the description of the connection object
    columnNames = [columnDes[i][0] for i in range(len(columnDes))]      # get columnnames
    df = pd.DataFrame([list(i) for i in result], columns=columnNames)       # Convert to data frame format
    row = df.iloc[0].values.tolist()
    password = row[0]
    strpassword = str(password)     #To STRING type
    if strpassword == sys_password:
        return 1
    else:
        return 0

def check_UserType(useremail):
    sql_get_type = '''select UserType from Users where Email = '{}' limit 1;'''
    sql_user_type  = sql_get_type.format(useremail)
    info = cursor.execute(sql_user_type)
    result = info.fetchall()  # Return all rows of sql staement
    columnDes = cursor.description  # Gets the description of the connection object
    columnNames = [columnDes[i][0] for i in range(len(columnDes))]  # get columnnames
    df = pd.DataFrame([list(i) for i in result], columns=columnNames)  # Convert to data frame format
    row = df.iloc[0].values.tolist()
    User_Type = row[0]
    if User_Type == 'Regular':
        return 1
    else:
        return 0



def log_in_asRegular():
    enter_email = input('Please enter your email address: ')
    if check_useremail(enter_email) == 0:
        if check_UserType(enter_email) == 1:
            user_pd = input('Please enter your password: ')
            if check_userpassword(enter_email, user_pd) == 1:
                global current_email
                current_email = enter_email
                print("Congratulations on your successful login!")
                return 0
            else:
                print("Incorrect password, please try again!")
                return 1
        else:
            print('Please log in through the administrator channel.')
            return 1
    else:
        print("The account does not exist. Please sign up or try again.")
        return 1

def log_in_asAdmin():
    enter_email = input('Please enter your email address: ')
    if check_useremail(enter_email) == 0:
        if check_UserType(enter_email) == 0:
            user_pd = input('Please enter your password: ')
            if check_userpassword(enter_email, user_pd) == 1:
                print("Congratulations on your successful login!")
                return 0
            else:
                print("Wrong password, please try again.")
                return 1
        else:
            print('Please log in through the Regular user channel.')
            return 1
    else:
        print("The account does not exist. Please sign up or try again.")
        return 1

def change_password():
    global current_email
    input_password = input('Please enter a new password: ')
    new_password = encode(input_password)
    sql_edit_password = '''update Users set Enc_Password = '{}' where Email = '{}';'''
    sql_edit_password_f = sql_edit_password.format(new_password,current_email)
    cursor.execute(sql_edit_password_f)
    connection.commit()
    update_csv('Users','./user.csv')
    print('Your password has been changed!')


# Regular User Menu
# 1.View all products menu:
def viewproducts():
    cursor.execute("SELECT * FROM Product")
    connection.commit()
    result = cursor.fetchall()
    columnDes = cursor.description
    columnNames = [columnDes[i][0] for i in range(len(columnDes))]
    df = pd.DataFrame([list(i) for i in result], columns = columnNames)
    print(df)

# 2.Search Product by ID:
def searchproduct():
    enter_pid = input("Please enter the ProductID you want to search for: ")
    global search
    search = enter_pid
    cursor.execute("SELECT * FROM Product WHERE ProductID = '{}'".format(int(search)))
    connection.commit()
    result = cursor.fetchall()
    columnDes = cursor.description
    columnNames = [columnDes[i][0] for i in range(len(columnDes))]
    df = pd.DataFrame([list(i) for i in result], columns=columnNames)
    print(df)
    buy = input("Do you want to buy this item?         Y: Buy    N: Return to Menu ")
    if buy == "Y":
        purchase()
    else:
        return


# 3.Purchase Product by ID:
# Define Update Functions:
# Get Id function:
def getid():
    global current_email
    cursor.execute("SELECT UserID FROM Users WHERE Email = '{}'".format(current_email))
    connection.commit()
    id = cursor.fetchall()
    return id[0][0]
# ex) returns 2 if Edison logs in

# Update PurchaseHistory function:
def updatePH():
    cursor.execute("""UPDATE Users SET PurchaseHistory = PurchaseHistory + 1
                         WHERE UserID = {}""".format(getid()))
    connection.commit()

# Update TotalSales function:
def getprice():
    global search
    cursor.execute("SELECT Price FROM Product WHERE ProductID = {}".format(int(search)))
    connection.commit()
    p = cursor.fetchall()
    return p[0][0]

def updateTS():
    global search
    cursor.execute("""UPDATE Users SET TotalSales = TotalSales + {}
                             WHERE UserID = {}""".format(getprice(), getid()))
    connection.commit()

# Update Product SalesHistory +1 AND STOCK -1:
def updateSHST():
    global search
    cursor.execute("""UPDATE Product SET SalesHistory = SalesHistory + 1,
                                         Stock = Stock - 1 
                             WHERE ProductID = {}""".format(int(search)))
    connection.commit()


#Update Order table, insert values into it.
def updateUT():
    global search
    cursor.execute("""INSERT INTO Orders VALUES
                  ({},{},{},{},datetime('now'))""".format(asc_id("OrderID", "Orders"), search, getid(), getprice()))

    connection.commit()

def purchase():
    print('Purchase has been completed')
    updatePH() # User purchase history + 1:
    updateTS() # User TotalSales + Price
    updateSHST() # Product SalesHistory +1, Stock -1.
    updateUT() # Update Order Table
    update_csv('Product','./product.csv')
    update_csv('Orders','./orders.csv')

def regular_menu():
    menu = '''
       ******************************Welcome***********************************
       1.View all products 2.Search product by id 3.Change the password  4.Quit 
                '''
    while True:
        print(menu)
        option = input('Please enter your operation')
        if option.strip() == '1':
            viewproducts()
        elif option.strip() == '2':
            searchproduct()
        elif option.strip() == '3':
            change_password()
        elif option.strip() == '4':
            break
        else:
            print('Input error, please re-enter')


def view_users():
    cursor.execute("SELECT * FROM Users")
    connection.commit()
    result = cursor.fetchall()
    columnDes = cursor.description
    columnNames = [columnDes[i][0] for i in range(len(columnDes))]
    df = pd.DataFrame([list(i) for i in result], columns=columnNames)
    print(df)


def update_users():
    edit_userid = input('Enter the UserID of the user you want to edit: ')
    sql_whole_table = '''select count(*) from Users where UserID = '{}' limit 1;'''       #Check whether the user's id column already contains input information
    sql_all = sql_whole_table.format(edit_userid)     #Adds user input information to the SQL statement
    allinfo = cursor.execute(sql_all)        #Store information after execution
    result = allinfo.fetchall()     #Return all rows of sql staement
    columnDes = cursor.description       # Gets the description of the connection object
    columnNames = [columnDes[i][0] for i in range(len(columnDes))]      #get columnnames
    df = pd.DataFrame([list(i) for i in result], columns=columnNames)       #Convert to data frame format
    row = df.iloc[0].values.tolist()
    repeatnum = row[0]      #Get the data in the Dataframe
    if repeatnum != 0:
        update_user_menu(edit_userid)
        update_csv('Users', './user.csv')
    else:
        print('The user does not exist!')

def update_user_menu(userid):
    edit_menu = '''
           1.Name 2.Gender 3.Phone Number 4.Email 5.Street 6.Province 7.Postalcode 8.PurchaseHistory 9.TotalSale 
           10.User Type 11.Password 12.Quit
                           '''
    while True:
        print(edit_menu)
        opt = input('Enter the user attribute you want to modify: ')
        if opt.strip() == '1':
            new_name = input('Enter a new name: ')
            cursor.execute('''UPDATE Users SET Name = '{}'
                             WHERE UserID = {}'''.format(new_name,userid))
            connection.commit()
        elif opt.strip() == '2':
            new_gender = input('Enter Gender: ')
            cursor.execute('''UPDATE Users SET Gender = '{}'
                                    WHERE UserID = {}'''.format(new_gender, userid))
            connection.commit()
        elif opt.strip() == '3':
            new_phone = input('Enter Phone Number: ')
            cursor.execute('''UPDATE Users SET Phone = '{}'
                                    WHERE UserID = {}'''.format(new_phone, userid))
            connection.commit()
        elif opt.strip() == '4':
            new_mail = input('Enter Email')
            cursor.execute('''UPDATE Users SET Email = '{}'
                                    WHERE UserID = {}'''.format(new_mail, userid))
            connection.commit()
        elif opt.strip() == '5':
            new_Street = input('Enter Street Name: ')
            cursor.execute('''UPDATE Users SET Gender = '{}'
                                    WHERE UserID = {}'''.format(new_Street, userid))
            connection.commit()
        elif opt.strip() == '6':
            new_Province = input('Enter Province: ')
            cursor.execute('''UPDATE Users SET Province = '{}'
                                           WHERE UserID = {}'''.format(new_Province, userid))
            connection.commit()
        elif opt.strip() == '7':
            new_PostalCode = input('Enter PostalCode: ')
            cursor.execute('''UPDATE Users SET PostalCode = '{}'
                                           WHERE UserID = {}'''.format(new_PostalCode, userid))
            connection.commit()
        elif opt.strip() == '8':
            new_PurchaseHistory = input('Enter PurchaseHistory: ')
            cursor.execute('''UPDATE Users SET PurchaseHistory = '{}'
                                           WHERE UserID = {}'''.format(new_PurchaseHistory, userid))
            connection.commit()
        elif opt.strip() == '9':
            new_TotalSales = input('Enter TotalSales: ')
            cursor.execute('''UPDATE Users SET TotalSales = '{}'
                                           WHERE UserID = {}'''.format(new_TotalSales, userid))
            connection.commit()
        elif opt.strip() == '10':
            new_UserType = input('Enter UserType: ')
            cursor.execute('''UPDATE Users SET UserType = '{}'
                                           WHERE UserID = {}'''.format(new_UserType, userid))
            connection.commit()
        elif opt.strip() == '11':
            new_password = input('Enter Password: ')
            enco_password = encode(new_password)
            cursor.execute('''UPDATE Users SET Enc_Password = '{}'
                                           WHERE UserID = {}'''.format(enco_password, userid))
            connection.commit()
        elif opt.strip() == '12':
            break
        else:
            print('Input error, please re-enter.')

def update_products():
    edit_productid = input('Enter the ID of the product you want to edit: ')
    sql_whole_table = '''select count(*) from Product where ProductID = '{}' limit 1;'''       #Check whether the user's id column already contains input information
    sql_all = sql_whole_table.format(edit_productid)     #Adds user input information to the SQL statement
    allinfo = cursor.execute(sql_all)        #Store information after execution
    result = allinfo.fetchall()     #Return all rows of sql staement
    columnDes = cursor.description       # Gets the description of the connection object
    columnNames = [columnDes[i][0] for i in range(len(columnDes))]      #get columnnames
    df = pd.DataFrame([list(i) for i in result], columns=columnNames)       #Convert to data frame format
    row = df.iloc[0].values.tolist()
    repeatnum = row[0]      #Get the data in the Dataframe
    if repeatnum != 0:
        update_product_menu(edit_productid)
        update_csv('Product', './product.csv')
    else:
        print('The product does not exist!')

def update_product_menu(proid):
    edit_menu = '''
               1.Year 2.Brand 3.Name 4.Size 5.Price 6.Stock 7.SalesHistory 8.Quit'''
    while True:
        print(edit_menu)
        opt = input('Enter the product attribute you want to modify: ')
        if opt.strip() == '1':
            new_year = input('Enter a new Year: ')
            cursor.execute('''UPDATE Product SET Year = '{}'
                             WHERE ProductID = {}'''.format(new_year,proid))
            connection.commit()
        elif opt.strip() == '2':
            new_Brand = input('Enter a new Brand: ')
            cursor.execute('''UPDATE Product SET Brand = '{}'
                             WHERE ProductID = {}'''.format(new_Brand,proid))
            connection.commit()
        elif opt.strip() == '3':
            new_Name = input('Enter a new Name: ')
            cursor.execute('''UPDATE Product SET Name = '{}'
                             WHERE ProductID = {}'''.format(new_Name, proid))
            connection.commit()
        elif opt.strip() == '4':
            new_Size = input('Enter a new Size: ')
            cursor.execute('''UPDATE Product SET Size = '{}'
                             WHERE ProductID = {}'''.format(new_Size, proid))
            connection.commit()
        elif opt.strip() == '5':
            new_Price = input('Enter a new Price: ')
            cursor.execute('''UPDATE Product SET Price = '{}'
                             WHERE ProductID = {}'''.format(new_Price, proid))
            connection.commit()
        elif opt.strip() == '6':
            new_Stock = input('Enter a new Stock: ')
            cursor.execute('''UPDATE Product SET Stock = '{}'
                             WHERE ProductID = {}'''.format(new_Stock, proid))
            connection.commit()
        elif opt.strip() == '7':
            new_SalesHistory = input('Enter a new SalesHistory: ')
            cursor.execute('''UPDATE Product SET SalesHistory = '{}'
                             WHERE ProductID = {}'''.format(new_SalesHistory, proid))
            connection.commit()
        elif opt.strip() == '8':
            break
        else:
            print('Input error, please re-enter!')

def del_user():
    del_uid = input('Please enter the ID of the user you want to delete: ')
    sql_whole_table = '''select count(*) from Users where UserID = '{}' limit 1;'''  # Check whether the user's id column already contains input information
    sql_all = sql_whole_table.format(del_uid)  # Adds user input information to the SQL statement
    allinfo = cursor.execute(sql_all)  # Store information after execution
    result = allinfo.fetchall()  # Return all rows of sql staement
    columnDes = cursor.description  # Gets the description of the connection object
    columnNames = [columnDes[i][0] for i in range(len(columnDes))]  # get columnnames
    df = pd.DataFrame([list(i) for i in result], columns=columnNames)  # Convert to data frame format
    row = df.iloc[0].values.tolist()
    repeatnum = row[0]  # Get the data in the Dataframe
    if repeatnum != 0:
        cursor.execute('''delete from Users WHERE UserID = {}'''.format(del_uid))
        connection.commit()
        update_csv('Users', './user.csv')
        print('Delete Successful.')
    else:
        print('The UserID does not exist!')

def del_product():
    del_pid = input('Please enter the ID of the product you want to delete: ')
    sql_whole_table = '''select count(*) from Product where ProductID = '{}' limit 1;'''  # Check whether the user's id column already contains input information
    sql_all = sql_whole_table.format(del_pid)  # Adds user input information to the SQL statement
    allinfo = cursor.execute(sql_all)  # Store information after execution
    result = allinfo.fetchall()  # Return all rows of sql staement
    columnDes = cursor.description  # Gets the description of the connection object
    columnNames = [columnDes[i][0] for i in range(len(columnDes))]  # get columnnames
    df = pd.DataFrame([list(i) for i in result], columns=columnNames)  # Convert to data frame format
    row = df.iloc[0].values.tolist()
    repeatnum = row[0]  # Get the data in the Dataframe
    if repeatnum != 0:
        cursor.execute('''delete from Product where ProductID = {}'''.format(del_pid))
        connection.commit()
        update_csv('Product', './product.csv')
        print('Delete Successful.')
    else:
        print('The Product does not exist!')

def add_user():
    enter_email = input('Please enter email: ')
    if check_useremail(enter_email) == 1:
        user_id = asc_id('UserID','Users')
        user_name = input('Please enter name: ')
        user_gender = input('Please enter gender: ')
        user_phone = input('Please enter phonenumber: ')
        user_street = input('Please enter street number: ')
        user_province = input('Please enter province: ')
        user_postalcode = input('Please enter postalcode: ')
        user_pd = input('Please enter password: ')
        sys_pd = encode(user_pd)
        user_PH = input('Please enter PurchaseHistory: ')
        user_TS = input('Please enter TotalSales: ')
        user_UT = input('Please enter UserType: ')
        sql_new_user = '''
        insert into Users (UserID,Name,Gender,Phone,Email,Street,Province,Postalcode,PurchaseHistory,TotalSales,UserType,Enc_Password)
         values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');
        '''
        sql_insert_new = sql_new_user.format(user_id,user_name,user_gender,user_phone,enter_email,user_street,user_province,
        user_postalcode,user_PH,user_TS,user_UT,sys_pd)
        cursor.execute(sql_insert_new)
        connection.commit()
        update_csv('Users','./user.csv')
        print("Congratulations on creating an account!")
    else:
        print("This email address has been registered, please log in instead!")

def add_product():
    prod_id = asc_id('ProductID','Product')
    prod_year = input('Please enter the year: ')
    prod_brand = input('Please enter the brand: ')
    prod_name = input('Please enter the name: ')
    prod_size = input('Please enter the size: ')
    prod_price = input('Please enter the price: ')
    prod_stock = input('Please enter the stock: ')
    prod_SH = input('Please enter the SalesHistory: ')
    sql_new_prod = '''
        insert into Product (ProductID,Year,Brand,Name,Size,Price,Stock,SalesHistory)
         values ('{}','{}','{}','{}','{}','{}','{}','{}');
        '''
    sql_insert_newprod = sql_new_prod.format(prod_id,prod_year,prod_brand,prod_name,prod_size,prod_price,prod_stock,prod_SH)
    cursor.execute(sql_insert_newprod)
    connection.commit()
    update_csv('Product', './product.csv')
    print('Product successfully added!')


#Generate 3 Reports:
# 1. Top5 Selling Products:
def top5_products():
    cursor.execute("SELECT * FROM Product ORDER BY SalesHistory DESC LIMIT 5")
    connection.commit()
    result = cursor.fetchall()
    columnDes = cursor.description
    columnNames = [columnDes[i][0] for i in range (len(columnDes))]
    df = pd.DataFrame([list(i) for i in result], columns = columnNames)
    print("\nTop5 Selling Products report:")
    print(df)

# 2. Top5 Customers:
def top5_customers():
    cursor.execute("SELECT UserID, Name, TotalSales FROM Users ORDER BY TotalSales DESC LIMIT 5")
    connection.commit()
    result = cursor.fetchall()
    columnDes = cursor.description
    columnNames = [columnDes[i][0] for i in range (len(columnDes))]
    df = pd.DataFrame([list(i) for i in result], columns = columnNames)
    print("\nTop5 Customers report:")
    print(df)

# 3. Gender Analysis Report:
def gender_analysis():
    cursor.execute("SELECT AVG(TotalSales) FROM Users GROUP BY Gender")
    connection.commit()
    result = cursor.fetchall()
    columnDes = cursor.description
    columnNames = [columnDes[i][0] for i in range (len(columnDes))]
    df = pd.DataFrame([list(i) for i in result], columns = columnNames)
    df['Gender'] = ['M','F']
    print("\nAverage Gender Spending:")
    print(df)

def report_menu():
    menu = '''
           ********************************Welcome************************************
           *1.Top5 Selling Products 2.Top5 Customers 3.Gender Analysis Report  4.Quit*
                    '''
    while True:
        print(menu)
        option = input('Please enter the report number you want to check: ')
        if option.strip() == '1':
            top5_products()
        elif option.strip() == '2':
            top5_customers()
        elif option.strip() == '3':
            gender_analysis()
        elif option.strip() == '4':
            break
        else:
            print('Input error, please re-enter.')

def admin_menu():
    menu = '''
       ********************************Welcome************************************
       1.Add Users  2.View Users  3.Update Users  4.Delete Users   5.Add Products
       6.View Products 7.Update Products 8.Delete Products 9.View Reports 10. Quit
                '''
    while True:
        print(menu)
        option = input('Please choose an option: ')
        if option.strip() == '1':
            add_user()
        elif option.strip() == '2':
            view_users()
        elif option.strip() == '3':
            update_users()
        elif option.strip() == '4':
            del_user()
        elif option.strip() == '5':
            add_product()
        elif option.strip() == '6':
            viewproducts()
        elif option.strip() == '7':
            update_products()
        elif option.strip() == '8':
            del_product()
        elif option.strip() == '9':
            report_menu()
        elif option.strip() == '10':
            break
        else:
            print('Input error, please re-enter.')


def main():
    menu = '''
    ****************************Welcome***********************************
    1.Common User Login 2.Log in as an administrator 3. Create an account 
                '''
    while True:  # In this menu, users can overwrite their previously logged accounts through log in
        print(menu)
        option = input('Please choose an option: ')
        if option.strip() == '1':
            rloop = log_in_asRegular()
            if rloop == 0:
                regular_menu()
            elif rloop == 1:
                continue
        elif option.strip() == '2':
            aloop = log_in_asAdmin()
            if aloop == 0:
                admin_menu()
            elif aloop == 1:
                continue
        elif option.strip() == '3':
            create_account()
        else:
            print('Input error, please re-enter.')



#CreateDatabase_InsertData()
main()
