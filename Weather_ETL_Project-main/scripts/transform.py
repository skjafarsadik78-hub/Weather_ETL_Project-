import json
import pandas as pd
import os
from logger import logger

try:

    logger.info("Transformation Started")

    with open("data/raw/weather.json", "r") as file:
        data = json.load(file)

    df = pd.DataFrame(data)

    os.makedirs("data/cleaned", exist_ok=True)

    df.to_csv("data/cleaned/weather.csv", index=False)

    print("✅ Data transformed successfully!")

    logger.info("Transformation Completed")

except Exception as e:
    logger.error(e)
    print(e)