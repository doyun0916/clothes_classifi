from __future__ import print_function, division

import torch.utils.data
from PIL import Image
from torch.autograd import Variable
from torchvision import transforms

model = torch.load("top_long.pt")
model.eval()

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

input_image = Image.open("./1.jpg")
input_image = input_image.crop((409.53107, 179.42564, 779.06305, 641.7564))
input_image.save('_2.jpg')
# http = urllib3.PoolManager()
# r = http.request('GET', 'https://wwws.dior.com/couture/ecommerce/media/catalog/product/cache/1/zoom_image_1/3000x2000/17f82f742ffe127f42dca9de82fb58b1/s/O/1570207502_943C439A4732_C900_E01_ZH.jpg')
# img = Image.open(r)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

def predict_image(image):
    image_tensor = preprocess(image).float()
    image_tensor = image_tensor.unsqueeze_(0)
    input = Variable(image_tensor)
    input = input.to(device)
    output = model(input)
    index = output.data.cpu().numpy().argmax()
    return index

prediction = predict_image(input_image)

if prediction == 0:
    print('cardi')
if prediction == 1:
    print ('coat')
if prediction == 2:
    print ('caot_fur')
if prediction == 3:
    print ('blazer')
if prediction == 4:
    print ('bomber')
if prediction == 5:
    print ('denim')
if prediction == 6:
    print ('leather')
if prediction == 7:
    print ('parka')
if prediction == 8:
    print ('trench_coat')
