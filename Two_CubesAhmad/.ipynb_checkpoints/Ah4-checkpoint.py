#!/usr/bin/env python
# coding: utf-8
# %%

# %%


# denoised DPIR25 Running out of space on my upload so only denoised the test, but to denoise the train just go to DNCNN/main_dpir.denoising.py and change testsets and resultsets to train instead of test
# and if you are denoising please move preprocessed_data to the DNCNN folder too. I have no datahub space left at all and cant even download the zip file

get_ipython().system('python AhmadChangesTrain4.py')
get_ipython().system('python Evaluate_model_pytorch4.py')

