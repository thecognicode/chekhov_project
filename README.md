# Text Processing and Word Cloud Generation from "The Bet" by Anton Chekhov




This project focuses on text processing and natural language processing (NLP) techniques applied to Anton Chekhov's short story "The Bet" from Project Gutenberg. The goal is to analyze the text by tokenizing, generating word clouds, and comparing key linguistic features across the document. Additionally, the project explores the use of TF-IDF (Term Frequency-Inverse Document Frequency) for identifying the most significant words in the text, along with bigram analysis to capture common word pairings.

##  What This Project Does

- **Cleans and Preps the Text**  
  Breaks the text into smaller parts (tokens) and removes punctuation and unnecessary characters.

- **Builds a Word Cloud**  
  Creates a visual where frequently used words appear larger—quickly showing what the text is about.

- **Finds Common Word Pairs (Bigrams)**  
  Identifies which two-word combinations show up most often next to each other.

- **Highlights Key Terms with TF-IDF**  
  Uses TF-IDF to spot the most important words—not just frequent, but meaningful in context.

- **Visualizes the Results**  
  Generates word clouds and bar charts to help you understand the text at a glance.



## Tools and Libraries

    Python

    WordCloud

    Matplotlib

    Scikit-learn

    NLTK/Regex

## Getting Started

1. Clone the Repository
To set up the project locally, follow the steps below:
git clone https://github.com/thecognicode/chekhov_project.git

   cd chekhov-text-analysis

3. Set Up a Virtual Environment
python -m venv venv
source venv/bin/activate or if you're using Windows `venv\Scripts\activate`

4. Install Dependencies
pip install -r requirements.txt

5. Running the Script
   python main.py

  ## Project Structure

   chekhov_project
- texts/                -> Folder containing the text files
- The_Bet.txt           ->Text file for analysis(The Bet by A.Checkhov)
- images/               -> Folder to store generated word clouds
- main.py               -> Main script for text processing and analysis
- requirements.txt      -> List of project dependencies
- .gitignore            -> Ignores venv

Example Output

## After executing the script it will generate:

    - A word cloud image based on the frequency of words in "The Bet".

    -A list of top bigrams (word pairs) that appear most frequently in the text.

    - The TF-IDF values for the top 5 most important words in the text.

## Special Thanks

    Project Gutenberg for making Anton Chekhov’s works freely available.











