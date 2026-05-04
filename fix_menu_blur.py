with open('index.html', 'r') as f:
    html = f.read()

# I will replace the background of the nav expanded state directly.
css_to_replace = """    .apple-nav.mobile-expanded::before {
      background: var(--bg-main);
      backdrop-filter: none;
      -webkit-backdrop-filter: none;
      box-shadow: none;
    }"""

new_css = """    .apple-nav.mobile-expanded::before {
      background: var(--bg-color);
      backdrop-filter: none;
      -webkit-backdrop-filter: none;
      box-shadow: none;
    }"""

if css_to_replace in html:
    html = html.replace(css_to_replace, new_css)
    with open('index.html', 'w') as f:
        f.write(html)
    print("Background CSS appended successfully.")
else:
    print("Could not find style block.")
