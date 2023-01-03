from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re
import pymysql

option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--window-size=1920,1080')
option.add_argument('--disable-gpu')
option.add_argument('--disable-dev-sh-usage')

URL = "https://www.transelectrica.ro/"
#works on windows-> driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Chrome(chrome_options=option)
driver.get('https://www.transelectrica.ro/')
driver.implicitly_wait(30)

soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup.text)
#print (re.findall("(\d*\.?\d+%)\s(Cărbune|Hidrocarburi|Hidro|Nuclear|Eolian|Biomasa|Foto)(\s.\s\d+)", soup.text))
results = re.findall("(\d*\.?\d+%)\s(Cărbune|Hidrocarburi|Hidro|Nuclear|Eolian|Biomasa|Foto)(\s.\s\d+)", soup.text)
for element in results:
    if "Eolian" in element:
        print("Productie eolian:",int(str(element[2]).strip(" -")))
        p_eolian = int(str(element[2]).strip(" -"))
    if "Cărbune" in element:
        print("Productie Cărbune:",int(str(element[2]).strip(" -")))
        p_carbune = int(str(element[2]).strip(" -"))
    if "Hidrocarburi" in element:
        print("Productie Hidrocarburi:",int(str(element[2]).strip(" -")))
        p_hidrocarburi = int(str(element[2]).strip(" -"))
    if "Hidro" in element:
        print("Productie Hidro:",int(str(element[2]).strip(" -")))
        p_hidro = int(str(element[2]).strip(" -"))
    if "Nuclear" in element:
        print("Productie Nuclear:",int(str(element[2]).strip(" -")))
        p_nuclear = int(str(element[2]).strip(" -"))
    if "Biomasa" in element:
        print("Productie Biomasa:",int(str(element[2]).strip(" -")))
        p_biomasa = int(str(element[2]).strip(" -"))
    if "Foto" in element:
        print("Productie Foto:",int(str(element[2]).strip(" -")))
        p_foto = int(str(element[2]).strip(" -"))

totals = re.findall("(Consum|Productie|Sold schimb):(\s.\d+\sMW)",soup.text)
#print(soup.text)
for element in totals:
    if "Consum" in element:
        print("Consumul este:", int(str(element[1]).strip("MW").strip(" ")))
        p_consum=int(str(element[1]).strip("MW").strip(" "))
    if "Productie" in element:
        print("Productia este:", int(str(element[1]).strip("MW").strip(" ")))
        p_productie = int(str(element[1]).strip("MW").strip(" "))
    if "Sold schimb" in element:
        print("Schimb:", float(str(element[1]).strip("MW").strip(" ")))
        p_schimb = int(str(element[1]).strip("MW").strip(" "))




#connect to database
connection = pymysql.connect(host='192.168.0.188',user='vladpalas',password='DePeTudorNeculai',db='db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        cursor.callproc('update_transelectrica',('U',p_hidro,p_eolian,p_nuclear,p_carbune,p_hidrocarburi,p_biomasa,p_foto,p_consum,p_productie,p_schimb))
        connection.commit()
finally:
    connection.close()