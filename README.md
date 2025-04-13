Text Processing and Word Cloud Generation from "The Bet" by Anton Chekhov




This project focuses on text processing and natural language processing (NLP) techniques applied to Anton Chekhov's short story "The Bet" from Project Gutenberg. The goal is to analyze the text by tokenizing, generating word clouds, and comparing key linguistic features across the document. Additionally, the project explores the use of TF-IDF (Term Frequency-Inverse Document Frequency) for identifying the most significant words in the text, along with bigram analysis to capture common word pairings.
Objectives

Text Preprocessing: Breaking the text into smaller pieces (tokens) and cleaning it by removing unnecessary characters.

Word Cloud Generation: Creating a visual image showing which words appear most often in the text.

Bigram Analysis: Finding the most common pairs of words (two words next to each other) in the text.

TF-IDF Analysis: Identifying important words by calculating their relevance in the text.

Visualization: Displaying word clouds and showing the most common word pairs to better understand the text.


Tools and Libraries

The project utilizes the following libraries:

    Python

    WordCloud

    Matplotlib

    Scikit-learn

    NLTK/Regex

Setup Instructions

1. Clone the Repository
To set up the project locally, follow the steps below:
git clone https://github.com/katiz1/chekhov-text-analysis.git
cd chekhov-text-analysis

2. Set Up a Virtual Environment
python -m venv venv
source venv/bin/activate or if you're using Windows `venv\Scripts\activate`

3. Install Dependencies
pip install -r requirements.txt

4. Running the Script
   python main.py

   Project Structure

   chekhov_project
- texts/                -> Folder containing the text files
- The_Bet.txt           ->Text file for analysis(The Bet by A.Checkhov)
- images/               -> Folder to store generated word clouds
- main.py               -> Main script for text processing and analysis
- requirements.txt      -> List of project dependencies
- .gitignore            -> Ignores venv

Example Output

Upon running the script, the following will be generated:

    A word cloud image based on the frequency of words in "The Bet".

    A list of top bigrams (word pairs) that appear most frequently in the text.

    The TF-IDF values for the top 5 most important words in the text.

Special Thanks

    Project Gutenberg for making Chekhov’s works freely available.











