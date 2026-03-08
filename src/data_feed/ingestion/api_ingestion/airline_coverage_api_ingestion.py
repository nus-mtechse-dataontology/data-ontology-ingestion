from gateway.api_gateway import ApiGateway
from ingestion.api_ingestion.api_ingestion import ApiIngestion
from services.airline_coverage_service import AirlineCoverageService


class AirlineCoverageApiIngestion(ApiIngestion):
	def __init__(
			self,
			api_gateway: ApiGateway,
			airline_coverage_service: AirlineCoverageService,
			config: dict
	):
		super().__init__(api_gateway, config)
		self._ingestion_name = "airline_coverage"
		self._service = airline_coverage_service
		
	def _upload_to_db(self, response_payload: dict):
		self._service.insert_coverages(response_payload["data"]["destinationList"])
	