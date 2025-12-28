# 🐼 Geo-Panda-Toolkit

A lightweight, open-source toolkit designed for correlating image metadata (EXIF) with geographical data points. This tool helps researchers identify where a photo was taken and maps it using public APIs.

> **Status:** Work in Progress. Experimental version.

## Features
* Automated EXIF extraction.
* Support for Google Maps and OpenStreetMap API.
* Batch processing for directory-wide analysis.

## Repository Structure
* `main.py` - The **main** execution engine for metadata correlation, coordinate mapping, and API integration. **This file is crucial!**
* `requirements.txt` - Configuration file containing all Python dependencies needed to run the toolkit.
  
## Installation
1. Clone the repo:
   `git clone https://github.com/dark-panda-99/Geo-Panda-Toolkit.git`
2. Install dependencies:
   `pip install -r requirements.txt`

## Usage
Run the main script with the path to your image directory:
`python main.py --dir ./evidence/`

---

## Author & Contributions
I am **Li**, a security researcher and photography enthusiast based in **Beijing, China**. 

I started this project to help the OSINT community better understand visual attribution. If you find bugs, want to collaborate, or have questions about the tool, feel free to reach out!

---
*Disclaimer: This tool is for educational and authorized research purposes only.*
