from urllib2 import urlopen
from PIL import Image
import ssl
url1 = 'https://www.cwb.gov.tw/V7/forecast/fcst/Data/I04_small.jpg'
context = ssl._create_unverified_context()
imageFile1 = urlopen(url1,context=context)
image1 = Image.open(imageFile1)
image1.save(".\\images\\normal.jpg")
halfSize = (image1.size[0]/2, image1.size[1]/2)
halfImage = image1.resize(halfSize, Image.ANTIALIAS)
halfImage.save('.\\images\\small.jpg')
rot1 = image1.transpose(Image.ROTATE_90)
rot1.save('.\\images\\r90.jpg')
