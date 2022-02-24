Feature: Contact page
    @contact
    Scenario:
        Given the user is on the Contact page
        When the user fills in the contact form
        And the user clicks on the Send button
        Then the contact message is sent

