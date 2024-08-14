import os.path

import pytest
from selenium import webdriver
from pageObjects.ContactLenses import ContactLenses
from utilities.logger import LogGen

# @pytest.mark.sanity
# def test_example_sanity():
#     driver = webdriver.Chrome()
#     driver.get("https://www.lenskart.com/")
#     assert driver.title == "Eyeglasses, Sunglasses, Contact Lens Online - Lenskart IN"
#     driver.quit()


@pytest.mark.logtest
def test_logtest(setup):
    # logger = LogGen()
    # logger.info("this is my log")
    assert True

@pytest.mark.sanity
def test_contact_lenses(setup):
    driver = setup
    contact_lenses = ContactLenses(driver)
    contact_lenses.open_lenskart("https://www.lenskart.com/")
    contact_lenses.validate_title()
    contact_lenses.actionChainsClick("Aqualens")
    contact_lenses.scroll()
    excel_file_path = os.path.abspath("TestData/Book1.xlsx")
    input_data = contact_lenses.read_excel_file(excel_file_path)
    contact_lenses.execute_test_cases(input_data)
    driver.quit()

# @pytest.mark.regression
# def test_example_regression():
#     driver = webdriver.Chrome()
#     driver.get("https://www.lenskart.com/")
#     assert "This should fail" in driver.title
#     driver.quit()
