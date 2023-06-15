#!/usr/bin/env python
# coding: utf-8
# %%

# %%


#this will run the baseline
# I set everything up so it will just run my pretrained checkpoint, because it takes a long time to train and I'm assuming you guys do not want to retrain everything
# but if you do want to train for some reason just set load_check=False in the training code
get_ipython().system('python AhmadChangesTrain.py')
get_ipython().system('python Evaluate_model_pytorch.py')

