# Medical Image Classification Using the MedNIST Dataset

Using Pytorch and Flask

## Requirements

Install them from `requirements.txt`:

    pip install -r requirements.txt

## Model
The improved model is named Mednet, in the model folder


The notebook is :
Blocks_test12c.ipynb


The file with the weights is on the following link :
https://drive.google.com/drive/folders/1i4UJ-neuBW4yNgvzB6QSId-263TPP0Tr?usp=sharing

The DB folder 'resized' is on the following Github link:
https://github.com/BenhajjiNoura/mednist-classification/tree/master/resized


## Local Deployment

Run the server:

    python app.py

Inferface informations:
    Select pitures in the folder 'Prediction_Test'
    Upload the selected pictures
    Selected Pictures will be stored in the relevant subfolders of the 'uploads' folder
    On new selections, only new pictures will be added to the existing folders


## License

The mighty MIT license. Please check `LICENSE` for more details.
