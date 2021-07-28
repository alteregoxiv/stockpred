from src import app_factory

app = app_factory()
app.run(debug = True , host="0.0.0.0")
