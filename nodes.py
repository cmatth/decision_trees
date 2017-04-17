import copy
import entropy as ent


tree = []

class root:
    def __init__(self, set, labels, attributes, mostCommon, list):
        self.children = {}
        self.default = 0 #this will hold largest subset for ? values
        self.feature = 'leaf'
        self.leaf = False
        list.append(self)

        # determine feature with highest info gain

        if len(attributes) > 1:
            self.feature = ent.maxInfoGain(set, labels, attributes)[0][0]            #print "feature",self.feature
            if self.feature == 0:
                for x in subsets:
                    print x, "*************subets"
                    print subsets[x]
                print '***************set'
                for x in set:
                    print x
                    print set[x]
                raw_input()
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
                    if len(subsets[x]) > 0:
                        self.children[x] = node(subsets[x], labels, attr, mostCommon, self, list)
                    else:
                        self.children[x] = leaf(mostCommon, self)
                        #print mostCommon

        # create leaf node
        else:
            #designates leaf node with classification
            # for largest class present in node's subset
            subsets = ent.divideByAttributes(labels['class'], set, attributes['class'])
            largest = 0
            for x in subsets:
                #find largest subset for ? values
                if len(subsets[x]) > largest:
                     self.default = x
                     largest = len(subsets[x])

            self.feature = self.default
            self.leaf = True
            #print self.feature

    def eval(self, labels, attributes, case, mostCommon):
        if self.leaf == True:
            #print 'classification', self.feature
            return self.feature
        else:
            case_Res = case[labels[self.feature]]
            if case_Res == '?':
                #print self.default
                try:
                    child = self.children[self.default]
                    return child.eval(labels, attributes, case, mostCommon)
                except:
                    return mostCommon
            else:
                #show(self.children)
                #print self.feature, self.children
                child = self.children[case_Res]
                return child.eval(labels, attributes, case, mostCommon)


class leaf():
    def __init__(self, feature, parent):
        self.feature = feature
        self.parent = parent
        self.leaf = True

    def eval(self, labels, attributes, case, mostCommon):
        return self.feature



class node(root):
    def __init__(self, set, labels, attributes, mostCommon, caller, list):
        self.parent = caller
        root.__init__(self, set, labels, attributes, mostCommon, list)

def show(childs):
    for x in childs:
        print x




