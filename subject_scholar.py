# Subject Scholar is a class for finding hierarchical subject matter motifs in natural language. Finds common word roots and suffixes, thematic phrases, and specialized subject discourses.

# Implementation: use CNN's and a custom information criterion to perform non-specific supervised learning. A model for extracting topics at various levels of linguistic hierarchy is selected and used to analyse bodies of text to determine their topical content. Model selection is a key process of the training phase, as not only do multiple models need to be trained, but compared on the basis of their statistical merits.
import keras, pandas

from sklearn.decomposition import TruncatedSVD

class Subject_Scholar(object):
    """ A topic analyzer that finds hierarchical subject matter motifs in natural language.

    """
    def __init__(self, num_topics):
        # Attribute to hold all Singular Value Decomposition transformers.
        self.SVDs = {}
        # Attribute to hold the objective score for each number of categories.
        self.scores = {}
        pass

    def train(self, training_data, n_gram_sizes, num_categories):
        # training_data should be raw text data.
        # num_cats should be a list of category sizes to try.
        """
        Section: Building N-Grams from a Corpus
        """
        # Assign words and phrases to a number of final categories, using the mutual information content with smooth priors to dynamically assign n-grams from samples to topic categories. See "Discriminative Neural Topic Models" by Pandey and Dukkipati for more on this criterion.

        # For word in training_data, add each singleton to our dataframe of inputs

        # For each level of n-gram above 1, systematically add each possible n-gram to our dataframe of inputs. We form n-grams up to the size specified.
        """
        Section: Obtaining an Ideal Synthetic Topic Assignment.
        """
        # Try a number of different synthetic categories, and compare how well each number does for the number or diversity of words we have.
        self.X = training_data
        # We can use something like LSA or SVD in sklearn to find topics through decomposition. We can try different thresholds to satisfy some criterion.
        for size in num_categories:
            self.assign_synthetic_categories(size)

        """
        Section: Training a CNN to Model Topics in Text.
        """
        # Once we have assigned topics to n-grams and documents, we have a supervised learning problem.
        # We need to vectorize our text.
        model = Sequential()
        # Some CNN layers would be good.
        # A final softmax layer for probabilistic predictions.
        # We can save the final model both with and without the final softmax layer.
        self.model = model
        pass

    def analyse(self, data):
        # Take a sample and return the detected topics it contains.
        pass

    def assign_synthetic_categories(num_categories):
        # use 'num_categories' number of synthetic categories to label the data, optimize the assignment, and report the objective function score.

        # Use the objective function F(theta) = H(Z|X) + KL(P_Z_j||P_Z; X) - H(Pbar) from Pandey and Dukkipati to assign n-grams to categories. Theta is an assignment of Z to X, F is calculated for all words and all possible assignments. We then use CNN's to perform supervised learning on n-grams and categories, training the CNN to develop appropriate filters for identifying topics from words and n-grams.

        svd = TruncatedSVD(n_components = num_categories)
        svd.fit_transform(self.X)
        self.SVDs[num_categories] = svd
        pass

    def objective_score(grams, topics, SVD, num_categories):
        # go through the grams and their assigned topics and use an objective function to assess how good or appropriate the whole assignment is. We can use scipy.stats.entropy to do the entropy calculations.
        objective_score = 0
        # TODO: Calculate objective score for the chosen SVD, num_categories, and assignments.
        self.scores[num_categories] = objective_score
        return objective_score

    def vectorize_text(text):
        # Transforms text into vectors of vectors. Uses a letter-based scheme instead of a fixed vocabulary.
