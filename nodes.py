import copy
import entropy as ent

tree = []

class root:
    def __init__(self, set, labels, attributes):
        self.children = {}
        self.default = 0#this will hold largest subset for ? values
        self.feature = 'leaf'
        self.leaf = False

        # determine feature with highest info gain
        if len(attributes) > 1:
            feature = ent.maxInfoGain(set, labels, attributes)[1][0]

            # remove it from subsequent versions of attributes
            attr = copy.deepcopy(attributes)
            del attr[feature]

            # split set into subsets by feature value
            subsets = ent.divideByAttributes(labels[feature], set, attributes[feature])

            #create a child node for each value of feature
            for x in subsets:
                #find largest subset for ? values
                if len(x.value) > default:
                    default = x
                if x != '?':
                    self.children[feature] = node(x, labels, attr, self)
        # create leaf node
        else:
            #designates leaf node with classification
            # for largest class present in node's subset
            classes = attributes["class"]
            for x in classes:
                #find largest subset for ? values
                if len(x.value) > default:
                    default = x
            self.feature = default
            self.leaf = True

    def eval(self, labels, attributes, case):
        if self.leaf == True:
            return self.feature
        else:
            case_Res = "shoo im cwint"




class node(root):
    def __init__(self, set, labels, attributes, caller):
        self.parent = caller



