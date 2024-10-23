Feature: Register user for tax number so that they can be able to file for efilling

  Scenario: Register user for tax number
    Given Service Manager Dashboard
    Then Select Work Items to navigate to Classify Case
    When Classify Case pane open click Authenticate Client
    Then Navigate to search client
    When Search client form opens, capture client information
    Then Search for the client to see if they exist and the add client

