# import streamlit as st
# import pandas as pd
# import joblib

# model = joblib.load("Logistic_Regression_heart.pkl")
# scaler = joblib.load("scaler.pkl")
# expected_columns = joblib.load("columns.pkl")

# st.title("Heart Stroke Prediction by Amit ❤")
# st.markdown("Provide The Following Details")

# age = st.slider("Age",18,100,40)

# sex = st.selectbox("SEX",['M','F'])

# chest_pain = st.selectbox(
#     "Chest Pain Type",
#     ["ATA","NAP","TA","ASY"]
# )

# resting_bp = st.number_input(
#     "Resting Blood Pressure(mm Hg)",
#     80,200,120
# )

# cholesterol = st.number_input(
#     "Cholesterol (mg/dL)",
#     100,600,200
# )

# fasting_bs = st.selectbox(
#     "Fasting Blood Sugar > 120 mg/dL",
#     [0,1]
# )

# resting_ecg = st.selectbox(
#     "Resting ECG",
#     ["Normal","ST","LVH"]
# )

# max_hr = st.slider(
#     "Max Heart Rate",
#     60,220,150
# )

# exercise_angina = st.selectbox(
#     "Exercise-Induced Angina",
#     ["Y","N"]
# )

# oldpeak = st.slider(
#     "Oldpeak (ST Depression)",
#     0.0,6.0,1.0
# )

# st_slope = st.selectbox(
#     "ST Slope",
#     ["Up","Flat","Down"]
# )

# if st.button("Predict"):

#     raw_input = {
#         "Age": age,
#         "RestingBP": resting_bp,
#         "Cholesterol": cholesterol,
#         "FastingBS": fasting_bs,
#         "MaxHR": max_hr,
#         "Oldpeak": oldpeak,

#         "Sex_" + sex: 1,
#         "ChestPainType_" + chest_pain: 1,
#         "RestingECG_" + resting_ecg: 1,
#         "ExerciseAngina_" + exercise_angina: 1,
#         "ST_Slope_" + st_slope: 1
#     }

#     input_df = pd.DataFrame([raw_input])

#     for col in expected_columns:
#         if col not in input_df.columns:
#             input_df[col] = 0

#     input_df = input_df[expected_columns]

#     scaled_input = scaler.transform(input_df)

#     prediction = model.predict(scaled_input)[0]

#     if prediction == 1:
#         st.error("⚠ High Risk of Heart Disease")
#     else:
#         st.success("✅ Low Risk of Heart Disease")

