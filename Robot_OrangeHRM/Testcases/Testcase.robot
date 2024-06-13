*** Settings ***
Documentation    OrangeHRmanagement Project. Validating login functionality,
...              admin module.
Library    SeleniumLibrary
Resource    ../pom/generic.robot
Resource    ../pom/login.robot
Resource    ../pom/admin.robot
Suite Setup    launching browser

*** Test Cases ***
validate application functionality
    Set Selenium Implicit Wait    5s
    login.login to application
    admin.admin page