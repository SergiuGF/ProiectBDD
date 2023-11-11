Feature: Test the functionality of the Cart Page

  Background: Open "Philips EP2236/40" coffee machine Page
    Given I am on the "Philips EP2236/40" Page

   @Cart1
   Scenario: Check the functionality of the "Cumpara" button
     When I click on the expand button
     When I click on the "Negru" option
     When I click on the "Cumpara" button
     When I click on the "Spre cos" button
     Then the "Philips EP2236/40" product is displayed