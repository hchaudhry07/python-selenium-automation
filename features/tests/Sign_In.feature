# Created by hasnainchaudhry at 10/7/20
Feature: Test Scenarios for Sign in prompt for account features

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open New Amazon page
    When Click on Orders
    Then Verify if Sign In is prompted

