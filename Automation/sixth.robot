*** Settings ***
Library Selenium Library


*** Variables ***
$[url]  https://www.orangehrm.com/en/orangehrm-starter-open-source-software/
$[browser]  Chrome




*** Test Cases ***
TC_01 Open URL
    Open Browser    $[url]  $[browser]
    




*** Keywords ***

