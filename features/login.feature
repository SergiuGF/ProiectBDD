Feature: Test the functionality of the Login Page

  Background: Open Login Page
    Given I am on the Login Page

   @Login1
   # scenariul 1 fara parametru
   Scenario: Check "Cu adresa de e-mail nu s-a creat inca cont." message is displayed when the user tries to login with an unregistered email ( no param )
     When I insert an unregistered email in the mail input
     When I insert a password in the password input
     When I click on the login button
     Then The error message is displayed
     Then The error message contains "Cu adresa de e-mail nu s-a creat inca cont." message

   @Login2
   Scenario: Check that "Please enter your email" message is displayed when the user enters empty email adress
#     When I insert " " in the mail input
     When I click on the login button
     Then Email error message is displayed
     Then Email error text contains "Please enter your email"
