import os

# clean models directory ../models
#############################################
model_dir = '../models'
models = os.listdir(model_dir)
for i in models:
	path = os.path.join(model_dir,i)
	os.system('rm ' + path)
os.system('rm result_*')