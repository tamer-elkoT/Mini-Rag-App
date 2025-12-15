from .BaseController import BaseController
from fastapi import UploadFile
from src.models import ResponseMessage

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        # Now self.app_settings is available here too because of inheritance from BaseController

    def validate_uploaded_file(self, file: UploadFile):
        """
        Validate the uploaded file based on allowed extensions and max size.

        """
        self.size_scale = 1024 * 1024 # convert MB to bytes for size comparison because UploadFile size is in bytes
        # Check the file type is allowed (belongs to allowed types from config)
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            # return False, f"File type {file.content_type} is not allowed."
            return False, ResponseMessage.FILE_TYPE_NOT_SUPPORTED.value # using enum message for consistency
        
        # Check the file size if it's less than the max size from config to be allowed
        if file.size > self.app_settings.FILE_MAX_SIZE_MB * self.size_scale:
            # return False, f"File size exceeds the maximum limit of {self.app_settings.FILE_MAX_SIZE_MB} MB."
            return False, ResponseMessage.FILE_SIZE_EXCEEDED.value # using enum message for consistency
        
        return True, "File is valid."

        
