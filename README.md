# Supreme Court Sentiment Analysis

A Python-based text analysis tool that performs sentiment analysis and readability scoring on Supreme Court opinions using natural language processing (NLP) techniques.

## Overview

This project analyzes Supreme Court opinions to extract insights about the language, sentiment, and complexity of judicial writing. Currently analyzing the Harvard Affirmative Action case (Students for Fair Admissions v. Harvard, 2023).

## Features

- **Text Collection**: Reads and processes Supreme Court opinion documents
- **Statistical Analysis**: Counts words, characters, and basic text metrics
- **Sentiment Analysis**: Uses NLTK's VADER (Valence Aware Dictionary and sEntiment Reasoner) to analyze emotional tone
- **Readability Scoring**: Calculates Flesch Reading Ease, Flesch-Kincaid Grade Level, and average sentence/word length

## Technologies Used

- **Python 3.9+**
- **NLTK** - Natural Language Toolkit for sentiment analysis
- **textstat** - Readability metrics and text statistics
- **pandas** - Data manipulation (planned for future use)
- **matplotlib** - Data visualization (planned for future use)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/TessaKibbe101/supreme-court-sentiment.git
cd supreme-court-sentiment
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download required NLTK data:
```bash
python setup_nltk.py
```

## Usage

Run the analysis script:
```bash
python scripts/collector.py
```

## Sample Output

```
Case: Harvard Affirmative Action 2023
Words: 76351
Characters: 475939

Sentiment Analysis: 
Positive: 0.098
Negative: 0.061
Neutral: 0.841
Compound: 1.0

Readability Analysis: 
Reading ease: 50.84
Reading grade: 10.03
Average sentence length: 15.53
Average word length: 4.93
```

## Key Insights

- **Sentiment**: The Harvard affirmative action opinion is overwhelmingly neutral (84.1%), which is typical for legal writing
- **Readability**: Requires a 10th grade reading level with a "fairly difficult" reading ease score of 50.8
- **Writing Style**: Moderate sentence length (15.5 words) and word complexity (4.9 characters per word)

## Project Structure

```
supreme-court-sentiment/
├── data/
│   └── raw_opinions/          # Supreme Court opinion text files
├── scripts/
│   ├── collector.py           # Main analysis script
│   └── test.py               # Testing utilities
├── outputs/                   # Analysis results (future)
├── requirements.txt          # Python dependencies
├── setup_nltk.py            # NLTK data downloader
└── README.md
```

## Future Improvements

- [ ] Compare sentiment across different justices (majority vs. dissent)
- [ ] Visualize sentiment trends over time
- [ ] Analyze multiple Supreme Court cases
- [ ] Generate comparative reports
- [ ] Export results to CSV/JSON
- [ ] Create data visualizations with matplotlib
- [ ] Build a web interface for analysis

## Author

Tessa Kibbe - Aspiring tech law professional building data analysis skills for legal technology applications

## License

This project is open source and available for educational purposes.
