Feature: Data-driven API testing using Behave

  Scenario Outline: Retrieve user details using API
    Given the API endpoint is available
    When I send a GET request for user <user_id>
    Then the response status should be <status>
    And the response should contain the expected user ID <user_id>

    Examples:
      | user_id | status |
      | 1       | 200    |
      | 2       | 200    |
      | 3       | 200    |
      | 4       | 200    |
      | 5       | 200    |