import subprocess
import time
import requests


def start_ollama():
    proc = subprocess.Popen(
        ["bash", "./app/start_ollama.sh"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    url = "http://127.0.0.1:11434/api/tags"

    for _ in range(50):
        try:
            requests.get(url, timeout=0.5)
            print("Ollama OK")
            return proc, "11434"
        except:
            time.sleep(0.2)

    print("Ollama FAIL")
    return None, None


def wait_ready(port):
    url = f"http://127.0.0.1:{port}/api/tags"

    for _ in range(50):
        try:
            requests.get(url, timeout=1)
            print("Ollama API ready")
            return True
        except:
            time.sleep(0.2)


def stop_ollama(proc):
    if proc:
        proc.terminate()
        proc.wait()