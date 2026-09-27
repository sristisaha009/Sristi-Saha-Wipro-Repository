Feature: Selenium automation using Python Behave

  Scenario: Submit the DemoQA text box form
    Given I open the DemoQA text box page
    When I enter my name, email and address
    And I submit the form
    Then I should see the submitted details