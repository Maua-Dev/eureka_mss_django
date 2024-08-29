from app.controllers.controller_interface import IController
from app.helpers.errors.common_errors import WrongTypeParameter, MissingParameters, RequestNotFound, \
    MethodNotAllowed
from app.helpers.http.http_codes import OK, BadRequest, Forbidden, InternalServerError
from app.helpers.http.http_models import HttpRequestModel
from app.helpers.functions.request_url_function import HelperGenerateUrl


class RequestGenerateUrlController(IController):

    def __init__(self):
        super().__init__()

    def __call__(self, request: HttpRequestModel):

        try:
            self.error_handling(request)
            response_data = self.business_logic(request)

            return OK(
                body=response_data,
                message="The presigned url was generated successfully"
            )

        except MissingParameters as e: 
            return BadRequest(
                message=str(e)
            )

        except WrongTypeParameter as e:
            return BadRequest(
                message=str(e)
            )

        except MethodNotAllowed as e:
            return Forbidden(
                message=str(e)
            )

        except Exception as e:
            return InternalServerError(
                message=str(e)
            )

    def error_handling(self, request: HttpRequestModel):
        try:
            # if request.method != "GET":
            #     raise MethodNotAllowed(method=request.method,
            #                            route='get_presigned_url')
            
            if request.method != "POST":
                raise MethodNotAllowed(method=request.method,
                                       route='get_presigned_url')

            if request.data.get('project_id') is None:
                raise MissingParameters(field='project_id',
                                        method='get_presigned_url')

            try:
                int(request.data.get('project_id'))
            except ValueError as ve:
                raise WrongTypeParameter(field='project_id')

            if request.data.get('upload_type') is None:
                raise MissingParameters(field='upload_type',
                                        method='get_presigned_url')

            if type(request.data.get('upload_type')) is not str:
                raise WrongTypeParameter(field='upload_type')

            if request.data.get('file_name') is None:
                raise MissingParameters(field='upload_type',
                                        method='get_presigned_url')

            if type(request.data.get('file_name')) is not str:
                raise WrongTypeParameter(field='file_name')

        except MissingParameters as e:
            raise e

        except WrongTypeParameter as e:
            raise e

        except MethodNotAllowed as e:
            raise e

        except Exception as e:

            raise RequestNotFound() from e

    def business_logic(self, request: HttpRequestModel):

        project_id = request.data.get('project_id')
        upload_type = request.data.get('upload_type')
        file_name = request.data.get('file_name')

        gen = HelperGenerateUrl()
        response = gen.get_presigned_url(project_id=project_id,
                                         upload_type=upload_type,
                                         file_name=file_name)

        return response
