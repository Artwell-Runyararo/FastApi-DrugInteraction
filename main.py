from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
from apis.base import api_router


def include_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)

    # ✅ CORS setup
    origins = [
        "http://localhost:5173",
        "http://127.0.0.1:8000",
        "http://127.0.0.1:5173",
    ]  # Vite dev server

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    include_router(app)
    return app


app = start_application()


@app.get("/")
def home():
    return {"msg": "Drugs Interactions 🚀"}
