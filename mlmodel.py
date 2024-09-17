import os
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras import (
    models,
    layers,
    applications,
    preprocessing,
    optimizers,
    callbacks,
)
from keras.preprocessing import image
import numpy as np
from PIL import Image as im
# Building the convolutional block
def ConvBlock(inputs, filters=64):
    
    # Taking first input and implementing the conv block
    conv1 = layers.Conv2D(filters, kernel_size=(3, 3), padding="same")(inputs)
    batch_norm1 = layers.BatchNormalization()(conv1)
    act1 = layers.ReLU()(batch_norm1)
    
    # Taking first input and implementing the second conv block
    conv2 = layers.Conv2D(filters, kernel_size=(3, 3), padding="same")(act1)
    batch_norm2 = layers.BatchNormalization()(conv2)
    act2 = layers.ReLU()(batch_norm2)
    
    return act2

# Building the encoder
def encoder(inputs, filters=64):
    
    # Collect the start and end of each sub-block for normal pass and skip connections
    enc1 = ConvBlock(inputs, filters)
    max_pool1 = layers.MaxPool2D(strides=(2, 2))(enc1)
    return enc1, max_pool1

# Building the decoder
def decoder(inputs, skip,filters):
    
    # Upsampling and concatenating the essential features
    upsample = layers.Conv2DTranspose(filters, (2, 2), strides=2, padding="same")(inputs)
    connect_skip = layers.Concatenate()([upsample, skip])
    out = ConvBlock(connect_skip, filters)
    return out

# Building the model
def U_Net(image_size):
    inputs = layers.Input(image_size)
    
    # Constructing the encoder blocks and increasing the filters by a factor of 2
    skip1, encoder_1 = encoder(inputs, 64)
    skip2, encoder_2 = encoder(encoder_1, 64*2)
    skip3, encoder_3 = encoder(encoder_2, 64*4)
    skip4, encoder_4 = encoder(encoder_3, 64*8)
    
    # Preparing the next block
    conv_block = ConvBlock(encoder_4, 64*16)
    
    # Constructing the decoder blocks and decreasing the filters by a factor of 2
    decoder_1 = decoder(conv_block, skip4, 64*8)
    decoder_2 = decoder(decoder_1, skip3, 64*4)
    decoder_3 = decoder(decoder_2, skip2, 64*2)
    decoder_4 = decoder(decoder_3, skip1, 64)
    
    # Output layer
    outputs = layers.Conv2D(1, 1, padding="same", activation="sigmoid")(decoder_4)
    
    model = models.Model(inputs=inputs, outputs=outputs)
    return model
# print(os.path.isfile('./_Net_Forest_Segmentation.h5'))
INPUT_SHAPE = (256, 256, 3)
model = U_Net(INPUT_SHAPE)

# Compiling the model

# model_forest = tf.keras.models.load_model('./U_Net_Forest_Segmentation.h5')
model.load_weights('./U_Net_Forest_Segmentation.h5')

model.compile(optimizer="Adam", loss="binary_crossentropy")
model.summary()
# model.evaluate(x_test, y_test, batch_size=32, verbose=2)
from PIL import Image
import numpy as np
import requests 


def prediction():
    green = 0 
    for i in range(0,16):
        k = i + 1 
        print(type(k))
        print(k)
        k = str(k) 
        print("./static/original/part_"+k+".jpg")
        img = image.load_img("./static/original/part_"+k+".jpg", target_size=(256,256))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        images = x/255    
        array = model.predict(images, batch_size=1)
        array = array.squeeze()
        # array[array >= 0.3] = 1
        # array[array < 0.3] = 0
        # print(array)
        white =0
        black = 0 
        greenThisImg=0
        for l in range(0,256):
            for j in range(0,256):
                greenThisImg+=array[l][j]

        greenThisImg = greenThisImg/(256*256)
        green+=greenThisImg
        binary_array = np.array(array)

    # Convert the binary array to a black and white image
        image_data = binary_array * 255  # Scaling values to 0 and 255 (white and black)
        savedImg = Image.fromarray(image_data.astype('uint8'), mode='L')

        # Save or display the image
        k = i + 1 

        k = str(k)

        print(type(k))
        savedImg.save("./static/mask/mask_"+k+".png")
    return green
    



# print(green)
# # print(array[1:2])
# print(np.matrix(array))
# plt.imshow(array,cmap='gray')

# # plt.plot(array)
# plt.show()
# # array = np.reshape(array, (256, 256,1))
# # print(type(array))



# # Example binary array
# binary_array = np.array(array)

# # Convert the binary array to a black and white image
# image_data = binary_array * 255  # Scaling values to 0 and 255 (white and black)
# image = Image.fromarray(image_data.astype('uint8'), mode='L')

# # Save or display the image
# image.save('forset.png')
# image.show()




# # image_1 = Image.open("/usr/local/src/test1.png")
 
# # image_2 = Image.open("/usr/local/src/test2.png")

# # box = (40, 120)

# # image_1.paste(image_2, box)

# # image_1.save("output/superimposed.png")

# # print(classes)



#     # for l in range(0,256):
#     #     for j in range(0,256):
#     #         if array[l][j] == 1:
#     #             white = white + 1 
#     #         else :
#     #             black = black + 1 
#     # green += white/(white+ black)
#     # binary_array = np.array(array)
