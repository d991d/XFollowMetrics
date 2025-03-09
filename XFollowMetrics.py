
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
import pickle
import argparse
from requests_oauthlib import OAuth1

# Configuration
X_DATA_PATH = Path('./X Data')  # Default path, should be modified by user
X_DATA_FILES = X_DATA_PATH / 'data'  # Data subdirectory
OUTPUT_FILE = Path(X_DATA_PATH / 'follower_report.xlsx')
CACHE_DIR = Path.home() / 'Library' / 'Application Support' / 'XFollowMetrics' / 'cache'

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

def setup_cache_dir():
    """Create cache directory if it doesn't exist"""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    return CACHE_DIR / 'user_info_cache.pkl'

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

def get_user_info(user_ids, use_cache=True, dev_mode=False):
    """Get user information from X API with caching support"""
    cache_file = setup_cache_dir()
    user_info = {}

    # Try to load from cache first
    if use_cache and cache_file.exists():
        try:
            with open(cache_file, 'rb') as f:
                cached_data = pickle.load(f)
                print("📂 Using cached user data")
                return cached_data
        except Exception as e:
            print(f"⚠️ Cache load failed: {e}")

    batch_size = 100  # X API limit
    max_retries = 3
    retry_count = 0
    total_batches = (len(user_ids) + batch_size - 1) // batch_size

    for batch_num, i in enumerate(range(0, len(user_ids), batch_size), 1):
        batch = user_ids[i:i + batch_size]
        print(f"🔄 Processing batch {batch_num}/{total_batches}")

        while retry_count < max_retries:
            try:
                # First attempt with Bearer token
                response = requests.get(
                    API_ENDPOINT,
                    headers=get_auth_headers(),
                    params={
                        "ids": ",".join(batch),
                        "user.fields": "name,username,created_at,public_metrics,description"
                    }
                )

                if response.status_code == 429:  # Rate limit exceeded
                    retry_after = int(response.headers.get('x-rate-limit-reset', 900))
                    print(f"⏳ Rate limit exceeded. Waiting {retry_after} seconds...")
                    if not dev_mode:  # Skip waiting in dev mode
                        time.sleep(retry_after)
                    continue

                if response.status_code == 200:
                    data = response.json()
                    print(f"✅ Retrieved data for {len(data.get('data', []))} users")
                    
                    for user in data.get('data', []):
                        user_info[user['id']] = {
                            'name': user.get('name', ''),
                            'username': user.get('username', ''),
                            'created_at': user.get('created_at', ''),
                            'followers_count': user.get('public_metrics', {}).get('followers_count', 0),
                            'following_count': user.get('public_metrics', {}).get('following_count', 0),
                            'tweet_count': user.get('public_metrics', {}).get('tweet_count', 0)
                        }
                    break
                
                retry_count += 1
                time.sleep(5)  # Wait before retry

            except Exception as e:
                print(f"❌ Error: {str(e)}")
                retry_count += 1
                time.sleep(5)

        if retry_count >= max_retries:
            print(f"⚠️ Failed to get data for batch {batch_num} after {max_retries} retries")

    # Save to cache if successful
    if user_info and use_cache:
        try:
            with open(cache_file, 'wb') as f:
                pickle.dump(user_info, f)
            print("💾 Cached user data saved")
        except Exception as e:
            print(f"⚠️ Cache save failed: {e}")

    return user_info

def main():
    parser = argparse.ArgumentParser(description='XFollowMetrics - X (Twitter) Follower Analytics Tool')
    parser.add_argument('--dev', action='store_true', help='Run in development mode')
    args = parser.parse_args()

    print("XFollowMetrics - X (Twitter) Follower Analytics Tool")
    print("Created by d991d")
    print("https://github.com/d991d/XFollowMetrics")
    print("\n" + "="*50 + "\n")

    if args.dev:
        print("🔧 Running in development mode")

    print(f"📂 Using Twitter data from: {X_DATA_PATH}")
    print(f"📝 Will save report to: {OUTPUT_FILE}")

    # Check for API credentials
    if API_KEY == "YOUR_API_KEY":
        print("\n❌ Error: API credentials not configured!")
        print("Please edit the script and add your X API credentials")
        return

    # Check data files
    check_data_files()

    # Load followers
    print("\n📊 Loading followers...")
    followers = load_followers(X_DATA_PATH)

    if not followers:
        print("❌ No followers found. Please check your Twitter data export.")
        return

    print(f"✅ Loaded {len(followers)} followers")
    
    # Use smaller sample in dev mode
    if args.dev:
        test_size = 3
        followers = followers[:test_size]
        print(f"\n🔧 Development mode: Testing with first {test_size} followers")
    
    # Get detailed user info
    print("\n🔄 Fetching user information...")
    user_ids = [user_id for user_id, _ in followers]
    user_info = get_user_info(user_ids, use_cache=True, dev_mode=args.dev)

    # Create report
    print("\n📊 Generating report...")
    follower_data = []
    for user_id, _ in followers:
        user_details = user_info.get(user_id, {
            'username': f"user_{user_id}",
            'name': f"Unknown User {user_id}",
            'created_at': 'N/A',
            'followers_count': 0,
            'following_count': 0,
            'tweet_count': 0
        })

        follower_data.append({
            'Display Name': user_details['name'],
            'Username': f"@{user_details['username']}",
            'User ID': user_id,
            'Account Created': user_details.get('created_at', 'N/A'),
            'Followers Count': user_details.get('followers_count', 0),
            'Following Count': user_details.get('following_count', 0),
            'Tweet Count': user_details.get('tweet_count', 0)
        })

    # Save to Excel
    df = pd.DataFrame(follower_data)
    df.to_excel(OUTPUT_FILE, index=False)
    print(f"\n✅ Report saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()