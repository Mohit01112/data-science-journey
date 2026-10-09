
from pathlib import Path

import joblib
import pandas as pd
from flask import Flask, render_template, request

# =====================================================
# 1. FLASK CONFIGURATION
# =====================================================

app = Flask(__name__)

BASE_DIR = Path(
    r"C:\Users\rajem\OneDrive\Desktop\DATA SCIENCE\data-science-journey\ml\waiter_tips_calculator"
)

MODEL_PATH = BASE_DIR / "tip_prediction_model.pkl"


# =====================================================
# 2. LOAD YOUR TRAINED MODEL
# =====================================================

if not MODEL_PATH.is_file():
    raise FileNotFoundError(
        f"Trained model not found at: {MODEL_PATH}"
    )

model = joblib.load(MODEL_PATH)

print("Trained model loaded successfully.")
print("Model type:", type(model).__name__)

if hasattr(model, "feature_names_in_"):
    print("Model features:", list(model.feature_names_in_))


# =====================================================
# 3. CATEGORY ENCODING
# These must match your model training code.
# =====================================================

SEX_MAPPING = {
    "Male": 0,
    "Female": 1,
}

SMOKER_MAPPING = {
    "No": 0,
    "Yes": 1,
}

DAY_MAPPING = {
    "Thur": 0,
    "Fri": 1,
    "Sat": 2,
    "Sun": 3,
}

TIME_MAPPING = {
    "Lunch": 0,
    "Dinner": 1,
}


# =====================================================
# 4. HOME PAGE
# =====================================================

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", error=None)


# =====================================================
# 5. PREDICTION PAGE
# =====================================================

@app.route("/predict", methods=["POST"])
def predict():

    try:
        # ---------------------------------------------
        # Read values submitted by index.html
        # ---------------------------------------------

        total_bill = float(request.form.get("total_bill", ""))
        size = int(request.form.get("size", ""))

        sex = request.form.get("sex", "")
        smoker = request.form.get("smoker", "")
        day = request.form.get("day", "")
        time = request.form.get("time", "")

        # ---------------------------------------------
        # Validate numeric inputs
        # ---------------------------------------------

        if not 0 < total_bill <= 100000:
            raise ValueError(
                "Enter a bill amount greater than zero."
            )

        if not 1 <= size <= 50:
            raise ValueError(
                "Party size must be between 1 and 50."
            )

        # ---------------------------------------------
        # Validate categorical inputs
        # ---------------------------------------------

        if sex not in SEX_MAPPING:
            raise ValueError("Select a valid server category.")

        if smoker not in SMOKER_MAPPING:
            raise ValueError("Select a valid smoking status.")

        if day not in DAY_MAPPING:
            raise ValueError("Select a valid day.")

        if time not in TIME_MAPPING:
            raise ValueError("Select a valid meal time.")

        # ---------------------------------------------
        # Prepare the model input
        # ---------------------------------------------

        input_data = {
            "total_bill": total_bill,
            "sex": SEX_MAPPING[sex],
            "smoker": SMOKER_MAPPING[smoker],
            "day": DAY_MAPPING[day],
            "time": TIME_MAPPING[time],
            "size": size,
        }

        # Preserve the model's expected feature order
        # when feature names are available.
        if hasattr(model, "feature_names_in_"):
            expected_features = list(model.feature_names_in_)

            missing_features = [
                feature for feature in expected_features
                if feature not in input_data
            ]

            if missing_features:
                raise ValueError(
                    "The model expects additional or different features: "
                    + ", ".join(missing_features)
                )

            input_df = pd.DataFrame(
                [input_data],
                columns=expected_features,
            )

        else:
            # Fallback for models trained without feature names.
            input_df = pd.DataFrame(
                [[
                    total_bill,
                    SEX_MAPPING[sex],
                    SMOKER_MAPPING[smoker],
                    DAY_MAPPING[day],
                    TIME_MAPPING[time],
                    size,
                ]],
                columns=[
                    "total_bill",
                    "sex",
                    "smoker",
                    "day",
                    "time",
                    "size",
                ],
            )

        # ---------------------------------------------
        # Predict using the already-trained model
        # ---------------------------------------------

        prediction = model.predict(input_df)

        predicted_tip = float(prediction[0])

        if not pd.notna(predicted_tip):
            raise ValueError(
                "The model returned an invalid prediction."
            )

        predicted_tip = max(0.0, predicted_tip)

        # ---------------------------------------------
        # Calculate result values
        # ---------------------------------------------

        tip_percentage = (
            predicted_tip / total_bill
        ) * 100

        total_amount = total_bill + predicted_tip

        tip_per_person = predicted_tip / size

        result = {
            "predicted_tip": round(predicted_tip, 2),
            "tip_percentage": round(tip_percentage, 2),
            "total_bill": round(total_bill, 2),
            "total_amount": round(total_amount, 2),
            "party_size": size,
            "tip_per_person": round(tip_per_person, 2),
        }

        # ---------------------------------------------
        # Show results on the separate result page
        # ---------------------------------------------

        return render_template(
            "result.html",
            result=result,
        )

    except (ValueError, TypeError) as exc:

        return render_template(
            "index.html",
            error=str(exc),
        ), 400

    except Exception as exc:

        app.logger.exception("Prediction failed")

        return render_template(
            "index.html",
            error=(
                f"Prediction failed: {type(exc).__name__}: {exc}"
            ),
        ), 500


# =====================================================
# 6. HEALTH CHECK
# =====================================================

@app.route("/health", methods=["GET"])
def health():
    return {
        "status": "ok",
        "model_loaded": True,
        "model_exists": MODEL_PATH.is_file(),
    }


# =====================================================
# 7. START FLASK
# =====================================================

if __name__ == "__main__":
    print("\nTipPredict is starting...")
    print("Model:", MODEL_PATH)
    print("Open: http://127.0.0.1:5000")

    app.run(debug=True)
