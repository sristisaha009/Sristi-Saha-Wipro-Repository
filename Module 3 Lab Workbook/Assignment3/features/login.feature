Feature: Login using Page Object Model

  Scenario: Login with valid credentials
    Given I open the Sauce Demo login page
    When I enter username "standard_user"
    And I enter password "secret_sauce"
    And I click the login button
    Then I should be redirected to the inventory page

  Scenario: Login with invalid credentials
    Given I open the Sauce Demo login page
    When I enter username "invalid_user"
    And I enter password "wrong_password"
    And I click the login button
    Then I should see the login error message