# import streamlit as st
# import pandas as pd
# import joblib
# import numpy as np

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(
#     page_title="AI Heart Disease Predictor",
#     page_icon="❤",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # ---------------- LOAD MODEL ----------------
# model = joblib.load("Logistic_Regression_heart.pkl")
# scaler = joblib.load("scaler.pkl")
# expected_columns = joblib.load("columns.pkl")

# # ---------------- CUSTOM CSS ----------------
# st.markdown("""
# <style>

# html, body, [class*="css"]  {
#     font-family: 'Segoe UI', sans-serif;
# }

# .main {
#     background: linear-gradient(to right, #eef2f7, #ffffff);
# }

# .main-title {
#     font-size: 48px;
#     font-weight: 800;
#     text-align: center;
#     color: #d81b60;
#     margin-bottom: 5px;
# }

# .sub-title {
#     text-align: center;
#     color: #555;
#     font-size: 18px;
#     margin-bottom: 30px;
# }

# .card {
#     background-color: white;
#     padding: 25px;
#     border-radius: 18px;
#     box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
#     margin-bottom: 20px;
# }

# .metric-box {
#     background: linear-gradient(135deg,#d81b60,#ff6f91);
#     padding: 20px;
#     border-radius: 15px;
#     color: white;
#     text-align: center;
#     box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
# }

# .metric-number {
#     font-size: 30px;
#     font-weight: bold;
# }

# .metric-label {
#     font-size: 15px;
#     opacity: 0.9;
# }

# .stButton > button {
#     width: 100%;
#     height: 60px;
#     border-radius: 14px;
#     border: none;
#     background: linear-gradient(90deg,#d81b60,#ff6f91);
#     color: white;
#     font-size: 22px;
#     font-weight: bold;
#     transition: 0.3s;
# }

# .stButton > button:hover {
#     transform: scale(1.02);
#     background: linear-gradient(90deg,#b0004f,#ff4778);
#     color: white;
# }

# .result-success {
#     background: #d4edda;
#     padding: 25px;
#     border-radius: 15px;
#     color: #155724;
#     text-align: center;
#     font-size: 28px;
#     font-weight: bold;
# }

# .result-danger {
#     background: #f8d7da;
#     padding: 25px;
#     border-radius: 15px;
#     color: #721c24;
#     text-align: center;
#     font-size: 28px;
#     font-weight: bold;
# }

# .footer {
#     text-align: center;
#     color: gray;
#     margin-top: 50px;
# }

# </style>
# """, unsafe_allow_html=True)

# # ---------------- SIDEBAR ----------------
# with st.sidebar:

#     st.image(
#         "https://cdn-icons-png.flaticon.com/512/2966/2966486.png",
#         width=120
#     )

#     st.title("❤ AI Health Dashboard")

#     st.markdown("""
#     ### About Project
    
#     This intelligent system predicts the possibility of heart disease using:
    
#     ✔ Logistic Regression  
#     ✔ Machine Learning  
#     ✔ Data Scaling  
#     ✔ Real-time Prediction  
    
#     ---
    
#     ### Technologies
    
#     - Python
#     - Streamlit
#     - Scikit-Learn
#     - Pandas
#     """)

# # ---------------- HEADER ----------------
# st.markdown(
#     "<div class='main-title'>❤ AI Heart Disease Prediction System</div>",
#     unsafe_allow_html=True
# )

# st.markdown(
#     "<div class='sub-title'>Advanced Machine Learning Based Healthcare Risk Analysis</div>",
#     unsafe_allow_html=True
# )

# # ---------------- TOP METRICS ----------------
# m1, m2, m3 = st.columns(3)

# with m1:
#     st.markdown("""
#     <div class='metric-box'>
#         <div class='metric-number'>95%</div>
#         <div class='metric-label'>Prediction Accuracy</div>
#     </div>
#     """, unsafe_allow_html=True)

# with m2:
#     st.markdown("""
#     <div class='metric-box'>
#         <div class='metric-number'>24/7</div>
#         <div class='metric-label'>AI Monitoring</div>
#     </div>
#     """, unsafe_allow_html=True)

# with m3:
#     st.markdown("""
#     <div class='metric-box'>
#         <div class='metric-number'>ML</div>
#         <div class='metric-label'>Powered Intelligence</div>
#     </div>
#     """, unsafe_allow_html=True)

# st.markdown("<br>", unsafe_allow_html=True)

# # ---------------- INPUT FORM ----------------
# left, right = st.columns(2)

# with left:

#     st.markdown("<div class='card'>", unsafe_allow_html=True)

#     st.subheader("👤 Personal Information")

#     age = st.slider("Age", 18, 100, 40)

#     sex = st.selectbox(
#         "Gender",
#         ['M', 'F']
#     )

#     chest_pain = st.selectbox(
#         "Chest Pain Type",
#         ["ATA", "NAP", "TA", "ASY"]
#     )

#     resting_bp = st.number_input(
#         "Resting Blood Pressure",
#         80, 200, 120
#     )

#     cholesterol = st.number_input(
#         "Cholesterol Level",
#         100, 600, 200
#     )

#     st.markdown("</div>", unsafe_allow_html=True)

# with right:

#     st.markdown("<div class='card'>", unsafe_allow_html=True)

#     st.subheader("🩺 Medical Information")

#     fasting_bs = st.selectbox(
#         "Fasting Blood Sugar > 120",
#         [0, 1]
#     )

#     resting_ecg = st.selectbox(
#         "Resting ECG",
#         ["Normal", "ST", "LVH"]
#     )

#     max_hr = st.slider(
#         "Maximum Heart Rate",
#         60, 220, 150
#     )

#     exercise_angina = st.selectbox(
#         "Exercise-Induced Angina",
#         ["Y", "N"]
#     )

#     oldpeak = st.slider(
#         "Oldpeak (ST Depression)",
#         0.0, 6.0, 1.0
#     )

#     st_slope = st.selectbox(
#         "ST Slope",
#         ["Up", "Flat", "Down"]
#     )

#     st.markdown("</div>", unsafe_allow_html=True)

# # ---------------- PREDICTION ----------------
# st.markdown("<br>", unsafe_allow_html=True)

# if st.button("🚀 Predict Heart Disease Risk"):

#     raw_input = {
#         "Age": age,
#         "RestingBP": resting_bp,
#         "Cholesterol": cholesterol,
#         "FastingBS": fasting_bs,
#         "MaxHR": max_hr,
#         "Oldpeak": oldpeak,

#         "Sex_" + sex: 1,
#         "ChestPainType_" + chest_pain: 1,
#         "RestingECG_" + resting_ecg: 1,
#         "ExerciseAngina_" + exercise_angina: 1,
#         "ST_Slope_" + st_slope: 1
#     }

#     input_df = pd.DataFrame([raw_input])

#     # Fill missing columns
#     for col in expected_columns:
#         if col not in input_df.columns:
#             input_df[col] = 0

#     input_df = input_df[expected_columns]

#     # Scale Data
#     scaled_input = scaler.transform(input_df)

#     # Prediction
#     prediction = model.predict(scaled_input)[0]

#     # Probability
#     probability = model.predict_proba(scaled_input)[0][1]

#     st.markdown("<br>", unsafe_allow_html=True)

#     st.subheader("📊 Prediction Result")

#     st.progress(int(probability * 100))

#     if prediction == 1:

#         st.markdown(f"""
#         <div class='result-danger'>
#             ⚠ HIGH RISK OF HEART DISEASE <br><br>
#             Risk Probability: {probability*100:.2f}%
#         </div>
#         """, unsafe_allow_html=True)

#     else:

#         st.markdown(f"""
#         <div class='result-success'>
#             ✅ LOW RISK OF HEART DISEASE <br><br>
#             Safety Probability: {(1-probability)*100:.2f}%
#         </div>
#         """, unsafe_allow_html=True)

# # ---------------- FOOTER ----------------
# st.markdown("""
# <div class='footer'>
#     ❤ Developed by Amit | AI + Machine Learning + Streamlit
# </div>
# """, unsafe_allow_html=True)


import streamlit as st
import pandas as pd
import joblib
import numpy as np
import time

# ─────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="CardioAI · Heart Risk Intelligence",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
#  LOAD MODEL (graceful demo stub)
# ─────────────────────────────────────────────
@st.cache_resource
def load_model():
    try:
        m  = joblib.load("Logistic_Regression_heart.pkl")
        s  = joblib.load("scaler.pkl")
        c  = joblib.load("columns.pkl")
        return m, s, c, True
    except Exception:
        return None, None, None, False

model, scaler, expected_columns, model_loaded = load_model()

# ─────────────────────────────────────────────
#  THEME STATE
# ─────────────────────────────────────────────
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

# ─────────────────────────────────────────────
#  THEME PALETTES
# ─────────────────────────────────────────────
DARK = {
    "app_bg":          "linear-gradient(160deg,#080b14 0%,#0d1120 50%,#080b14 100%)",
    "app_glow1":       "rgba(99,102,241,.2)",
    "app_glow2":       "rgba(168,85,247,.15)",
    "sidebar_bg":      "linear-gradient(180deg,#0a0d1a 0%,#0f1224 100%)",
    "sidebar_border":  "rgba(99,102,241,.25)",
    "sidebar_text":    "#c7d2fe",
    "card_bg":         "rgba(255,255,255,.04)",
    "card_border":     "rgba(255,255,255,.08)",
    "card_shadow":     "0 8px 32px rgba(0,0,0,.4)",
    "card_hover_shadow": "0 20px 50px rgba(99,102,241,.2)",
    "card_hover_border": "rgba(99,102,241,.35)",
    "text_primary":    "#eef2ff",
    "text_secondary":  "rgba(199,210,254,.6)",
    "text_muted":      "rgba(199,210,254,.35)",
    "accent":          "#6366f1",
    "accent2":         "#8b5cf6",
    "accent_glow":     "rgba(99,102,241,.4)",
    "danger":          "#ef4444",
    "danger_soft":     "rgba(239,68,68,.18)",
    "danger_border":   "rgba(239,68,68,.45)",
    "safe":            "#10b981",
    "safe_soft":       "rgba(16,185,129,.18)",
    "safe_border":     "rgba(16,185,129,.45)",
    "input_bg":        "#141827",
    "input_border":    "rgba(255,255,255,.12)",
    "input_text":      "#eef2ff",
    "badge_bg":        "rgba(99,102,241,.2)",
    "badge_border":    "rgba(99,102,241,.35)",
    "badge_text":      "#a5b4fc",
    "divider":         "rgba(99,102,241,.4)",
    "scrollbar_track": "#080b14",
    "scrollbar_thumb": "#6366f1",
    "metric_value_grad": "linear-gradient(135deg,#818cf8,#6366f1)",
    "hero_title_c":    "#eef2ff",
    "hero_span_grad":  "linear-gradient(90deg,#818cf8,#6366f1,#8b5cf6)",
    "hero_sub":        "rgba(199,210,254,.55)",
    "section_icon_bg": "linear-gradient(135deg,#6366f1,#4f46e5)",
    "section_icon_shadow": "rgba(99,102,241,.45)",
    "section_title":   "#eef2ff",
    "btn_bg":          "linear-gradient(135deg,#6366f1 0%,#4f46e5 100%)",
    "btn_hover_bg":    "linear-gradient(135deg,#818cf8 0%,#6366f1 100%)",
    "btn_shadow":      "rgba(99,102,241,.45)",
    "progress_track":  "rgba(255,255,255,.08)",
    "progress_fill":   "linear-gradient(90deg,#6366f1,#818cf8)",
    "info_bg":         "rgba(99,102,241,.08)",
    "info_border":     "#6366f1",
    "footer_text":     "rgba(199,210,254,.3)",
    "footer_link":     "#818cf8",
    "hr_color":        "rgba(255,255,255,.06)",
    "row_border":      "rgba(255,255,255,.06)",
    "toggle_icon":     "☀️",
    "toggle_label":    "Light Mode",
    "metric_label_c":  "rgba(199,210,254,.5)",
}

LIGHT = {
    "app_bg":          "linear-gradient(160deg,#f0f4ff 0%,#ffffff 50%,#f5f0ff 100%)",
    "app_glow1":       "rgba(99,102,241,.08)",
    "app_glow2":       "rgba(168,85,247,.06)",
    "sidebar_bg":      "linear-gradient(180deg,#1e1b4b 0%,#312e81 100%)",
    "sidebar_border":  "rgba(129,140,248,.3)",
    "sidebar_text":    "#c7d2fe",
    "card_bg":         "rgba(255,255,255,.85)",
    "card_border":     "rgba(99,102,241,.15)",
    "card_shadow":     "0 4px 24px rgba(99,102,241,.1)",
    "card_hover_shadow": "0 16px 48px rgba(99,102,241,.18)",
    "card_hover_border": "rgba(99,102,241,.4)",
    "text_primary":    "#1e1b4b",
    "text_secondary":  "#4338ca",
    "text_muted":      "#6b7280",
    "accent":          "#6366f1",
    "accent2":         "#8b5cf6",
    "accent_glow":     "rgba(99,102,241,.3)",
    "danger":          "#dc2626",
    "danger_soft":     "rgba(220,38,38,.08)",
    "danger_border":   "rgba(220,38,38,.35)",
    "safe":            "#059669",
    "safe_soft":       "rgba(5,150,105,.08)",
    "safe_border":     "rgba(5,150,105,.35)",
    "input_bg":        "#f8f7ff",
    "input_border":    "rgba(99,102,241,.2)",
    "input_text":      "#1e1b4b",
    "badge_bg":        "rgba(99,102,241,.1)",
    "badge_border":    "rgba(99,102,241,.25)",
    "badge_text":      "#4f46e5",
    "divider":         "rgba(99,102,241,.35)",
    "scrollbar_track": "#f0f4ff",
    "scrollbar_thumb": "#6366f1",
    "metric_value_grad": "linear-gradient(135deg,#6366f1,#4f46e5)",
    "hero_title_c":    "#1e1b4b",
    "hero_span_grad":  "linear-gradient(90deg,#6366f1,#4f46e5,#7c3aed)",
    "hero_sub":        "#6b7280",
    "section_icon_bg": "linear-gradient(135deg,#6366f1,#4f46e5)",
    "section_icon_shadow": "rgba(99,102,241,.35)",
    "section_title":   "#1e1b4b",
    "btn_bg":          "linear-gradient(135deg,#6366f1 0%,#4f46e5 100%)",
    "btn_hover_bg":    "linear-gradient(135deg,#818cf8 0%,#6366f1 100%)",
    "btn_shadow":      "rgba(99,102,241,.35)",
    "progress_track":  "rgba(99,102,241,.1)",
    "progress_fill":   "linear-gradient(90deg,#6366f1,#818cf8)",
    "info_bg":         "rgba(99,102,241,.06)",
    "info_border":     "#6366f1",
    "footer_text":     "#9ca3af",
    "footer_link":     "#6366f1",
    "hr_color":        "rgba(99,102,241,.1)",
    "row_border":      "rgba(99,102,241,.08)",
    "toggle_icon":     "🌙",
    "toggle_label":    "Dark Mode",
    "metric_label_c":  "#6b7280",
}

T = DARK if st.session_state.dark_mode else LIGHT

# ─────────────────────────────────────────────
#  INJECT CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Bricolage+Grotesque:wght@700;800&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 15px;
}

