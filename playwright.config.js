module.exports = {
  testDir: './tests/playwright/generated',
  use: {
    headless: false,
    baseURL: 'https://the-internet.herokuapp.com',
    video: 'on',
  },
};
