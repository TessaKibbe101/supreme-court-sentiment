import pandas as pd
import matplotlib.pyplot as plt

def load_data(filepath):
    data = pd.read_csv(filepath)
    return data

def create_sentiment_chart(data):

    row = data.iloc[0]

    categories = ['Positive', 'Negative', 'Neutral']
    scores = [row['Positive'], row['Negative'], row['Neutral']]

    plt.figure(figsize=(8,6))
    plt.bar(categories, scores, color=['green', 'red', 'gray'])
    plt.xlabel('Sentiment Type')
    plt.ylabel('Score')
    plt.title('Sentiment Analysis - Harvard Affirmative Action (2023)')
    plt.ylim(0,1)

    plt.savefig('outputs/sentiment_chart.png')
    plt.close()

    print("Sentiment chart saved to outputs/sentiment_chart.png")

def create_readability_chart(data):

    row = data.iloc[0]

    categories = ['Reading Ease', 'Reading Grade']
    scores = [row['Reading Ease'], row['Reading Grade']]

    plt.figure(figsize=(8,6))
    plt.bar(categories, scores, color=['blue','green'])
    plt.xlabel('Readability type')
    plt.ylabel('Score')
    plt.title('Readability Analysis - Harvard Affirmative Action (2023)')
    plt.ylim(0,100)

    plt.savefig('outputs/readability_chart.png')
    plt.close()

    print("Readbility chart saved to outputs/readability_chart.png")

def main():
    data = load_data("outputs/analysis_results.csv")
    create_sentiment_chart(data)
    create_readability_chart(data)

if __name__ == "__main__":
    main()