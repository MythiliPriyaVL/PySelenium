from selenium import webdriver
import time

# myD = webdriver.Chrome(executable_path= "C:\Users\Mythili\Software\chromedriver.exe") - Not working
#myD = webdriver.Chrome(executable_path= r"C:\Users\Mythili\Software\chromedriver.exe") - Working
myD = webdriver.Chrome(executable_path= "C:/Users/Mythili/Software/chromedriver.exe") # Working

myD.maximize_window()
myD.get("https://www.mortgagecalculator.org/")

myD.find_element_by_id("homeval").send_keys("350000")
# myD.find_element_by_name("param[downpayment_type]").click() - Not working
myD.find_element_by_css_selector("#calc > form > section > section.content-area > div > div > div.calculation-container > div > div > div.cal-content > div.cal-left-box > div.calcu-block > div:nth-child(2) > span > label:nth-child(2) > input[type=radio]").click()
time.sleep(1)
myD.find_element_by_id("downpayment").send_keys("35")
print(myD.find_element_by_id("loanamt").get_attribute("value"))
myD.find_element_by_id("intrstsrate").send_keys("3.2")

myD.find_element_by_id("loanterm").send_keys("20")
myD.find_element_by_name("param[start_month]").send_keys("Jan")
myD.find_element_by_id("start_year").send_keys("2010")
myD.find_element_by_id("pptytax").send_keys("3000")
myD.find_element_by_id("pmi").send_keys("1.8")
myD.find_element_by_id("hoi").send_keys("3500")
myD.find_element_by_id("hoa").send_keys("350")
myD.find_element_by_name("param[milserve]").send_keys("FHA")

myD.find_element_by_name("param[refiorbuy]").send_keys("Buy")
myD.find_element_by_id("credit_rating").send_keys("Excellent (720+)")

myD.find_element_by_xpath("//*[@id='calc']/form/section/section[2]/div/div/div[1]/div/div/div[4]/div[1]/div[2]/a").click()
myD.find_element_by_id("draw_charts").click()
myD.find_element_by_id("show_m_vs_w").click()
myD.find_element_by_id("show_annual").click()
myD.find_element_by_id("show_monthly").click()
myD.find_element_by_id("hide_ads").click()

myD.find_element_by_name("cal").click()
time.sleep(3)
expEMI = "$3,142.85"
actEMI = myD.find_element_by_xpath("//*[@id='calc']/form/section/section[2]/div/div/div[1]/div/div/div[4]/div[2]/div/div[1]/div[1]/h3").text

if actEMI == expEMI:
    print("Expected EMI and Actual are matching")
else:
    print("Expected EMI and Actual are not matching",actEMI)

myD.close()