# Basado en https://medium.datadriveninvestor.com/easy-implementation-of-decision-tree-with-python-numpy-9ec64f05f8ae

class Nodo:
    def __init__(self):
        
        self.left = None
        self.right = None
        
        self.column = None
        self.threshold = None
        
        self.probas = None
        self.depht = None
        
        self.is_terminal = False

class ArbolDecision:
    def __init__(self, max_depth = 3, min_samples_leaf = 1, min_samples_split = 2):
        
        self.max_deph = max_depth
        self.min_samples_leaf = min_samples_leaf
        self.min_samples_split = min_samples_split
        
        self.clases = None
        
        self.Tree = None
        
    def nodoProbas(self, y):
        probas = []
        
        for c in self.clases:
            proba = y[y == c].shape[0]/y.shape[0]
            probas.append(proba)
        return np.asarray(probas)
    
    def gini(self, probas):
        return 1 - np.sum(probas**2)
    
    def calcImpureza(self, y):
        return self.gini(self.nodoProbas(y))
    
    def calcMejorSplit(self, X, y):
        bestSplitCol = None
        bestThresh = None
        bestInfoGain = -999
        
        impurezaAnterior = self.calcImpureza(y)
        
        for c in range(x.shape[1]):
            x_col = x[:, c]
            
            for x_i in x_col:
                t = x_i # threshold
                y_der = u[x_col > t]
                y_iz = y[x_col <= t]
                
                if y_der.shape[0] == 0 or y_iz.shape[0] == 0:
                    continue
                    
                impurezaDer = self.calcImpureza(y_der)
                impurezaIz = self.calcImpureza(y_iz)
                
                gananciaInfo = impurezaAnterior
                gananciaInfo -= (impurezaIz * y_iz.shape[0])
                
                if gananciaInfo > bestInfoGain:
                    bsetSplitCol = c
                    bestThresh = t
                    bestInfoGain = gananciaInfo
                    
        if bestInfoGain == -999:
            return None, None, None, None, None, None
        
        x_col = X[:, bestSplitCol]
        x_iz, x_der = X[x_col <= bestThresh, :], X[x_col > bestThresh, :]
        y_iz, y_der = y[x_col <= bestThresh], y[x_col > bestThresh]
        
        return bestSplitCol, bestThresh, x_iz, y_iz, x_der, y_der
    
    def construccionArbl(self, X, y, nodo):
        if nodo.depth >= self.max_depth:
            node.is_terminal = True
            return 
        
        if X.shape[0] < self.min_samples_split:
            nodo.in_terminal = True
            return 
        
        if np.unique(y).shape[0] == 1:
            nodo.is_terminal = True
            return
        
        splitCol, thresh, x_iz, y_iz, x_der, y_der = self.calcMejorSplit(X, y)
        
        if splitCol is None:
            node.is_terminal = True
            
        if x_iz.shape[0] < self.min_samples_leafs or x_der.shape[0] < self.min_samples_leafs:
            node.is_terminal = True
            return
        
        nodo.column = splitCol
        nodo.threshold = thresh
        
        nodo.left = Nodo()
        nodo.left.depth = nodo.depth + 1
        nodo.left.probas = self.nodoProbas(y_iz)
        
        nodo.right = Nodo()
        nodo.right.depth = nodo.depth + 1
        nodo.rigth.probas = self.nodoProbas(y_der)
        
        self.construccionArbol(x_der, y_der, nodo.right)
        self.construccionArbol(x_iz, y_iz, nodo.left)
              
        
    
    def fit(self, X, y):
        if type(X) == pd.DataFrame:
            X = np.asarray(X)
            
        self.clases = np.unique(y)
        
        self.Tree = Nodo()
        self.Tree.depth = 1
        self.Tree.probas = self.nodoProbas(y)
        
    def predictSamples(self, x, nodo):
    
        if nodo.is_terminal:
            return nodo.probas

        if x[nodo.column] > nodo.threshold:
            probas = self.predictSample(x, nodo.right)
        else:
            probas = self.predictSample(x, nodo.left)

        return probas
    
    def predict(self, X):
        if type(X) == pd.DataFrame:
            X = np.asarray(X)
            
        predicciones = []
        
        for x in X:
            pred = np.argmax(self.predictSamples(x, self.Tree))
            predicciones.append(pred)
        
        return np.asarray(predicciones)