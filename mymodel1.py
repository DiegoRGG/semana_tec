from tensorflow import keras
from tensorflow.keras import layers


model = keras.models.Sequential([
    layers.Dense(units=1, input_shape=[2,4])
])

print(model.summary())
w,b = model.weights

print(w)
print(w.numpy())
print(b)
print(b.numpy())