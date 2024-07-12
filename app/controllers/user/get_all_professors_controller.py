from app.controllers.controller_interface import IController
from app.helpers.http.django_http_request import DjangoHttpRequest
from app.helpers.http.http_codes import InternalServerError, OK
from app.repos.user.user_repository_interface import IUserRepository


class GetAllProfessorsController(IController):
    def __init__(self, repo: IUserRepository):
        super().__init__(repo)
        self.repo = repo

    def __call__(self, request: DjangoHttpRequest):
        try:
            self.error_handling(request)
            response_data = self.business_logic(request)

            if len(response_data) == 0:
                return OK(
                    body=[],
                    message="No professors were found"
                )
            else:
                return OK(
                    body=[professor.to_dict() for professor in response_data] if type(response_data[0]) != dict else response_data, # TODO: Refactor this (entity? repo use to dict? idk)
                    message="All professors were successfully retrieved"
                )

        except Exception as err:
            return InternalServerError(
                message=str(err)
            )

    def error_handling(self, request: DjangoHttpRequest):
        pass

    def business_logic(self, request: DjangoHttpRequest):
        return self.repo.get_all_professors()
