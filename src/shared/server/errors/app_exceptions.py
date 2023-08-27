from fastapi.exceptions import HTTPException


class AppExceptions(HTTPException):
    @staticmethod
    def resource_not_found() -> HTTPException:
        detail = {
            "errorCode": "RESOURCE_NOT_FOUND",
            "errorMessages": {
                "pt-BR": "Recurso não encontrado",
                "en-US": "Resource not found",
            },
        }
        return HTTPException(
            status_code=404,
            detail=detail,
        )

    @staticmethod
    def email_in_use() -> HTTPException:
        detail = {
            "errorCode": "EMAIL_ALREADY_IN_USE",
            "errorMessages": {
                "pt-BR": "Email já está em uso",
                "en-US": "Email already in use",
            },
        }
        return HTTPException(
            status_code=400,
            detail=detail,
        )
