# TipPredict — Flask ML Website

A warm, restaurant-inspired website that uses a trained scikit-learn model to estimate a tip from bill and dining details.

## Project structure

```text
tippredict_flask/
├── app.py
├── tip_prediction_model.pkl   # copy your existing trained model here
├── tips.csv                   # copy your existing dataset here
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

## 1. Set up locally (Windows PowerShell)

Open PowerShell in this project folder:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks activation, run this once for the current terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Copy your existing `tip_prediction_model.pkl` and `tips.csv` into the same folder as `app.py`.

## 2. Run the website

```powershell
python app.py
```

Open <http://127.0.0.1:5000> in your browser. The `/health` endpoint is available at <http://127.0.0.1:5000/health>.

## 3. How the Flask app works

1. `templates/index.html` contains the form and the result page.
2. The browser sends the form values to Flask's `/predict` route.
3. `app.py` validates the values and encodes the categories.
4. The app loads `tip_prediction_model.pkl` and calls `model.predict(...)`.
5. Flask sends the prediction back to the template, where the estimated tip and total are shown.
6. `static/style.css` styles the page and `static/script.js` prevents repeated form submissions.

## 4. Important: match your training schema

This app assumes the model was trained with the following feature order:

```python
X = df.drop("tip", axis=1)
# expected order: total_bill, sex, smoker, day, time, size
```

It also assumes these mappings were used **before training**:

```python
df["sex"] = df["sex"].map({"Male": 0, "Female": 1})
df["smoker"] = df["smoker"].map({"Yes": 1, "No": 0})
df["day"] = df["day"].map({"Thur": 0, "Fri": 1, "Sat": 2, "Sun": 3})
df["time"] = df["time"].map({"Lunch": 0, "Dinner": 1})
```

If your notebook used a different column order or mappings, update `FEATURE_ORDER` and `CATEGORY_MAPS` in `app.py` to match. A model trained with different inputs can produce incorrect predictions or raise an error.

## 5. Deploying

For a simple Python hosting platform that supports Flask:

- Set the build/install command to `pip install -r requirements.txt`.
- Set the start command to `gunicorn app:app`.
- Ensure `app.py`, the template/static folders, and the model file are included in the deployed project.
- If the model file is large, use your hosting provider's supported artifact storage or Git LFS. Do not commit secrets.

The built-in `app.run(debug=True)` is for local development only. Production should use the Gunicorn start command.

## Notes

- The UI uses dollar signs because the commonly used Seaborn `tips` dataset records are in dollars. Change the currency labels if your use case is different.
- The model estimate is for educational demonstration; tipping norms vary by location and service.
- Only load pickle files you trust. Pickle files can execute code when loaded.
