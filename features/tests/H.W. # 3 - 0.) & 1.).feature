# Created by hasnainchaudhry at 10/17/20
Feature: Amazon Search
  # Enter feature description here

  Scenario: Amazon product search
    Given Open the Amazon page
    When Input "Glasses" and click search
    Then Verify that page contains "Glasses"

# 2.) # 2.) Update a test case for support search using BDD
## User can search for Cancelling an order on Amazon (test case from Ex 2 of HW2)
Feature: Cancel Order Check

  Scenario: User can search for cancelling orders
    Given Open Amazon help page
    When Searching for 'Cancelling Orders'
    Then Verify if user can see option to Cancelling Orders
