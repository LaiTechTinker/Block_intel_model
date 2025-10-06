import logging
from from_root import from_root
import os
from datetime import datetime

logging_filename= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logdir="logs"
logs_path = os.path.join(from_root(), logdir, logging_filename)

os.makedirs(logdir, exist_ok=True)


logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)