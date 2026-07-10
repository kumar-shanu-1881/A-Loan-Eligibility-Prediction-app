import threading
import time
import requests
import streamlit as st

API_URL = "https://loan-api-iuqc.onrender.com"


class ApiWakeState:
    def __init__(self):
        self.awake = False


def wake_url(state):
    """
    Keep pinging the API until it wakes up.
    Runs in a background thread.
    """

    while True:
        try:
            response = requests.get(API_URL, timeout=30)

            if response.status_code == 200:
                state.awake = True
                return

        except requests.exceptions.RequestException:
            pass

        time.sleep(5)


@st.cache_resource
def start_api_wakeup():
    state = ApiWakeState()

    threading.Thread(
        target=wake_url,
        args=(state,),
        daemon=True
    ).start()

    return state


api_state = start_api_wakeup()


def ensure_api_awake(timeout=90):
    """
    Wait until API becomes available.
    Returns True if awake, False otherwise.
    """

    if api_state.awake:
        return True

    start = time.time()

    with st.spinner("☁️ Waking cloud prediction service...\nPlease wait 20-60 seconds..."):

        while time.time() - start < timeout:

            if api_state.awake:
                return True

            time.sleep(1)

    return False