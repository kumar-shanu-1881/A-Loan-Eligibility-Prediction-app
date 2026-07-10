import threading
import time
import requests
import streamlit as st

API_URL = "https://loan-api-iuqc.onrender.com"


class ApiWakeState:
    def __init__(self):
        self.awake = False


def wake_url(state, url=API_URL, max_wait=120, retry_every=3):
    """Runs in a background thread. Keeps retrying until the API responds."""
    start = time.time()
    while time.time() - start < max_wait:
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code < 500:
                state.awake = True
                return
        except requests.exceptions.RequestException:
            pass
        time.sleep(retry_every)


@st.cache_resource
def start_api_wakeup():
    """Runs once per container. Starts the wake-up thread and returns instantly."""
    state = ApiWakeState()
    threading.Thread(target=wake_url, args=(state,), daemon=True).start()
    return state


api_state = start_api_wakeup()


def ensure_api_awake(max_wait=60):
    """Call before sending the real /predict request."""
    if api_state.awake:
        return True
    start = time.time()
    with st.spinner("Waking up prediction service..."):
        while time.time() - start < max_wait:
            if api_state.awake:
                return True
            time.sleep(1)
    return False