def index():
    with open('tempates/index.html') as template:
        return template.read()



def blog():
    with open('tempates/blog.html') as template:
        return template.read()

def static(url):
    with open('static/{}'.format(url).lstrip('/')) as static:
        return static.read()
