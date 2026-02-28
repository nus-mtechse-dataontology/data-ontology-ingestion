import sys
import os
import pytest
from sqlmodel import SQLModel, create_engine

from entities.airport import Airport
from entities.city import City
from entities.country import Country
from entities.airline import Airline
from entities.airline_coverage import AirlineCoverage
from entities.fact_flight_info import FactFlightInfo
from entities.currency_rate import CurrencyRate


@pytest.fixture
def in_memory_engine():
    """Return a fresh SQLite in-memory engine with tables created."""
    engine = create_engine("sqlite:///:memory:", echo=False)
    SQLModel.metadata.create_all(engine)
    return engine
