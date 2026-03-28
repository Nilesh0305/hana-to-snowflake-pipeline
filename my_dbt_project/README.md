# 🚀 End-to-End Data Engineering Pipeline

## SAP HANA → Python → Snowflake → dbt → Power BI

---

## 📌 Project Overview

This project demonstrates a complete **end-to-end data engineering pipeline** built using modern tools.

The objective is to extract data from **SAP HANA Calculation Views**, load it into **Snowflake**, transform it using **dbt**, and visualize insights in **Power BI**.

---

## 🧠 What I Implemented (Step-by-Step)

### 🔹 Step 1: SAP HANA Setup

* Connected to SAP HANA Cloud using `hdbcli`
* Accessed Calculation Views
* Verified data extraction using SQL queries

---

### 🔹 Step 2: Python Data Extraction

* Created Python scripts:

  * `hana_to_snowflake.py`
  * `hana_to_snow_cv.py`
* Used:

  * `hdbcli` → Connect to HANA
  * `pandas` → Data processing

✔ Extracted data from HANA into DataFrames

---

### 🔹 Step 3: Load Data into Snowflake

* Connected to Snowflake (trial account)
* Loaded extracted data into Snowflake tables
* Verified data load using SQL queries

---

### 🔹 Step 4: Setup dbt Project

* Initialized dbt project inside:

  ```
  my_dbt_project/
  ```
* Configured:

  * `dbt_project.yml`
  * `profiles.yml`

✔ Created dbt folder structure:

* models
* macros
* seeds
* snapshots
* tests

---

### 🔹 Step 5: Created dbt Models

* Built transformation models:

  * `my_first_dbt_model.sql`
  * `my_second_dbt_model.sql`
* Added schema file:

  * `schema.yml`

✔ Executed:

```
dbt run
dbt test
```

---

### 🔹 Step 6: Project Structuring

* Organized project as:

```
end_to_end_project/
│
├── Python scripts
├── dbt project
├── logs
├── .gitignore
```

✔ Followed industry-standard structure

---

### 🔹 Step 7: Git Setup & Version Control

* Initialized Git in root folder
* Configured `.gitignore`:

  * `.venv`
  * `__pycache__`
  * `target/`
  * `dbt_packages/`

✔ Performed:

* Git Add
* Commit
* Push

✔ Repository created on GitHub:

* All code version controlled
* Clean commit history

---

### 🔹 Step 8: GitHub Integration

* Connected PyCharm with GitHub
* Pushed complete project
* Verified:

  * `origin/main` synced with `main`

---

## 🏗️ Architecture

SAP HANA → Python → Snowflake → dbt → Power BI

---

## 🛠️ Tech Stack

* **SAP HANA Cloud**
* **Python (hdbcli, pandas)**
* **Snowflake**
* **dbt**
* **Power BI**
* **Git & GitHub**
* **PyCharm**

---

## 📂 Project Structure

```
end_to_end_project/
│
├── hana_to_snowflake.py
├── hana_to_snow_cv.py
│
├── my_dbt_project/
│   ├── models/
│   ├── macros/
│   ├── seeds/
│   ├── snapshots/
│   ├── tests/
│   ├── dbt_project.yml
│   └── README.md
│
├── .gitignore
└── README.md
```

---

##  Data Pipeline Flow

1. Extract data from SAP HANA
2. Load into Snowflake using Python
3. Transform using dbt models
4. Validate using dbt tests
5. Visualize using Power BI

---

## How to Run

### 1. Install Dependencies

```
pip install pandas hdbcli snowflake-connector-python dbt-core dbt-snowflake
```

### 2. Run Data Load

```
python hana_to_snowflake.py
```

### 3. Run dbt

```
cd my_dbt_project
dbt run
dbt test
```

---

##  Key Highlights

✔ End-to-end pipeline implementation
✔ SAP HANA to Snowflake integration
✔ dbt-based transformation layer
✔ Clean Git version control
✔ Modular & scalable design

---

##  Future Enhancements

* Add scheduling (Airflow / dbt Cloud)
* Add CI/CD pipeline
* Add logging & monitoring
* Add dashboard screenshots

---

## Author

**Nilesh Kulkarni**

---

##  If you like this project, give it a star!