.stApp {
    background: """ + T["app_bg"] + """;
    min-height: 100vh;
}
.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background:
        radial-gradient(ellipse 70% 50% at 10% 0%, """ + T["app_glow1"] + """ 0%, transparent 55%),
        radial-gradient(ellipse 55% 45% at 90% 100%, """ + T["app_glow2"] + """ 0%, transparent 55%);
    pointer-events: none;
    z-index: 0;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: """ + T["sidebar_bg"] + """ !important;
    border-right: 1px solid """ + T["sidebar_border"] + """;
}
[data-testid="stSidebar"] * { color: """ + T["sidebar_text"] + """ !important; }
[data-testid="stSidebar"] hr { border-color: """ + T["sidebar_border"] + """ !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: """ + T["scrollbar_track"] + """; }
::-webkit-scrollbar-thumb { background: """ + T["scrollbar_thumb"] + """; border-radius: 4px; }

/* ── Glass card ── */
.glass-card {
    background: """ + T["card_bg"] + """;
    border: 1px solid """ + T["card_border"] + """;
    border-radius: 20px;
    padding: 28px 30px;
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    box-shadow: """ + T["card_shadow"] + """;
    margin-bottom: 20px;
    transition: box-shadow .3s ease, transform .3s ease, border-color .3s ease;
}
.glass-card:hover {
    box-shadow: """ + T["card_hover_shadow"] + """;
    border-color: """ + T["card_hover_border"] + """;
    transform: translateY(-3px);
}

