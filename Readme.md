# Retail Sales Forecasting (Minimal, Portfolio-Ready)

This repository contains a compact, beginner-friendly but professional retail sales forecasting project. It includes a cleaned dummy dataset, a notebook walkthrough covering all project phases, and a reusable training script.

Structure
- `data/retail_sales_dummy.csv` — example time-series data with `date`, `sales`, and `promotion`.
- `notebook.ipynb` — end-to-end project notebook (EDA, cleaning, FE, modeling, forecasting, business insights, slides & Q&A).
- `train_model.py` — script to train models, evaluate, and save the best model and predictions.
- `requirements.txt` — Python dependencies.

Quick start
1. Create and activate a Python environment (recommended: `python -m venv .venv`).
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the training script:

```
python train_model.py
```

4. Open `notebook.ipynb` in Jupyter or VS Code for the full guided walkthrough and visualizations.

Resume blurb (copy for LinkedIn/GitHub):
"Implemented an end-to-end retail sales forecasting pipeline using Python (pandas, scikit-learn, seaborn). Built and compared linear and tree-based models, produced business-facing insights on promotion lift and inventory recommendations, and documented results in a professional notebook for presentation." 

Presentation & report notes
- The notebook contains a short project report and slide bullet points suitable for a 10–12 minute internship presentation. Use the plotted figures for slides.

Next steps (suggested enhancements)
- Add hyperparameter tuning (GridSearchCV) and time-series cross-validation.
- Deploy a small dashboard (Streamlit) to explore forecasts and scenario analysis.

If you want, I can:
- run `train_model.py` here and attach `test_predictions.csv` and `sales_model.joblib`.
- create a small `slides.md` with slide content or export to a PPTX file.
