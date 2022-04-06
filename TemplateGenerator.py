'''
Generator file for the activities screen of the ESSF

@Author: Pim van Leeuwen 
@Date: 23-10-2021
'''

from PIL import Image, ImageFont, ImageDraw
import PIL

# This will be the image that is used as a template, this is in the same folder. 
template_image = Image.open("Template.png")
# These are the positions of the different elements, 4x (date-y, title-y, logo-y)
template_positions = [0.17, 0.21, 0.158, 0.31, 0.35, 0.301, 0.45, 0.495, 0.445, 0.61, 0.65, 0.60]
# This is just to make the image editable
editable_image = ImageDraw.Draw(template_image)

# These are the two fonts for the date and the main event title
date_font = ImageFont.truetype("Fonts/Montserrat-Regular.otf", 130)
main_font = ImageFont.truetype("Fonts/Montserrat-Bold.otf", 270)

# This will be the data from the input file, in the following format:
'''
date 1 
event 1
ssa 1
date 2
event 2
ssa 2
date 3 
event 3
ssa 3
date 4 
event 4
ssa 4
'''
# If a line is missing, DO STILL INSERT A WHITELINE. Empty lines will be counted and just left empty (also for logos)
# White lines at the end can be left out
input_data = open("input.txt", "r")
lines = input_data.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")

# For each of the at most 4 activities we do this
for i in range(len(lines)):
    # The date of the activity
    if (i % 3 == 0):
        editable_image.text((template_image.width*0.06,template_image.height*template_positions[i]), lines[i], 
            (255,255,255), font=date_font)

    # The title of the activity
    elif (i % 3 == 1):
        editable_image.text((template_image.width*0.06,template_image.height*template_positions[i]), lines[i], 
            (255,255,255), font=main_font)

    # The logo of the association (currently have essf + 37 ssas), spaces must be in here, no initials. 
    # so NOT ESTC TWIST, but Twist (or TWIST, twist, capitals are irrelevant)
    else:
        if not (lines[i].replace(" ", "") == ""):
            # This makes sure that all the images have the same color coding which is needed for pasting them over each
            # other 
            logo = Image.open("Logo/" + lines[i].lower() + ".png").convert("RGBA")

            # We resize the image whilst keeping the aspect ratio.
            ratio = logo.width/logo.height
            logo = logo.resize((int(template_image.height*0.12*ratio),int(template_image.height*0.12)), 
                PIL.Image.NEAREST)
            
            # Then we past the image on the correct spot in the template.
            template_image.paste(logo, (int(template_image.width*0.78), 
                int(template_image.height*template_positions[i])), logo)

# We save the final image in the output.png file
template_image.save("output.png")