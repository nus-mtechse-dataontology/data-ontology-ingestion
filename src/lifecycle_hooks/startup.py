import logging
import os
from contextlib import asynccontextmanager
import tomllib
import traceback


from fastapi import FastAPI
from pathlib import Path
from sqlmodel import SQLModel

from entities.aircraft import Aircraft
from entities.airport import Airport
from entities.city import City
from entities.country import Country
from entities.fact_flight_info import FactFlightInfo
from entities.airline_coverage import AirlineCoverage
from entities.currency_rate import CurrencyRate
from sessions.db_session import DBSession


log = logging.getLogger("ingestion")


def load_config() -> dict:
    """
    Loads the config for the named ingestion.
    """
    with open(Path(os.getenv("PROJECT_PATH", os.getcwd()), "resources", "config.toml")) as cf:
        try:
            return tomllib.loads(cf.read())
        
        except tomllib.TOMLDecodeError as exc:
            log.error("Startup: error while loading config, %s", exc)
            log.error(traceback.format_exc())
            raise exc


@asynccontextmanager
async def startup(app: FastAPI):
    """
    Initialise all dependencies for the Application
    """
    config = load_config()
    session = DBSession(config)
    SQLModel.metadata.create_all(session.engine)
    
    app.state.session = session
    
    yield
