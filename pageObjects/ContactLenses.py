import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utilities.XlUtilities import XLUtils
from utilities.logger import LogGen
from utilities.readProperties import ReadConfig


class ContactLenses:

    # XPath locators for various elements on the webpage

    aqualens_xpath = "//*[@id='header']/div[3]/div/div[1]/div[4]/div/div/div[2]/div[1]/a"
    reset_filter_xpath = "//span[@class='SelectedFiltersStyles__ResetFilters-sc-o9ka5-3 isMbxh']"
    disposability_xpath = "//*[@id='contact_disposable_type']/div[2]/div"
    monthly_disposable_xpath = "//*[@id='contact_disposable_type']/div[2]/div/div[1]/label/div"
    daily_disposable_xpath = "//*[@id='contact_disposable_type']/div[2]/div/div[2]/label/div"
    brands_xpath = "//*[@id='brandname_id']/div[2]/div"
    aqualens_brands_xpath = "//*[@id='brandname_id']/div[2]/div/div[2]/label/div"
    aquacolor_brands_xpath = "//*[@id='brandname_id']/div[2]/div/div[1]/label/div"
    left_sidebar_xpath = "//*[@id='next']/div[2]/div/div/div[2]/aside"
    price_xpath = "//*[@id='lenskart_price']/div[2]/div"
    products_xpath = "//*[@id='card-wrapper-parent']/div/div"
    first_product_xpath = "/html/body/div[2]/div[2]/main/div[2]/div/div/div[2]/div/div/section/div/div[3]/div/div/div[1]"
    left_eye_box_xpath = "//*[@id='pdp-cl-info-section-134538']/div[6]/div[2]/div[2]/div[2]/div/div[2]/div[5]/select"
    box1_value_xpath = "//*[@id='pdp-cl-info-section-134538']/div[6]/div[2]/div[2]/div[2]/div/div[2]/div[5]/select"
    right_eye_box_xpath = "//*[@id='pdp-cl-info-section-134538']/div[6]/div[2]/div[2]/div[2]/div/div[2]/div[6]/select"
    box2_value_xpath = "//*[@id='pdp-cl-info-section-134538']/div[6]/div[2]/div[2]/div[2]/div/div[2]/div[6]/select"
    sph_box1_xpath = "//*[@id='pdp-cl-info-section-134538']/div[6]/div[2]/div[2]/div[2]/div/div[2]/div[8]/select"
    sph1_xpath = "//*[@id='pdp-cl-info-section-134538']/div[6]/div[2]/div[2]/div[2]/div/div[2]/div[8]/select"
    sph_box2_xpath = "//*[@id='pdp-cl-info-section-134538']/div[6]/div[2]/div[2]/div[2]/div/div[2]/div[9]/select"
    sph2_xpath = "//*[@id='pdp-cl-info-section-134538']/div[6]/div[2]/div[2]/div[2]/div/div[2]/div[9]/select"
    continue_btn_xpath = "//button[@id='btn-primary-cl']"
    buy_now_btn_xpath = "//*[@id='btn-primary-cl']"

    # ID locators for various elements on the webpage

    proceed_btn_id = "button"
    price_0_499_id = "lenskart_price-0"
    price_500_999_id = "lenskart_price-1"
    contact_lens_id = "lrd4"

    def __init__(self, driver):
        # Initializing the ContactLenses class with a Selenium WebDriver instance
        self.driver = driver
        self.logger = LogGen.loggen()

    # def webLink(self):
    #     self.driver.get(ReadConfig.getApplicationURL())
    #     self.logger.info("Opened Lenskart website")

    def open_lenskart(self, url):
        # Method to open the Lenskart website and log relevant information
        self.logger.info("================= Opening Lenskart website =====================a")
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        title = self.driver.title
        self.logger.info("Title of the page: {}".format(title))

    def validate_title(self):
        # Method to validate the title of the webpage
        lenskartTitle = self.driver.title
        self.logger.info(f"The title of the webpage is : {lenskartTitle}")
        if "Sunglasses" in lenskartTitle:
            self.logger.info("Lenskart Title Validated Successfully")

    def actionChainsClick(self, link):
        # Method to perform ActionChains click on specified link
        btn_contact_lenses_element = self.driver.find_element(By.ID, self.contact_lens_id)
        ActionChains(self.driver).move_to_element(btn_contact_lenses_element).perform()

        list_elements = []

        for i in range(1, 7):
            hover_element = f"//*[@id='header']/div[3]/div/div[1]/div[4]/div/div/div[2]/div[{i}]"
            element = self.driver.find_element(By.XPATH,hover_element)
            ActionChains(self.driver).move_to_element(element).perform()
            list_elements.append(element.text)

        self.logger.info("Available brands are :")
        self.logger.info(list_elements)

        if link in list_elements:
            link_aqualens_element = self.driver.find_element(By.XPATH, self.aqualens_xpath)
            ActionChains(self.driver).move_to_element(btn_contact_lenses_element).move_to_element(link_aqualens_element).click().perform()
            time.sleep(2)

    def scroll(self):
        # Method to scroll the webpage
        self.driver.execute_script("window.scrollBy(0, 500);")

    def resetFilters(self):
        # Method to reset applied filters
        self.driver.find_element(By.XPATH, self.reset_filter_xpath).click()

    def filterLenses_Disposability(self, period):
        # Method to filter lenses based on disposability
        try:
            disposability = self.driver.find_elements(By.XPATH, self.disposability_xpath)
            self.logger.info("\nAvailable Disposabilities are :")

            radio_monthly_disposable_element = self.driver.find_element(By.XPATH, self.monthly_disposable_xpath)
            radio_daily_disposable_element = self.driver.find_element(By.XPATH, self.daily_disposable_xpath)

            for disposable in disposability:
                self.logger.info(disposable.text)
                if "Monthly" in period and "Monthly" in disposable.text:
                    ActionChains(self.driver).move_to_element(radio_monthly_disposable_element).click().perform()
                    time.sleep(3)

                elif "Daily" in period and "Daily" in disposable.text:
                    ActionChains(self.driver).move_to_element(radio_daily_disposable_element).click().perform()
                    time.sleep(3)

                else:
                    self.logger.info("\nNo other Disposability options")

        except Exception as e:
            self.logger.error(f"Exception occurred while filtering product on the basis of Disposability: {e}")

    def filterLenses_Brands(self, brand):
        # Method to filter lenses based on brands
        try:
            brands_items = self.driver.find_elements(By.XPATH, self.brands_xpath)

            radio_aqualens_brands = self.driver.find_element(By.XPATH, self.aqualens_brands_xpath)
            radio_aquacolor_brands = self.driver.find_element(By.XPATH, self.aquacolor_brands_xpath)

            self.logger.info("\nAvailable Brands are :")
            for items in brands_items:
                self.logger.info(items.text)
                if "Aqualens" in brand and "Aqualens" in items.text:
                    ActionChains(self.driver).move_to_element(radio_aqualens_brands).click().perform()
                    time.sleep(3)

                elif "Aquacolor" in brand and "Aquacolor" in items.text:
                    ActionChains(self.driver).move_to_element(radio_aquacolor_brands).click().perform()
                    time.sleep(3)

                else:
                    self.logger.info("\nBrand names are not there!!!")
            self.driver.execute_script("window.scrollBy(0, 700);")

        except Exception as e:
            self.logger.error(f"Exception occurred while filtering product on the basis of Brands: {e}")

    def filterLenses_Price(self, priceRange):
        # Method to filter lenses based on price range
        try:
            self.driver.implicitly_wait(5)
            scroll_left_sidebar = self.driver.find_element(By.XPATH, self.left_sidebar_xpath)
            self.driver.execute_script("arguments[0].scrollTop += 100;", scroll_left_sidebar)
            time.sleep(2)

            opt_choose_price = self.driver.find_elements(By.XPATH, self.price_xpath)

            radio_price_range_0_499 = self.driver.find_element(By.ID, self.price_0_499_id)
            radio_price_range_500_999 = self.driver.find_element(By.ID, self.price_500_999_id)

            self.logger.info("\nAvailable Price Range is :")
            for prices in opt_choose_price:
                self.logger.info(prices.text)

                if "499" in priceRange:
                    ActionChains(self.driver).move_to_element(radio_price_range_0_499).click().perform()
                    time.sleep(5)

                elif "999" in priceRange:
                    ActionChains(self.driver).move_to_element(radio_price_range_500_999).click().perform()
                    time.sleep(5)

                else:
                    self.logger.info("Price Range Exceeds than 999")

        except Exception as e:
            self.logger.error(f"Exception occurred while filtering product on the basis of Price: {e}")

    def chooseProduct(self):
        # Method to choose a product from the available options
        self.driver.execute_script("window.scrollBy(0, 200);")
        self.driver.implicitly_wait(10)

        all_products_xpath = self.driver.find_elements(By.XPATH, self.products_xpath)

        self.logger.info("-----------------------------------------------------------")
        for i in range(len(all_products_xpath)):
            self.logger.info(f"\n\n{all_products_xpath[i].text}")

        link_product1 = self.driver.find_element(By.XPATH, self.first_product_xpath)
        ActionChains(self.driver).move_to_element(link_product1).click().perform()
        self.logger.info("\n----------------Product Selected Successfully-----------------")

        time.sleep(2)

    def selectedProductOperation(self):
        # Method to perform operations on the selected product
        try:
            WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
            all_window_handles = self.driver.window_handles
            self.logger.info(f"\n\nNo of windows Opened: {len(all_window_handles)}")
            self.driver.switch_to.window(all_window_handles[1])
            self.logger.info("\n")
            self.logger.info("Title of the webpage is: " + self.driver.title)

            if "10H" in self.driver.title:
                # Save screenshot with a filename based on the product index
                screenshot_filename = f"product_1_screenshot.png"
                self.driver.save_screenshot(f"Screenshots/{screenshot_filename}")
                self.logger.info(f"Screenshot saved: {screenshot_filename}")

                select_box1 = self.driver.find_element(By.XPATH, self.left_eye_box_xpath)
                select_box1.click()

                select_box1_value = Select(self.driver.find_element(By.XPATH, self.box1_value_xpath))
                select_box1_value.select_by_visible_text("3 Box")
                time.sleep(2)

                select_box2 = self.driver.find_element(By.XPATH, self.right_eye_box_xpath)
                select_box2.click()

                select_box2_value = Select(self.driver.find_element(By.XPATH, self.box2_value_xpath))
                select_box2_value.select_by_visible_text("3 Box")
                time.sleep(2)

                select_sph1_box = self.driver.find_element(By.XPATH, self.sph_box1_xpath)
                select_sph1_box.click()

                select_sph1 = Select(self.driver.find_element(By.XPATH, self.sph1_xpath))
                select_sph1.select_by_visible_text("-0.50")
                time.sleep(2)

                select_sph2_box = self.driver.find_element(By.XPATH, self.sph_box2_xpath)
                select_sph2_box.click()

                select_sph2 = Select(self.driver.find_element(By.XPATH, self.sph2_xpath))
                select_sph2.select_by_visible_text("-1.00")
                time.sleep(2)

                btn_continue = self.driver.find_element(By.XPATH, self.continue_btn_xpath)
                btn_continue.click()
                time.sleep(5)

                self.driver.execute_script("window.scrollBy(0, 500);")

            elif "Aquacolor" in self.driver.title:
                # Save screenshot with a filename based on the product index
                screenshot_filename = f"product_2_screenshot.png"
                self.driver.save_screenshot(f"Screenshots/{screenshot_filename}")
                self.logger.info(f"Screenshot saved: {screenshot_filename}")

                self.logger.info("Aquacolor title" + self.driver.title)

                btn_buynow = self.driver.find_element(By.XPATH, self.buy_now_btn_xpath)
                btn_buynow.click()
                time.sleep(5)

                self.driver.execute_script("window.scrollBy(0, 500);")

        except Exception as e:
            self.logger.error(f"Window Handling Exception occurred: {e}")

    def proceedToCheckout(self):
        # Method to proceed to checkout
        self.logger.info("\n----------------Checkout is Done---------------------")
        btn_proceed = self.driver.find_element(By.ID, self.proceed_btn_id)
        btn_proceed.click()
        time.sleep(3)

    def back_to_main_window(self):
        # Method to switch back to the main window
        main_window_handle = self.driver.window_handles[0]
        self.driver.switch_to.window(main_window_handle)
        time.sleep(2)

    def read_excel_file(self, file_path):
        # Method to read data from an Excel file
        xl = XLUtils()
        xl_path = file_path
        rows = xl.getRowCount(xl_path, 'Sheet1')
        cols = xl.getColumnCount(xl_path, 'Sheet1')
        input_data = []
        for r in range(2, rows + 1):
            data_row = []
            for c in range(1, cols + 1):
                data_row.append(xl.readData(xl_path, 'Sheet1', r, c))
            input_data.append(data_row)
        return input_data

    def execute_test_cases(self, input_data):
        # Method to execute test cases based on input data from an Excel file
        for row in input_data:
            disposability, brand, price_range = row
            self.filterLenses_Disposability(disposability)
            self.filterLenses_Brands(brand)
            self.filterLenses_Price(price_range)
            self.chooseProduct()
            self.selectedProductOperation()
            self.proceedToCheckout()
            self.driver.close()
            self.back_to_main_window()
            self.resetFilters()
