import web

"""
execute this file and tes to call 

http://localhost:8080/artur/42

"""

urls = {
    '/(.*)/(.*)', 'index'
}

render = web.template.render('resources/')
app = web.application(urls, globals())


class index:
    def GET(self, name, age):
        print(name)
        print(age)
        return render.main(name, age)


if __name__ == '__main__':
    app.run()