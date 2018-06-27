
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd


def load_dataset():
    """
    preprocessed dataset (preprocessing should happen somewhere else
    :return:
    """
    from sklearn.datasets import load_iris
    dataset = load_iris()

    X = dataset.data
    y = dataset.target

    return X, y


def humanize_output(model_output):
    from sklearn.datasets import load_iris
    dataset = load_iris()

    labels = dataset.target_names
    print('returning item {} of {}'.format(model_output, labels))

    if type(model_output) == list:
        output = []
        for m in model_output:
            output.append(labels[m])
    else:
        output = labels[model_output]

    return output


def rf_classifier(n_estimators=10):
    from sklearn.ensemble import RandomForestClassifier
    return RandomForestClassifier(n_estimators=n_estimators)


def save_model(model_in, filepath='model.pkl'):
    import pickle
    with open(filepath, 'wb') as f:
        pickle.dump(model_in, f)


def load_model(filepath_in='./ml/saved/model.pkl'):
    import pickle
    with open(filepath_in, 'rb') as nn_model:
        model = pickle.load(nn_model)
        return model


# GET
def predict_iris(x_input):
    global model
    x_np = np.asarray(x_input).reshape(1, len(x_input))

    prediction = model.predict(x_np)

    prediction = prediction.tolist()[0]
    print('we have results! ', prediction)

    return humanize_output(prediction)

# file input POST
def predict_iris_file(x_file_input):
    global model
    input_file = pd.read_csv(x_file_input, header=None)

    #input_file = input_file.values
    print('predicting: ', input_file)

    prediction = model.predict(input_file)

    prediction = prediction.tolist()
    print('we have results! ', prediction)

    return humanize_output(prediction)


model = load_model()




if __name__ == '__main__':
    def train_predict(save=False):
        seed = 42
        X, y = load_dataset()

        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.5)

        print(X_test)

        classifier = rf_classifier()
        classifier.fit(X_train, y_train)

        prediction = classifier.predict(X_test)

        # accuracy
        acc_score = accuracy_score(y_test, prediction)
        print(acc_score)

        if save: save_model(classifier, filepath='./saved/model.pkl')

    t = humanize_output(0)
    print(t)