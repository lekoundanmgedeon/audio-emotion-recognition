import pandas as pd
from sklearn.metrics import f1_score, accuracy_score

# Load ground truth and submission
truth = pd.read_csv("data/test_labels.csv")
submission = pd.read_csv("results/submission.csv")

# Merge on ID
merged = truth.merge(submission, on="id")
y_true = merged["label_x"]
y_pred = merged["label_y"]

# Compute metrics
f1 = f1_score(y_true, y_pred, average="macro")
acc = accuracy_score(y_true, y_pred)

print(f"Macro F1-score: {f1:.4f}")
print(f"Accuracy: {acc:.4f}")

# Append to leaderboard
leaderboard = pd.read_csv("results/leaderboard.csv")
new_entry = pd.DataFrame([{"team":"TeamName", "f1":f1, "accuracy":acc}])
leaderboard = pd.concat([leaderboard, new_entry], ignore_index=True)
leaderboard.to_csv("results/leaderboard.csv", index=False)
