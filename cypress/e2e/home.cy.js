describe('Homepage Smoke Test', () => {
  it('loads the app root and shows expected UI elements', () => {
    cy.visit('/')

    // Check for app title or branding
    cy.contains('One FM')  // Replace with your actual app name text

    // Check for a common button like "Sign In" or "Login"
    cy.contains('Sign In')  // Or 'Login', 'Continue', etc.

    // Optional: check if the navbar or footer is visible
    cy.get('nav').should('exist')
    cy.get('footer').should('exist')
  })
})