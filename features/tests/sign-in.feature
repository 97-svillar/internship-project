# Created by sergiovillar at 7/15/25
Feature: # Tests for Reelly Sign-in
  # Enter feature description here

  Scenario: User can go to settings and edit the personal information
    Given Open Reelly sign-up page
    When login to the page with 97svillar@gmail.com and Derrickrose#1
    And Click on the settings option
    And Click on the Edit profile option
    Then Enter some test information in the input fields
    And Check the right information is present in the input fields
#    And Check the “Close” and “Save Changes” buttons are available and clickable.

