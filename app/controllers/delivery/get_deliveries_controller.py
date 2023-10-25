
from app.controllers.controller_interface import IController
from app.helpers.errors.common_errors import MissingParameters
from app.helpers.http.http_codes import BadRequest, InternalServerError, OK
from app.helpers.http.http_models import HttpRequestModel
from app.repos.delivery.delivery_repository_interface import IDeliveryRepository


class GetDeliveriesController(IController):

    def __init__(self, repo: IDeliveryRepository):
        super().__init__(repo)
        self.repo = repo

    def __call__(self, request: HttpRequestModel):

        try:
            self.error_handling(request)
            response_data = self.business_logic(request)

            return OK(
                body=response_data,
                message="The delivery have been retrieved successfully"
            )

        except MissingParameters as e:
            return BadRequest(
                message=str(e)
            )

        except Exception as e:
            return InternalServerError(
                message=str(e)
            )

    def error_handling(self, request: HttpRequestModel):
        if request.method != "GET":
            raise MissingParameters('body', 'get_deliveries')

        if request.data.get('project_id') is None:
            raise MissingParameters('project_id', 'get_deliveries')

    def business_logic(self, request: HttpRequestModel):
        response = self.repo.get_deliveries(request.data)
        return response
