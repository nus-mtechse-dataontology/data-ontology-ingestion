from abc import ABC, abstractmethod


class Driver(ABC):
	def __init__(self):
		self._connection_url: str | None = None
	
	@abstractmethod
	def get_connection(self) -> str:
		"""
		Create a new database connections.
		"""
		pass
