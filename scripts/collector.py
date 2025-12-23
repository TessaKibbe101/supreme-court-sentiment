from nltk.sentiment.vader import SentimentIntensityAnalyzer
import textstat
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

def main():
    opinion_file = read_opinion_file("/Users/tessakibbe/supreme-court-sentiment/data/raw_opinions/Harvard_2023.txt")
    if opinion_file is None:
        return

    count = count_stats(opinion_file)
    sentiment = analyze_sentiment(opinion_file)
    readability = calculate_readability(opinion_file)

    print("Case: Harvard Affirmative Action 2023")
    print(f"Words: {count['words']}")
    print(f"Characters: {count['characters']}\n")
    print("Sentiment Analysis: ")
    print(f"Positive: {sentiment['pos']}")
    print(f"Negative: {sentiment['neg']}")
    print(f"Neutral: {sentiment['neu']}")
    print(f"Compound: {sentiment['compound']}\n")
    print("Readability Analysis: ")
    print(f"Reading ease: {readability['flesch_reading_ease']}")
    print(f"Reading grade: {readability['flesch_kincaid_grade']}")
    print(f"Average sentence length: {readability['avg_sentence_length']}")
    print(f"Average word length: {readability['avg_word_length']}")
    print(f"First 100 characters: {opinion_file[:100]}")

if __name__ == "__main__":
    main()