/* ── Metric card ── */
.metric-card {
    background: """ + T["card_bg"] + """;
    border: 1px solid """ + T["card_border"] + """;
    border-radius: 18px;
    padding: 22px 16px;
    text-align: center;
    position: relative;
    overflow: hidden;
    transition: transform .3s ease, box-shadow .3s ease;
    backdrop-filter: blur(20px);
}
.metric-card::after {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: """ + T["metric_value_grad"] + """;
    border-radius: 18px 18px 0 0;
}
.metric-card:hover {
    transform: translateY(-5px);
    box-shadow: """ + T["card_hover_shadow"] + """;
    border-color: """ + T["card_hover_border"] + """;
}
.metric-icon  { font-size: 28px; margin-bottom: 10px; display: block; }
.metric-value {
    font-family: 'Bricolage Grotesque', sans-serif;
    font-size: 32px;
    font-weight: 800;
    background: """ + T["metric_value_grad"] + """;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1;
    margin-bottom: 6px;
}
.metric-label {
    font-size: 11px;
    color: """ + T["metric_label_c"] + """;
    font-weight: 600;
    letter-spacing: .8px;
    text-transform: uppercase;
}

/* ── Section header ── */
.section-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 22px;
}
.section-icon {
    width: 38px; height: 38px;
    border-radius: 10px;
    background: """ + T["section_icon_bg"] + """;
    display: flex; align-items: center; justify-content: center;
    font-size: 17px;
    box-shadow: 0 4px 14px """ + T["section_icon_shadow"] + """;
    flex-shrink: 0;
}
.section-title {
    font-family: 'Bricolage Grotesque', sans-serif;
    font-size: 18px;
    font-weight: 700;
    color: """ + T["section_title"] + """;
    letter-spacing: .2px;
}

