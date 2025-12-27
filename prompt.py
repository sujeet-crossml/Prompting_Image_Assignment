from PIL import Image

# Prompt
prompt = '''
I have given you an image of form that has stored some INFORMATION.
 Read that information from the image and show all the necessary details from the image.
'''
# Opening Image
image = Image.open("form.png")
# image2  = Image.Image.load("form.png")

# system_instruction
system_instruction = '''
    You are an image analyst.
    Your work is to read the details of image and show the relevent details from image.
    '''
