# Checking Versions
# Date: 11th March 2018
# Edited by Lee, Stephen 
# How To Use:  
# python3 check_versions_of_TF_Keras_Pytorch.py

import os

print("------------------S T A R T-----------------")
print("Python versions: ")
print("--------------------------------------------")
os.system('python -V')
os.system('python2 -V')
os.system('python3 -V')
#os.system('apt -V')
#os.system('jupyter -V')

print("")
print("--------------------------------------------")
print("Pip versions: ")
print("--------------------------------------------")
os.system('pip -V')
os.system('pip2 -V')
os.system('pip3 -V')

print("")
print("--------------------------------------------")
print("JetPack version: ")
print("--------------------------------------------")
os.system('sudo apt-cache show nvidia-jetpack')

print("")
print("--------------------------------------------")
print("Deep Learning Frameworks: ")
print("--------------------------------------------")
print("TensorFlow Version: ")
print("Python2: ")
os.system("python2 -c 'import tensorflow as tf; print(tf.__version__)' ")
print("Python3: ")
os.system("python3 -c 'import tensorflow as tf; print(tf.__version__)' ")
print("--------------------------------------------")
print("Pytorch Version: ")
print("Python2: ")
os.system("python2 -c 'import torch; print(torch.__version__)' ")
print("Python3: ")
os.system("python3 -c 'import torch; print(torch.__version__)' ")
print("--------------------------------------------")
print("Keras Version: ")
print("Python2: ")
os.system("python2 -c 'import keras; print(keras.__version__)' ")
print("Python3: ")
os.system("python3 -c 'import keras; print(keras.__version__)' ")
os.system('jupyter notebook --version')
print("--------------------------------------------")
print("Scikit-Learn Version: ")
print("Python2: ")
os.system("python2 -c 'import sklearn; print(sklearn.__version__)' ")
print("Python3: ")
os.system("python3 -c 'import sklearn; print(sklearn.__version__)' ")
print("--------------------------------------------")
print("Jupyter-notebook Version: ")
os.system('jupyter notebook --version')
print("--------------------------------------------")
print("OpenCV Version: ")
os.system("python3 -c 'import cv2; print(cv2.__version__)' ")
print("------------------E N D---------------------")

# References:
# https://forums.developer.nvidia.com/t/how-to-check-the-jetpack-version/69549
