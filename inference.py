import json

from commons import get_model, transform_image
from PIL import Image
import torch
import os
import sys
from models.mednet import MedNet




model = MedNet(64,64,6)
model.load_state_dict(torch.load('./models/saved_model_12c.pt'))
model.eval()
imagenet_class_index = json.load(open('imagenet_class_index.json'))


def to_numpy(tensor):
    return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()

def get_prediction(image_bytes):
    try:
        img_y = transform_image(image_bytes)
        output = model(img_y)
        print(output)
        pred = output.max(1)[1].tolist()[0]
        print('########',file=sys.stderr)
        print(pred,file=sys.stderr)
        print(type(pred),file=sys.stderr)
        print('########',file=sys.stderr)
    except Exception:
        return 404, 'error'
    return pred, imagenet_class_index.get(str(pred))

   