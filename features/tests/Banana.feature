# Created by Alex Kardash at 02/11/20
Feature: Banana
  Check Crinkle chrome extension is displayed correctly for all partners

  @regression
  Scenario: Validate bananarepublic
    Given I open page 'bananarepublic.gap.com'
    When I add to bag
    When I open checkout page
    When I verify extension has product
