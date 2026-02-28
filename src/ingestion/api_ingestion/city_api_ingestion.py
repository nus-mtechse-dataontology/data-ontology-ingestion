from gateway.api_gateway import ApiGateway
from ingestion.api_ingestion.api_ingestion import ApiIngestion
from services.city_service import CityService


class CityApiIngestion(ApiIngestion):
	def __init__(self, api_gateway: ApiGateway, city_service: CityService, config: dict):
		super().__init__(api_gateway, config)
		self._ingestion_name = "city"
		self._service = city_service
	
	def _upload_to_db(self, response_payload: dict):
		self._service.insert_cities(response_payload["data"]["destinationList"])
