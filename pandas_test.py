import pandas as pd

try:
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    print("✅ Pandas is working! Sample DataFrame:")
    print(df)
except Exception as e:
    print(f"❌ Pandas error: {e}")
