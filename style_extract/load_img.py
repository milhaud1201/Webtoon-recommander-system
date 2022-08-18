
import torchvision.datasets as dset
import torchvision.transforms as transforms

style_dir = '/Users/gim-yelim/likelion/webtoon/thumbnail_img_kakao/'

def load_img(image_size, style_dir): 
    data = dset.ImageFolder(style_dir,transform= transforms.Compose([
        transforms.Resize(image_size),
        transforms.CenterCrop(image_size),
        transforms.Grayscale(num_output_channels=3),
        transforms.ToTensor()
    ]))
    return data
