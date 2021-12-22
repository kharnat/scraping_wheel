import time

from RPA.Browser.Selenium import Selenium

browser = Selenium()
info = []


def open_browser():
    browser.open_available_browser('https://www.wheel-size.com/')


def open_url():
    browser.click_button('//*[@id="vehicle_form"]/div/div[1]/div[1]/button')
    return len(browser.find_elements('//*[@id="vehicle_form"]/div/div[1]/div[1]/div/ul/li')) - 1


def scrapping(num_of_make):
    try:
        for make_index in range(1, num_of_make):
            if make_index > 2:
                break
            browser.go_to('https://www.wheel-size.com/')
            time.sleep(1)
            browser.click_button('//*[@id="vehicle_form"]/div/div[1]/div[1]/button')
            browser.click_element('//*[@id="vehicle_form"]/div/div[1]/div[1]/div/ul/li[' + str(make_index + 1) + ']')
            time.sleep(1)
            browser.click_button('//*[@id="vehicle_form"]/div/div[1]/div[2]/button')
            num_of_years = len(browser.find_elements('//*[@id="vehicle_form"]/div/div[1]/div[2]/div/ul/li')) - 1

            for year_index in range(1, num_of_years):  # (цикл по годам)
                if year_index > 3:
                    break
                if year_index > 1:
                    browser.go_to('https://www.wheel-size.com/')
                    time.sleep(1)
                    browser.click_button('//*[@id="vehicle_form"]/div/div[1]/div[1]/button')
                    browser.click_element(
                        '//*[@id="vehicle_form"]/div/div[1]/div[1]/div/ul/li[' + str(make_index + 1) + ']')
                    time.sleep(1)
                    browser.click_button('//*[@id="vehicle_form"]/div/div[1]/div[2]/button')
                browser.click_element('//*[@id="vehicle_form"]/div/div[1]/div[2]/div/ul/li[' + str(year_index + 1) + ']')
                time.sleep(1)
                browser.click_button('//*[@id="vehicle_form"]/div/div[1]/div[3]/button')
                num_of_models = len(browser.find_elements('//*[@id="vehicle_form"]/div/div[1]/div[3]/div/ul/li')) - 1

                for model_index in range(1, num_of_models):
                    if model_index > 3:
                        break
                    if model_index > 1:
                        browser.go_to('https://www.wheel-size.com/')
                        time.sleep(1)
                        browser.click_button('//*[@id="vehicle_form"]/div/div[1]/div[1]/button')
                        browser.click_element(
                            '//*[@id="vehicle_form"]/div/div[1]/div[1]/div/ul/li[' + str(make_index + 1) + ']')
                        time.sleep(1)
                        browser.click_button('//*[@id="vehicle_form"]/div/div[1]/div[2]/button')
                        browser.click_element(
                            '//*[@id="vehicle_form"]/div/div[1]/div[2]/div/ul/li[' + str(year_index + 1) + ']')
                        time.sleep(2)
                        browser.click_button('//*[@id="vehicle_form"]/div/div[1]/div[3]/button')
                    time.sleep(1.5)
                    browser.click_element('//*[@id="vehicle_form"]/div/div[1]/div[3]/div/ul/li[' + str(model_index + 1) + ']')
                    time.sleep(2)
                    browser.wait_until_page_contains_element('//*[@id="vehicle-market-data"]/div/section')

    except Exception as e:
        print(e)


if __name__ == "__main__":
    open_browser()
    num_of_make = open_url()
    scrapping(num_of_make)
