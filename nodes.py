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
            self.feature = ent.maxInfoGain(set, labels, attributes)[0][0]
            if self.feature == 'class':
                self.feature = ent.maxInfoGain(set,labels,attributes)[1][0]

            # remove it from subsequent versions of attributes
            attr = copy.deepcopy(attributes)
            del attr[self.feature]

            # split set into subsets by feature value
            subsets = ent.divideByAttributes(labels[self.feature], set, attributes[self.feature])

            #create a child node for each value of feature
            for x in subsets:
                #find largest subset for ? values
                if len(subsets[x]) > self.default:
                    if x != '?':
                        self.default = x
                if x != '?':
                    self.children[x] = node(subsets[x], labels, attr, self)
        # create leaf node
        else:
            #designates leaf node with classification
            # for largest class present in node's subset
            classes = attributes["class"]
            subsets = ent.divideByAttributes(labels['class'], set, attributes['class'])
            for x in classes:
                #find largest subset for ? values
                if len(subsets[x]) > self.default:
                    default = x
            self.feature = self.default
            self.leaf = True

    def eval(self, labels, attributes, case):
        print self.leaf
        if self.leaf == True:
            return self.feature
        else:
            case_Res = case[labels[self.feature]]
            if case_Res == '?':
                print self.default
                child = self.children[self.default]
                return child.eval(labels, attributes, case)
            else:
                #show(self.children)
                child = self.children[case_Res]
                return child.eval(labels, attributes, case)





class node(root):
    def __init__(self, set, labels, attributes, caller):
        self.parent = caller
        root.__init__(self, set, labels, attributes)

def show(childs):
    for x in childs:
        print x




