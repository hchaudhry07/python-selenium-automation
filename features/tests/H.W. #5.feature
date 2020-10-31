# Created by hasnainchaudhry at 10/25/20
# 1. Make a test case similar to the example from class, use https://www.amazon.com/gp/product/B07BJKRR25/ color selection OR ANY OTHER ITEM.
# Create 1 test case that will loop through colors (in any way you prefer)

Feature: Test for Men's Pants selection
  # Enter feature description here

  Scenario: Open Amazon Men's Pants Page
    Given Go Open Amazon Men's Pants B07BJKRR25 Page
    Then Verify Users can select different colors