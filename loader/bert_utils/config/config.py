
import torch

GLOBAL_CONFIG = {
    "MODEL_PATH": "./bin/bert_models/model.pt",
    "USE_CUDA_IF_AVAILABLE": True,
    "ROUND_DIGIT": 9,
    'MAX_TOKEN_LEN': 256,
    "BERT_MODEL_NAME": 'bert-base-uncased'
}

TASKS_LABELS = {
    "LABELS_1": ['HATE', 'NOT', 'OFFENSIVE'],
    "LABELS_2": ['PROFANITY'],
    "LABELS_3": ['Race', 'Religion', 'Gender', 'Other', 'None']
}


def get_config() -> dict:
    config = GLOBAL_CONFIG.copy()
    config.update(TASKS_LABELS)

    config['DEVICE'] = 'cuda' if torch.cuda.is_available(
    ) and config['USE_CUDA_IF_AVAILABLE'] else 'cpu'

    return config


config = get_config()
