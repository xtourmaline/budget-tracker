#!/usr/bin/env python3

# file    : budget.py
# purpose :
# author  : vanessa trinh and ali rizvi
# date    : april 12th, 2023

import os
import sqlalchemy

from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    engine = sqlalchemy.create_engine(f"mysql+mysqldb://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASS')}@localhost")

    with engine.connect() as db:
        db.execute(sqlalchemy.text("CREATE DATABASE IF NOT EXISTS budget_db;"))
        db.commit()
        db.close()