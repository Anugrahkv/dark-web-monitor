import requests
import json

# This public feed aggregates posts from Dark Web Tor ransomware leak sites
# It simulates an enterprise Threat Intelligence feed
FEED_URL = "https://raw.githubusercontent.com/joshhighet/ransomwatch/main/posts.json"

# The company we are monitoring for breaches
TARGET_COMPANY = "bugcrowd"

def monitor_dark_web_leaks():
    print("[*] Connecting to Dark Web Ransomware / Leak Aggregator...")
    
    try:
        response = requests.get(FEED_URL, timeout=10)
        if response.status_code != 200:
            print("[-] Failed to fetch threat intel feed.")
            return
            
        data = response.json()
        print(f"[+] Successfully loaded {len(data)} recent dark web posts.")
        
        # 1. Search for our specific target
        print(f"\n[*] Hunting for mentions of '{TARGET_COMPANY}'...")
        found = False
        for post in data:
            if TARGET_COMPANY.lower() in post.get('post_title', '').lower():
                found = True
                print(f"[CRITICAL LEAK] Target found on {post.get('group_name')} leak site!")
                print(f" - Discovered: {post.get('discovered')}")
                
        if not found:
            print(f"[+] Target '{TARGET_COMPANY}' is safe. No mentions found in current leaks.")
            
        # 2. Track general Threat Actor activity (HUMINT)
        print("\n[*] Tracking Latest Threat Actor Activity (Recent 5 Victims):")
        for post in data[:5]:
            group = post.get('group_name', 'Unknown')
            victim = post.get('post_title', 'Unknown')
            print(f" - Threat Group: [{group}] | Victim: {victim}")
            
    except Exception as e:
        print(f"[-] Error parsing threat feed: {e}")

if __name__ == "__main__":
    monitor_dark_web_leaks()