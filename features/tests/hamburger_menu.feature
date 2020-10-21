# Created by hasnainchaudhry at 10/19/20
Feature: Test for Amazon Hamburger Menu
  # Enter feature description here

  Scenario: User sees all links when menu opens
    Given Open Amazon page
    When Click to Open Amazon Hamburger Menu
    Then Verify 47 links are visible