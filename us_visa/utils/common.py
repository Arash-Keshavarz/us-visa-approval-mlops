import os
import sys
import yaml
import dill
import numpy as np
import pandas as pd
from us_visa.exception import USVisaException
from us_visa.logger import logger

def read_yaml_file(file_path: str) -> dict:
    """Reads a YAML file and returns its contents as a dictionary."""
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise USVisaException(e, sys) from e

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """Writes a dictionary/object to a YAML file."""
    try:
        if replace and os.path.exists(file_path):
            os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise USVisaException(e, sys) from e

def save_object(file_path: str, obj: object) -> None:
    """Saves a python object (like a model or scaler) using dill."""
    try:
        logger.info(f"Entered the save_object method of MainUtils")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        logger.info(f"Exited the save_object method of MainUtils")
    except Exception as e:
        raise USVisaException(e, sys) from e

def load_object(file_path: str) -> object:
    """Loads a python object from a file path."""
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file: {file_path} is not exists")
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise USVisaException(e, sys) from e
    
    
def save_numpy_array_data(file_path: str, array: np.array):
    """
    Saves numpy array data to a file.
    file_path: str location of file to save
    array: np.array data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise USVisaException(e, sys) from e


def load_numpy_array_data(file_path: str) -> np.array:
    """
    Loads numpy array data from a file.
    file_path: str location of file to load
    return: np.array data loaded
    """
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file {file_path} does not exist")
        with open(file_path, "rb") as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise USVisaException(e, sys) from e
    
    

def drop_columns(dataframe: pd.DataFrame, cols: list) -> pd.DataFrame:
    """
    Drops the specified columns from a pandas DataFrame.
    dataframe: pd.DataFrame
    cols: list of column names to be dropped
    """
    try:
        logger.info(f"Entered the drop_columns method of MainUtils")
        # Only drop columns that actually exist in the dataframe to avoid errors
        existing_cols = [col for col in cols if col in dataframe.columns]
        dataframe = dataframe.drop(columns=existing_cols, axis=1)
        
        logger.info(f"Dropped columns: {existing_cols}")
        logger.info(f"Exited the drop_columns method of MainUtils")
        return dataframe
    except Exception as e:
        raise USVisaException(e, sys) from e