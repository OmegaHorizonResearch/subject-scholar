# Subject Scholar is a class for finding hierarchical subject matter motifs in natural language. Finds common word roots and suffixes, thematic phrases, and specialized subject discourses.

# Implementation: use CNN's and a custom information criterion to perform non-specific supervised learning. A model for extracting topics at various levels of linguistic hierarchy is selected and used to analyse bodies of text to determine their topical content. Model selection is a key process of the training phase, as not only do multiple models need to be trained, but compared on the basis of their statistical merits.

class Subject_Scholar(object):
    """ A topic analyzer that finds hierarchical subject matter motifs in natural language.

    """
    def __init__(self, num_topics):
        # num_topics = auto or preset value (?)
        pass

    def train(self, training_data):
        # Assign convolutional outputs to a number of final categories, using the mutual information content with smooth priors to dynamically assign n-grams from samples to topic categories. See "Discriminative Neural Topic Models" by Pandey and Dukkipati for more on this criterion.
        pass

    def analyse(self, data):
        pass
