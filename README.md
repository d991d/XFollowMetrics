# XFollowMetrics

A comprehensive Python tool for analyzing X (Twitter) followers and interactions. Created by [d991d](https://github.com/d991d).

## Features

- Analyzes your X (Twitter) data export
- Creates detailed Excel reports about your followers
- Tracks interaction history
- Combines local data with current X API information
- Smart rate limit handling with caching support
- Development mode for faster testing

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
```bash
python XFollowMetrics.py
```

### Development Mode

For faster development and testing:
```bash
python XFollowMetrics.py --dev
```
This mode:
- Uses cached API responses when available
- Tests with a smaller sample size
- Reduces wait times during development

## Rate Limits

The script handles X API rate limits automatically:
- Waits during rate limit windows (typically 15 minutes)
- Caches responses to minimize API calls
- Shows progress during rate limit waiting periods

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

## Note

The script's runtime depends on:
- Number of followers
- X API rate limits
- Cache availability
- Development mode settings

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

## License

MIT License - See LICENSE file for details

## Author

Created by [d991d](https://github.com/d991d)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.