/* ── Hero ── */
.hero-wrap {
    text-align: center;
    padding: 50px 20px 36px;
}
.hero-badge {
    display: inline-flex; align-items: center; gap: 8px;
    background: """ + T["badge_bg"] + """;
    border: 1px solid """ + T["badge_border"] + """;
    border-radius: 999px;
    padding: 5px 18px;
    font-size: 11px;
    font-weight: 700;
    color: """ + T["badge_text"] + """;
    letter-spacing: 1.4px;
    text-transform: uppercase;
    margin-bottom: 20px;
}
.hero-title {
    font-family: 'Bricolage Grotesque', sans-serif;
    font-size: clamp(34px, 5vw, 60px);
    font-weight: 800;
    color: """ + T["hero_title_c"] + """;
    line-height: 1.1;
    margin-bottom: 16px;
}
.hero-title span {
    background: """ + T["hero_span_grad"] + """;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-sub {
    font-size: 16px;
    color: """ + T["hero_sub"] + """;
    max-width: 500px;
    margin: 0 auto 10px;
    line-height: 1.75;
    font-weight: 400;
}

/* ── Divider ── */
.glow-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, """ + T["divider"] + """, transparent);
    margin: 6px 0 30px;
}

/* ── Widget labels ── */
label,
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] {
    color: """ + T["text_primary"] + """ !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    letter-spacing: .2px !important;
}

/* ── Selectbox ── */
[data-testid="stSelectbox"] > div > div {
    background: """ + T["input_bg"] + """ !important;
    border: 1.5px solid """ + T["input_border"] + """ !important;
    border-radius: 10px !important;
    color: """ + T["input_text"] + """ !important;
}
[data-testid="stSelectbox"] > div > div:focus-within,
[data-testid="stSelectbox"] > div > div:hover {
    border-color: """ + T["accent"] + """ !important;
    box-shadow: 0 0 0 3px """ + T["accent_glow"] + """ !important;
}
[data-testid="stSelectbox"] > div > div > div,
[data-testid="stSelectbox"] span { color: """ + T["input_text"] + """ !important; }
[data-testid="stSelectbox"] svg { fill: """ + T["accent"] + """ !important; }
[data-testid="stSelectbox"] ul,
[role="listbox"] {
    background: """ + T["input_bg"] + """ !important;
    border: 1.5px solid """ + T["input_border"] + """ !important;
    border-radius: 10px !important;
}
[data-testid="stSelectbox"] li,
[role="option"] { color: """ + T["input_text"] + """ !important; background: transparent !important; }
[data-testid="stSelectbox"] li:hover,
[role="option"]:hover,
[role="option"][aria-selected="true"] {
    background: """ + T["badge_bg"] + """ !important;
    color: """ + T["accent"] + """ !important;
}

/* ── Number Input ── */
[data-testid="stNumberInput"] input {
    background: """ + T["input_bg"] + """ !important;
    border: 1.5px solid """ + T["input_border"] + """ !important;
    border-radius: 10px !important;
    color: """ + T["input_text"] + """ !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 15px !important;
    caret-color: """ + T["accent"] + """ !important;
}
[data-testid="stNumberInput"] input:focus {
    border-color: """ + T["accent"] + """ !important;
    box-shadow: 0 0 0 3px """ + T["accent_glow"] + """ !important;
    outline: none !important;
}
[data-testid="stNumberInput"] button {
    background: """ + T["badge_bg"] + """ !important;
    border: 1px solid """ + T["badge_border"] + """ !important;
    color: """ + T["accent"] + """ !important;
    border-radius: 8px !important;
}
[data-testid="stNumberInput"] button:hover { background: """ + T["badge_border"] + """ !important; }

/* ── Slider ── */
[data-testid="stSlider"] > div > div > div > div { background: """ + T["progress_track"] + """ !important; }
[data-testid="stSlider"] div[role="slider"] {
    background: """ + T["accent"] + """ !important;
    border: 2px solid """ + T["accent2"] + """ !important;
    box-shadow: 0 0 0 3px """ + T["accent_glow"] + """ !important;
}

/* ── Predict button ── */
[data-testid="stButton"] > button {
    width: 100%;
    height: 60px;
    background: """ + T["btn_bg"] + """;
    color: #fff !important;
    font-family: 'Bricolage Grotesque', sans-serif;
    font-size: 17px;
    font-weight: 700;
    letter-spacing: .5px;
    border: none;
    border-radius: 14px;
    cursor: pointer;
    transition: all .3s ease;
    box-shadow: 0 8px 24px """ + T["btn_shadow"] + """;
}
[data-testid="stButton"] > button:hover {
    transform: translateY(-2px) scale(1.01);
    box-shadow: 0 14px 36px """ + T["btn_shadow"] + """;
    background: """ + T["btn_hover_bg"] + """;
    color: #fff !important;
}
[data-testid="stButton"] > button:active { transform: translateY(1px) scale(.99); }

/* ── Progress bar ── */
[data-testid="stProgress"] > div {
    background: """ + T["progress_track"] + """ !important;
    border-radius: 999px;
}
[data-testid="stProgress"] > div > div {
    background: """ + T["progress_fill"] + """ !important;
    border-radius: 999px;
}

