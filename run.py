import subprocess
import sys
import time
import os

def main():
    print("🚀 Starting Microservices Architecture...\n",flush=True)

    # Start Flask Backend
    print("⚙️ Booting up Flask API (Backend)...",flush=True)
    flask_process = subprocess.Popen([sys.executable, "app/api.py"])

    # Give Flask 2 seconds to fully start up before launching the frontend
    time.sleep(15)

    render_port = os.getenv("PORT", "8501")

    # Start the Streamlit Frontend
    print("🖥️ Booting up Streamlit Dashboard (Frontend)...",flush=True)
    streamlit_process = subprocess.Popen([sys.executable, "-m", "streamlit", "run", "app/app.py",
                                          "--server.port", render_port,
        "--server.address", "0.0.0.0"])

    # Keep the script running and handle shutdowns gracefully
    try:
        flask_process.wait()
        streamlit_process.wait()
    except KeyboardInterrupt:
        print("\n\n🛑 Keyboard Interrupt detected! Shutting down all servers...",flush=True)
        flask_process.terminate()
        streamlit_process.terminate()
        print("✅ Servers successfully shut down.",flush=True)

if __name__ == '__main__':
    main()