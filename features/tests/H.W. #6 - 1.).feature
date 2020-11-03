# Created by hasnainchaudhry at 11/1/20
# 1. Create a window handling test case from the class and verify that user can open amazon applications from Terms of Conditions
#https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088

Feature: Verify that user can open amazon applications from Terms of Conditions

  # Enter feature descriptionhere

  Scenario: User can open and close Amazon Applications
    Given  Open Amazon T&C page
    Then Store original windows
    And Click on Amazon applications link
    And Switch to the newly opened window
    Then Amazon app page is opened
    And User can close new window and switch back to original