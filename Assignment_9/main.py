import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer

# Ensure necessary NLTK resources are downloaded
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('sentiment/vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')

# Function to summarize text
def nltk_summarizer(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())

    # Filter words to remove stop words
    words = [word for word in words if word.isalpha() and word not in stop_words]

    # Calculate word frequencies
    word_freq = nltk.FreqDist(words)

    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Ensure there are sentences to score
    if not sentences:
        return "No sentences found to summarize."

    # Initialize a dictionary to hold sentence scores
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                # Score the sentence based on the frequency of the words it contains
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_freq[word]
                else:
                    sentence_scores[sentence] += word_freq[word]

    # Sort the sentences by score in descending order
    if not sentence_scores:
        return "No sentences scored for summary."

    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:3]  # Select top 3 sentences

    # Create a summary from the selected top sentences
    summary = ' '.join(top_sentences)

    # Clean up sentence endings for better readability
    summary = summary.replace(";", ".").replace(".", ". ")  # Optional: adjust punctuation

    return summary.strip()

# Load reviews from input.txt
file_path = 'input.txt'  # Update with your actual file path
with open(file_path, 'r') as file:
    reviews = file.readlines()

# Initialize Sentiment Intensity Analyzer
sia = SentimentIntensityAnalyzer()

# Categorize reviews based on sentiment
positive_reviews = []
neutral_reviews = []
negative_reviews = []

for review in reviews:
    review = review.strip()
    sentiment_score = sia.polarity_scores(review)
    compound = sentiment_score['compound']

    if compound >= 0.5:
        positive_reviews.append(review)
    elif compound <= -0.2:
        negative_reviews.append(review)
    else:
        neutral_reviews.append(review)
# Plotting the number of reviews in each class
labels = ['Positive', 'Neutral', 'Negative']
counts = [len(positive_reviews), len(neutral_reviews), len(negative_reviews)]

plt.bar(labels, counts, color=['green', 'gray', 'red'])
plt.title('Number of Reviews in Each Sentiment Class')
plt.xlabel('Sentiment Class')
plt.ylabel('Number of Reviews')
plt.ylim(0, max(counts) + 5)  # Set y-axis limit slightly higher than max count
plt.show()

# Summarizing the reviews for each class
positive_text = "\n".join(positive_reviews)
neutral_text = "\n".join(neutral_reviews)
negative_text = "\n".join(negative_reviews)

positive_summary = nltk_summarizer(positive_text)
neutral_summary = nltk_summarizer(neutral_text)
negative_summary = nltk_summarizer(negative_text)

# Print the summaries
print("Positive Summary:", positive_summary)
print("Neutral Summary:", neutral_summary)
print("Negative Summary:", negative_summary)

# Save summaries to separate files
with open('positive_summary.txt', 'w') as pos_file:
    pos_file.write(positive_summary)

with open('neutral_summary.txt', 'w') as neu_file:
    neu_file.write(neutral_summary)

with open('negative_summary.txt', 'w') as neg_file:
    neg_file.write(negative_summary)

print("Summaries have been saved to positive_summary.txt, neutral_summary.txt, and negative_summary.txt.")

