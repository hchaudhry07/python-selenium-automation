# Created by hasnainchaudhry at 10/31/20
# 0.) Repeat everything I coded during the class.

Feature: Weekly Deals Page
  # Enter feature description here

  Scenario: Verify all tags are present
  Given Open WholeFoods
  Then Each Item has Regular field and Product name
