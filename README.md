# FaceBook-Login-Functionlality-using-Behave
## Project Overview

This project focuses on automating the testing of Facebook's login flow. By leveraging Behave, we define user behaviors in a human-readable format (Gherkin syntax) and then implement the underlying automation logic using Python and a web automation library (e.g., Selenium). This approach ensures that tests are easy to understand for both technical and non-technical stakeholders, promoting better collaboration.

## Features Covered

* **Successful Login:**
    * Login with valid credentials.
    * Login with credentials and "Remember Me" option.
* **Unsuccessful Login:**
    * Login with invalid email/password.
    * Login with empty email/password.
    * Login with special characters in credentials (negative testing).
* **UI Elements:**
    * Verification of presence of login fields (email, password).
    * Verification of presence of login button.
    * Verification of error messages.

## Technologies Used

* **Python:** The primary programming language.
* **Behave:** A Behavior-Driven Development (BDD) framework for Python.
* **Selenium WebDriver:** For browser automation and interaction with web elements.
* **[Browser Driver]:** (e.g., ChromeDriver for Chrome, geckodriver for Firefox) - *Specify the browser driver you are using.*

## Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.x:** Download from [python.org](https://www.python.org/downloads/).
* **[Web Browser]:** (e.g., Google Chrome, Mozilla Firefox)
* **[Browser Driver]:** Download the appropriate driver for your browser and ensure it's in your system's PATH.
    * [ChromeDriver](https://sites.google.com/chromium.org/driver/)
    * [GeckoDriver (Firefox)](https://github.com/mozilla/geckodriver/releases)
