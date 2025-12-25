import pandas as pd
import matplotlib.pyplot as plt

def load_data(filepath):
    data = pd.read_csv(filepath)
    return data


def create_sentiment_chart(data):
    fig, ax = plt.subplots(figsize=(12, 6))

    x = range(len(data))
    width = 0.25

    ax.bar([i - width for i in x], data['Positive'], width, label='Positive', color='green')
    ax.bar(x, data['Negative'], width, label='Negative', color='red')
    ax.bar([i + width for i in x], data['Neutral'], width, label='Neutral', color='gray')

    ax.set_xlabel('Case')
    ax.set_ylabel('Score')
    ax.set_title('Sentiment Analysis Across Supreme Court Cases')
    ax.set_xticks(x)
    ax.set_xticklabels(data['Case_name'], rotation=45, ha='right')
    ax.legend()
    ax.set_ylim(0, 1)

    plt.tight_layout()
    plt.savefig('outputs/sentiment_chart.png')
    plt.close()

    print("Sentiment chart saved to outputs/sentiment_chart.png")


def create_readability_chart(data):
    fig, ax = plt.subplots(figsize=(12, 6))

    x = range(len(data))

    ax.bar(x, data['Reading Ease'], color='blue', alpha=0.7)
    ax.set_xlabel('Case')
    ax.set_ylabel('Flesch Reading Ease (Higher = Easier)')
    ax.set_title('Readability Across Supreme Court Cases')
    ax.set_xticks(x)
    ax.set_xticklabels(data['Case_name'], rotation=45, ha='right')
    ax.axhline(y=50, color='red', linestyle='--', alpha=0.5, label='Fairly Difficult')
    ax.legend()

    plt.tight_layout()
    plt.savefig('outputs/readability_chart.png')
    plt.close()

    print("Readability chart saved to outputs/readability_chart.png")


def create_time_series_charts(data):
    majority_data = data[data['Case_name'].str.contains('Majority')].sort_values('Year')
    dissent_data = data[data['Case_name'].str.contains('Dissent')].sort_values('Year')


    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    ax1.plot(majority_data['Year'], majority_data['Reading Ease'],
             marker='o', label='Majority', color='blue', linewidth=2)
    ax1.plot(dissent_data['Year'], dissent_data['Reading Ease'],
             marker='s', label='Dissent', color='red', linewidth=2)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Flesch Reading Ease (Higher = Easier)')
    ax1.set_title('Reading Ease Over Time (1973-2023)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.plot(majority_data['Year'], majority_data['Compound'],
             marker='o', label='Majority', color='blue', linewidth=2)
    ax2.plot(dissent_data['Year'], dissent_data['Compound'],
             marker='s', label='Dissent', color='red', linewidth=2)
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Compound Sentiment (-1 to +1)')
    ax2.set_title('Sentiment Over Time (1973-2023)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=0, color='black', linestyle='--', alpha=0.3)

    plt.tight_layout()
    plt.savefig('outputs/time_series_analysis.png')
    plt.close()

    print("Time series chart saved to outputs/time_series_analysis.png")

def main():
    data = load_data("outputs/analysis_results.csv")
    create_sentiment_chart(data)
    create_readability_chart(data)
    create_time_series_charts(data)

if __name__ == "__main__":
    main()