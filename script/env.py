import sys
import os

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
FATHER_PATH = os.path.join(FILE_PATH, '..')
ORIGIN_DATA_PATH = os.path.join(FATHER_PATH, 'origin_data')
if os.path.exists(ORIGIN_DATA_PATH) == False:
    os.mkdir(ORGIN_DATA_PATH)
