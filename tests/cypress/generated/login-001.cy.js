describe('Successful Login with Valid Credentials', () => {
  it('Verify user can login to https://the-internet.herokuapp.com/login with valid credentials', () => {
    // Navigate to the login page
    cy.visit('https://the-internet.herokuapp.com/login');
    
    // Wait for page to load
    cy.url().should('include', '/login');

    // Enter valid credentials - trying multiple possible selectors
    cy.get('input[type="email"], input[type="text"], input[name="username"], input[name="email"], input[name="user"], #username, #email, #user, [data-test="username"], [data-cy="username"], [placeholder*="email" i], [placeholder*="username" i]')
      .first()
      .should('be.visible')
      .clear()
      .type('tomsmith');
    
    cy.get('input[type="password"], input[name="password"], input[name="pass"], #password, #pass, [data-test="password"], [data-cy="password"], [placeholder*="password" i]')
      .first()
      .should('be.visible')
      .clear()
      .type('SuperSecretPassword!');
    
    // Submit the form - trying multiple possible selectors
    cy.get('button[type="submit"], input[type="submit"], button:contains("Login"), button:contains("Sign in"), button:contains("Log in"), button:contains("Submit"), [data-test="login-button"], [data-cy="login-button"], form button')
      .first()
      .click();
    
    // Wait for navigation/response
    cy.wait(2000);
    
    // Verify successful login - check for common success indicators
    cy.url().then(url => {
      // Check if URL changed from login page
      expect(url).to.not.include('/login');
    });
  });
});