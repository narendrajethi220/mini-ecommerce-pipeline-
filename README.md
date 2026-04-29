Mini E-commerce Data Pipeline - Local Setup

Goal: Understand the ETL flow without cloud complexity
What You'll Build:

Scrape product data from a dummy e-commerce site (or use Faker library)
Clean & transform data with Pandas
Load into SQLite database
Create basic SQL queries for analysis

Tech Stack:

Python (requests/BeautifulSoup or Faker)
Pandas for transformation
SQL for storage
Basic SQL queries

Deliverables:

mini-ecommerce-pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
│   ├── data_extraction.py
│   ├── data_transformation.py
│   ├── data_loading.py
│   └── run_pipeline.py
│
├── analysis.sql
├── requirements.txt
├── README.md
├── .gitignore
└── venv/

Key Learnings:

ETL concepts
Data quality checks
Basic pipeline orchestration