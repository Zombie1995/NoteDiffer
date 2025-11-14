import uvicorn
from src.config import get_settings
from src.controller import fastapi_app

# Get settings from environment
settings = get_settings()


class App:
    def run(self):
        uvicorn.run(
            "src.main:fastapi_app",
            host=settings.APP_HOST,
            port=settings.APP_PORT,
            log_level="debug",
            reload=True
        )


app = App()
