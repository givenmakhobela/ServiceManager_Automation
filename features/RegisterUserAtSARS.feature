Feature: Register user at SARS so that they can be able to file

  Scenario: Register user at SARS
    Given Service Manager Dashboard
    Then Select Work Items to navigate to Classify Case
    When Classify Case pane open click Authenticate Client
    Then Navigate to search client
    When Search client form opens, capture client information
    Then Search for the client to see if they exist and the add client
    Given Entity Registration form apply xml data
    Then Click Done button