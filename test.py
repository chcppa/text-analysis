import joblib

model = joblib.load("model.pkl")

print(model.predict(['Ты ужасна']))
print(model.predict(['Ты прекрасна']))
print(model.predict(['Ты плохой парень']))
print(model.predict(['Ты хороший парень']))