import uvicorn


class App:
    def run(self):
        uvicorn.run("main:fastapi_app", host="127.0.0.1",
                    port=8000, reload=True)


app = App()
