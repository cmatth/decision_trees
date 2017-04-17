import readData as rd
import labels as l
import entropy as ent
import nodes

dataset = 'voting'


# set up dataset then split into training and test
#path = "/home/casey/PycharmProjects/decision_trees/" + dataset + "_data.txt"
path = "/home/kmoney/Documents/decision_trees/decision_trees/" + dataset + "_data.txt"
set = rd.readFromFile(path)
set = rd.parseToArrays(set)
sets = rd.splitIntoSets(set, 3)
train = sets[0] + sets[1]
test = sets[2]

labels = l.getLabels(dataset)
attributes = l.getAttributes(dataset)

tree = nodes.root(train, labels, attributes)

raw_input('begin evaluation')

# Evaluate Test Set Performance
correct = 0
total = len(test)
for x in test:
    if x[labels['class']] == tree.eval(labels, attributes,x):
        correct += 1
    else:
        pass
print "Results: %d \%" %(correct/total)



### TESTING ###
'''
attr = 'doors'
train = ent.divideByAttributes(labels[attr], train, attributes[attr])
for key in train:
    print '***************' + key + '*****************'
    for x in train[key]:
        print x[labels['class']]
'''
'''''
print 'Entropy(S) = %f' %(ent.entropy(train, attributes['class'], labels['class']))

results = []
for attr in attributes:
    pass
    #print 'InfoGain('+ dataset +','+attr+') = %f' \
#%(ent.infoGain(labels[attr], attributes[attr],train,attributes['class'],labels['class']))
print ent.maxInfoGain(train, labels, attributes)
'''