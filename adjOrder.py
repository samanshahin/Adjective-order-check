import spacy
import pandas as pnd

    def adjOrder(s):
        adjOrderedCorrect = 0
        n = 0
        natCat = pnd.read_csv('csv/natCat.csv')  # importing from ...Cat.csv files
        natCat = natCat.transpose()
        colorCat = pnd.read_csv('csv/colorCat.csv')
        colorCat = colorCat.transpose()
        ageCat = pnd.read_csv('csv/ageCat.csv')
        ageCat = ageCat.transpose()
        shapeCat = pnd.read_csv('csv/shapeCat.csv')
        shapeCat = shapeCat.transpose()
        qualCat = pnd.read_csv('csv/qualCat.csv')
        qualCat = qualCat.transpose()
        adjOrderList = []
        for k in range(len(s)):
            if (s[k].pos_ == 'ADJ'):
                if (len(adjOrderList) >= 1 and str(adjOrderList[-1]) != 'VERB'):
                    adjOrderList.append(str(adjOrderList[-1]) + ' ' + str(s[k]))
                adjOrderList.append(str(s[k]))
            if (s[k].pos_ != 'ADJ'):
                adjOrderList.append('VERB')
        print(f"adjOrderList : {adjOrderList}")
        print('start checking adj order')
        for adj in str(adjOrderList):
            if(adj != 'VERB'):
                ll = len(adj)-n-1
                for n in range(len(adj)):
                    if (adj[ll] in natCat):
                        adjOrderedCorrect += 1
                        break
                    if (adj[ll] in colorCat):
                        adjOrderedCorrect += 1
                        break
                    if (adj[ll] in ageCat):
                        adjOrderedCorrect += 1
                        break
                    if (adj[ll] in shapeCat):
                        adjOrderedCorrect += 1
                        break
                    if (adj[ll] in qualCat):
                        adjOrderedCorrect += 1
                        break
            if (adjOrderedCorrect == 1):
                print('This adjective combination is NOT ordered correctly:\n' + adj)
