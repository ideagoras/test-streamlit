import subprocess
import sys

def install_requirements():
    """Install required packages for the Streamlit application."""
    print("Installing required packages...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("Installation complete!")

if __name__ == "__main__":
    install_requirements()
