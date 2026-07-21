import pandas as pd
import mysql.connector
from datetime import datetime
from logger import logger

try:

    logger.info("Loading Started")

    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="YOUR_PASSWORD",
        database="weather_db"
    )

    cursor = connection.cursor()

    df = pd.read_csv("data/cleaned/weather.csv")

    sql = """
    INSERT INTO weather_data
    (city,time,temperature,humidity,wind_speed,recorded_at)
    VALUES(%s,%s,%s,%s,%s,%s)
    """

    for _, row in df.iterrows():

        values = (
            row["city"],
            row["time"],
            row["temperature"],
            row["humidity"],
            row["wind_speed"],
            datetime.now()
        )

        cursor.execute(sql, values)

    connection.commit()

    print("✅ Data loaded successfully!")

    logger.info("Loading Completed")

    cursor.close()
    connection.close()

except Exception as e:
    logger.error(e)
    print(e)