from sklearn.metrics import classification_report

actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]

report = classification_report(actual, predicted)

print(report)
#         precision    recall  f1-score   support

#            0       0.75      0.75      0.75         4
#            1       0.75      0.75      0.75         4

#     accuracy                           0.75         8
#    macro avg       0.75      0.75      0.75         8
# weighted avg       0.75      0.75      0.75         8
