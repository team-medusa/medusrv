import medusrv

app = medusrv.create_app()
app.run(port=9988, debug=True, use_evalex=False)
