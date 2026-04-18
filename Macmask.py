import subprocess

def mask():
    # Definisco l'interfaccia come variabile così è facile da cambiare in futuro
    interface = "wlan0"
    
    try:
        subprocess.run(["sudo", "ip", "link", "set", interface, "down"], check=True)
        subprocess.run(["sudo", "macchanger", "-r", interface], check=True)
        subprocess.run(["sudo", "ip", "link", "set", interface, "up"], check=True)

        print(f"MAC Address changed for {interface}. You are now a ghost! 👻")
    except subprocess.CalledProcessError as e:
        print(f"Error during execution: {e}")

if __name__ == "__main__":
    mask()
