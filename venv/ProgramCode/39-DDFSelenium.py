from selenium import webdriver
import openpyxl
from openpyxl import Workbook
import time

# https://www.journaldev.com/33325/openpyxl-python-read-write-excel-files

testData = openpyxl.load_workbook('ExcelTestData.xlsx')
testDataSheet = testData['TestData']

print(testDataSheet.max_row)
print(testDataSheet.max_column)

homeValue = testDataSheet.cell(row=2,column=3).value
downPaymentOption = testDataSheet.cell(row=2,column=4).value
downPaymentValue = testDataSheet.cell(row=2,column=5).value
interestRate = testDataSheet.cell(row=2,column=7).value
loanTerm = testDataSheet.cell(row=2,column=8).value
startDate = testDataSheet.cell(row=2,column=9).value
propertyTax = testDataSheet.cell(row=2,column=10).value
pmi = testDataSheet.cell(row=2,column=11).value
homeInsurance = testDataSheet.cell(row=2,column=12).value
monthlyHoa = testDataSheet.cell(row=2,column=13).value
loanType = testDataSheet.cell(row=2,column=14).value
buyOrRefi = testDataSheet.cell(row=2,column=15).value
creditRating = testDataSheet.cell(row=2,column=16).value
showAmortizationTables = testDataSheet.cell(row=2,column=17).value
expectedEMI = testDataSheet.cell(row=2,column=18).value


myD = webdriver.Chrome(executable_path= "C:/Users/Mythili/Software/chromedriver.exe") # Working

myD.maximize_window()
myD.get("https://www.mortgagecalculator.org/")

myD.find_element_by_id("homeval").send_keys(homeValue)

if downPaymentOption == "Percent":
    myD.find_element_by_css_selector("#calc > form > section > section.content-area > div > div > div.calculation-container > div > div > div.cal-content > div.cal-left-box > div.calcu-block > div:nth-child(2) > span > label:nth-child(2) > input[type=radio]").click()
    time.sleep(1)
myD.find_element_by_id("downpayment").send_keys(downPaymentValue)

loanAmount = float(myD.find_element_by_id("loanamt").get_attribute("value"))
testDataSheet.cell(row=2,column=6).value = loanAmount

myD.find_element_by_id("intrstsrate").send_keys(interestRate)
myD.find_element_by_id("loanterm").send_keys(loanTerm)

startDateList = startDate.split("-")
myD.find_element_by_name("param[start_month]").send_keys(startDateList[0])
myD.find_element_by_id("start_year").send_keys(startDateList[1])

myD.find_element_by_id("pptytax").send_keys(propertyTax)
myD.find_element_by_id("pmi").send_keys(pmi)
myD.find_element_by_id("hoi").send_keys(homeInsurance)
myD.find_element_by_id("hoa").send_keys(monthlyHoa)
myD.find_element_by_name("param[milserve]").send_keys(loanType)

myD.find_element_by_name("param[refiorbuy]").send_keys(buyOrRefi)
myD.find_element_by_id("credit_rating").send_keys(creditRating)


myD.find_element_by_xpath("//*[@id='calc']/form/section/section[2]/div/div/div[1]/div/div/div[4]/div[1]/div[2]/a").click()
if showAmortizationTables == "Draw charts":
    myD.find_element_by_id("draw_charts").click()
elif showAmortizationTables == "Monthly vs bi-weekly payments":
    myD.find_element_by_id("show_m_vs_w").click()
elif showAmortizationTables == "Show annual amortization table":
    myD.find_element_by_id("show_annual").click()
elif showAmortizationTables == "Show monthly amortization table":
    myD.find_element_by_id("show_monthly").click()
elif showAmortizationTables == "Hide Ads":
    myD.find_element_by_id("hide_ads").click()
else:
    print("Wrong selection")

myD.find_element_by_name("cal").click()
time.sleep(3)

actualEMI = myD.find_element_by_xpath("//*[@id='calc']/form/section/section[2]/div/div/div[1]/div/div/div[4]/div[2]/div/div[1]/div[1]/h3").text

if actualEMI == expectedEMI:
    print("Expected EMI and Actual are matching")
    testDataSheet.cell(row=2, column=19).value = actualEMI
    executionStatus = "Pass"
else:
    print("Expected EMI and Actual are not matching",actualEMI)
    testDataSheet.cell(row=2, column=19).value = actualEMI
    executionStatus = "Fail"

testDataSheet.cell(row=2,column=20).value = executionStatus

myD.close()

testData.save('ExcelTestData.xlsx')