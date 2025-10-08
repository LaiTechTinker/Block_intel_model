from Block_intel_classifier.logger import logging
from Block_intel_classifier.exception import Block_intelException
import sys
logging.info("Testing my logging file")
try:
    x=3/0
except Exception as e:
   raise Block_intelException(e,sys)