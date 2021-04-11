import logging
import numpy as np


def logs_file_setup(file: str, level=logging.INFO):
    import os
    import sys
    import time
    from datetime import date

    today = date.today()
    timestamp = str(time.time()).replace('.', '')
    logs_dir = f"logs/logs-{today.strftime('%d-%m-%Y')}"
    logs_file = f'{logs_dir}/{os.path.splitext(os.path.basename(file))[0]}-{timestamp}.log'
    os.makedirs(logs_dir, exist_ok=True)
    logging.basicConfig(filename=logs_file, filemode='w+', level=level)
    sh = logging.StreamHandler(sys.stdout)
    logging.getLogger().addHandler(sh)


def set_seed(seed: int):
    np.random.seed(seed)
