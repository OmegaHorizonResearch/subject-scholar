# Subject Scholar is a class for finding hierarchical subject matter motifs in natural language. Finds common word roots and suffixes, thematic phrases, and specialized subject discourses.

# Implementation: use CNN's and a custom information criterion to perform non-specific supervised learning. A model for extracting topics at various levels of linguistic hierarchy is selected and used to analyse bodies of text to determine their topical content. Model selection is a key process of the training phase, as not only do multiple models need to be trained, but compared on the basis of their statistical merits.
import keras, pandas

class Subject_Scholar(object):
    """ A topic analyzer that finds hierarchical subject matter motifs in natural language.

    """
    def __init__(self, num_topics):
        # num_topics = auto or preset value (?)
        pass

    def train(self, training_data, n_gram_size):
        # Assign convolutional outputs to a number of final categories, using the mutual information content with smooth priors to dynamically assign n-grams from samples to topic categories. See "Discriminative Neural Topic Models" by Pandey and Dukkipati for more on this criterion.

        # For word in training_data, add each singleton to our dataframe of inputs

        # For each level of n-gram above 1, systematically add each possible n-gram to our dataframe of inputs

        # Try a number of different synthetic categories, and compare how well each number does for the number or diversity of words we have.


        pass

    def analyse(self, data):
        # Take a sample and return the detected topics it contains.
        pass

    def assign_synthetic_categories(num_categories):
        # use 'num_categories' number of synthetic categories to label the data, optimize the assignment, and report the objective function score.

        # We form n-grams up to the size specified. We use the objective function F(theta) = H(Z|X) + KL(P_Z_j||P_Z; X) - H(Pbar) from Pandey and Dukkipati to assign n-grams to categories. Theta is an assignment of Z to X, F is calculated for all words and all possible assignments. We then use CNN's to perform supervised learning on n-grams and categories, training the CNN to develop appropriate filters for identifying topics from words and n-grams.
        pass
