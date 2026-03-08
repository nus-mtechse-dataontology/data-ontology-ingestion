from typing import Any

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from configurations.app_config import AppConfig
from configurations.logger_config import LoggerConfig
from endpoints.routes.ingestion.ingestion_routes import ingestion_router
from lifecycle_hooks.startup import startup
from models.app_model import AppModel


class Ingestion:
    def __init__(self):
        self._app: FastAPI | None = None
        self._config: AppModel | None = None
        self._logger_config: dict[str, Any] | None = None

    def start(self):
        """
        Starting point for the app.
        1. Loads all configurations.
        2. Initialise the app with configurations loaded.
        """
        self._load_config()
        self._init_app()
        print('starting')
        uvicorn.run(
            self._app,
            host=self._config.host,
            port=self._config.port,
            reload=self._config.reload,
            log_config=self._logger_config
        )

    def _load_config(self):
        self._config = AppConfig().app_config
        self._logger_config = LoggerConfig.get_config()

    def _init_app(self):
        """
        Initialise and configures the FastAPI application
        """
        self._app = FastAPI(
            title="Data Ontology",
            docs_url=self._config.api_endpoint.docs_url,
            redoc_url=self._config.api_endpoint.redoc_url,
            root_path=self._config.api_endpoint.root_path,
            lifespan=startup
        )

        self._add_middleware()
        self._include_routers()

    def _add_middleware(self):
        self._app.add_middleware(TrustedHostMiddleware)
        self._app.add_middleware(
            CORSMiddleware,
            allow_origins=self._config.api_endpoint.allow.origins,
            allow_credentials=self._config.api_endpoint.allow.credentials,
            allow_methods=self._config.api_endpoint.allow.methods,
            allow_headers=self._config.api_endpoint.allow.headers,
        )

    def _include_routers(self):
        self._app.include_router(ingestion_router)


if __name__ == "__main__":
    Ingestion().start()
