import requests
import time 

def wake_url():
    max_wait=120
    retry_every=3
    url = "https://loan-api-iuqc.onrender.com"
    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/json,*/*;q=0.8",
    }
    print(f"Waking up: {url}")
    start = time.time()
    attempt = 0
 
    while time.time() - start < max_wait:
        attempt += 1
        try:
            resp = requests.get(url, headers=HEADERS, timeout=10)
            elapsed = round(time.time() - start, 1)
            print(f"  Attempt {attempt}: status {resp.status_code} (after {elapsed}s)")
            if resp.status_code < 500:
                # Any non-server-error response means the service is up
                print(f"Service is awake after {elapsed}s.")
                return True
        except requests.exceptions.RequestException as e:
            elapsed = round(time.time() - start, 1)
            print(f"  Attempt {attempt}: not reachable yet ({e.__class__.__name__}) after {elapsed}s")
 
        time.sleep(retry_every)
 
    print(f"Gave up after {max_wait}s — service did not wake up in time.")
    return False
 
 
if __name__ == "__main__":
    wake_url()
 