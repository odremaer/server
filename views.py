def index():
    with open('tempates/index.html') as template:
        return template.read()



def blog():
    with open('tempates/blog.html') as template:
        return template.read()

def css(url):
    with open('{}'.format(url).lstrip('/')) as css:
        return css.read()