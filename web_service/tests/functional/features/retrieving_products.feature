Feature: Retrieving categories from the web service

  Scenario: Fetching products from a category
    Given I have imported example data from 2017-02-01
     when I get products belonging to the Shirts category
     then I a list of 30 products

  Scenario: Fetching all products
    Given I have imported example data from 2017-02-01
     when I get all products
     then I a list of 111 products
