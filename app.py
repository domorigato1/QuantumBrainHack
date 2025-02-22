import requests
import time
import winsound  # For Windows beep alerts
import pyautogui  # For auto-clicking (optional)
import os

# BTC Price Tracker with Alerts
def get_btc_price():
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
        data = response.json()
        price = data["bitcoin"]["usd"]
        return price
    except Exception as e:
        print(f"Error fetching BTC price: {e}")
        return None

def btc_tracker(last_price=None):
    price = get_btc_price()
    if price:
        print(f"BTC: ${price} at {time.ctime()}")
        with open("btc_log.txt", "a") as f:
            f.write(f"BTC: ${price} at {time.ctime()}\n")
        
        if last_price:
            change = ((price - last_price) / last_price) * 100
            if abs(change) > 2:  # 2% swing triggers alert
                winsound.Beep(1000, 500)  # Beep at 1000Hz for 500ms
                print(f"ALERT: BTC { 'up' if change > 0 else 'down' } {change:.2f}%!")
        
        return price
    return last_price

# Satoshi Earnings Logger
def log_satoshi(amount):
    with open("satoshi_stack.txt", "a") as f:
        f.write(f"Earned {amount} satoshis at {time.ctime()}\n")
    print(f"Logged {amount} satoshis—stacking #CodeMoney!")

# Auto-Clicker (Optional - Use with caution per site rules)
def auto_click(x, y, clicks=10, delay=1):
    print(f"Auto-click starting in 5s at ({x}, {y})—move mouse to spot!")
    time.sleep(5)
    for _ in range(clicks):
        pyautogui.click(x, y)
        time.sleep(delay)
    print("Auto-click done—check your satoshis!")

# Main Loop
def main():
    print("Starting BTC Money Machine - #SavageHealth #CodeMoney")
    last_price = None
    
    # Example: Log some satoshis (replace with real earnings)
    log_satoshi(50)  # Call this after microtasks
    
    # Optional: Auto-click setup (uncomment to use)
    # x, y = pyautogui.position()
    # auto_click(x, y, clicks=5, delay=2)  # 5 clicks, 2s delay
    
    # BTC price tracking loop
    while True:
        last_price = btc_tracker(last_price)
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Stopped by user—keep stacking, savage!")