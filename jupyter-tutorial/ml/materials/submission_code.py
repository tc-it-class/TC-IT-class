
x_train, y_train, x_test = load_fashionmnist()

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def softmax(x):
    # WRITE ME

# weights
W = # WRITE ME
b = # WRITE ME

# 学習データと検証データに分割
x_train, x_valid, y_train, y_valid = train_test_split(x_train, y_train, test_size=0.1)

def train(x, t, eps=1.0):
    # WRITE ME

def valid(x, t):
    # WRITE ME

for epoch in range(1):
    # オンライン学習
    # WRITE ME

y_pred = # WRITE ME

submission = pd.Series(y_pred, name='label')
submission.to_csv('/root/userspace/submission_pred.csv', header=True, index_label='id')
