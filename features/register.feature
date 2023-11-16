Feature: Test the functionality of the Register Page

  Background: Open Register Page
    Given I am on the Register Page

   @Register1
   Scenario: Check that success message is displayed when the user registers with a new email
     When I set a new email
     When I set password as "Password8910"
     When I click register button
     Then Success message is displayed

   @Register2
   Scenario: Check that error message is displayed when the user enters empty email adress
    When I insert ' ' in the mail input
    When I click register button - Scenario 2
    Then Email error message is displayed
    Then Email error text contains "Completarea campului este obligatorie!" message

   @Register3
   Scenario: Check that error message is displayed when the user enters empty password input
    When I set a new email - Scenario 3
    When I insert ' ' in the password input
    When I click register button - Scenario 3
    Then Password error message is displayed
    Then Password error text contains "Completarea campului este obligatorie!" message