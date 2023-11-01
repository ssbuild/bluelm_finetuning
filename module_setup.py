# -*- coding: utf-8 -*-
# @Author  : ssbuild
# @Time    : 2023/8/16 16:03

from deep_training.utils.hf import register_transformer_model,register_transformer_config,register_transformer_tokenizer
from transformers import AutoModelForCausalLM
from aigc_zoo.model_zoo.bluelm.llm_model import MyBlueLMForCausalLM,BlueLMTokenizer,BlueLMConfig
__all__ = [
    "module_setup"
]

def module_setup():
    # 导入模型
    register_transformer_config(BlueLMConfig)
    register_transformer_model(MyBlueLMForCausalLM, AutoModelForCausalLM)
    register_transformer_tokenizer(BlueLMConfig,BlueLMTokenizer,BlueLMTokenizer)