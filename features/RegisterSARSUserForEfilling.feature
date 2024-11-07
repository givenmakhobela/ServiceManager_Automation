Feature: Register a SARS registered user for efilling


  Scenario: Register for efilling
    Given Service Manager Dashboard - efilling
    Then Select Work Items to navigate to Classify Case - efilling
    When Classify Case pane open click Authenticate Client - efilling
    Then Navigate to search client - efilling
    When Search client form opens, capture client information - efilling
    Then Search for the registered client and select the client - efilling
    And Perform eFilling registration service - efilling