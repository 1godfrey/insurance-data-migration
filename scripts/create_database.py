from sqlalchemy import create_engine, text

# Database connection
DATABASE_URL = "postgresql+psycopg2://postgres:Masonmason123!@insurance-db.clyokumkkjlx.us-east-2.rds.amazonaws.com:5432/postgres"
engine = create_engine(DATABASE_URL)

# SQL schema
schema = """
CREATE TABLE IF NOT EXISTS insurance_policies (
    PolicyID INT PRIMARY KEY,
    CustomerName VARCHAR(255),
    PolicyType VARCHAR(50),
    PremiumAmount DECIMAL(10, 2),
    StartDate DATE,
    EndDate DATE
);
"""

# Execute schema creation
with engine.connect() as connection:
    connection.execute(text(schema))
    print("Database schema created successfully!")
