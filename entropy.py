import math

#return a dataset separated into subsets by results of given attribute
def divideByAttributes(attr_index, dataset, attribute):
    subsets = {}
    for x in attribute:
        subsets[x] = []
    subsets['?'] = []
    for x in dataset:
        result = x[attr_index]
        subsets[result].append(x)
    return subsets

# returns entropy measurement of dataset by 'class' attribute
def entropy(dataset, classes, class_index):
    size = len(dataset)
    entropy = 0

    # separate the data set into its classes
    dataset = divideByAttributes(class_index, dataset, classes)

    #measure entropy of each dataset
    for x in dataset:
        x_size =  len(dataset[x])
        if x_size > 0:
            prop = float(x_size) / size
            log = math.log(prop,2)
            entropy += (-1 *prop) * log
    return entropy

def infoGain(attr_index, attribute, set, classes, class_index):
    setEntropy = entropy(set, classes, class_index)
    size = len(set)

    newSets = divideByAttributes(attr_index, set, attribute)
    newEntropy = 0
    for v in newSets:
        v_size = len(newSets[v])
        if v_size != 0:
            v_ent = entropy(newSets[v], classes, class_index)
            newEntropy += (float(v_size) / size) * v_ent
    return (setEntropy - newEntropy)

def maxInfoGain():
    pass
