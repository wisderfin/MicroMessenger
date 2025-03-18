from schemas.base import BaseSchema

class BaseResponseSchema(BaseSchema):
    pass

class ResponseSchema(BaseResponseSchema):
    code: int
    message: str
