with open('index.html', 'r') as f:
    html = f.read()

# Make the theme toggle icon styling better
css_to_replace = """    .theme-toggle-btn {
      font-size: 20px;
      color: #0071e3;
      cursor: pointer;
    }"""

new_css = """    .theme-toggle-btn {
      font-size: 20px;
      color: #0071e3;
      cursor: pointer;
    }

    #mobileThemeBtn {
      font-size: 24px;
      margin-top: 20px;
      margin-left: 5px;
      color: var(--text-main);
    }"""

if css_to_replace in html:
    html = html.replace(css_to_replace, new_css)
    with open('index.html', 'w') as f:
        f.write(html)
    print("Theme icon CSS updated successfully.")
else:
    print("Could not find theme icon CSS block. Attempting more general replace...")
    # Just append it to the end of the style block
    if '</style>' in html:
      html = html.replace('</style>', """    #mobileThemeBtn {
      font-size: 24px;
      margin-top: 20px;
      margin-left: 5px;
      color: var(--text-main);
    }
</style>""")
      with open('index.html', 'w') as f:
          f.write(html)
      print("Theme icon CSS appended successfully.")
