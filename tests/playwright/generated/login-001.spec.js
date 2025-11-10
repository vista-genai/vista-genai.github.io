import { test, expect } from '@playwright/test';
	
	// 配置慢速执行
	test.use({
	  // 每个操作延迟500ms
	  launchOptions: {
		slowMo: 500,
	  },
	  // 视口大小
	  viewport: { width: 1280, height: 720 },
	  // 录制视频
	  video: 'on',
	  // 截图
	  screenshot: 'on',
	});
	
	test('Successful Login with Valid Credentials', async ({ page }) => {
	  // 设置默认超时
	  test.setTimeout(60000);
	  
	  // 导航到登录页面
	  await page.goto('https://the-internet.herokuapp.com/login');
	  console.log('📍 Navigated to: https://the-internet.herokuapp.com/login');
	  
	  // 等待页面完全加载
	  await page.waitForLoadState('networkidle');
	  await page.waitForTimeout(2000); // 额外等待2秒
	  
	  // 截图 - 初始页面
	  await page.screenshot({ path: 'login-page.png' });
	
	  
	  // 🔍 查找用户名输入框
	  console.log('🔍 Finding username input...');
	  const usernameInput = page.locator('#username');
	  await usernameInput.scrollIntoViewIfNeeded();
	  await usernameInput.hover(); // 悬停效果
	  await page.waitForTimeout(1000);
	  
	  // ✏️ 输入用户名
	  console.log('✏️ Typing username: tomsmith');
	  await usernameInput.click();
	  await usernameInput.fill(''); // 先清空
	  
	  // 逐字输入，模拟真人打字
	  for (const char of 'tomsmith') {
		await usernameInput.type(char, { delay: 100 });
	  }
	  await page.waitForTimeout(1000);
	  
	  // 🔍 查找密码输入框
	  console.log('🔍 Finding password input...');
	  const passwordInput = page.locator('#password');
	  await passwordInput.scrollIntoViewIfNeeded();
	  await passwordInput.hover();
	  await page.waitForTimeout(1000);
	  
	  // ✏️ 输入密码
	  console.log('✏️ Typing password...');
	  await passwordInput.click();
	  await passwordInput.fill('');
	  
	  // 逐字输入密码
	  for (const char of 'SuperSecretPassword!') {
		await passwordInput.type(char, { delay: 100 });
	  }
	  await page.waitForTimeout(1500);
	  
	  // 📸 截图 - 填写完成
	  await page.screenshot({ path: 'filled-form.png' });
	  
	  // 🖱️ 查找并点击登录按钮
	  console.log('🖱️ Finding login button...');
	  const loginButton = page.locator('button[type="submit"]');
	  await loginButton.scrollIntoViewIfNeeded();
	  await loginButton.hover(); // 悬停在按钮上
	  await page.waitForTimeout(1000);
	  
	  // 高亮显示按钮
	  await loginButton.evaluate(el => {
		el.style.border = '3px solid red';
		el.style.boxShadow = '0 0 10px red';
	  });
	  await page.waitForTimeout(1000);
	  
	  console.log('🚀 Clicking login button...');
	  await loginButton.click();
	  
	  // 等待导航
	  await page.waitForTimeout(2000);
	  
	  // 验证登录成功
	  console.log('✅ Verifying successful login...');
	  await expect(page).toHaveURL(/.*secure/);
	  
	  // 📸 最终截图
	  await page.screenshot({ path: 'login-success.png' });
	  console.log('✅ Test completed successfully!');
	});