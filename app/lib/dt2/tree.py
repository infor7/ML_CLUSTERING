from IPython import get_ipython
# For testing in IPython
get_ipython().magic('reset -f')
get_ipython().magic('load_ext autoreload')
get_ipython().magic('aimport node')
get_ipython().magic('autoreload 1')

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.datasets import load_iris
from sklearn.datasets import load_breast_cancer
from sklearn.datasets import load_digits
from sklearn.datasets import load_wine

# Self implemented classes
from node import Node



class Tree:
    def __init__(self, target, data, metric = "gini", max_depth = 0, min_split = 2, min_members = 1, min_gain = 0):
        self.root = Node(target, data)
        self.metric = metric
        self.max_depth = max_depth
        self.min_split = min_split
        self.min_members = min_members
        self.min_gain = min_gain



    
    def fit_cart(self, target, data, depth):
        """ Basic CART algorithm using gini impurity"""
        parent_score = Node.gini(self.root.target)
        gain = 0.0
        split_feature = None
        split_value = None
        split_datasets = None

        features_count = self.root.data.shape[1]

        for feature in range(0, features_count):
            vals, counts = np.unique(self.root.data[:,feature], return_counts = True)
            for val in vals:
                t_target, t_data, f_target, f_data = Node.split_data(self.root.target, self.root.data, feature, val)
                p = (len(t_target) / (len(t_target) + len(f_target)))
                new_gain = parent_score - p*Node.gini(t_target) - (1-p)*Node.gini(f_target)

        if gain > self.min_gain:
            t_children = fit_cart(t_target, t_data, depth + 1)
            f_children = fit_cart(f_target, f_data, depth + 1)
            return Node(target, data, depth, )
        else:



    
    def fit_id3(self, target, data):
        """Pseudo ID3 implementation
         - prunes used features, but can works with non-binary targets"""
        parent_score = Node.entropy(self.root.target)
        gain = 0.0
        split_feature = None
        split_value = None
        split_datasets = None

        features_count = self.root.data.shape[1]
        for feature in range(0, features_count):
            vals, counts = np.unique(self.root.data[:,feature], return_counts = True)
            for val in vals:
                t_target, t_data, f_target, f_data = Node.split_data(self.root.target, self.root.data, feature, val)
                p = (len(t_target) / (len(t_target) + len(f_target)))
                new_gain = parent_score - p*Node.entropy(t_target) - (1-p)*Node.entropy(f_target)


        pass


    def fit(self):
        if self.metric == "gini":
            self.fit_cart(self.root.target, self.root.data, 0)
        else:
            self.fit_id3(self.root.target, self.root.data, 0)


    def fit(self):
        if gain > self.min_gain:
            t_children = fit

    
    def classify(data):
            pass


    


# Testcode
def main():
    print("Running Decision Tree Example: iris")
    iris = load_iris()
    iris_tree_g = Tree(iris.target, iris.data)
    iris_tree_g.fit()

    print("Running Decision Tree Example: wine")
    wine = load_wine()


    print("Running Decision Tree Example: cancer")
    cancer = load_breast_cancer()

    # Warning - very slow
    print("Running Decision Tree Example: digits")





if __name__ == "__main__":
    main()