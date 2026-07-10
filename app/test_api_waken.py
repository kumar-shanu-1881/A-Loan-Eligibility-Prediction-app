import time
import requests

API_URL = "https://loan-api-iuqc.onrender.com"

MAX_WAIT = 120      # seconds
RETRY_EVERY = 3     # seconds

def wake_api():
    print("🚀 Trying to wake the Render service...\n")

    start = time.time()

    while time.time() - start < MAX_WAIT:

        try:
            print("📡 Sending request...")
            response = requests.get(API_URL, timeout=30)

            print(f"Status Code: {response.status_code}")

            if response.status_code == 200:
                print("\n✅ API is awake!")
                print("Response:")
                print(response.text)
                return True

        except requests.exceptions.RequestException as e:
            print(f"❌ {e}")

        print(f"⏳ Waiting {RETRY_EVERY} seconds...\n")
        time.sleep(RETRY_EVERY)

    print("\n❌ API did not wake within the time limit.")
    return False


if __name__ == "__main__":
    wake_api()