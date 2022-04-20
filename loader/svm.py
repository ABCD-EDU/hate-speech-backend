from typing import List
from joblib import load

# TODO: Convert "scores" from list of scores to a dictionary of label -> scores
def get_result(message: str, task_ids: List[int]) -> dict:
    res = []
    message = preprocess(message)

    if 1 in task_ids:
        res.append(create_score_dict(message, 1))
    if 2 in task_ids:
        res.append(create_score_dict(message, 2))
    if 3 in task_ids:
        res.append(create_score_dict(message, 3))
    
    return res

def create_score_dict(message: str, task_id: int) -> dict:
    _scores, _classes = produce_result(message, task_id)
    return {
        "task_id":task_id,
        "scores": [{
            "class": _classes[i],
            "score": _scores[i]
        } for i in range(len(_scores))]
    }

def produce_result(message: str, task_ids:int) -> list:
    model_path: str = "./bin/svm_models/subtask{_task_id}.joblib.z".format(_task_id=task_ids)
    clf = load(model_path)
    
    return list(clf.predict_proba([message.lower()])[0]), list(clf.classes_)

# TODO: Add string preprocessing that is same with what is previously done
# in the notebooks
def preprocess(message: str) -> str:
    return message