
# Evaluation metrics

- Evaluation metrics are crucial in machine learning (ML) for assessing the performance of models. 
- The choice of metric depends on the type of problem (classification, regression, clustering, etc.).

<!-- Confusion Matrix
AUC
Accuracy etc...

Train test splitting datasets etc.... -->

---

# Classification Metrics

- Accarcy
- Precision
- Recall (Sensitivity, True Positive Rate)
- F1 Score
- Confusion Matrix
- ROC - AUC
- Precision-Recall (PR) AUC
- Log Loss

<!-- ROC (Receiver Operating Characteristic) - AUC (Area Under Curve) -->
---

# Accuracy

- The proportion of correctly predicted instances among the total instances.

$$
    Accuracy = \frac{TP + TN}{TP + TN + FP + FN}
$$


---

# Precision

- Used to evaluate the performance of a classification model. 
- It answers the question, "Of all the instances the model predicted as positive, how many were actually positive?"

$$
    Precision = \frac{TP}{TP+FP}
$$

<!-- $$
    Precision = \frac{80}{80+20} = 0.8
$$ -->

---

# Recall

- known as sensitivity or true positive rate, is used to evaluate the performance of a classification model. 
- Recall is the ratio of true positive predictions to the total number of actual positive instances. 
- It answers the question, "Of all the instances that are actually positive, how many did the model correctly identify as positive?"

$$
    Recall = \frac{TP}{TP + FN}
$$

---

# F1 Score

- Used to evaluate the performance of a classification model by combining precision and recall into a single number. 
- A way to providing a balance between the two metrics. 
- Useful when you need to balance the trade-off between precision and recall, and when the class distribution is imbalanced.

$$
    F1 Score = 2 \times \frac{Precision \times Recall}{Precision+Recall}
$$
---

# Confusion Matrix

<style scoped>
img[alt~="right-centre"] {
  position: absolute;
  top: 150px;
  right: 75px;
}
</style>
![right-centre](image-7.png)

---
# ROC - AUC

<style scoped>
img[alt~="right-centre"] {
  position: absolute;
  top: 50px;
  right: 75px;
  width: 50%
}
</style>

![right-centre](image-9.png)

<!-- 

The ROC-AUC (Receiver Operating Characteristic - Area Under Curve) is a performance metric used to evaluate the ability of a classification model to distinguish between classes. It is particularly useful for binary classification problems.

ROC Curve
The ROC curve is a graphical representation of a model's performance. It plots the True Positive Rate (TPR) against the False Positive Rate (FPR) at various threshold settings. The TPR is also known as recall, and the FPR is defined as the proportion of actual negatives that are incorrectly classified as positives.

The AUC measures the entire two-dimensional area underneath the ROC curve from (0,0) to (1,1). The AUC value ranges from 0 to 1, with a higher value indicating better model performance.

AUC = 0.5: The model has no discriminative power (equivalent to random guessing).
AUC > 0.5: The model has some discriminative power.
AUC = 1: The model has perfect discriminative power.

 -->

<!-- ---

```python
import numpy as np
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

# Example true labels and predicted probabilities
y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.35, 0.8])

# Calculate the ROC curve
fpr, tpr, thresholds = roc_curve(y_true, y_scores)

# Calculate the AUC
auc = roc_auc_score(y_true, y_scores)

# Plot the ROC curve
plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()

print(f'AUC: {auc:.2f}')
``` -->

---

# Precision-Recall (PR) AUC

- The PR curve provides a graphical representation of the trade-off between precision and recall for different threshold values.
- The area under the Precision-Recall curve (PR AUC) summarises the performance of the model across all thresholds. 
- A higher PR AUC value indicates better model performance.

---

```python
import numpy as np
from sklearn.metrics import precision_recall_curve, auc
import matplotlib.pyplot as plt

# Example true labels and predicted probabilities
y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.35, 0.8])

# Calculate the precision-recall curve
precision, recall, thresholds = precision_recall_curve(y_true, y_scores)

# Calculate the PR AUC
pr_auc = auc(recall, precision)

# Plot the precision-recall curve
plt.figure()
plt.plot(recall, precision, color='b', lw=2, label='PR curve (area = %0.2f)' % pr_auc)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend(loc="lower left")
plt.show()

print(f'PR AUC: {pr_auc:.2f}')
```

---

# Log Loss

$$
    \text{Log Loss} = - \frac{1}{N} \sum_{i=1}^{N} \left[ y_i \log(p_i) + (1 - y_i) \log(1 - p_i) \right]
$$
---

$$
\begin{aligned}
\text{Log Loss} &= - \frac{1}{4} \left[ 1 \cdot \log(0.9) + 0 \cdot \log(1 - 0.9) + 0 \cdot \log(0.1) + 1 \cdot \log(1 - 0.1) \right. \\
&\qquad \left. + 1 \cdot \log(0.8) + 0 \cdot \log(1 - 0.8) + 0 \cdot \log(0.4) + 1 \cdot \log(1 - 0.4) \right] \\
&= - \frac{1}{4} \left[ \log(0.9) + \log(1 - 0.1) + \log(0.8) + \log(1 - 0.4) \right] \\
&= - \frac{1}{4} \left[ \log(0.9) + \log(0.9) + \log(0.8) + \log(0.6) \right] \\
&= - \frac{1}{4} \left[ -0.105 + -0.105 + -0.223 + -0.511 \right] \\
&= - \frac{1}{4} \left[ -0.944 \right] \\
&= 0.236
\end{aligned}
$$

<!-- I don't think this is right.... -->

---

```python
from sklearn.metrics import log_loss

# True labels
y_true = [1, 0, 1, 0]

# Predicted probabilities
y_pred = [0.9, 0.1, 0.8, 0.4]

# Calculate log loss
loss = log_loss(y_true, y_pred)

print(f'Log Loss: {loss:.3f}')
```
<!-- Converting the maths formula into code from the previous slide -->

---