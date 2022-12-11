# %%
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from modules import IDriver

# %%
driver = webdriver.Chrome()

# %%
driver.close()

# %%
driver.get("http://www.towoshiya.com/950/")

# %%
oo = driver.find_element(By.ID, "LMW1")
oo

# %%
tenpos = oo.find_elements(By.CLASS_NAME, "SH3")
len(tenpos)

# %%
[name.text for name in tenpos]

# %%
for i, tenpo in enumerate(tenpos):
    name = tenpo.text
    print(i, name)
    if "梓川店" in name:
        print(tenpo.find_element(By.XPATH, "./following-sibling::div").text)
        print(
            tenpo.find_element(
                By.XPATH, "./following-sibling::span[contains(text(),'店舗TEL')]"
            ).text
        )
        print(
            tenpo.find_element(
                By.XPATH, "./following-sibling::span[contains(text(),'調剤TEL')]"
            ).text
        )
        print(
            tenpo.find_element(
                By.XPATH, "./following-sibling::div[contains(.,'調剤FAX')]"
            ).text
        )
    elif "島内店" in name:
        print(tenpo.find_element(By.XPATH, "./following-sibling::div").text)
        print(
            tenpo.find_element(
                By.XPATH, "./following-sibling::div/span[contains(text(),'店舗TEL')]"
            ).text
        )
        print(
            tenpo.find_element(
                By.XPATH, "./following-sibling::div/span[contains(text(),'調剤TEL')]"
            ).text
        )
        print(
            tenpo.find_element(
                By.XPATH,
                "./following-sibling::div/span[contains(text(),'調剤FAX')]/following-sibling::span[2]",
            ).text
        )
    elif "松本庄内店" in name:
        print(tenpo.find_element(By.XPATH, "./following-sibling::div").text)
        print(
            tenpo.find_element(
                By.XPATH, "./following-sibling::span[contains(text(),'店舗TEL')]"
            ).text
            or tenpo.find_element(
                By.XPATH, "./following-sibling::div//span[contains(text(),'店舗TEL')]"
            ).text
        )
        print(
            tenpo.find_element(
                By.XPATH, "./following-sibling::span[contains(text(),'調剤TEL')]"
            ).text
            or tenpo.find_element(
                By.XPATH,
                "./following-sibling::div/span[contains(text(),'調剤FAX')]/following-sibling::span[2]",
            ).text
        )
        print(
            tenpo.find_element(
                By.XPATH,
                "./following-sibling::div/span[contains(text(),'調剤FAX')]/following-sibling::span[2]",
            ).text
        )

    elif "穂高店" in name:
        print(tenpo.find_element(By.XPATH, "./following-sibling::div/div").text)
        try:
            print(
                tenpo.find_element(
                    By.XPATH, "./following-sibling::span[contains(text(),'店舗TEL')]"
                ).text
            )
        except:
            pass
        print(
            tenpo.find_element(
                By.XPATH, "./following-sibling::div//span[contains(text(),'調剤TEL')]"
            ).text
        )
        print(
            tenpo.find_element(
                By.XPATH,
                "./following-sibling::div//span[contains(text(),'調剤FAX')]/following-sibling::span[1]",
            ).text
        )
        print("########################")

    elif i == 8 or i >= 10:
        print(
            tenpo.find_element(
                By.XPATH, "./following-sibling::div//span[contains(.,'〒')]"
            ).text
        )
        try:
            print(
                tenpo.find_element(
                    By.XPATH, "./following-sibling::div/span[contains(text(),'店舗TEL')]"
                ).text
            )
        except:
            print(
                tenpo.find_element(
                    By.XPATH,
                    "./following-sibling::div/div/span[contains(text(),'店舗TEL')]",
                ).text
            )
        print(
            tenpo.find_element(
                By.XPATH, "./following-sibling::div//span[contains(text(),'調剤TEL')]"
            ).text
        )
        print(
            tenpo.find_element(
                By.XPATH,
                "./following-sibling::div//span[contains(text(),'調剤FAX')]/following-sibling::span",
            ).text
        )
        print("########################")
    else:
        print(tenpo.find_element(By.XPATH, "./following-sibling::div").text)
        print(
            tenpo.find_element(
                By.XPATH, "./following-sibling::span[contains(text(),'店舗TEL')]"
            ).text
            or tenpo.find_element(
                By.XPATH, "./following-sibling::div//span[contains(text(),'店舗TEL')]"
            ).text
        )
        print(
            tenpo.find_element(
                By.XPATH, "./following-sibling::span[contains(text(),'調剤TEL')]"
            ).text
            or tenpo.find_element(
                By.XPATH,
                "./following-sibling::div/span[contains(text(),'調剤FAX')]/following-sibling::span[2]",
            ).text
        )
        print(
            tenpo.find_element(
                By.XPATH,
                "./following-sibling::div/span[contains(text(),'調剤FAX')]/following-sibling::span",
            ).text
        )
        print("########################")


# %%
