def index():
    with open('tempates/index.html') as template:
        return template.read()



def blog():
    with open('tempates/blog.html') as template:
        return template.read()

<<<<<<< HEAD
def static(url):
    with open('static/{}'.format(url).lstrip('/')) as static:
        return static.read()

def img(url):
    with open('static/{}'.format(url).lstrip('/'), 'rb') as static:
        return static.read()
=======
def css(url):
    with open('{}'.format(url).lstrip('/')) as css:
        return css.read()
>>>>>>> 5aebd31... can send any css files to server(working on static files)
