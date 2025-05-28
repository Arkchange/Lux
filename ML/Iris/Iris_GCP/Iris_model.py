{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3055833a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['iris_model.pkl']"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.datasets import load_iris\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "import joblib\n",
    "\n",
    "iris = load_iris()\n",
    "X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)\n",
    "\n",
    "model = RandomForestClassifier()\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "joblib.dump(model, \"iris_model.pkl\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "env",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
