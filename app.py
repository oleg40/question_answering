import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the texts and preprocess
text_dir = 'text_data'
texts = []
for file in os.listdir(text_dir):
    if file.endswith('.txt'):
        with open(os.path.join(text_dir, file), 'r', encoding='utf-8') as f:
            text = f.read().lower()
            text = ' '.join([word for word in word_tokenize(text) if word not in stopwords.words('english')])
            texts.append(text)

# Create a corpus
corpus = '\n'.join(texts)

# Tokenize the corpus
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform([corpus])

# Process the questions
def process_question(question):
    question = question.lower()
    question = ' '.join([word for word in word_tokenize(question) if word not in stopwords.words('english')])
    return question

# Search and match
def search_and_match(question):
    question = process_question(question)
    question_tfidf = tfidf_vectorizer.transform([question])
    similarity_scores = cosine_similarity(question_tfidf, tfidf_matrix)[0]
    max_index = similarity_scores.argmax()
    return texts[max_index]

# Answer the question
def answer_question(question):
    answer = search_and_match(question)
    return answer

# Example usage
question = "Reporting efforts?"
answer = answer_question(question)
print(answer)
