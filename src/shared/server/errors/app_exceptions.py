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

    @staticmethod
    def invalid_user_password_combination() -> HTTPException:
        detail = {
            "errorCode": "INVALID_USER_PASSWORD_COMBINATION",
            "errorMessages": {
                "pt-BR": "Combinação de usuário e senha inválida",
                "en-US": "Invalid user and password combination",
            },
        }
        return HTTPException(
            status_code=400,
            detail=detail,
        )
