from blogr import create_app, sqlite, create_app2
from blogr.sqlite3 import transferir_datos
if __name__ == '__main__':
    app = create_app()
    app2 = create_app2()
    transferir_datos(sqlite=sqlite, app=app, app2=app2)
    app.run()
