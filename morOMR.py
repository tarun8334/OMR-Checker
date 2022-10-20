# Author: @BVK
# Assignment 3: Question 1 Boiler Plate
import cv2 as cv
import numpy as np
# do not import any other library
# Note: this is just a boiler plate
# feel free to make changes in the structure
# however, input/output should essentially be the same.
# IMPORTANT: When you use this, save it in the path src/morOMR.py - if you don't
# your test will fail automatically.
def min1(im,k):
    len,bre = im.shape
    im1 = im.copy()
    k1 =int(k/2)
    n = int((k*k)/2)
    for i in range(k1,len-k1):
        for j in range(k1,bre-k1):
            # v= []
            # for x in range(-k1,k1+1):
            #     for y in range(-k1,k1+1):
            #         v.append(int(im[i+x][j+y])) 
            im1[i][j] = np.min(im[i-k1:i+k1+1,j-k1:k1+1+j])           
            # im1[i][j] = np.min(v)
    return im1    

def threshold(im,k):
    len,bre = im.shape
    for i in range(len):
        for j in range(bre):
            if(im[i][j] > k):
                im[i][j] = 0
            else:
                im[i][j] = 255
    return im  

def max1(im,k):
    len,bre = im.shape
    im1 = im.copy()
    k1 =int(k/2)
    n = int((k*k))
    for i in range(k1,len-k1):
        for j in range(k1,bre-k1):
        #     v= []
        #     for x in range(-k1,k1+1):
        #         for y in range(-k1,k1+1):
        #             v.append(int(im[i+x][j+y]))
        #   #  v.sort()     
            im1[i][j] = np.max(im[i-k1:i+k1+1,j-k1:k1+1+j])           
       
        #     im1[i][j] = np.max(v)
    return im1    

def fun(img,y,x):
    count = 0
    for i in range(30):
        for j in range(30):
            if img[y+i][x+j] == 255:
                count = count+1
    if count >= 200:
       return 1
    else:
        return 0            

def option(img,y_cord,x_cord,i):
    if i <= 14:
       return 1*fun(img,y_cord[i],x_cord[0]) +  2*fun(img,y_cord[i],x_cord[1]) +3*fun(img,y_cord[i],x_cord[2]) +4*fun(img,y_cord[i],x_cord[3])

    elif i <=29:
       return 1*fun(img,y_cord[i-15],x_cord[4]) +  2*fun(img,y_cord[i-15],x_cord[5]) +3*fun(img,y_cord[i-15],x_cord[6]) +4*fun(img,y_cord[i-15],x_cord[7])

    else:
       return 1*fun(img,y_cord[i-30],x_cord[8]) +  2*fun(img,y_cord[i-30],x_cord[9]) +3*fun(img,y_cord[i-30],x_cord[10]) +4*fun(img,y_cord[i-30],x_cord[11])

def anskey(img,y_cord,x_cord):
    len,bre = img.shape
    final_ans = np.zeros(45)
    for i in range(45):
        final_ans[i] = option(img,y_cord,x_cord,i)
    return final_ans


def getAnswers(img)->list:
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    thresholded_img = threshold(img,70)
    eroded_img = min1(thresholded_img,7)
    dilated_img = max1(eroded_img,7)

    y_cord = np.zeros(15)
    y_cord[0] = 800
    y_cord[1] = 842
    y_cord[2] = 884
    y_cord[3] = 926
    y_cord[4] = 968
    y_cord[5] = 1010
    y_cord[6] = 1054
    y_cord[7] = 1096
    y_cord[8] = 1138
    y_cord[9] = 1180
    y_cord[10] = 1222
    y_cord[11] = 1264
    y_cord[12] = 1308
    y_cord[13] = 1350
    y_cord[14] = 1393
    y_cord = y_cord.astype('int')

    # print(y_cord)

    x_cord = np.zeros(12)
    x_cord[0] = 222
    x_cord[1] = 262
    x_cord[2] = 307
    x_cord[3] =  349
    x_cord[4] = 560
    x_cord[5] = 602
    x_cord[6] = 645
    x_cord[7] = 686
    x_cord[8] = 896
    x_cord[9] = 937
    x_cord[10] = 980
    x_cord[11] = 1022
    x_cord = x_cord.astype('int')
    # print(x_cord)
    ## lenght breadth 20 pix each
    # img = cv2.imread('./imgs/ans.png')
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # org = img.copy()
    v = anskey(dilated_img,y_cord,x_cord)
    v = v.astype('int')
    final = [-1]*45
    for i in range(45):
        if v[i] == 1:
            final[i] = 'A'
        elif v[i] == 2:
             final[i] = 'B'
        elif v[i] == 3:
             final[i] = 'C'
        elif v[i] == 4:
            final[i] = 'D'
        else:
            final[i] = -1
    return final                         







if __name__ == "__main__":
  
  # Read the number of test cases
  # input() returns str by default, i.e. 1000 is read as '1000'.
  # .strip() used here to strip of the trailing `\n` character
      
  T = int(input().strip())
                           
  
  for i in range(T):
    
    fileName = input().strip() # read path to image
    omr_sheet = cv.imread(fileName)
    
    
    answers = getAnswers(omr_sheet) # fetch your answer
    for answer in answers: # assuming answers is a list
      print(answer)  # print() function automatically appends the `\n`
