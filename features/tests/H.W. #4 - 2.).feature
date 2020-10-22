# Created by hasnainchaudhry at 10/21/20
# Create a test case that will open amazon BestSellers page: https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers
# And verify there are 5 links:

Feature: Test Scenario to verify if 5 links are present on the bestseller page


  Scenario: Verify if the 5 links are present on Amazon's BestSeller page
    Given Open Amazon BestSeller Page
    Then Verify if 5 links are present