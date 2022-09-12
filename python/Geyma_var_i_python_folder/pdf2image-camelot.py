from stuff import *

from pdf2image import convert_from_path
pdfs = convert_from_path(file)

h,w = get_pdf_size(file)
new_h,new_w = pdfs[0].height, pdfs[0].width
def get_converted_pixel(img, x,y):
    converter_h = new_h/h
    converter_w = new_w/w
    new_x, new_y = converter_w * x, new_h - (converter_h * y)
    return img.getpixel((new_x,new_y))