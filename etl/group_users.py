
import argparse
import logging
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime
import os


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

def group_and_save(df, group_col, output_dir, timestamp):
    grouped = (
        df.groupby(group_col)["user_id"]
        .agg(user_count="count", user_ids=lambda x: ",".join(map(str, x)))
        .reset_index()
    )
    out_path = os.path.join(output_dir, f"group_by_{group_col}_{timestamp}.csv")
    grouped.to_csv(out_path, index=False)
    logging.info(f" Wrote {len(grouped)} rows to {out_path}")

def main():
    parser = argparse.ArgumentParser(description="Group users by bank, company, and pincode.")
    parser.add_argument("--db-uri", required=True, help="Database connection URI")
    parser.add_argument("--output-dir", default="etl/output", help="Directory to save CSV files")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    engine = create_engine(args.db_uri)

    query = """
        SELECT 
        u.id AS user_id,
        CONCAT(u.first_name, ' ', u.last_name) AS full_name,
        e.company_name,
        b.bank_name,
        u.pincode
    FROM users u
    JOIN employment_info e ON u.id = e.user_id
    JOIN user_bank_info b ON u.id = b.user_id;
    """

    logging.info("Connecting to db")
    with engine.connect() as conn:
        df = pd.read_sql(text(query), conn)

    timestamp = datetime.now().strftime("%Y%m%dT%H%M%S")

    group_and_save(df, "bank_name", args.output_dir, timestamp)
    group_and_save(df, "company_name", args.output_dir, timestamp)
    group_and_save(df, "pincode", args.output_dir, timestamp)

    logging.info("ETL completed")

if __name__ == "__main__":
    main()
