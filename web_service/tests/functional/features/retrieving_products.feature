Feature: Retrieving categories from the web service

  Scenario: Fetching products from a category
    Given I have imported example data from 2017-01-31
     when I get products belonging to the Shirts category
     then I a list of 28 products

  Scenario: Fetching all products
    Given I have imported example data from 2017-01-31
     when I get all products
     then I a list of 109 products
