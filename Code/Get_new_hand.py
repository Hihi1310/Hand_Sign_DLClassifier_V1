import cv2
import os
import time
import datetime
import time

def move_img(old_dir, new_dir): #the old dir and the new dir must have identical root dir
    imgs= os.listdir(old_dir)
    exist_labels= os.listdir(new_dir) #the existing labels

    for img in imgs:
        old_path= os.path.join(old_dir, img)
        temp= img[:img.index('_')]
        if temp not in exist_labels:
            new_folder= os.path.join(new_dir, temp)
            new_path= os.path.join(new_folder, img)
            os.makedirs(new_folder)
            exist_labels= os.listdir(new_dir) #update label
            os.rename(old_path, new_path)
            continue
        else:
            folder= os.path.join(new_dir, temp)
            new_path = os.path.join(folder, img)
            os.rename(old_path, new_path)
            continue
    return

def capture(img, count):
    
    # get current time
    current_date = str(datetime.datetime.today())[:19]
    current_date = current_date.replace(' ', '_').replace(':', '')

    print('capture successfully')
    new_img_place= os.path.join(Dir_path_temp, f'{label}_{current_date}_{count}.png')

    print(new_img_place)# save place
    cv2.imwrite(new_img_place, img)
    os.chdir(Dir_path_temp)


#Some constant paramater
Dir_path_temp= r'C:\Users\Admin\Desktop\DPL302m\RockPapperScissor\temp'
Dir_path_main= r'C:\Users\Admin\Desktop\DPL302m\RockPapperScissor\img'
cam= cv2.VideoCapture(0)

label = input('Enter label name: ').lower()

def main():
    max_count=50
    interval= 1
    count= 0

    start_time= time.time()
    interval= 2
    second_counter= 10
    gate= None
    wait_time=10

    while True:
        ret, frame= cam.read()
        frame= cv2.resize(frame,(840,520))
        frame= cv2.flip(frame, 1)
        frame= cv2.rectangle(frame, pt1=(0,0), pt2=(326,326), thickness=3, color=(0,255,0))
        cv2.imshow('cam1',frame) 
        
        current_time= time.time()
        time_pass= current_time-start_time
        # print(int(time_pass))
        
        if int(time_pass) == wait_time:
            print('start')
            gate= True

        if int(time_pass) == second_counter and gate:
            count+=1
            second_counter+= interval
            capture(frame[3:323, 3:323], count)
            print(frame[3:353, 3:353].shape)
            
        
        if count==max_count:
            break
       
        if cv2.waitKey(1) & 0xFF == ord('x'):
                break
        
       
            
    cam.release()
    cv2.destroyAllWindows()
    move_img(old_dir=Dir_path_temp, new_dir=Dir_path_main)


if __name__ == '__main__':
    main()