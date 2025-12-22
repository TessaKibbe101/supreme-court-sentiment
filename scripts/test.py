# scripts/test.py
# Test script to verify everything is installed correctly

import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import textstat
import matplotlib.pyplot as plt

def test_setup():
    """
    Test that all libraries work
    """
    print("Testing setup...")
    print("-" * 40)
    
    # Test 1: Pandas
    df = pd.DataFrame({'test': [1, 2, 3]})
    print("✓ Pandas working")
    
    # Test 2: NLTK sentiment
    sia = SentimentIntensityAnalyzer()
    test_text = "The Supreme Court ruled favorably."
    sentiment = sia.polarity_scores(test_text)
    print(f"✓ NLTK working (sentiment: {sentiment['compound']:.2f})")
    
    # Test 3: Textstat
    grade = textstat.flesch_kincaid_grade(test_text)
    print(f"✓ Textstat working (grade level: {grade:.1f})")
    
    # Test 4: Matplotlib
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.savefig('outputs/test_chart.png')
    plt.close()
    print("✓ Matplotlib working (saved test_chart.png)")
    
    print("-" * 40)
    print("✅ All systems operational!")

if __name__ == "__main__":
    test_setup()
