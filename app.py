import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="OrbitalWatch AI",
    page_icon="🛰️",
    layout="centered"
)

st.title("OrbitalWatch AI")
st.subheader("Classificação de risco de focos de calor")

st.write(
    "Este aplicativo usa o modelo treinado no notebook para classificar "
    "o risco de um foco de calor detectado por satélite. "

)

st.write(
    "Preencha os dados abaixo e siga com a classificação dos riscos"
)

modelo_salvo = joblib.load("orbitalwatch_model.joblib")

modelo = modelo_salvo["model"]
features = modelo_salvo["features"]

st.markdown("### Dados do foco de calor")

entrada = {}

for feature in features:
    if feature == "latitude":
        entrada[feature] = st.number_input("Latitude", value=-3.10)
    elif feature == "longitude":
        entrada[feature] = st.number_input("Longitude", value=-60.00)
    elif feature == "temperatura_brilho_principal":
        entrada[feature] = st.number_input("Temperatura de brilho principal", value=330.0)
    elif feature == "temperatura_brilho_secundaria":
        entrada[feature] = st.number_input("Temperatura de brilho secundária", value=290.0)
    elif feature == "scan":
        entrada[feature] = st.number_input("Scan", value=0.5)
    elif feature == "track":
        entrada[feature] = st.number_input("Track", value=0.5)
    elif feature == "frp":
        entrada[feature] = st.number_input("FRP - Fire Radiative Power", value=25.0)
    elif feature == "confianca_deteccao":
        entrada[feature] = st.selectbox("Confiança da detecção", [0, 1, 2], index=1)
    elif feature == "periodo_dia_noite":
        entrada[feature] = st.selectbox("Período", [0, 1], format_func=lambda x: "Dia" if x == 0 else "Noite")
    elif feature == "codigo_instrumento":
        entrada[feature] = st.number_input("Código do instrumento", value=0)
    elif feature == "codigo_satelite":
        entrada[feature] = st.number_input("Código do satélite", value=0)
    else:
        entrada[feature] = st.number_input(feature, value=0.0)

if st.button("Classificar risco"):
    dados = pd.DataFrame([entrada])[features]

    predicao = modelo.predict(dados)[0]

    st.success(f"Risco classificado: {predicao}")

    if hasattr(modelo, "predict_proba"):
        probabilidades = modelo.predict_proba(dados)[0]

        st.markdown("### Probabilidades por classe")
        resultado = pd.DataFrame({
            "classe": modelo.classes_,
            "probabilidade": probabilidades
        })

        st.dataframe(resultado)