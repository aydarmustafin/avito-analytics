#!/usr/bin/env python
# coding: utf-8

# In[175]:


class CountVectorizer:
    """Convert a collection of text documents to a matrix of token counts"""

    def __init__(self, list_of_lines):
        self.list_of_lines = list_of_lines
        pass

    def fit_transform(self):
        """Learn the vocabulary dictionary and return document-term matrix"""
        list_of_lists_of_words = [line.lower().split() for line in self.list_of_lines]
        unique_words_list = list(dict.fromkeys([word.lower() for line in self.list_of_lines for word in line.split()]))

        fit_transform_list = []

        for line in list_of_lists_of_words:
            fit_transform_line = []
            for word in unique_words_list:
                fit_transform_line.append(line.count(word))
            fit_transform_list.append(fit_transform_line)

        return fit_transform_list

    def get_feature_names(self):
        """Get feature names"""
        unique_words_list = list(dict.fromkeys([word.lower() for line in self.list_of_lines for word in line.split()]))

        return unique_words_list


# In[176]:


corpus = [
 'Crock Pot Pasta Never boil pasta again',
 'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]
vectorizer = CountVectorizer(corpus)
print(vectorizer.fit_transform())
print(vectorizer.get_feature_names())

