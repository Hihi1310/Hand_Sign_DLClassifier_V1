import cv2 as cv
import numpy as np
import tensorflow as tf


def load_tf_model(path):
    model= tf.keras.models.load_model(path)
    return model

def get_hand(frame):
    hand= frame[3:323, 3:323]
    img= cv.resize(hand, dsize=(256,256))

    img= cv.cvtColor(img, cv.COLOR_BGR2YCrCb)
    img= cv.GaussianBlur(img, ksize=(3,3), sigmaX=1, sigmaY=1)
    img= cv.cvtColor(img, cv.COLOR_YCrCb2RGB)
    res= img
    return res

label={0:'papper',
      1:'rock',
      2:'scissor',
      3:'unknown'}

def main():
    cam= cv.VideoCapture(0)
    count = 0
    model_path= r'C:\Users\Admin\Desktop\DPL302m\RockPapperScissor\my_model.h5'
    model= load_tf_model(model_path)
    print(model.summary())

    while True:
        ret, frame= cam.read()
        frame= cv.resize(frame,(840,520))
        frame= cv.flip(frame, 1)
        
        hand= get_hand(frame)
        hand= np.divide(hand, 255)
        hand= np.expand_dims(hand, axis=0)

        pred_label= model.predict(hand)
        print(pred_label)
        idx= np.argmax(pred_label)
        print(idx)
        
        text= str(label[idx])+str(pred_label[:,idx])
        frame= cv.rectangle(frame, pt1=(0,0), pt2=(326,326), thickness=3, color=(0,255,0))
        cv.putText(frame, text, (326, 326-10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
        cv.imshow('cam1',frame)
       
        if cv.waitKey(1) & 0xFF == ord('x'):
                break
            
    cam.release()
    cv.destroyAllWindows()
    


if __name__ == '__main__':
    main()

    # model_path= r'C:\Users\Admin\Desktop\DPL302m\RockPapperScissor\my_model.h5'
    # model= load_tf_model(model_path)

    # test_img= r'C:\Users\Admin\Desktop\DPL302m\RockPapperScissor\test_img\papper\papper_2023-05-21_161511_1.png'
    # test_img= cv.imread(test_img)
    # test_img= np.expand_dims(get_hand(test_img), axis=0)
    # print(test_img.shape)
    # label= model.predict(test_img)
    # print(label)