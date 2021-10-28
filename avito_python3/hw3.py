class CountVectorizer:
    """Convert a collection of text documents to a matrix of token counts"""

    def __init__(self):
        pass

    def fit_transform(self, list_of_lines: list):
        """Learn the vocabulary dictionary and return document-term matrix"""
        self.list_of_lines = list_of_lines
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
