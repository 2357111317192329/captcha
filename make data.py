import cv2
import random
import os
import numpy as np
for k in range(1):
     img4 = np.zeros((102,102, 3), np.uint8)
     p=random.randrange(0,34)
     if(p<10):
          pn=str(p)
     elif((p>=10)and(p<18)):
          p+=55
          pn=chr(p)
     elif((p>=18)and(p<23)):
          p+=56
          pn=chr(p)
     else:
          p+=57
          pn=chr(p)
     s='input'+pn+'.png'
     img2 = cv2.imread(s)
     dice=random.randrange(0,2)
     if (dice==1):
          for i in range(102):
               for j in range(102):
                   if((i==0)or(j==0)or(i==101)or(j==101)):
                       num=random.randrange(0,256)
                       img4[i][j][0]=num
                       img4[i][j][1]=num
                       img4[i][j][2]=num
                   else:
                       img4[i][j][0]=img2[i-1][j-1][0]
                       img4[i][j][1]=img2[i-1][j-1][1]
                       img4[i][j][2]=img2[i-1][j-1][2]
     else:
          c=random.randrange(0,256)
          for i in range(102):
               for j in range(102):
                    img4[i][j][0]=c
                    img4[i][j][1]=c
                    img4[i][j][2]=c
     for i in range(100):
         for j in range(100):
             m=int((int(img4[i][j][0])+int(img4[i+1][j][0])+int(img4[i+2][j][0])+int(img4[i][j+1][0])+int(img4[i+2][j+1][0])+int(img4[i][j+2][0])+int(img4[i+1][j+2][0])+int(img4[i+2][j+2][0]))/8)
             r=random.randrange(105,145)
             num=random.randrange(max(m-r,0),min(m+r,255))
             img4[i+1][j+1][0]=num
             img4[i+1][j+1][1]=num
             img4[i+1][j+1][2]=num
     img=img4[1:101,1:101]
     kn=str(k+1)
     if (dice==1):
          dcr='contain'+pn
     else:
          dcr='none'
     ds='data'+kn+dcr+'.png'
     cv2.imwrite(ds,img)
