#!/usr/bin/env python
# coding: utf-8
# %%

# %%


#denoised local means
get_ipython().system('python GaussianRemover.py')
get_ipython().system('python AhmadChangesTrain3.py')
get_ipython().system('python Evaluate_ModelAh3.py')

