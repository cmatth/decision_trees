def carLabels():
    dict = {     'buying' : 0,
            'maintenance' : 1,
                  'doors' : 2,
                'persons' : 3,
               'lug_Boot' : 4,
                 'safety' : 5,
                  'class' : 6 }
    return dict

def carAttributes():
    dict = {      'doors' : ['2', '3', '4', '5more'],
                  'class' : ['unacc', 'acc', 'good', 'vgood'],
                'persons' : ['2', '4', 'more'],
               'lug_Boot' : ['small', 'med', 'big'],
                 'safety' : ['low', 'med', 'high'],
            'maintenance' : ['vhigh', 'high', 'med', 'low'],
                 'buying' : ['vhigh', 'high', 'med', 'low'] }
    return dict



def cancerAttributes():
    dict = {'class' : ['no-recurrence-events', 'recurrence-events'],
              'age' : ['10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90-99'],
        'menopause' : ['lt40', 'ge40', 'premeno'],
        'tumor-size': ['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59'],
        'inv-nodes' : ['0-2', '3-5', '6-8', '9-11', '12-14', '15-17', '18-20', '21-23', '24-26', '27-29', '30-32', '33-35', '36-39'],
        'node-caps' : ['yes', 'no'],
         'deg-malig': ['1', '2', '3'],
            'breast': ['left', 'right'],
       'breast-quad': ['left-up', 'left-low', 'right-up',	'right-low', 'central'],
          'irradiat': ['yes', 'no'] }
    return dict

def votingAttributes():
    dict = {                     'class' : ['democrat', 'republican'],
                    'handicapped-infants': ['y','n'],
             'water-project-cost-sharing': ['y','n'],
     'adoption-of-the-budget-resolution' : ['y','n'],
                   'physician-fee-freeze': ['y','n'],
                        'el-salvador-aid': ['y','n'],
            'religious-groups-in-schools': ['y','n'],
                'anti-satellite-test-ban': ['y','n'],
              'aid-to-nicaraguan-contras': ['y','n'],
                             'mx-missile': ['y','n'],
                            'immigration': ['y','n'],
           'synfuels-corporation-cutback': ['y','n'],
                     'education-spending': ['y','n'],
                 'superfund-right-to-sue': ['y','n'],
                                  'crime': ['y','n'],
                      'duty-free-exports': ['y','n'],
 'export-administration-act-south-africa': ['y','n'] }
    return dict

def votingLabels():
    dict = {                                 'class': 0,
                               'handicapped-infants': 1,
                        'water-project-cost-sharing': 2,
                 'adoption-of-the-budget-resolution': 3,
                              'physician-fee-freeze': 4,
                                   'el-salvador-aid': 5,
                       'religious-groups-in-schools': 6,
                           'anti-satellite-test-ban': 7,
                         'aid-to-nicaraguan-contras': 8,
                                        'mx-missile': 9,
                                       'immigration': 10,
                      'synfuels-corporation-cutback': 11,
                                'education-spending': 12,
                            'superfund-right-to-sue': 13,
                                             'crime': 14,
                                 'duty-free-exports': 15,
            'export-administration-act-south-africa': 16 }
    return dict

def getLabels(data):
    if data == 'car':
        return carLabels()
    elif data == 'voting':
        return votingLabels()

def getAttributes(data):
    if data == 'car':
        return carAttributes()
    elif data == 'voting':
        return votingAttributes()