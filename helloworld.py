import tensorflow as tf
import os
import numpy as np

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10),
    ]
)

predictions = model(x_train[:1]).numpy()
print(predictions, type(predictions))

# to Local
files = os.listdir(".")
for f in files:
    if os.path.isfile(f):
        print(f)
writeMypredictions = open("predictions.txt", "a+")
# for p in predictions[0]:
#     writeMypredictions.write(p + "\n")
predictionsArr = np.array(predictions)
print(type(predictionsArr))
writeMypredictions.write(str(predictionsArr) + "\n")
writeMypredictions.write(str(tf.nn.softmax(predictions).numpy()) + "\n")

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
loss_fn(y_train[:1], predictions).numpy()
model.compile(optimizer="adam", loss=loss_fn, metrics=["accuracy"])

writeMyAnalysis = open("Analysis.txt", "a+")
model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test, verbose=2)
writeMyAnalysis.write(str(np.array(model)))
probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
probability_model(x_test[:5])
