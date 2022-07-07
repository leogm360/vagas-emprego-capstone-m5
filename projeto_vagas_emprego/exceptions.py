from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_409_CONFLICT


class DataConflict(APIException):
    status_code = HTTP_409_CONFLICT
    default_detail = "Internal data is conflicting."
    default_code = "data_conflict"

    def __init__(self, detail=None, code=None):
        super().__init__(detail, code)
