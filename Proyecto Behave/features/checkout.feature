Feature: Checkout page
    @checkout
    Scenario:
        Given the user is on the main page
        When the user searches for blouses
        And the user follows the checkout steps
        Then the user succesfully purchases the blouses

