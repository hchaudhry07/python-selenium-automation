# Created by hasnainchaudhry at 10/21/20
# 1. [If you did not do that in HW3!] Create your own test case to add any product you want into the cart,
# and make sure it’s there (check for the number of items in the cart OR open the cart
# and verify it’s there, up to you!)

Feature: Test Scenarios for verifying Items are present in cart, after adding them
  Only when adding items to cart.

  Scenario: User can have items added/saved into cart after selections
    Given Open up the Amazon page
    When Search for Costume for Men
    Then Click on the awesome costume there
    Then Add the Costume to cart
    When Input drones into search bar
    Then Click on the Drone you like
    And Add the Drone to cart
    Then Click on Shopping Cart icon
    And Verify the items are there





