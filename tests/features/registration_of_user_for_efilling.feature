Feature: Register user for tax number so that they can file for efilling

  Scenario: Register user for tax number
    Given Service Manager Dashboard
    Then Select work items to Classify Case
    When Classify Case pane open authenticate client