# AdClick_Optimiser

## 🎯 Project Overview
A machine learning pipeline to predict user ad clicks using real-world advertising data. The project includes model training, evaluation, and simulated A/B testing to assess the impact of ML-driven targeting versus standard ad delivery.

---

## 🛠 Tools & Technologies
- Python (Jupyter Notebooks via VSCode)
- SQL (PostgreSQL or SQLite)
- scikit-learn, XGBoost, Pandas, Statsmodels
- Tableau Public (for dashboards)
- Git & GitHub (version control)
- Optional: DBeaver (for SQL querying)

---

## 📊 Data Source
- **Dataset:** [CriteoClickLogs – Hugging Face](https://huggingface.co/datasets/criteo/CriteoClickLogs)
- **File Used:** `day_0.parquet`
- **Size:** ~1.75GB
- **Description:** Real ad click logs with 13 numerical and 26 categorical features. Each row represents a display of an ad with a binary `label` (1 = clicked, 0 = not clicked).

---

## 💡 Key Features
- CTR prediction using Logistic Regression and XGBoost
- SQL queries for filtering and analysis
- A/B test simulation using control and ML-driven treatment groups
- Statistical evaluation (t-tests, z-tests)
- Tableau dashboards to visualize insights

---

## 📈 Visualizations
- Click distribution and CTR trends
- Feature importance plots
- Control vs treatment group CTR comparison
- ROC curves and confusion matrices

---

## 📁 Folder Structure

- `data/`
  - `raw/` – Original `day_0.parquet` file
  - `processed/` – Cleaned and sampled data
- `notebooks/` – Jupyter notebooks for EDA, modeling, and testing
- `scripts/` – Python scripts for preprocessing and model training
- `sql/` – SQL queries for analysis
- `tableau/` – Tableau workbooks and exported dashboards
- `outputs/` – Charts, model metrics, reports
- `docs/` – Project documentation and references

---

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AdClick_Optimiser.git
   cd AdClick_Optimiser
   

## License
This project is open source and available under the [MIT License](LICENSE).
