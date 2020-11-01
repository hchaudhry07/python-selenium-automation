# Created by hasnainchaudhry at 10/31/20
# 0.) Repeat everything I coded during the class.

Feature: Amazon Main Page
  # Enter feature description here
  Scenario: Sign-In Popup disappears
    Given Open Amazon
    Then Sign-In Popup is present and clickable
    When Sign-In Popup disappears
    Then Verify Sign-In Popup is not clickable