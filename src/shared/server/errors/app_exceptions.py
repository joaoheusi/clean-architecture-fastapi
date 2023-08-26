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
