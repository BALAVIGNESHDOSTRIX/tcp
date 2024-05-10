import os, pickle
from statistics import mode 
import tensorflow as tf
from tensorflow.keras.layers import TextVectorization

def text_vectors(text=''):
	pickle_path = os.path.join('kw_src', 'toxic_vectorizer.pkl')
	from_disk = pickle.load(open(pickle_path, "rb"))
	vector_object = TextVectorization.from_config(from_disk['config'])
	vector_object.set_weights(from_disk['weights'])
	return vector_object(text)

def TSensePredict(text_arr=[]):
	model_path = os.path.join('kw_src', 'toxic_model.h5')
	model = tf.keras.models.load_model(model_path)
	return model.predict(text_arr)


