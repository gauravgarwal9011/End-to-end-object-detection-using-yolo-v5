from ObjectDetection.logger import logging
from ObjectDetection.exception import AppException

try:
    a = 3 /"s"
except Exception as e:
    raise AppException(e,sys)