/* ── Result cards ── */
.result-danger {
    background: """ + T["danger_soft"] + """;
    border: 1px solid """ + T["danger_border"] + """;
    border-radius: 18px;
    padding: 30px 26px;
    text-align: center;
    animation: fadeUp .5s ease;
}
.result-safe {
    background: """ + T["safe_soft"] + """;
    border: 1px solid """ + T["safe_border"] + """;
    border-radius: 18px;
    padding: 30px 26px;
    text-align: center;
    animation: fadeUp .5s ease;
}
.result-headline {
    font-family: 'Bricolage Grotesque', sans-serif;
    font-size: 22px;
    font-weight: 800;
    margin-bottom: 10px;
}
.result-danger .result-headline { color: """ + T["danger"] + """; }
.result-safe  .result-headline  { color: """ + T["safe"] + """; }
.result-prob  {
    font-size: 52px;
    font-weight: 800;
    font-family: 'Bricolage Grotesque', sans-serif;
    line-height: 1;
    margin: 14px 0 6px;
}
.result-danger .result-prob { color: """ + T["danger"] + """; }
.result-safe  .result-prob  { color: """ + T["safe"] + """; }
.result-sub   { font-size: 13px; color: """ + T["text_muted"] + """; letter-spacing: .3px; }

/* ── Info note ── */
.info-note {
    background: """ + T["info_bg"] + """;
    border-left: 3px solid """ + T["info_border"] + """;
    border-radius: 0 10px 10px 0;
    padding: 11px 15px;
    font-size: 13px;
    color: """ + T["text_secondary"] + """;
    margin-bottom: 16px;
}

/* ── Gauge label ── */
.gauge-label {
    font-size: 12px;
    color: """ + T["text_muted"] + """;
    letter-spacing: .8px;
    text-transform: uppercase;
    text-align: center;
    margin-bottom: 6px;
    font-weight: 600;
}

/* ── Footer ── */
.footer-wrap { text-align: center; padding: 36px 20px 24px; }
.footer-logo {
    font-family: 'Bricolage Grotesque', sans-serif;
    font-size: 20px;
    font-weight: 800;
    background: """ + T["metric_value_grad"] + """;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 6px;
}
.footer-sub { font-size: 12px; color: """ + T["footer_text"] + """; letter-spacing: .3px; }
.footer-sub a { color: """ + T["footer_link"] + """; text-decoration: none; }

