# Apex Reef Tank Monitor

An [xbar](https://xbarapp.com)/[SwiftBar](https://swiftbar.app) plugin that displays real-time temperature, pH, and salinity from your Neptune Apex controller in the macOS menu bar.

![Screenshot](screenshot.png)

## Features

- Live readings from your local Apex controller
- Updates every 5 minutes (configurable via filename)
- Zero dependencies - uses only built-in macOS Python
- Quick link to Apex Fusion
- Easy configuration through xbar's plugin settings

## Requirements

- macOS 10.15 or later
- [xbar](https://xbarapp.com) or [SwiftBar](https://swiftbar.app)
- Neptune Apex controller on your local network

## Installation

### From xbar Plugin Browser

1. Open xbar
2. Click **xbar > Plugin Browser...**
3. Search for "Apex"
4. Click **Install**

### Manual Installation

1. Download [`apex.5m.py`](https://raw.githubusercontent.com/SteveBlackUK/Apex-Menu-Bar/main/apex.5m.py)

2. Move to your plugins folder:
   - xbar: `~/Library/Application Support/xbar/plugins/`
   - SwiftBar: Check preferences for your plugins folder

3. Make executable:
   ```bash
   chmod +x apex.5m.py
   ```

4. Refresh xbar/SwiftBar

## Configuration

1. Click the plugin in your menu bar
2. Select **xbar > Open Plugin...** (or right-click in SwiftBar)
3. Set your Apex IP address in the variables section

### Finding Your Apex IP Address

- **From Apex Fusion:** Dashboard > Network tile
- **From your router:** Look for "Apex" in connected devices
- **Common default:** `apex.local`

### Configuration Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `APEX_IP` | (empty) | Your Apex's local IP address |
| `APEX_USER` | `admin` | Username (if authentication enabled) |
| `APEX_PASS` | (empty) | Password (if authentication enabled) |

Most Apex controllers don't require authentication for local network access.

## Customization

### Refresh Interval

Rename the file to change how often it updates:
- `apex.1m.py` - Every minute
- `apex.5m.py` - Every 5 minutes (default)
- `apex.15m.py` - Every 15 minutes

## Troubleshooting

**"Setup" keeps showing**
- Configure your Apex IP in plugin settings

**"Connection failed"**
- Verify your Apex is powered on
- Check you're on the same network
- Try the IP in a browser: `http://YOUR_IP/cgi-bin/status.json`

**"Could not read sensor values"**
- Your probe names may differ from defaults (Tmp, pH, Salt)
- Check your Apex configuration for actual probe names

**"Authentication required"**
- Set `APEX_USER` and `APEX_PASS` in plugin settings

## Contributing

Issues and pull requests welcome!

## License

MIT License - see [LICENSE](LICENSE)

## Acknowledgments

- [xbar](https://xbarapp.com) by @matryer
- [SwiftBar](https://swiftbar.app) by @melonamin
- [Neptune Systems](https://www.neptunesystems.com)

---

*Not affiliated with Neptune Systems*
