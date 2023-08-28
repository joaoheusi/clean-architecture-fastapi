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

    @staticmethod
    def no_authentication_provided() -> HTTPException:
        detail = {
            "errorCode": "NO_AUTHENTICATION_PROVIDED",
            "errorMessages": {
                "pt-BR": "Nenhuma autenticação fornecida",
                "en-US": "No authentication provided",
            },
        }
        return HTTPException(
            status_code=401,
            detail=detail,
        )

    @staticmethod
    def invalid_authentication_method() -> HTTPException:
        detail = {
            "errorCode": "INVALID_AUTHENTICATION_METHOD",
            "errorMessages": {
                "pt-BR": "Método de autenticação inválido",
                "en-US": "Invalid authentication method",
            },
        }
        return HTTPException(
            status_code=401,
            detail=detail,
        )

    @staticmethod
    def invalid_or_expired_token() -> HTTPException:
        detail = {
            "errorCode": "INVALID_OR_EXPIRED_TOKEN",
            "errorMessages": {
                "pt-BR": "Token inválido ou expirado",
                "en-US": "Invalid or expired token",
            },
        }
        return HTTPException(
            status_code=401,
            detail=detail,
        )

    @staticmethod
    def insufficient_security_clearance() -> HTTPException:
        detail = {
            "errorCode": "INSUFFICIENT_SECURITY_CLEARANCE",
            "errorMessages": {
                "pt-BR": "Autorização insuficiente",
                "en-US": "Insufficient security clearance",
            },
        }
        return HTTPException(
            status_code=403,
            detail=detail,
        )

    @staticmethod
    def insufficient_application_clearance() -> HTTPException:
        detail = {
            "errorCode": "INSUFFICIENT_APPLICATION_CLEARANCE",
            "errorMessages": {
                "pt-BR": "Autorização insuficiente",
                "en-US": "Insufficient application clearance",
            },
        }
        return HTTPException(
            status_code=403,
            detail=detail,
        )
