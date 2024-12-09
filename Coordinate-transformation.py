# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 10:12:42 2024

@author: adimopoulos
"""


from pyproj import Transformer
from rich.logging import RichHandler
from rich.prompt import Prompt
from tkinter import filedialog
import logging
import os
import pandas as pd
import sys

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)
log = logging.getLogger("rich")

try:
    to_crd = int(sys.argv[2])
    from_crd = int(sys.argv[1])
except:
    log.info("No arguments have been passed")
    from_crd = Prompt.ask(
        "What is the EPSG of the original coordinate system: ",
        choices=["32630", "27700", "4326"],
        default="32630",
    )
    to_crd = Prompt.ask(
        "What is the EPSG of the target coordinate system: ",
        choices=["32630", "27700", "4326"],
        default="27700",
    )

log.info(f"Original EPSG: {from_crd}, Target EPSG: {to_crd}")


transformer = Transformer.from_crs(f"EPSG:{from_crd}", f"EPSG:{to_crd}")

file_types = [("CSV Files", "*.csv"), ("Text Files", "*.txt")]

open_file_path = filedialog.askopenfilename(filetypes=file_types)
open_file_name = open_file_path.split("/")[-1].split(".")[0]

try:
    df = pd.read_csv(open_file_path)
    log.info(f"File {open_file_name} has been loaded \n {df}")
except Exception as ex:
    log.error(f"{ex}")


df_transformed = pd.DataFrame(columns=["Name", "x_trans", "y_trans", "x_or", "y_or"])
for idx, row in df.iterrows():
    x = row.iat[1]
    y = row.iat[2]
    name = row.iat[0]
    # breakpoint()
    transformed = transformer.transform(x, y)
    df_transformed.loc[idx] = [name, transformed[0], transformed[1], x, y]

save_file_path = filedialog.askdirectory()

try:
    save_file_path = f"{save_file_path}/{open_file_name}_transformed.csv"
    df_transformed.to_csv(save_file_path)
    log.info(
        f"File has been succesfully saved into {save_file_path} \n {df_transformed}"
    )
except Exception as e:
    log.error(f"{e}")

os.system("pause")
