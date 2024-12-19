import time
import pytest
import openpyxl
from Source.Login_Page import class_Login_page
from datetime import datetime

#Function to read  data from Excel file.

def Read_test_data():
    #Code to load the data from excel file
    workbook = openpyxl.load_workbook(filename=r"C:\Users\ayesh\PycharmProjects\pythonProject5\pythonProject\Data_Driven_Framework\Data\login_page.xlsx")
    sheet = workbook["Sheet1"]
    data_list=[] #creating empty list to add every row of exccel file data

    #Adding data to data_list from excel file
    for row in sheet.iter_rows(min_row=2,values_only=True):
        user, pwd, result = row
        #here two brackets use one for append() method , Seconf is for tupple(row)
        data_list.append((user,pwd,result))
    return data_list
#Calling func test_data is a object of resd test adta function
test_data = Read_test_data()

#Parameterizing the test function with data from tthe excel file
@pytest.mark.parametrize("username,password,Expresult",test_data)

def test_login(username,password,Expresult,Login_Logout_Setup):

    #This is conftest file method to open browseer, and display login page.
    driver = Login_Logout_Setup
    #creating a object (login page) for login_page class of source pacakge
    #this class login_page class will find username,password and login button elements loactors.
    login_page = class_Login_page(driver)
    time.sleep(5)

    login_page.Username(username)
    login_page.Password(password)
    login_page.Login()

    if Expresult == "pass":
        assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        dt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        time.sleep(5)
        driver.save_screenshot(f"C:\\Users\\ayesh\\PycharmProjects\\pythonProject5\\pythonProject\\Data_Driven_Framework\\screenshots\\Login_success_{dt}.png")
        time.sleep(5)
        print(f"Login test with username '{username}' and password '{password}' Test passed!")
    else:
        dt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        time.sleep(5)
        driver.save_screenshot(f"C:\\Users\\ayesh\\PycharmProjects\\pythonProject5\\pythonProject\\Data_Driven_Framework\\screenshots\\Login_fail_{dt}.png")
        time.sleep(5)
        assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        print(f"Login test with username '{username}' and password '{password}' Test Failed!")
