import web

render = web.template.render('templates/')

urls = (
    '/(.*)', 'Index'
)
app = web.application(urls, globals())


class Index:
    def GET(self, name):
        if not name:
            name = 'World'
        return render.indexcalendar()


if __name__ == "__main__":
    app.run()
