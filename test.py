# from my_lib.imagelib import add_margin

from PIL import Image

im = Image.open('a.png')


def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result


im_new = add_margin(im, 0, 10, 0, 0, (0, 0, 0))
im_new.show()
# im_new.save('a.jpg', quality=95)
