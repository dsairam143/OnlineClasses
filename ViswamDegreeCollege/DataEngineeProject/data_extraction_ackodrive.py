import pandas as pd
from selenium import webdriver
import time
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

results = []

for page in range(1, 4):
    driver = webdriver.Chrome(executable_path=r"C:\Users\Bhavani_Sai\Downloads\chromedriver_win32 (2)\chromedriver.exe")
    driver.maximize_window()
    driver.get('https://ackodrive.com/page/'+str(page)+'/')

    element = driver.find_element(By.XPATH, '//*[@id="header"]/div[3]/div/div/div/div[2]/div[2]/a[1]')

    element.click()

    data = driver.page_source

    jsop = BeautifulSoup(data)
    div = jsop.find('div', attrs={'class':'listingNew__CarListWrapper-sc-15tb2vz-2 fzqDWl'})

    for sub_div in div.find_all('div', attrs={'data-testid':'listingcardesktop'}):
        make = sub_div.find('span', attrs={'class': re.compile('styles__Make')})
        make = make.text if make else make
        print(make)

        model_name = sub_div.find('span', attrs={'class': re.compile('styles__ModelName')})
        model_name = model_name.text if model_name else model_name

        body_type = sub_div.find('p', attrs={'data-testid': 'car_model_body_type'})
        body_type = body_type.text if body_type else body_type

        seat = sub_div.find('p', attrs={'data-testid': 'car_model_seat'})
        seat = seat.text if seat else seat

        variant = sub_div.find('p', attrs={'data-testid': 'car_model_variants'})
        variant = variant.text if variant else variant

        variant_title = sub_div.find('h4', attrs={'class': re.compile('styles__VariantTitl')})
        variant_title = variant_title.text if variant_title else variant_title

        fuel = sub_div.find('p', attrs={'data-testid': 'car_variant_fuel_type'})
        fuel = fuel.text if fuel else fuel

        type_ = sub_div.find('p', attrs={'data-testid': 'car_variant_transmission'})
        type_ = type_.text if type_ else type_

        city = sub_div.find('div', attrs={'class': re.compile('styles__CityName')})
        city = city.text if city else city

        price = sub_div.find('div', attrs={'class': re.compile('styles__Price-sc-')})
        price = price.text if price else price

        original_price = sub_div.find('div', attrs={'class': re.compile('styles__ActualPrice-sc-')})
        original_price = original_price.text if original_price else original_price

        data = {
            'Manufacturer': make,
            'Model': model_name,
            'Body Type': body_type,
            'Seat': seat,
            'Variant': variant,
            'Variant Title': variant_title,
            'Fuel': fuel,
            'Type': type_,
            'City': city,
            'Offer Price': price,
            'Original Price': original_price

        }
        # print(sub_div)
        results.append(data)
        print('==============================================')
    driver.close()
df = pd.DataFrame(results)

df.to_csv('Final Cars Data2.csv', index=False)





# time.sleep(60000)



