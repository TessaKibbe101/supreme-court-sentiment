from nltk.sentiment.vader import SentimentIntensityAnalyzer
import textstat
import pandas as pd
import os
import sys
import re
def read_opinion_file(filepath):
    try:
        with open(filepath, 'r') as f:
            opinion_file = f.read()
            return opinion_file
    except FileNotFoundError:
        print("File not found")
        return None

def count_stats(text):
    word_count = len(text.split())
    character_count = len(text)
    return {'words': word_count, 'characters': character_count}

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    return score

def calculate_readability(text):
    reading_ease = textstat.flesch_reading_ease(text)
    reading_grade = textstat.flesch_kincaid_grade(text)
    avg_sentence_length = textstat.words_per_sentence(text)
    avg_word_length = textstat.avg_letter_per_word(text)
    return {
        'flesch_reading_ease': reading_ease,
        'flesch_kincaid_grade': reading_grade,
        'avg_sentence_length': avg_sentence_length,
        'avg_word_length': avg_word_length
    }
def save_to_csv(case_name, year, stats, sentiment, readability, filepath):
    data = {
        'Case_name': [case_name],
        'Year': [year],
        'Words': [stats['words']],
        'Characters': [stats['characters']],
        'Positive': [sentiment['pos']],
        'Negative': [sentiment['neg']],
        'Neutral': [sentiment['neu']],
        'Compound': [sentiment['compound']],
        'Reading Ease': [readability['flesch_reading_ease']],
        'Reading Grade': [readability['flesch_kincaid_grade']],
        'Avg Sentence Length': [readability['avg_sentence_length']],
        'Avg Word Length': [readability['avg_word_length']]
    }

    new_df = pd.DataFrame(data)

    if os.path.exists(filepath):
        existing_df = pd.read_csv(filepath)
        existing_df = existing_df[~((existing_df['Case_name'] == case_name) & (existing_df['Year'] == year))]
        combined_df = pd.concat([existing_df, new_df], ignore_index=True)
        combined_df.to_csv(filepath, index=False)
    else:
        new_df.to_csv(filepath, index=False)

def split_opinion_sections(text):
    pattern = r'JUSTICE \w+.*(concurring|dissenting)'

    sections = re.split(pattern, text)

    majority = sections[0]
    dissents = []
    for i in range(1, len(sections), 2):
        if i < len(sections) and sections[i] == 'dissenting':
            if i + 1 < len(sections):
                dissents.append(sections[i + 1])

    all_dissents =' '.join(dissents)

    return {
        'majority': majority,
        'dissents': all_dissents
    }

def main():

    if len(sys.argv) != 4:
        print('Usage: python scripts/collector.py <case_name> <year> <filepath>')
        return
    case_name = sys.argv[1]
    year = int(sys.argv[2])
    filepath = sys.argv[3]

    opinion_file = read_opinion_file(filepath)

    if opinion_file is None:
        return
    sections = split_opinion_sections(opinion_file)
    count = count_stats(opinion_file)
    majority_sentiment = analyze_sentiment(sections['majority'])
    majority_readability = calculate_readability(sections['majority'])
    dissent_sentiment = analyze_sentiment(sections['dissents'])
    dissent_readability = calculate_readability(sections['dissents'])

    print(f"Case: {case_name}, {year}")
    print(f"Words: {count['words']}")
    print(f"Characters: {count['characters']}")
    print("\n=== MAJORITY vs DISSENT COMPARISONS ===\n")
    print("MAJORITY OPINION: ")
    print(f"  Sentiment - Pos: {majority_sentiment['pos']}, Neg: {majority_sentiment['neg']}, Neu: {majority_sentiment['neu']}, Compound: {majority_sentiment['compound']}")
    print(f"  Reading Ease: {majority_readability['flesch_reading_ease']}")
    print(f"  Grade Level: {majority_readability['flesch_kincaid_grade']}\n")

    print("DISSENTING OPINIONS:")
    print(f"  Sentiment - Pos: {dissent_sentiment['pos']}, Neg: {dissent_sentiment['neg']}, Neu: {dissent_sentiment['neu']}, Compound: {dissent_sentiment['compound']}")
    print(f"  Reading Ease: {dissent_readability['flesch_reading_ease']}")
    print(f"  Grade Level: {dissent_readability['flesch_kincaid_grade']}\n")

    print(f"Average sentence length: {majority_readability['avg_sentence_length']}")
    print(f"Average word length: {majority_readability['avg_word_length']}")
    print(f"First 100 characters: {opinion_file[:100]}")

    save_to_csv(
        case_name=f"{case_name} - Majority",
        year=year,
        stats=count_stats(sections['majority']),
        sentiment=majority_sentiment,
        readability=majority_readability,
        filepath="outputs/analysis_results.csv"
    )

    save_to_csv(
        case_name=f"{case_name} - Dissent",
        year=year,
        stats=count_stats(sections['dissents']),
        sentiment=dissent_sentiment,
        readability=dissent_readability,
        filepath="outputs/analysis_results.csv"
    )
    print("\nResults saved to outputs/analysis_results.csv")

if __name__ == "__main__":
    main()
