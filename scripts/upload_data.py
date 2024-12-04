import pandas as pd
import sqlalchemy
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection
DATABASE_URL = os.getenv("DATABASE_URL")
engine = sqlalchemy.create_engine(DATABASE_URL)

# Folder containing Excel files
DATA_FOLDER = '/home/ec2-user/insurance-data-migration/data/'

# Read and upload each file
for file_name in os.listdir(DATA_FOLDER):
    if file_name.endswith(".xlsx"):
        file_path = os.path.join(DATA_FOLDER, file_name)
        print(f"Processing file: {file_path}")
        df = pd.read_excel(file_path)
        df.to_sql("insurance_policies", engine, if_exists="append", index=False)
        print(f"Uploaded data from {file_name} successfully!")
