from urllib2 import urlopen
from PIL import Image

url1 = 'https://cache.movidius.com/images/remote/http_cache.movidius.com/images/made/images/remote/https_movidius-uploads.s3.amazonaws.com/1522334117-movidius-chip-angle-blue-bg-reflection_640_445_s_c1.png'
fileToSave = urlopen(url1)
# manually make a directory images
image1 = Image.open(fileToSave)
image1.save('.\\images\\original.png')
halfSize = (image1.size[0] // 2, image1.size[1] // 2)
halfImage = image1.resize(halfSize, Image.ANTIALIAS)
halfImage.save('.\\images\\half.png')
# transpose
rotation1 = halfImage.transpose(Image.ROTATE_90)
rotation1.save('.\\images\\r90.png')
rotation2 = halfImage.transpose(Image.ROTATE_180)
rotation2.save('.\\images\\r180.png')
rotation3 = halfImage.transpose(Image.ROTATE_270)
rotation3.save('.\\images\\r270.png')
rotation4 = halfImage.rotate(65)
rotation4.save('.\\images\\r65.png')