# Created by hasnainchaudhry at 10/18/20
# 3.) Create a test case using BDD that opens amazon.com, clicks on the cart icon and verifies that Your Shopping Cart is empty.
Feature: Amazon can confirm if your cart is empty when you have nothing in your cart
  # Enter feature description here

  Scenario: Amazon verifies that Your Shopping Cart is empty
    Given Open Amazon website
    When Clicking on 'Cart'
    Then Verify if Amazon displays your cart as empty