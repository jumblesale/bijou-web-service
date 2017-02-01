Feature: Retrieving categories from the web service

  Scenario: Fetching all categories
    Given I have imported example data
     when I get all categories from the database
     then I get the following list of categories
      | name |
      | whatever |
