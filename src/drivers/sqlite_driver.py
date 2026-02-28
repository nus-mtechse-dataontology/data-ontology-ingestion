from drivers.driver import Driver


class SQLiteDriver(Driver):
	def __init__(self, config: dict):
		super().__init__()
		self._config = config
	
	def get_connection(self) -> str:
		if self._connection_url is None:
			self._connection_url = self._config["datasource"]["database"]['connection_url']
		
		return self._connection_url
	