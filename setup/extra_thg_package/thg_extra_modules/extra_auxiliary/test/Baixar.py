from thgconsole.core.exploit import *
from thgconsole.core.http.http_client import HTTPClient
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Exploit(HTTPClient):
    __info__ = {
        "name": "Exploit Name",
        "description": "Short Description",
        "authors": (
             "Author",  # routesploit module
        ),
        "references": (
             "Address URL",
        ),
        "devices": (
            "Vulnerable targets",
        ),
    }

    target = OptString("", "Target IPv4 or IPv6 address")

    def run(self):
        """ Method executes on "exploit" or "run" command (both works the same way).

        It should result in exploiting target.

        :returns None:
        """
        driver = webdriver.Firefox()
        # faz request na pg
        driver.get(self.target)
        fotos = []
        elements_len = len(driver.find_elements_by_class_name("thumb-adv"))

        for index in range(elements_len):
            driver.find_elements_by_class_name("thumb-adv")[index].click()
            a = driver.find_element_by_class_name("label-short").click()
            driver.back()
            if index >= 23:
                driver.get("https://www.wallpaperup.com/search/results/space/2")



    @mute
    def check(self):
        """ Method that verifies if the target is vulnerable.

        :returns
         - True - if target is vulnerable
         - False - if target is not vulnerable
         - None - if it is not possible to verify if target is vulnerable
        """

        return True