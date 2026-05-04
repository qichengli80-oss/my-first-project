with open('index.html', 'r') as f:
    html = f.read()

# Fix the duplicate mobile-nav-item definition
css_to_remove = """
    .mobile-nav-item {
      text-decoration: none;
      color: var(--text-main);
      font-size: 18px;
      font-weight: 600;
      transition: color 0.3s ease;
    }"""

if css_to_remove in html:
    html = html.replace(css_to_remove, "")
    with open('index.html', 'w') as f:
        f.write(html)
    print("Cleaned up CSS.")
else:
    print("Could not find CSS to remove.")
