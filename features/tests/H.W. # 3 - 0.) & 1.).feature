# Created by hasnainchaudhry at 10/17/20
Feature: Amazon Search
  # Enter feature description here

  Scenario: Amazon product search
    Given Open the Amazon page
    When Input "Glasses" and click search
    Then Verify that page contains "Glasses"




