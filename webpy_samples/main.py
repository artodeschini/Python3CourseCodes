import web

"""
execute this file and tes to call 

http://localhost:8080/your%20name

"""

urls = {
    '/(.*)', 'index'
}

app = web.application(urls, globals())


class index:
    def GET(self, name):
        print(name)
        return '<h1>Hello ' + name + '.</h1>How are you?'


if __name__ == '__main__':
    app.run()
