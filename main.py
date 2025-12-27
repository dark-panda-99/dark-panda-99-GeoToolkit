import os
import sys

# Geo-Panda Toolkit v0.1-alpha
# Author: dark_panda_99

def extract_metadata(image_path):
    print(f"[+] Analyzing: {image_path}")
    # TODO: Integration with internal mapping API
    pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <image_directory>")
    else:
        print("Initializing Geo-Panda...")
        # 🚩 BONUS FLAG HIDDEN BELOW 🚩
        # TODO: Remember to reset the password for the 
        # internal staging server: dev-panda-staging.beijing.io