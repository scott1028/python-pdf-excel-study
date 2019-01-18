from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
from jinja2 import Template

font_config = FontConfiguration()

t = Template('{% for item in items%}<div width="100" style="border: 1px solid coral;">{{ item }}</div>{% endfor %}')

output = '''
<div>
  %s
</div>
''' % t.render(items=[1,2,3,4,5,6])

print(output)

html = HTML(string=output)
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
