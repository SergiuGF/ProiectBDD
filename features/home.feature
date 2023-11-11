Feature: Test the functionality of the Search Bar

  Background: Open Home Page
    Given I am on the Home Page

   @Search1
   Scenario: Check that you get at least 10 results when you search for ”tableta Samsung Galaxy”
     When I click on the Search bar
     When I insert ”tableta Samsung Galaxy” in the Search Bar
     When I click Search button
     Then At least 10 products are displayed

   @Filter
   Scenario: Check the functionality of the Filter feature
     When I click on the "Telefoane mobile" - under "Electronice" tab
     When I click "Valori individuale" - under "Pret" tab
     When I set the min value at 1000
     When I set the max value at 2000
     When I click "ok" button - under "Pret" tab
     Then All products displayed are between 1000 and 2000 lei

    @Test_URL
   Scenario: Check the functionality of the redirection to the Cart Page "https://checkout.compari.ro/"
     When I click on the Cart button
     Then I am redirected to the Cart Page "https://checkout.compari.ro/"
