from typing import List


# I don't like idea of closure, so expected top 5 is a default parameter
def most_frequent_n_words(text: str, top_n: int = 5, min_word_length: int = 3) -> dict:
    dict_of_words = dict()
    for word in [_ for _ in text.split(" ") if len(_) >= min_word_length]:
        if word not in dict_of_words:
            dict_of_words[word] = 1
        else:
            dict_of_words[word] += 1
    dict_of_words[" "] = sum([1 for _ in text if _.isspace()])
    return dict(sorted(dict_of_words.items(), key=lambda x: x[1], reverse=True)[:top_n])
