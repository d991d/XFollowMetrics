# XFollowMetrics

A comprehensive Python tool for analyzing X (Twitter) followers and interactions. Created by [d991d](https://github.com/d991d).

## Features

- Analyzes your X (Twitter) data export
- Creates detailed Excel reports about your followers
- Tracks interaction history
- Combines local data with current X API information
- Handles rate limits automatically

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

The script may take 1-2 hours to run for accounts with many followers due to X API rate limits.

## License

MIT License - See LICENSE file for details

## Author

Created by [d991d](https://github.com/d991d)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.