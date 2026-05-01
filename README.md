# 🛒 Mini E-commerce Data Pipeline (Local Setup)

## 🎯 Goal

Understand the **ETL (Extract, Transform, Load)** process without cloud complexity.

---

## 🚀 Build 

* Extract product data (via Faker)
* Clean and transform data using Pandas
* Load processed data into a SQLite database
* Perform basic analysis using SQL queries

---

## 🛠️ Tech Stack

* Python (requests / Faker)
* Pandas (data transformation)
* MySQL (data storage)
* SQL (analysis)

---

## 📁 Project Structure

```
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
```

---

## 🧠 Key Learnings

* ETL pipeline fundamentals
* Data cleaning & quality checks
* Basic pipeline orchestration

---

## ▶️ How to Run

1. Create and activate virtual environment
2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```
3. Run pipeline:

   ```
   python scripts/run_pipeline.py
   ```

---

## 📌 Notes

* Raw data is stored in `data/raw/`
* Cleaned data is stored in `data/processed/`
* SQL queries are in `analysis.sql`

---
