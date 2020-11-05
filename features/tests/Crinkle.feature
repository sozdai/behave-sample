# Created by Alex Kardash at 02/11/20
Feature: Crinkle
  Check Crinkle chrome extension is displayed correctly for all partners

  @smoke
  Scenario Outline: Validate extension triggered on checkout with selected product
    Given I open page '<website>'
    When I add to bag
    When I open checkout page

    Examples:
      | website                |
      | apple.com              |
      | apple.com.invalid      |
