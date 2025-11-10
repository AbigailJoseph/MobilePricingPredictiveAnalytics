import streamlit as st
import requests

st.title("📱 Mobile Price Range Predictor")
st.write("Enter the phone specifications below to predict the price category.")

# Input fields
battery_power = st.number_input("Battery Power", min_value=500, max_value=5000, value=1500)
blue = st.selectbox("Bluetooth", [0,1])
clock_speed = st.number_input("Clock Speed (GHz)", min_value=0.5, max_value=3.5, value=2.0)
dual_sim = st.selectbox("Dual SIM", [0,1])
fc = st.number_input("Front Camera (MP)", min_value=0, max_value=20, value=5)
four_g = st.selectbox("4G", [0,1])
int_memory = st.number_input("Internal Memory (GB)", min_value=2, max_value=256, value=16)
m_dep = st.number_input("Mobile Depth (cm)", min_value=0.0, max_value=1.0, value=0.5)
mobile_wt = st.number_input("Weight (g)", min_value=50, max_value=250, value=150)
n_cores = st.number_input("Number of CPU Cores", min_value=1, max_value=8, value=4)
pc = st.number_input("Primary Camera (MP)", min_value=0, max_value=25, value=8)
px_height = st.number_input("Pixel Height", min_value=0, max_value=2000, value=800)
px_width = st.number_input("Pixel Width", min_value=0, max_value=2000, value=1280)
ram = st.number_input("RAM (MB)", min_value=256, max_value=8000, value=3000)
sc_h = st.number_input("Screen Height", min_value=1, max_value=20, value=13)
sc_w = st.number_input("Screen Width", min_value=1, max_value=20, value=7)
talk_time = st.number_input("Talk Time (hrs)", min_value=1, max_value=20, value=10)
three_g = st.selectbox("3G", [0,1])
touch_screen = st.selectbox("Touch Screen", [0,1])
wifi = st.selectbox("WiFi", [0,1])

if st.button("Predict Price Range"):
    data = {
        "battery_power": battery_power,
        "blue": blue,
        "clock_speed": clock_speed,
        "dual_sim": dual_sim,
        "fc": fc,
        "four_g": four_g,
        "int_memory": int_memory,
        "m_dep": m_dep,
        "mobile_wt": mobile_wt,
        "n_cores": n_cores,
        "pc": pc,
        "px_height": px_height,
        "px_width": px_width,
        "ram": ram,
        "sc_h": sc_h,
        "sc_w": sc_w,
        "talk_time": talk_time,
        "three_g": three_g,
        "touch_screen": touch_screen,
        "wifi": wifi
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=data)
    
    if response.status_code == 200:
        result = response.json()["predicted_price_range"]
        st.success(f"📊 Predicted Price Category: **{result}** (0=Low, 1=Medium, 2=High, 3=Premium)")
    else:
        st.error("Error: Could not get prediction from API.")