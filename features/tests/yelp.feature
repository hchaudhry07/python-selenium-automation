# Created by hasnainchaudhry at 11/1/20
# 0.) Repeat everything I coded during the class.

Feature: Window Handling
  # Enter feature description here

  Scenario: Company's website is open in a new tab
    Given Open Yelp Page
    When Click on Website Link
    And Switch to a new window
    Then The Table Website is open
    And A user can close the new window and go to the original

