import re

with open('index.html', 'r') as f:
    html = f.read()

# Replace the mobile-expanded styles
css_to_replace = """    /* 移动端展开时的样式 */
    .apple-nav.mobile-expanded { height: auto; min-height: 340px; border-radius: 30px; }
    .apple-nav.mobile-expanded::before { bottom: -310px; transition: all 0.45s cubic-bezier(0.34, 1.2, 0.64, 1) 0s; }

    /* 修复展开时logo和按钮垂直居中导致的重叠问题 */
    .apple-nav.mobile-expanded .nav-container { align-items: flex-start; padding-top: 20px; }

    .apple-nav.mobile-expanded .mobile-menu-btn .line-top { transform: translateY(3px) rotate(45deg); }
    .apple-nav.mobile-expanded .mobile-menu-btn .line-bottom { transform: translateY(-3px) rotate(-45deg); }

    .mobile-menu-panel {
      display: flex;
      flex-direction: column;
      position: absolute;
      top: 70px;
      left: 0;
      width: 100%;
      padding: 20px 30px;
      opacity: 0;
      visibility: hidden;
      transform: translateY(-10px);
      transition: opacity 0.3s ease, transform 0.4s cubic-bezier(0.34, 1.2, 0.64, 1), visibility 0.3s;
      z-index: 10;
      pointer-events: none;
    }

    .apple-nav.mobile-expanded .mobile-menu-panel {
      opacity: 1;
      visibility: visible;
      transform: translateY(0);
      transition: opacity 0.4s ease 0.1s, transform 0.4s cubic-bezier(0.34, 1.2, 0.64, 1) 0.1s;
      pointer-events: auto;
    }

    .mobile-menu-links {
      display: flex;
      flex-direction: column;
      gap: 20px;
      margin-bottom: 20px;
      margin-top: 20px;
    }"""

new_css = """    /* 按照Apple官网手机端展开时的全屏样式 */
    .apple-nav.mobile-expanded {
      top: 0;
      width: 100%;
      max-width: 100%;
      height: 100vh;
      border-radius: 0;
      align-items: flex-start; /* 将子元素置于顶部 */
      transition: all 0.5s cubic-bezier(0.32, 0.72, 0, 1);
    }

    /* 当展开时，保持nav-container的高度和内边距与原来类似，但是修正top */
    .apple-nav.mobile-expanded .nav-container {
      height: 60px; /* 固定高度，避免拉伸到100vh */
      margin-top: 24px; /* 补偿因为top变为0而失去的顶部间距 */
      align-items: center; /* 保持logo和按钮在这一行居中对齐 */
    }

    .apple-nav.mobile-expanded .mobile-menu-btn .line-top { transform: translateY(3px) rotate(45deg); }
    .apple-nav.mobile-expanded .mobile-menu-btn .line-bottom { transform: translateY(-3px) rotate(-45deg); }

    .mobile-menu-panel {
      display: flex;
      flex-direction: column;
      position: absolute;
      top: 84px; /* margin-top(24) + height(60) */
      left: 0;
      width: 100%;
      height: calc(100vh - 84px);
      padding: 20px 40px;
      opacity: 0;
      visibility: hidden;
      transform: translateY(-20px);
      transition: opacity 0.3s ease, transform 0.4s cubic-bezier(0.32, 0.72, 0, 1), visibility 0.3s;
      z-index: 10;
      pointer-events: none;
      box-sizing: border-box;
      overflow-y: auto;
    }

    .apple-nav.mobile-expanded .mobile-menu-panel {
      opacity: 1;
      visibility: visible;
      transform: translateY(0);
      transition: opacity 0.4s ease 0.2s, transform 0.5s cubic-bezier(0.32, 0.72, 0, 1) 0.1s;
      pointer-events: auto;
    }

    .mobile-menu-links {
      display: flex;
      flex-direction: column;
      gap: 0;
    }

    .mobile-nav-item {
      text-decoration: none;
      color: var(--text-main);
      font-size: 28px; /* Apple官网手机端字体较大 */
      font-weight: 600;
      padding: 15px 0;
      border-bottom: 1px solid rgba(128, 128, 128, 0.2);
      transition: color 0.3s ease;
    }

    .mobile-nav-item:last-child {
      border-bottom: none;
    }"""

if css_to_replace in html:
    html = html.replace(css_to_replace, new_css)
    with open('index.html', 'w') as f:
        f.write(html)
    print("CSS updated successfully.")
else:
    print("Could not find the exact CSS block to replace.")
