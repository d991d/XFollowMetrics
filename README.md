
# XFollowMetrics

A comprehensive Python tool for analyzing X (Twitter) followers and interactions. Created by [d991d](https://github.com/d991d).

## Features

- Analyzes your X (Twitter) data export
- Creates detailed Excel reports about your followers
- Tracks interaction history
- Combines local data with current X API information
- Handles rate limits automatically
- Caches API responses for faster subsequent runs
- Development mode for testing
- Command-line interface with arguments

## Prerequisites

- Python 3.6 or higher
- Required packages: pandas, requests, requests_oauthlib
- X (Twitter) API credentials
- Your Twitter data export

## Installation

1. Clone the repository:
```bash
git clone https://github.com/d991d/XFollowMetrics.git
```

2. Install required packages:
```bash
pip install pandas requests requests_oauthlib
```

3. Configure your X API credentials in `XFollowMetrics.py`:
```python
API_KEY = "your_api_key"
API_SECRET_KEY = "your_api_secret_key"
BEARER_TOKEN = "your_bearer_token"
ACCESS_TOKEN = "your_access_token"
ACCESS_TOKEN_SECRET = "your_access_token_secret"
```

## Usage

1. Download your Twitter data export
2. Place the export files in the `X Data/data` directory
3. Run the script:

For normal operation:
```bash
python XFollowMetrics.py
```

For development/testing mode (processes only 3 followers):
```bash
python XFollowMetrics.py --dev
```

## Cache Management

The script now caches API responses in:
```
~/Library/Application Support/XFollowMetrics/cache/
```

This improves performance for subsequent runs and reduces API calls.

## Output

The script generates an Excel report (`follower_report.xlsx`) containing:
- Display Name
- Username
- User ID
- Account Created Date
- Followers Count
- Following Count
- Tweet Count
- Last Interaction Date
- Days Since Last Interaction

## Development Mode

Use development mode for testing changes or debugging:
- Processes only the first 3 followers
- Skips rate limit waiting periods
- Maintains all other functionality
- Useful for quick testing and validation

## Note

The script may take 1-2 hours to run for accounts with many followers due to X API rate limits. Using development mode (`--dev`) for testing is recommended.

## Mac Application

For macOS users, you can run XFollowMetrics as a native application:

1. Follow the instructions in `MAC_INSTALLATION.md` to create the app
2. Double-click XFollowMetrics to run
3. Click "Run Analysis" in the dialog

The Mac app provides:
- Easy double-click execution
- User-friendly interface
- Progress tracking in Terminal
- Native macOS integration

## Troubleshooting

Common issues and solutions:

1. **API Rate Limits**: The script automatically handles rate limits by waiting
2. **Cache Issues**: Delete the cache directory to force fresh API calls:
   ```bash
   rm -rf ~/Library/Application\ Support/XFollowMetrics/cache/
   ```
3. **Testing New Features**: Use `--dev` flag for quick testing

## License

MIT License - See LICENSE file for details

## Author

Created by [d991d](https://github.com/d991d)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.