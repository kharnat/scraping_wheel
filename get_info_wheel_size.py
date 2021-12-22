from RPA.Browser.Selenium import Selenium
import json

browser = Selenium()
info = []


def open_needed_url():
    browser.open_available_browser('https://www.wheel-size.com/size/acura/cdx/2021/')


def get_info():
    engine_1 = browser.get_text('//*[@id="trim-15t-chdm-180"]/div[1]/div/h5/span[2]')  # for 1.5T
    engine_2 = browser.get_text('//*[@id="trim-20i-chdm-212"]/div[1]/div/h5/span[2]')  # for 2.0i
    cb_1 = browser.get_text('//*[@id="cb9e174996"]')
    cb_2 = browser.get_text('//*[@id="82b79da1d3"]')
    pcd_1 = browser.get_text('//*[@id="trim-15t-chdm-180"]/div[2]/div[2]/div/div[2]/span[2]')
    pcd_2 = browser.get_text('//*[@id="trim-20i-chdm-212"]/div[2]/div[2]/div/div[2]/span[2]')
    tire_1_1 = browser.get_text('//*[@id="260005"]/td[1]/span/span[1]')
    rim_1_1 = browser.get_text('//*[@id="260005"]/td[2]/span/span')
    tire_1_2 = browser.get_text('//*[@id="324349"]/td[1]/span/span[1]')
    rim_1_2 = browser.get_text('//*[@id="324349"]/td[2]/span/span')
    tire_2_1 = browser.get_text('//*[@id="280193"]/td[1]/span/span[1]')
    rim_2_1 = browser.get_text('//*[@id="280193"]/td[2]/span/span')
    tire_2_2 = browser.get_text('//*[@id="324350"]/td[1]/span/span[1]')
    rim_2_2 = browser.get_text('//*[@id="324350"]/td[2]/span/span')

    default_or_usdm = 'usdm' if browser.is_element_visible(
        '//*[@id="trim-430i-usdm-248"]/div[2]/div[1]/div/div[2]') else 'default'

    info.append(
        {
            default_or_usdm: {
                engine_1: {
                    "cb": cb_1,
                    "pcd": pcd_1,
                    "pairs": [
                        {
                            "tire": tire_1_1,
                            "rim": rim_1_1
                        },
                        {
                            "tire": tire_1_2,
                            "rim": rim_1_2
                        }
                    ]
                },
                engine_2: {
                    "cb": cb_2,
                    "pcd": pcd_2,
                    "pairs": [
                        {
                            "tire": tire_2_1,
                            "rim": rim_2_1
                        },
                        {
                            "tire": tire_2_2,
                            "rim": rim_2_2
                        }
                    ]
                }
            }
        }
    )


def convert_to_json():
    json_file_name = browser.get_text('//*[@id="trim-15t-chdm-180"]/div[1]/div/h5/span[1]')
    with open(json_file_name + '.json', 'w') as convert_file:
        convert_file.write(json.dumps(info))


if __name__ == "__main__":
    open_needed_url()
    get_info()
    print(info)
    convert_to_json()
