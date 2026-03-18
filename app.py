import streamlit as st

# Streamlit handles the 'index' and 'routing' automatically
st.title("Iris Flower Predictor")

# Instead of index.html, you build the UI here
st.write("Welcome to the predictor! Use the sidebar to enter values.")

# Add your prediction logic here...

import os  # Fixed: 'import os' must be on its own line
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # This works on Render/Railway, but NOT on Streamlit Cloud
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
