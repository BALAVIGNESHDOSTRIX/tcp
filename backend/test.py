from kw_src.toxic_predictor import text_vectors, TSensePredict
import numpy as np


vector = text_vectors("fuck")
res = TSensePredict(np.expand_dims(vector,0))
print((res > 0.5).astype(int))