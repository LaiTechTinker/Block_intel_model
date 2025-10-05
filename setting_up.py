import os
import logging
import pathlib
from pathlib import Path

Project_name="Block_intel_classifier"
list_of_files=[
     f"{Project_name}/components/__init__.py",
    f"{Project_name}/components/Data_ingestion.py",
    f"{Project_name}/components/Data_validation.py",
    f"{Project_name}/components/Data_transformation.py",
    f"{Project_name}/components/model_trainer.py",
    f"{Project_name}/components/model_evaluation.py",
    f"{Project_name}/components/model_pusher.py",
    f"{Project_name}/configuration/__init__.py",
    f"{Project_name}/constants/__init__.py",
    f"{Project_name}/components/__init__.py",
    f"{Project_name}/entity/__init__.py",
    f"{Project_name}/exception/__init__.py",
    f"{Project_name}/entity/config_entity.py",
    f"{Project_name}/entity/artifact_entity.py",
    f"{Project_name}/utils/__init__.py",
    f"{Project_name}/logger/__init__.py",
    f"{Project_name}/utils/main_utils.py",
    f"{Project_name}/pipline/__init__.py",
    f"{Project_name}/pipline/training_pipeline.py",
    f"{Project_name}/pipline/prediction_pipeline.py",
    "requirements.txt",
    "setup.py",
    "demo.py",
    "app.py",
    "Dockerfile",
    ".dockerignore",
    "config/model.yaml",
    "config/schema.yaml"
]
for file in list_of_files:
    file_path=Path(file)
    filedir,filename=file_path.parent,file_path.name
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info("creating directory:{} for filename:{}".format(filedir,filename))
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
         with open(file_path,"w") as f:
            pass
            logging.info(f"creating empty file:{filename}")
    else:
        logging.info(f"file with name:{filename} already exists")