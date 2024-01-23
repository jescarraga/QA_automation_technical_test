Feature: Search

    @completed
    Scenario: User can search with “Google Search”
        Given I’m on the homepage
        When I type “test automation” into the search field
        And I click the Google Search button
        Then I go to the search results page, and the first 3 results contain the word “automation”
    
    @completed
    Scenario: User can go to the first search result
        Given I search by keyword
        When I click on the first result link
        Then I go to the page, and the page title contains the word "automation”