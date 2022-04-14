from skimage.transform import resize

def resize_image(image, proportion):
    assert 0 <= proportion <= 1, "specify a valid proportion between 0 and 1."
    height = round(image.shape[0] * proportion)
    whidth = round(image.shape[1] * proportion)
    image_resized = resize(image, (height, whidth), anti_aliasing=True)
    return image_resized