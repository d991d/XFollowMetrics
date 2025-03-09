# XFollowMetrics Mac Application Setup

## Creating the Mac Application

1. Open "Script Editor" on your Mac (use Spotlight and type "Script Editor")
2. Create a new script and paste the contents from `XFollowMetrics.applescript`
3. Click File → Export
4. In the Export dialog:
   - Set File Format to "Application"
   - Check "Run-only"
   - Name it "XFollowMetrics"
   - Choose a save location (e.g., Applications folder)

## Post-Creation Setup

1. Create a "Resources" folder in the app bundle:
   ```bash
   cd /Applications/XFollowMetrics.app/Contents/
   mkdir Resources
   ```

2. Copy the shell script to the Resources folder:
   ```bash
   cp /path/to/run_xfollowmetrics.sh /Applications/XFollowMetrics.app/Contents/Resources/
   ```

3. Make the shell script executable:
   ```bash
   chmod +x /Applications/XFollowMetrics.app/Contents/Resources/run_xfollowmetrics.sh
   ```

4. Copy XFollowMetrics.py to the same folder as the app:
   ```bash
   cp XFollowMetrics.py /Applications/XFollowMetrics.app/Contents/Resources/
   ```

## Usage

1. Double-click the XFollowMetrics application
2. Click "Run Analysis" in the dialog
3. The analysis will run in a Terminal window
4. Results will be saved in the specified output location

## Troubleshooting

If you get a security warning:
1. Go to System Preferences → Security & Privacy
2. Click "Open Anyway" for XFollowMetrics
3. You may need to right-click the app and select "Open" the first time

## Requirements

- macOS 10.13 or later
- Python 3.6 or higher
- Internet connection for API access