import os
from pathlib import Path
import tomllib

from logging.config import dictConfig


class LoggerConfig:
	@staticmethod
	def config_logger():
		config = LoggerConfig.get_config()
		dictConfig(config["logger"])
	
	@staticmethod
	def get_config():
		root = os.environ.get("PROJECT_PATH", os.getcwd())
		
		with open(Path(root, "resources", "config.toml"), "r") as cf:
			data = cf.read()
			config = tomllib.loads(data)
			return config
