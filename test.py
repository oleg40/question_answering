import nltk
from nltk.corpus import stopwords

corpus = []
directory = "text_data"
with open("text_data/about.txt", "r", encoding="utf-8") as filename:
    corpus = filename.read()



sentences = nltk.sent_tokenize(corpus.lower())


def find_words(query):
    found = []
    words = nltk.word_tokenize(query.lower())
    for sentence in sentences:
        for word in words:
            sentence_wo_stopwords = [word for word in nltk.word_tokenize(sentence) if word not in stopwords.words('english')]
            if word in sentence_wo_stopwords:
                found.append(sentence.capitalize())
    found = set(found)
    answer = " ".join(found)
    return answer


print(find_words("who does improvado help?"))