# Lenskart Website Automation

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white)
![Test Automation](https://img.shields.io/badge/Testing-Automation-blue?style=for-the-badge)

## 📌 Project Overview
This repository contains a robust automation testing suite for the **Lenskart** website. The framework is built using **Python** and **Selenium WebDriver**, following the **Page Object Model (POM)** design pattern to ensure scalability, reusability, and easy maintenance.

The suite automates end-to-end user flows and validates various submodules of the Lenskart platform, providing detailed execution logs and visual evidence for failures.

---

## 🚀 Key Features
* **POM Architecture:** Separation of page objects and test scripts for cleaner code.
* **Data-Driven Testing:** Utilizes external data sources for comprehensive test coverage.
* **Automated Reporting:** Generates detailed HTML reports of test execution.
* **Failure Analysis:** Automatically captures screenshots when a test case fails.
* **Logging:** Integrated logging system to track execution steps and debug issues.

---

## 📂 Project Structure
```text
Lenskart-Automation/
├── Configurations/    # Configuration files (URL, credentials, etc.)
├── Logs/              # Execution logs
├── pageObjects/       # Page classes with element locators and actions
├── Reports/           # Generated test execution reports
├── Screenshots/       # Screenshots of failed test cases
├── TestData/          # Test data files (Excel/JSON)
├── testCases/         # Actual test scripts
├── utilities/         # Common utility functions (Read Config, Custom Logger)
├── run.bat            # Batch file to execute tests
└── README.md          # Project documentation
```
---

## 🛠️ Prerequisites
Before running the tests, ensure you have the following installed:
* Python 3.x
* Google Chrome / Firefox
* Appropriate WebDriver (ChromeDriver/GeckoDriver)

---
## Installation & Setup
* Clone the repository:
git clone [https://github.com/harsh7781/Lenskart-Automation.git](https://github.com/harsh7781/Lenskart-Automation.git)
cd Lenskart-Automation

* Install dependencies:
pip install selenium pytest pytest-html pytest-xdist

---

## 🏃Execution
You can run the entire test suite using the provided batch file or via terminal:
* Option 1: Using Batch File
Double-click run.bat to execute the predefined test suite.

Option 2: Using Pytest (Terminal)
* Run all tests
pytest -v -s testCases/

* Run tests and generate HTML report
pytest -v -s --html=Reports/report.html testCases/

---

## 🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create.
* Fork the Project.
* Create your Feature Branch (git checkout -b feature/NewFeature)
* Commit your Changes (git commit -m 'Add some NewFeature')
* Push to the Branch (git push origin feature/NewFeature)
* Open a Pull Request

---

## 📄 License
Distributed under the MIT License. See LICENSE for more information.

Author: Harshal Meshram
