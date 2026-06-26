import subprocess
import sys
import time
import os

def main():
    print("🚀 Starting Microservices Architecture...\n")

    # Start Flask Backend
    print("⚙️ Booting up Flask API (Backend)...")
    flask_process = subprocess.Popen([sys.executable, "app/api.py"])

    # Give Flask 2 seconds to fully start up before launching the frontend
    time.sleep(2)

    render_port = os.getenv("PORT", "8501")

    # Start the Streamlit Frontend
    print("🖥️ Booting up Streamlit Dashboard (Frontend)...")
    streamlit_process = subprocess.Popen([sys.executable, "-m", "streamlit", "run", "app/app.py",
                                          "--server.port", render_port,
        "--server.address", "0.0.0.0"])

    # Keep the script running and handle shutdowns gracefully
    try:
        flask_process.wait()
        streamlit_process.wait()
    except KeyboardInterrupt:
        print("\n\n🛑 Keyboard Interrupt detected! Shutting down all servers...")
        flask_process.terminate()
        streamlit_process.terminate()
        print("✅ Servers successfully shut down.")

if __name__ == '__main__':
    main()