from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

font_config = FontConfiguration()
html = HTML(string='''
  <html>
    <h1>The title</h1>
    <body>
      <div>
        <div>
          <div width="100" style="border: 1px solid coral;">Test</div>
          <div width="100" style="border: 1px solid coral;">Test1</div>
        </div>
        <div>
          <div width="100" style="border: 1px solid coral;">Test</div>
          <div width="100" style="border: 1px solid coral;">Test</div>
        </div>
        <div>
          <div width="100" style="border: 1px solid coral;">Test</div>
          <div width="100" style="border: 1px solid coral;">Test</div>
        </div>
      </div>
    </body>
  </html>
''')
css = CSS(string='''
    @page {
      size: A4; /* Change from the default size of A4 */
      margin: 0.5cm; /* Set margin on each page */
    }
    @font-face {
        font-family: Gentium;
        src: url(http://example.com/fonts/Gentium.otf);
    }
    h1 { font-family: Gentium }''', font_config=font_config)
html.write_pdf(
    './example.pdf', stylesheets=[css],
    font_config=font_config)
