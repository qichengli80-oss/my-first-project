with open('index.html', 'r') as f:
    html = f.read()

# Make the menu panel solid too
css_to_replace = """    .mobile-menu-panel {
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
    }"""

new_css = """    .mobile-menu-panel {
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
      background: var(--bg-color); /* Ensure full solid background */
    }"""

if css_to_replace in html:
    html = html.replace(css_to_replace, new_css)
    with open('index.html', 'w') as f:
        f.write(html)
    print("Background CSS appended successfully.")
else:
    print("Could not find style block.")
