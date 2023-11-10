Feature: Test the functionality of the Register Page

  Background: Open Register Page
    Given I am on the Register Page

   @Register1
   Scenario: Check that success message is displayed when the user registers with a new email
     When I set a new email
     When I set password as "Password8910"
     When I click register button
     Then Success message is displayed
