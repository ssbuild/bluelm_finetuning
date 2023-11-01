# -*- coding: utf-8 -*-
# @Time:  23:20
# @Author: tk
# @File：model_maps
from aigc_zoo.constants.define import (TRANSFORMERS_MODELS_TO_LORA_TARGET_MODULES_MAPPING,
                                       TRANSFORMERS_MODELS_TO_ADALORA_TARGET_MODULES_MAPPING,
                                       TRANSFORMERS_MODELS_TO_IA3_TARGET_MODULES_MAPPING,
                                       TRANSFORMERS_MODELS_TO_IA3_FEEDFORWARD_MODULES_MAPPING)

__all__ = [
    "TRANSFORMERS_MODELS_TO_LORA_TARGET_MODULES_MAPPING",
    "TRANSFORMERS_MODELS_TO_ADALORA_TARGET_MODULES_MAPPING",
    "TRANSFORMERS_MODELS_TO_IA3_TARGET_MODULES_MAPPING",
    "TRANSFORMERS_MODELS_TO_IA3_FEEDFORWARD_MODULES_MAPPING",
    "MODELS_MAP"
]

MODELS_MAP = {
    'BlueLM-7B-Chat': {
        'model_type': 'BlueLM',
        'model_name_or_path': '/data/nlp/pre_models/torch/bluelm/BlueLM-7B-Chat',
        'config_name': '/data/nlp/pre_models/torch/bluelm/BlueLM-7B-Chat/config.json',
        'tokenizer_name': '/data/nlp/pre_models/torch/bluelm/BlueLM-7B-Chat',
    },
    'BlueLM-7B-Chat-32K': {
        'model_type': 'BlueLM',
        'model_name_or_path': '/data/nlp/pre_models/torch/bluelm/BlueLM-7B-Chat-32K',
        'config_name': '/data/nlp/pre_models/torch/bluelm/BlueLM-7B-Chat-32K/config.json',
        'tokenizer_name': '/data/nlp/pre_models/torch/bluelm/BlueLM-7B-Chat-32K',
    },
    'BlueLM-7B-Base': {
        'model_type': 'BlueLM',
        'model_name_or_path': '/data/nlp/pre_models/torch/opt/BlueLM-7B-Base',
        'config_name': '/data/nlp/pre_models/torch/opt/BlueLM-7B-Base/config.json',
        'tokenizer_name': '/data/nlp/pre_models/torch/opt/BlueLM-7B-Base',
    },

    'BlueLM-7B-Base-32K': {
        'model_type': 'BlueLM',
        'model_name_or_path': '/data/nlp/pre_models/torch/opt/BlueLM-7B-Base-32K',
        'config_name': '/data/nlp/pre_models/torch/opt/BlueLM-7B-Base-32K/config.json',
        'tokenizer_name': '/data/nlp/pre_models/torch/opt/BlueLM-7B-Base-32K',
    },

}


# 按需修改
# TRANSFORMERS_MODELS_TO_LORA_TARGET_MODULES_MAPPING
# TRANSFORMERS_MODELS_TO_ADALORA_TARGET_MODULES_MAPPING
# TRANSFORMERS_MODELS_TO_IA3_TARGET_MODULES_MAPPING
# TRANSFORMERS_MODELS_TO_IA3_FEEDFORWARD_MODULES_MAPPING




