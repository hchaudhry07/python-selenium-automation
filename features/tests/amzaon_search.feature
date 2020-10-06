# Created by hasnainchaudhry at 10/3/20
Feature: Tests for Amazon Search
  # Enter feature description here

  Scenario: Amazon search returns correct result
    Given Open Amazon page
    When Input Guitar into Amazon search field
    And Click on Amazon search icon
    Then Search results for Guitar are shown

   Scenario: Amazon search returns correct result
    Given Open Amazon page
    When Input Guitar into Amazon search field
    Then Verify input value is Guitar
