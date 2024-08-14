from sklearn.pipeline import Pipeline
from sklearn.dummy import DummyClassifier

predict_level: int = 1
sample_weight_col_name: str = None # not supported yet!

pipeline = Pipeline([
  ("clf", DummyClassifier()),
)

param_grid = {
  "clf__strategy": [“most_frequent”, “prior”]
}


