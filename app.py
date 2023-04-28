import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

corpus = []
directory = "text_data"
with open("text_data/texts.txt", "r", encoding="utf-8") as filename:
    corpus = filename.read()


sentences = nltk.sent_tokenize(corpus.lower())


def find_words(query):
    # Matches words from user's query with sentences from texts
    query_words = nltk.word_tokenize(query)
    lemmatizer = WordNetLemmatizer()
    best_sent = {}
    for sentence in sentences:
        for query_word in query_words:
            # Lemmatizing both query and texts and avoiding the most common and useless words
            sentence_wo_stopwords = [lemmatizer.lemmatize(text_word) for text_word in nltk.word_tokenize(sentence) if text_word not in stopwords.words('english') and text_word != "?"]
            if query_word[0].isupper() and lemmatizer.lemmatize(query_word.lower()) in sentence_wo_stopwords:
                best_sent[sentence] = best_sent.get(sentence, 0) + 1000
                # print(lemmatizer.lemmatize(query_word))

            else:
                if lemmatizer.lemmatize(query_word.lower()) in sentence_wo_stopwords:
                    # print(lemmatizer.lemmatize(query_word))
                    best_sent[sentence] = best_sent.get(sentence, 0) + 1
    # print(f"best sent: {best_sent}")
    try:
        best_match_sent = max(best_sent, key=best_sent.get)
        # Adding the next sentense as well just in case
        result = f"{best_match_sent.capitalize()} {sentences[sentences.index(best_match_sent) + 1].capitalize()}"
        # print(f"\n \n \n \n best sent: {best_sent}")
        return result
    except ValueError:
        return "Sorry, I don't know the answer"


your_question = "What are the types of data validation?"
print(find_words(your_question))
# print(stopwords.words('english'))
