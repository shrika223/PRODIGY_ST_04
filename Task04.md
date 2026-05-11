# Task-04: Cross-Browser Testing with BrowserStack

## Demo Site
[https://www.saucedemo.com/](https://www.saucedemo.com/)

## Objective
Perform automated cross-browser testing using Selenium WebDriver integrated with BrowserStack’s Selenium Grid.  
Verify login functionality and ensure consistent user experience across Chrome, Firefox, Safari, and Edge.

---

## Test Cases

| Test Case ID | Browser   | Scenario                  | Steps                                                                 | Expected Result                          | Actual Result                            | Status |
|--------------|-----------|---------------------------|----------------------------------------------------------------------|------------------------------------------|------------------------------------------|--------|
| TC01         | Chrome    | Valid Login               | Enter `standard_user` + `secret_sauce` → Click Login                 | Redirect to inventory page                | Redirect successful                       | Pass   |
| TC02         | Firefox   | Valid Login               | Enter `standard_user` + `secret_sauce` → Click Login                 | Redirect to inventory page                | Redirect successful (slight delay)        | Pass   |
| TC03         | Safari    | Valid Login               | Enter `standard_user` + `secret_sauce` → Click Login                 | Redirect to inventory page                | Redirect successful (UI misaligned)       | **Fail** |
| TC04         | Edge      | Valid Login               | Enter `standard_user` + `secret_sauce` → Click Login                 | Redirect to inventory page                | Redirect successful (slow load)           | Pass   |
| TC05         | Chrome    | Invalid Login             | Enter `locked_out_user` + `secret_sauce` → Click Login               | Error message displayed                   | Error message displayed                   | Pass   |
| TC06         | Firefox   | Empty Credentials         | Leave username & password blank → Click Login                        | Error message displayed                   | Error message displayed                   | Pass   |
| TC07         | Safari    | Username Only             | Enter username only → Click Login                                    | Error message displayed                   | Error message not aligned properly        | **Fail** |
| TC08         | Edge      | Logout Functionality      | Login → Click Menu → Logout                                          | Redirect to login page                    | Redirect successful                       | Pass   |

---

## Observations
- Chrome: Smooth login, no issues.  
- Firefox: Slight delay in rendering login button.  
- Safari: UI alignment issues → caused **Fail** in TC03 and TC07.  
- Edge: Slower page load compared to Chrome.  

---

## Conclusion
Cross-browser testing confirmed that functionality works consistently across most browsers.  
Safari showed **UI alignment defects**, which were logged as Fail cases.  
This highlights the importance of testing across multiple environments to catch hidden issues.

---

## Technologies Used
- Python  
- Selenium WebDriver  
- BrowserStack Selenium Grid
