
"""
XFollowMetrics - X (Twitter) Follower Analytics Tool
Created by d991d
https://github.com/d991d/XFollowMetrics

A comprehensive tool for analyzing X (Twitter) followers and interactions.
"""

import pandas as pd
from datetime import datetime
from pathlib import Path
import json
import os
import requests
import time
from requests_oauthlib import OAuth1

# Configuration
X_DATA_PATH = Path('./X Data')  # Default path, should be modified by user
X_DATA_FILES = X_DATA_PATH / 'data'  # Data subdirectory
OUTPUT_FILE = Path(X_DATA_PATH / 'follower_report.xlsx')

# X API Configuration - Replace with your credentials
API_KEY = "YOUR_API_KEY"
API_SECRET_KEY = "YOUR_API_SECRET_KEY"
BEARER_TOKEN = "YOUR_BEARER_TOKEN"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"

API_ENDPOINT = "https://api.twitter.com/2/users"

# OAuth 1.0a handler
oauth = OAuth1(
    API_KEY,
    client_secret=API_SECRET_KEY,
    resource_owner_key=ACCESS_TOKEN,
    resource_owner_secret=ACCESS_TOKEN_SECRET
)

def get_auth_headers(use_oauth=False):
    """Get authentication headers based on the authentication method"""
    if use_oauth:
        return {"User-Agent": "XFollowMetrics/1.0"}
    else:
        return {
            "Authorization": f"Bearer {BEARER_TOKEN}",
            "User-Agent": "XFollowMetrics/1.0"
        }

def check_data_files():
    """Check if required data files exist"""
    followers_file = X_DATA_FILES / 'follower.js'

    print("\nChecking data files:")
    print(f"Looking for follower.js in: {X_DATA_FILES}")
    print(f"Directory exists: {X_DATA_FILES.exists()}")
    print(f"Is directory: {X_DATA_FILES.is_dir()}")
    print(f"Followers file exists: {followers_file.exists()}")

    if X_DATA_FILES.exists() and X_DATA_FILES.is_dir():
        print("\nFiles in directory:")
        for file in X_DATA_FILES.glob('*.js'):
            print(f"- {file.name}")

def load_followers(data_path):
    """Load followers from Twitter data export"""
    followers_file = Path(data_path) / 'data' / 'follower.js'
    if not followers_file.exists():
        print(f"❌ Followers file not found at: {followers_file}")
        return []

    try:
        with open(followers_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Handle the JavaScript format
            if 'window.YTD.follower.part0 = ' in content:
                content = content.replace('window.YTD.follower.part0 = ', '')
            
            content = content.strip().rstrip(';')
            data = json.loads(content)

            followers = []
            for entry in data:
                if isinstance(entry, dict) and 'follower' in entry:
                    followers.append((
                        entry['follower']['accountId'],
                        datetime.now()
                    ))

            print(f"✅ Successfully processed {len(followers)} followers")
            return followers

    except Exception as e:
        print(f"❌ Error loading followers: {str(e)}")
        return []

def main():
    print("XFollowMetrics - X (Twitter) Follower Analytics Tool")
    print("Created by d991d")
    print("https://github.com/d991d/XFollowMetrics")
    print("\n" + "="*50 + "\n")

    print(f"📂 Using Twitter data from: {X_DATA_PATH}")
    print(f"📝 Will save report to: {OUTPUT_FILE}")

    # Check for API credentials
    if API_KEY == "YOUR_API_KEY":
        print("\n❌ Error: API credentials not configured!")
        print("Please edit the script and add your X API credentials")
        return

if __name__ == "__main__":
    main()