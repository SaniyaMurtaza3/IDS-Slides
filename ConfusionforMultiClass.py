from sklearn.metrics import confusion_matrix,classification_report
from sklearn.metrics import  ConfusionMatrixDisplay
import numpy as np
import matplotlib.pyplot as plt
# #### Classes ##########
# C=Cats, D=Dogs, W=Wolf, T=Tiger
y_actual  = ['C','C','T','D','D','C','W','T','C','D',
             'W','C','C','T','D', 'C','W','T','D','T',
             'W','D','C','W','T','W','D','C','D','T',
             'D','W','W','T','C','D','T']#37
y_predict = ['C','C','C','D','W','T','D','T','C','D',
             'D','T','C','C','D','T','W','T','C','D',
             'D','C','W','C','D','D','W','C','D','D',
             'W','T','W','C','C','W','T']#37
cm = confusion_matrix(y_true=y_actual, y_pred=y_predict)
cm = np.transpose(cm)
print(cm)
cm_report = classification_report(y_actual,y_predict, digits=3)
print(cm_report)
cmd = ConfusionMatrixDisplay(cm, display_labels=['C','D','T','W'])
cmd.plot(colorbar=False, cmap='Blues')
cmd.ax_.set(xlabel='Actual', ylabel='Predicted', title='Confusion Matrix Actual vs Predicted')
plt.show()
