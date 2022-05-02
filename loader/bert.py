
import torch
from transformers import AutoTokenizer
from loader.bert_utils.NeuralNet.bertNN import MultiTaskNN


from loader.bert_utils.config.config import config
from loader.bert_utils.schema.schema import *
import gdown
import os
from pathlib import Path


def download_model():
    # script_dir = os.path.dirname(__file__)
    path = "./bin/bert_models/model.pt"
    # abs_file_path = os.path.join(script_dir, rel_path)
    path = Path(path)

    url = "https://drive.google.com/uc?id=1ExkkBYxpuWHb_ffUzGbArgLCbay77_Ip"
    if path.is_file() == False:
        gdown.download(
            url=url, output="./bin/bert_models/model.pt", quiet=False)
    else:
        print('Model file already downloaded')


download_model()


loaded_model = MultiTaskNN(bert_model_name=config["BERT_MODEL_NAME"])
device = torch.device(config['DEVICE'])

loaded_model.load_state_dict(torch.load(
    config['MODEL_PATH']))

loaded_model = loaded_model.to(device)
loaded_model.eval()
loaded_model.freeze()

tokenizer = AutoTokenizer.from_pretrained(config["BERT_MODEL_NAME"])


def encode_text(text: TextInput) -> dict:
    
    encoding = tokenizer.encode_plus(
        text.lower(),
        add_special_tokens=True,
        max_length=config['MAX_TOKEN_LEN'],
        return_token_type_ids=False,
        padding="max_length",
        truncation=True,
        return_attention_mask=True,
        return_tensors='pt'
    )

    return dict(
        input_ids=encoding['input_ids'].flatten(),
        attention_mask=encoding['attention_mask'].flatten()
    )


def get_result(text: TextInput) -> ModelResponse:

    item = encode_text(text)
    with torch.no_grad():
        prediction = loaded_model(
            item['input_ids'].unsqueeze(dim=0).to(device),
            item['attention_mask'].unsqueeze(dim=0).to(device))

        all_task_classes_score = []
        for i in range(3):
            task_classes_score = []
            for idx, score in enumerate(prediction[i].flatten().tolist()):
                task_class_score = TaskClassScore(
                    class_value=config[f"LABELS_{i+1}"][idx], score=score)
                task_classes_score.append(task_class_score)

            all_task_classes_score.append(TaskClassesScore(
                task_id=i+1, scores=task_classes_score))

        return ModelResponse(response=all_task_classes_score)


print('BERT MODEL READY')