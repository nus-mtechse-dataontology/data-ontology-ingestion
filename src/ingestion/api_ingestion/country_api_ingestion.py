from gateway.api_gateway import ApiGateway
from ingestion.api_ingestion.city_api_ingestion import ApiIngestion
from services.country_service import CountryService


class CountryApiIngestion(ApiIngestion):
	def __init__(self, api_gateway: ApiGateway, country_service: CountryService, config: dict):
		super().__init__(api_gateway, config)
		self._ingestion_name = "country"
		self._service = country_service
		
	def _upload_to_db(self, response_payload: dict):
		self._service.insert_countries(response_payload["data"]["destinationList"])
