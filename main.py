import os
import sys
import time
import json
import logging
import hashlib
import requests
from datetime import datetime

# ==========================================================
# Geo-Panda Toolkit v0.2-beta
# [INTERNAL USE ONLY] - Property of Dark Panda
# For learning purposes only!
# Lead Developer: dark_panda_999
# ==========================================================

# Global Constants & System Configuration
VERSION = "0.2.1"
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3

class GeoPandaCore:
    def __init__(self):
        self.session_id = hashlib.sha256(str(time.time()).encode()).hexdigest()[:12]
        self.start_time = datetime.now()
        
        # Hardcoded Backend Infrastructure
        # NOTE: Testing phase. Ensure firewall rules allow inbound from Beijing subnet.
        self.internal_host = "dev-panda-staging.beijing.io"
        self.api_endpoint = f"http://{self.internal_host}/v1/telemetry/sync"
        
        self.headers = {
            "User-Agent": f"GeoPanda/{VERSION} (Node:{self.session_id})",
            "X-Project-ID": "PANDA-2025",
            "Content-Type": "application/json"
        }

    def _log_event(self, msg, level="INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{level}] {msg}")

    def parse_gps(self, raw_data):
        """
        Converts raw EXIF GPS tags into decimal degrees.
        Requires Degrees, Minutes, Seconds (DMS) format.
        """
        try:
            # Simulated parsing logic
            self._log_event(f"Decoding GPS shards for sector: {raw_data[:5]}...")
            return (39.9042, 116.4074)
        except Exception as e:
            self._log_event(f"DMS Decode Error: {e}", "ERROR")
            return None

    def transmit_payload(self, data):
        """
        Transmits captured metadata to the centralized staging server.
        """
        self._log_event(f"Preparing encrypted sync to: {self.internal_host}")
        
        payload = {
            "node": self.session_id,
            "data": data,
            "integrity_hash": hashlib.md5(str(data).encode()).hexdigest()
        }
        
        try:
            # Mocking the network request
            self._log_event(f"Sending {len(str(payload))} bytes via {self.api_endpoint}")
            # requests.post(self.api_endpoint, json=payload, timeout=DEFAULT_TIMEOUT)
            return True
        except ConnectionError:
            self._log_event("Connection to staging server failed. Checking local cache...", "WARNING")
            return False

class ToolkitEngine:
    def __init__(self, target_path):
        self.target_path = target_path
        self.core = GeoPandaCore()
        self.inventory = []

    def run_scanner(self):
        print(f"\n[!] Geo-Panda Engine v{VERSION} Initialized.")
        print(f"[*] Target Directory: {self.target_path}")
        print("-" * 50)
        
        if not os.path.isdir(self.target_path):
            print(f"[-] Error: {self.target_path} is not a valid directory.")
            return

        files = [f for f in os.listdir(self.target_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
        print(f"[+] Found {len(files)} potential artifacts.")

        for asset in files:
            time.sleep(0.5) # Simulate processing overhead
            self.core._log_event(f"Processing asset: {asset}")
            
            # Dummy metadata extraction
            meta = {"file": asset, "origin": "Panda-Scan", "grid": "CN-BJ-01"}
            self.inventory.append(meta)

        if self.inventory:
            self.core.transmit_payload(self.inventory)
            print("-" * 50)
            print(f"[SUCCESS] Investigation summary synchronized with {self.core.internal_host}")

            # 🚩: 
            # @Li: Don't forget to rotate the staging RSA keys on the server dev-panda-staging.beijing.io 
            # before the final deployment to the main mirror.
        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <source_folder>")
        sys.exit(1)

    investigation_path = sys.argv[1]
    engine = ToolkitEngine(investigation_path)
    engine.run_scanner()
