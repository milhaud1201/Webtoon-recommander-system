from load_img import data 
from gram_matrix import GramMatrix
from resnet import resnet
import torch
from torch.autograd import Variable
from sklearn.decomposition import PCA


def extract_style(data):
    total_arr = []
    label_arr = []

    for idx, (image, label) in enumerate(data):
        i = Variable(image)
        i = i.view(-1, i.size()[0], i.size()[1], i.size()[2])
        
        style_target = list(GramMatrix()(i) for i in resnet(i))
        
        arr = torch.cat([style_target[0].view(-1), style_target[1].view(-1), style_target[2].view(-1), style_target[3].view(-1)])
        gram = arr.cpu().data.numpy().reshape(1, -1)
        
        total_arr.append(gram.reshape(-1))
        label_arr.append(label)
    return total_arr, label_arr

def PCA_style(total_arr):
    return PCA(n_components=2, n_oversamples=5, svd_solver='randomized').fit_transform(total_arr)
