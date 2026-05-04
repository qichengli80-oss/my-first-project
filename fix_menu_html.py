with open('index.html', 'r') as f:
    html = f.read()

# Make the theme toggle icon styling better for the full screen menu
css_to_replace2 = """    .mobile-theme-icon {
      font-size: 20px;
      color: #0071e3;
      cursor: pointer;
    }"""

new_css2 = """    .mobile-theme-icon {
      font-size: 24px;
      color: var(--text-main);
      cursor: pointer;
      margin-top: 30px;
    }"""

if css_to_replace2 in html:
    html = html.replace(css_to_replace2, new_css2)
    with open('index.html', 'w') as f:
        f.write(html)
    print("Theme icon CSS updated successfully.")
else:
    print("Could not find theme icon CSS block.")
