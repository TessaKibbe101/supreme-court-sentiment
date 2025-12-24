# Supreme Court Sentiment Analysis

A Python-based text analysis tool that performs sentiment analysis and readability scoring on Supreme Court opinions using natural language processing (NLP) techniques.

## Overview

This project analyzes Supreme Court opinions to extract insights about the language, sentiment, and complexity of judicial writing. The tool processes opinion text files, generates statistical metrics, performs NLP analysis, and creates visualizations of the results.

## Features

- **Text Collection**: Reads and processes Supreme Court opinion documents from any case
- **Statistical Analysis**: Counts words, characters, and basic text metrics
- **Sentiment Analysis**: Uses NLTK's VADER (Valence Aware Dictionary and sEntiment Reasoner) to analyze emotional tone
- **Readability Scoring**: Calculates Flesch Reading Ease, Flesch-Kincaid Grade Level, and average sentence/word length using textstat
- **Data Persistence**: Exports analysis results to CSV for tracking multiple cases
- **Data Visualization**: Generates professional charts (sentiment distribution, readability metrics) with matplotlib
- **Flexible Analysis**: Command-line interface supports analyzing any Supreme Court case

## Technologies Used

- **Python 3.9+**
- **NLTK** - Natural Language Toolkit for sentiment analysis
- **textstat** - Readability metrics and text statistics
- **pandas** - Data manipulation and CSV export
- **matplotlib** - Data visualization and chart generation

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

### Analyze a Supreme Court case:

```bash
python scripts/collector.py "<Case Name>" <Year> <filepath>
```

**Example:**
```bash
python scripts/collector.py "Harvard Affirmative Action" 2023 data/raw_opinions/Harvard_2023.txt
```

### Generate visualizations:

```bash
python scripts/visualizer.py
```

This reads the CSV data and generates:
- `outputs/sentiment_chart.png` - Bar chart of sentiment scores
- `outputs/readability_chart.png` - Bar chart of readability metrics

## Sample Output

### Terminal Output:
```
Case: Harvard Affirmative Action, 2023
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

Results saved to outputs/analysis_results.csv
```

### Generated Files:
- **analysis_results.csv** - Structured data with all metrics for each analyzed case
- **sentiment_chart.png** - Visual representation of emotional tone distribution
- **readability_chart.png** - Visual representation of text complexity metrics

## Key Insights

- **Sentiment**: The Harvard affirmative action opinion is overwhelmingly neutral (84.1%), which is typical for legal writing
- **Readability**: Requires a 10th grade reading level with a "fairly difficult" reading ease score of 50.8
- **Writing Style**: Moderate sentence length (15.5 words) and word complexity (4.9 characters per word)

## Project Structure

```
supreme-court-sentiment/
├── data/
│   └── raw_opinions/          # Supreme Court opinion text files
│       └── Harvard_2023.txt
├── scripts/
│   ├── collector.py           # Main analysis script (CLI)
│   ├── visualizer.py          # Chart generation script
│   └── test.py               # Testing utilities
├── outputs/
│   ├── analysis_results.csv   # Exported data
│   ├── sentiment_chart.png    # Sentiment visualization
│   └── readability_chart.png  # Readability visualization
├── requirements.txt          # Python dependencies
├── setup_nltk.py            # NLTK data downloader
└── README.md
```

## Completed Milestones

- [x] **Milestone 1:** Environment setup and dependencies
- [x] **Milestone 2:** Text collection and basic statistics
- [x] **Milestone 3:** Sentiment analysis with VADER
- [x] **Milestone 4:** Readability scoring with textstat
- [x] **Milestone 5:** CSV export for data persistence
- [x] **Milestone 6:** Data visualization with matplotlib
- [x] **Milestone 7:** Command-line interface for multiple cases

## Future Improvements

- [ ] **Milestone 8:** Compare sentiment across different justices (majority vs. dissent)
- [ ] **Milestone 9:** Time-series analysis across multiple Supreme Court cases
- [ ] **Milestone 10:** Automated report generation with findings and visualizations
- [ ] Build a web interface for easier analysis
- [ ] Add support for PDF file input
- [ ] Create comparative dashboards across multiple cases
- [ ] Implement topic modeling to identify key themes in opinions

## Author

Tessa Kibbe - Aspiring tech law professional building data analysis skills for legal technology applications

## License

This project is open source and available for educational purposes.
