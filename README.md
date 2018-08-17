# Heritage Recognition with Deep Learning

#To train and use deep learning model:

*Install Depemdncies: python - 3.5.5, keras-2.2.0, matplotlib - 2.2.2, numpy - 1.15.0, opencv - 3.4.1, pillow- 5.2.0, scikit-learn - 0.19.1, tensorflow - 1.9.0

1. Download and extract DL model for Heritages folder.
2. Download image dataset from this link https://drive.google.com/open?id=1XBWU8mc81FJMYFcs8O4nzcxrIo5iTrM7 and extract inside previous folder.
3. Open CMD(Command Prompt) from inside the folder and run 'VGG16_Custom.py'
   -->> python VGG16_Custom.py
4. Model is trained and saved as 'trained_model.hdf5'
5. To recognise an image with trained model run 'recogniser.py'
   -->> python recogniser.py
6. Select a photo from Test images folder and output will be displayed in console. 

#To run Web Application:

*Install dependencies: python - 3.5.5, django-1.9.2, keras-2.2.0, matplotlib - 2.2.2, numpy - 1.15.0, opencv - 3.4.1, pillow- 5.2.0, scikit-learn - 0.19.1, tensorflow - 1.9.0
1. Download and extract Heritages WebApp folder.
2. Open CMD(Command Prompt) from inside the folder.
3. Run command 'python manage.py runserver' and copy server address.
4. Enter server adress in a web browser and WebApp is ready to use. 


