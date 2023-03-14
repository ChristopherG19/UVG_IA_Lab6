def gini(y):
    # p = y.value_counts()/y.shape[0]
    p = np.unique(y, return_counts = True)[1]
    gini = 1-np.sum(p**2)
    return gini
    
    
def varianza(y):
    if (len(y) == 1):
        return 0
    else:
        return y.var()
    
    
def ganancia_info(y, mask, fun = gini):
    a = sum(mask)
    b = mask.shape[0] - a
    
    if (a == 0 or b == 0):
        ig  = 0
        
    else:
        if y.dtypes != 'O':
            ig = varianza(y) - (a/(a+b)* varianza(y[mask])) - (b/(a+b)*varianza(y[-mask]))
        else:
            ig = func(y)-a/(a+b)*func(y[mask])-b/(a+b)*func(y[-mask])
            
    return ig

import itertools

def opciones_categoricas(a):
    
    a = np.unique(a, return_counts = True)[1]
    
    opciones = []
    for L in range(len(a) + 1):
        for subset in itertootls.combinations(a, L):
            subset = list(subset)
            opciones.append(subset)
            
    return opciones[0:-1]

def max_ganancia_info_split(x, y, func=gini):
    
    split_value = []
    ig = []
    
    variable_num = True if x.dtypes != 'O' else FAlse
    
    # Crear opciones
    if variable_num:
        opciones = np.sort(np.unique(x))[1:]
    else:
        opciones = opciones_categoricas(x)
        
    # calcular ig para todos los valroes
    for val in opciones:
        mask = x < val if variable_num else x.isin(val)
        val_ig = ganancia_info(y, mak, func)
        
        # Agregar resultado
        ig.append(val_ig)
        split_value.append(val)
        
        
    if len(ig) == 0:
        return(None, None, None, False)
    
    else:
        best_gi = max(ig)
        best_ig_index = ig.index(best_ig)
        best_split = split_value[best_ig_index]
        return(best_ig,best_split,numeric_variable, True)
    
def get_mejor_split(y, data):
    masks = data.drop(y, axis = 1)