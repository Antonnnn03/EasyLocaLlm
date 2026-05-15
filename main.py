from backend.ollama import start_ollama, wait_ready
from ui import start_ui


def main():
    proc, port = start_ollama()

    if not port:
        print("Ollama failed")
        return

    wait_ready(port)

    start_ui(port, proc)


if __name__ == "__main__":
    main()