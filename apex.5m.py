#!/usr/bin/env python3

# <xbar.title>Apex Reef Tank Monitor</xbar.title>
# <xbar.version>v1.0</xbar.version>
# <xbar.author>Steve Black</xbar.author>
# <xbar.author.github>steveblack</xbar.author.github>
# <xbar.desc>Display real-time temperature, pH, and salinity from your Neptune Apex aquarium controller</xbar.desc>
# <xbar.image>https://raw.githubusercontent.com/USERNAME/apex-menubar/main/screenshot.png</xbar.image>
# <xbar.dependencies>python3</xbar.dependencies>
# <xbar.abouturl>https://github.com/USERNAME/apex-menubar</xbar.abouturl>

"""
Apex Reef Tank Monitor - xbar/SwiftBar Plugin

Displays real-time temperature, pH, and salinity from your local Neptune Apex
controller in the macOS menu bar.

Works out of the box - no configuration needed.
Your Apex just needs to be on the same network.
"""

import json
import urllib.request
import urllib.error

APEX_URL = "http://apex.local/cgi-bin/status.json"
APEX_FUSION_URL = "https://apexfusion.com"


def fetch_status() -> dict:
    """Fetch current status from Apex controller."""
    try:
        with urllib.request.urlopen(APEX_URL, timeout=10) as response:
            return json.loads(response.read().decode())
    except urllib.error.URLError:
        return {"error": "Cannot connect to apex.local"}
    except json.JSONDecodeError:
        return {"error": "Invalid response from Apex"}
    except Exception as e:
        return {"error": str(e)}


def get_probe_value(status: dict, name: str) -> float | None:
    """Extract probe value by name from status JSON."""
    try:
        inputs = status.get("istat", {}).get("inputs", [])
        for probe in inputs:
            if probe.get("name") == name:
                return probe.get("value")
    except (KeyError, TypeError):
        pass
    return None


def main():
    status = fetch_status()

    # Handle errors
    if "error" in status:
        print("⚠️ Apex")
        print("---")
        print(status["error"])
        print("---")
        print("Refresh | refresh=true")
        print(f"Open Apex Fusion | href={APEX_FUSION_URL}")
        return

    # Extract sensor values
    temp = get_probe_value(status, "Tmp")
    ph = get_probe_value(status, "pH")
    salt = get_probe_value(status, "Salt")

    if temp is None or ph is None or salt is None:
        print("⚠️ Apex")
        print("---")
        print("Could not read sensors")
        print("---")
        print("Refresh | refresh=true")
        print(f"Open Apex Fusion | href={APEX_FUSION_URL}")
        return

    # Success
    print(f"🐠 {temp}° {ph} {salt}")
    print("---")
    print(f"Temperature: {temp}°C")
    print(f"pH: {ph}")
    print(f"Salinity: {salt} ppt")
    print("---")
    print("Refresh | refresh=true")
    print(f"Open Apex Fusion | href={APEX_FUSION_URL}")


if __name__ == "__main__":
    main()