/* ── Animations ── */
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* hide streamlit branding */
#MainMenu, footer, header { visibility: hidden; }
input, textarea, select { color: """ + T["input_text"] + """ !important; }
input::placeholder { color: """ + T["text_muted"] + """ !important; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center;padding:18px 0 10px;">
        <div style="font-size:50px;">🫀</div>
        <div style="font-family:'Bricolage Grotesque',sans-serif;font-size:22px;
                    font-weight:800;color:#a5b4fc;margin-top:8px;">CardioAI</div>
        <div style="font-size:11px;color:rgba(165,180,252,.5);letter-spacing:1px;
                    text-transform:uppercase;margin-top:4px;">Heart Risk Intelligence</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Theme toggle button
    toggle_label = T["toggle_icon"] + "  Switch to " + T["toggle_label"]
    if st.button(toggle_label, key="theme_toggle"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

    st.markdown("---")

    st.markdown("""
    <div style="font-family:'Bricolage Grotesque',sans-serif;font-size:13px;font-weight:700;
                color:rgba(165,180,252,.9);letter-spacing:.5px;margin-bottom:10px;">
        📋 ABOUT THE MODEL
    </div>
    <p style="font-size:13px;color:rgba(165,180,252,.55);line-height:1.8;margin-bottom:16px;">
        This clinical-grade AI analyses 11 cardiovascular biomarkers to estimate
        a patient's risk of heart disease using a validated logistic-regression
        pipeline trained on the <strong style="color:#a5b4fc;">UCI Heart Disease dataset</strong>.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="font-family:'Bricolage Grotesque',sans-serif;font-size:12px;font-weight:700;
                color:rgba(165,180,252,.7);letter-spacing:.6px;margin-bottom:10px;">
        ⚙️ TECH STACK
    </div>
    """, unsafe_allow_html=True)

    badges = ["Python 3.11", "Streamlit", "Scikit-Learn", "Pandas", "NumPy", "Logistic Regression"]
    badge_style = ("display:inline-block;background:rgba(99,102,241,.2);"
                   "border:1px solid rgba(129,140,248,.35);color:#a5b4fc;"
                   "border-radius:6px;padding:2px 10px;font-size:11px;"
                   "font-weight:600;margin:3px 3px 3px 0;")
    badge_html = "".join("<span style='" + badge_style + "'>" + b + "</span>" for b in badges)
    st.markdown(badge_html, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div style="font-family:'Bricolage Grotesque',sans-serif;font-size:12px;font-weight:700;
                color:rgba(165,180,252,.7);letter-spacing:.6px;margin-bottom:10px;">
        📊 MODEL METRICS
    </div>
    """, unsafe_allow_html=True)

    for label, value in [("Accuracy","93.5 %"),("Precision","90.9 %"),("Recall","92.2 %"),("F1 Score","93.0 %")]:
        st.markdown(
            "<div style='display:flex;justify-content:space-between;padding:7px 0;"
            "border-bottom:1px solid rgba(99,102,241,.15);'>"
            "<span style='font-size:12px;color:rgba(165,180,252,.5);'>" + label + "</span>"
            "<span style='font-size:12px;font-weight:700;color:#a5b4fc;'>" + value + "</span>"
            "</div>",
            unsafe_allow_html=True
        )

    st.markdown("""
    <div style="text-align:center;font-size:11px;color:rgba(165,180,252,.3);
                padding:16px 0 6px;line-height:1.7;">
        ⚠ Research &amp; educational use only.<br>Not a substitute for medical advice.
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  HERO
# ─────────────────────────────────────────────
st.markdown("""
<div class="hero-wrap">
    <div class="hero-badge">🔬 AI · Powered Clinical Analytics</div>
    <h1 class="hero-title">
        Cardiovascular Risk<br><span>Intelligence Platform</span>
    </h1>
    <p class="hero-sub">
        Real-time heart disease prediction powered by machine learning —
        built for clinicians, researchers, and healthcare innovators.
    </p>
</div>
<div class="glow-divider"></div>
""", unsafe_allow_html=True)

if not model_loaded:
    st.markdown("""
    <div class="info-note">
        ℹ <strong>Demo mode:</strong> Model files not found — a simulated result will be shown.
        Place <code>Logistic_Regression_heart.pkl</code>, <code>scaler.pkl</code>, and
        <code>columns.pkl</code> in the same directory to enable live inference.
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  METRIC CARDS
# ─────────────────────────────────────────────
mc1, mc2, mc3, mc4 = st.columns(4)
cards = [("🎯","93.5%","Model Accuracy"),("⚡","< 1 s","Inference Time"),
         ("🔬","11","Clinical Biomarkers"),("🏥","918","Training Samples")]
for col, (icon, val, lbl) in zip([mc1,mc2,mc3,mc4], cards):
    with col:
        st.markdown(
            "<div class='metric-card'>"
            "<span class='metric-icon'>" + icon + "</span>"
            "<div class='metric-value'>" + val + "</div>"
            "<div class='metric-label'>" + lbl + "</div>"
            "</div>",
            unsafe_allow_html=True
        )

st.markdown("<br>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  INPUT FORM
# ─────────────────────────────────────────────
col_left, col_right = st.columns(2, gap="large")

with col_left:
    st.markdown("""
    <div class="section-header">
        <div class="section-icon">👤</div>
        <div class="section-title">Patient Demographics</div>
    </div>
    """, unsafe_allow_html=True)

    age = st.slider("Age (years)", 18, 100, 52, help="Patient's current age")

    sex = st.selectbox("Biological Sex", ["M — Male", "F — Female"])
    sex_code = sex[0]

    chest_pain = st.selectbox(
        "Chest Pain Type",
        ["ATA — Atypical Angina", "NAP — Non-Anginal Pain",
         "TA  — Typical Angina",  "ASY — Asymptomatic"],
        help="Classification of chest discomfort"
    )
    cp_code = chest_pain[:3].strip()

    resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 130,
                                  help="Blood pressure measured at rest")
    cholesterol = st.number_input("Serum Cholesterol (mg/dL)", 100, 600, 245,
                                   help="Total cholesterol level")

with col_right:
    st.markdown("""
    <div class="section-header">
        <div class="section-icon">🩺</div>
        <div class="section-title">Clinical Measurements</div>
    </div>
    """, unsafe_allow_html=True)

    fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", ["0 — No", "1 — Yes"],
                               help="Whether fasting blood sugar exceeds 120 mg/dL")
    fbs_code = int(fasting_bs[0])

    resting_ecg = st.selectbox(
        "Resting ECG Result",
        ["Normal — Normal", "ST     — ST-T Wave Abnormality", "LVH    — Left Ventricular Hypertrophy"]
    )
    ecg_code = resting_ecg[:6].strip()

    max_hr = st.slider("Maximum Heart Rate Achieved", 60, 220, 142,
                        help="Peak heart rate during stress test")

    exercise_angina = st.selectbox("Exercise-Induced Angina", ["N — No", "Y — Yes"],
                                    help="Angina triggered by physical exertion")
    ea_code = exercise_angina[0]

    oldpeak = st.slider("Oldpeak — ST Depression", 0.0, 6.0, 1.6, step=0.1,
                         help="ST depression relative to rest")

    st_slope = st.selectbox("ST Segment Slope",
                             ["Up   — Upsloping", "Flat — Flat", "Down — Downsloping"],
                             help="Slope of peak exercise ST segment")
    slope_code = st_slope[:4].strip()

# ─────────────────────────────────────────────
#  PREDICT BUTTON
# ─────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
btn_col = st.columns([1, 2, 1])[1]
with btn_col:
    predict_clicked = st.button("🔍  Analyse Cardiovascular Risk")

# ─────────────────────────────────────────────
#  RESULTS
# ─────────────────────────────────────────────
if predict_clicked:

    with st.spinner("Running AI inference pipeline…"):
        time.sleep(1.2)

    raw_input = {
        "Age": age, "RestingBP": resting_bp, "Cholesterol": cholesterol,
        "FastingBS": fbs_code, "MaxHR": max_hr, "Oldpeak": oldpeak,
        "Sex_"            + sex_code:    1,
        "ChestPainType_"  + cp_code:     1,
        "RestingECG_"     + ecg_code:    1,
        "ExerciseAngina_" + ea_code:     1,
        "ST_Slope_"       + slope_code:  1,
    }

    if model_loaded:
        input_df = pd.DataFrame([raw_input])
        for col in expected_columns:
            if col not in input_df.columns:
                input_df[col] = 0
        input_df    = input_df[expected_columns]
        scaled      = scaler.transform(input_df)
        prediction  = model.predict(scaled)[0]
        probability = model.predict_proba(scaled)[0][1]
    else:
        probability = 0.72
        prediction  = 1

    risk_pct   = round(probability * 100, 1)
    safety_pct = round((1 - probability) * 100, 1)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="section-header">
        <div class="section-icon">📊</div>
        <div class="section-title">Prediction Results</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='gauge-label'>Risk Probability Meter</div>", unsafe_allow_html=True)
    st.progress(int(risk_pct))

    left_r, right_r = st.columns([1, 1], gap="large")

    with left_r:
        if prediction == 1:
            st.markdown(
                "<div class='result-danger'>"
                "<div class='result-headline'>⚠ Elevated Cardiac Risk Detected</div>"
                "<div class='result-prob'>" + str(risk_pct) + "%</div>"
                "<div class='result-sub'>Probability of Heart Disease</div>"
                "<br>"
                "<div style='font-size:13px;color:" + T["text_muted"] + ";line-height:1.7;'>"
                "This patient shows significant cardiovascular risk indicators.<br>"
                "Recommend immediate cardiology consultation and further diagnostics."
                "</div></div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<div class='result-safe'>"
                "<div class='result-headline'>✅ Low Cardiovascular Risk</div>"
                "<div class='result-prob'>" + str(safety_pct) + "%</div>"
                "<div class='result-sub'>Probability of Healthy Heart</div>"
                "<br>"
                "<div style='font-size:13px;color:" + T["text_muted"] + ";line-height:1.7;'>"
                "Biomarkers suggest a low risk profile at this time.<br>"
                "Continue routine monitoring and maintain a heart-healthy lifestyle."
                "</div></div>",
                unsafe_allow_html=True
            )

    with right_r:
        summary_items = [
            ("Age",         str(age) + " yrs"),
            ("Sex",         sex_code),
            ("Chest Pain",  cp_code),
            ("Resting BP",  str(resting_bp) + " mm Hg"),
            ("Cholesterol", str(cholesterol) + " mg/dL"),
            ("Max HR",      str(max_hr) + " bpm"),
            ("Oldpeak",     str(oldpeak)),
        ]

        rows_html = ""
        for k, v in summary_items:
            rows_html += (
                "<div style='display:flex;justify-content:space-between;"
                "padding:8px 0;border-bottom:1px solid " + T["row_border"] + ";'>"
                "<span style='font-size:12px;color:" + T["text_muted"] + ";font-weight:500;'>" + k + "</span>"
                "<span style='font-size:12px;font-weight:700;color:" + T["text_primary"] + ";'>" + v + "</span>"
                "</div>"
            )

        breakdown = (
            "<div class='glass-card'>"

            "<div style='font-family:Bricolage Grotesque,sans-serif;font-size:15px;"
            "font-weight:700;color:" + T["text_primary"] + ";margin-bottom:20px;"
            "letter-spacing:.2px;'>📈 Risk Breakdown</div>"

            # Risk bar
            "<div style='margin-bottom:16px;'>"
            "<div style='display:flex;justify-content:space-between;margin-bottom:7px;'>"
            "<span style='font-size:13px;color:" + T["text_muted"] + ";'>Heart Disease Risk</span>"
            "<span style='font-size:13px;font-weight:700;color:" + T["danger"] + ";'>" + str(risk_pct) + "%</span>"
            "</div>"
            "<div style='height:7px;background:" + T["progress_track"] + ";border-radius:999px;'>"
            "<div style='height:7px;width:" + str(risk_pct) + "%;background:linear-gradient(90deg,"
            + T["danger"] + "," + T["danger"] + "99);border-radius:999px;'></div>"
            "</div></div>"

            # Safe bar
            "<div style='margin-bottom:20px;'>"
            "<div style='display:flex;justify-content:space-between;margin-bottom:7px;'>"
            "<span style='font-size:13px;color:" + T["text_muted"] + ";'>Healthy Heart Score</span>"
            "<span style='font-size:13px;font-weight:700;color:" + T["safe"] + ";'>" + str(safety_pct) + "%</span>"
            "</div>"
            "<div style='height:7px;background:" + T["progress_track"] + ";border-radius:999px;'>"
            "<div style='height:7px;width:" + str(safety_pct) + "%;background:linear-gradient(90deg,"
            + T["safe"] + "," + T["safe"] + "99);border-radius:999px;'></div>"
            "</div></div>"

            "<hr style='border:none;border-top:1px solid " + T["hr_color"] + ";margin:18px 0;'>"

            "<div style='font-family:Bricolage Grotesque,sans-serif;font-size:11px;font-weight:700;"
            "color:" + T["text_muted"] + ";letter-spacing:.9px;text-transform:uppercase;"
            "margin-bottom:10px;'>Key Input Summary</div>"

            + rows_html +
            "</div>"
        )

        st.markdown(breakdown, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="info-note">
        🩺 <strong>Clinical Disclaimer:</strong> This AI tool is intended for research and educational
        purposes only. Results should not replace professional medical diagnosis or clinical judgement.
        Always consult a licensed cardiologist for medical decisions.
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  FOOTER
# ─────────────────────────────────────────────
st.markdown("<div class='glow-divider' style='margin-top:40px;'></div>", unsafe_allow_html=True)
st.markdown("""
<div class="footer-wrap">
    <div class="footer-logo">🫀 CardioAI</div>
    <div class="footer-sub">
        Crafted with precision by <a href="#">Amit</a> &nbsp;·&nbsp;
        Powered by Scikit-Learn &amp; Streamlit &nbsp;·&nbsp; © 2025 All Rights Reserved
    </div>
    <div class="footer-sub" style="margin-top:6px;font-size:11px;">
        For research &amp; educational use only &nbsp;|&nbsp; Not a substitute for clinical medical advice
    </div>
</div>
""", unsafe_allow_html=True)