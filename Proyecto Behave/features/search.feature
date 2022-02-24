Feature: Search
    @search
    Scenario Outline: Search for items
        Given the user is on the main page
        When the user searches for <item>
        Then the user sees <item> displayed on the results

        Examples:
            | item    |
            | blouses |
            | t-shirt |
            | dresses |