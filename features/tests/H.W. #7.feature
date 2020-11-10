# Created by hasnainchaudhry at 11/9/20

# 1. Rewrite these scenarios to use Page Object pattern:

Feature: Testing Out Some Features On Amazon
 Scenario: Logged out user sees Sign in page when clicking Orders
 Given Open Amazon page
 When Click Amazon Orders link
 Then Verify Sign In page is opened

Scenario: 'Your Shopping Cart is empty' shown if no product added
 Given Open Amazon page
 When Click on cart icon
 Then Verify 'Your Shopping Cart is empty.' text present

# H.W. #7 - - Part #2*.) Write this scenarios to use Page Object pattern:

Scenario: Amazon Music has 7 menu items
 Given Open Amazon page
 When Click on hamburger menu
 And Click on Amazon Music menu item
 Then 7 menu items are present

