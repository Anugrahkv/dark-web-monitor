# Dark Web & Threat Actor Monitor (HUMINT)

## Overview
This Python-based Threat Intelligence tool automates the monitoring of Dark Web (Tor) ransomware leak sites. It acts as an early-warning system to detect if a specific target organization has been compromised and listed by ransomware syndicates.

Additionally, the tool tracks general Threat Actor activity (HUMINT), extracting the latest victims claimed by notorious groups (e.g., RagnarLocker, Lorenz, LockBit) to maintain situational awareness of the evolving threat landscape.

## Features
* **Automated Data parsing:** Pulls and parses aggregated JSON feeds of dark web posts without requiring a direct, unproxied connection to the Tor network.
* **Targeted Breach Hunting:** Iterates through thousands of recent leaks to identify specific organizational targets, facilitating rapid incident response.
* **HUMINT Tracking:** Extracts and logs the most recent victims and the associated Threat Actor groups claiming responsibility.

## How to Run
1. Clone this repository.
2. Install the required libraries: `pip install requests`
3. Update the `TARGET_COMPANY` variable in the script with the organization you are monitoring.
4. Run the script: `python dark_web_monitor.py`

*Disclaimer: This tool consumes publicly aggregated OSINT data for defensive Threat Intelligence and educational purposes only.*
