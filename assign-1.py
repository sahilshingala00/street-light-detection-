from PIL import Image
from PIL import ImageFilter
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import os
import cv2
    
def xml(imgPath):
    image = cv2.imread(imgPath)
    print(imgPath)
    l=imgPath.split('.')
    tree=ET.parse(l[0]+'.xml')
    root=tree.getroot()
    for object in root.findall('object'):
         bndbox = object.find('bndbox')
         xmin = int(float(bndbox.find('xmin').text))
         ymin = int(float(bndbox.find('ymin').text))
         xmax = int(float(bndbox.find('xmax').text))
         ymax = int(float(bndbox.find('ymax').text))
         name=object.find('name').text
         print(name)
         start_point = (xmin,ymin)
         end_point = (xmax,ymax)
         # Blue color in BGR
         color = (255, 0, 0)
         # Line thickness of 2 px
         thickness = 2
         image = cv2.rectangle(image, start_point, end_point, color, thickness)
         # font
         font = cv2.FONT_HERSHEY_SIMPLEX
         # org
         org = (xmin-10, ymin-10)
         # fontScale
         fontScale = 1
         # Using cv2.putText() method
         image = cv2.putText(image,name, org, font, 
                   fontScale, color, 1, cv2.LINE_AA)
    return image
         
         
        
def main():
	# path of the folder containing the raw images
	inPath ="C:\\Users\\Admin\\Desktop\\assignment-box\\intern-assignment\\"

	# path of the folder that will contain the modified image
	outPath ="C:\\Users\\Admin\\Desktop\\assignment-box\\output"
    
	for imagePath in os.listdir(inPath):
		# imagePath contains name of the image
		if (imagePath.endswith(".png") | imagePath.endswith(".jpg")):
			inputPath=os.path.join(inPath,imagePath)
			img = Image.open(inputPath)
			out_img=xml(imagePath)
			fullOutPath=os.path.join(outPath,'invert_'+imagePath)
			#out_img.save(fullOutPath)
			cv2.imwrite(fullOutPath,out_img)
            
if __name__== '__main__':
    main()

   
  
  

  