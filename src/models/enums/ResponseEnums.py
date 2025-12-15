from enum import Enum

class ResponseMessage(str, Enum):
    FILE_UPLOADED_SUCESS = "File uploaded successfully."
    FILE_VALIDATION_FAILED = "File validation failed."
    FILE_TYPE_NOT_SUPPORTED = "File type is not supported."
    FILE_SIZE_EXCEEDED = "File size exceeds the maximum limit."
    FILE_VALIDATION_SUCCESS = "File is valid."
    