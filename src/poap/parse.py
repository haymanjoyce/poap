import svgwrite

from src.poap.config import SAMPLE_SVG_PATH


def create_sample_svg():
    # Create an SVG with arbitrary units (here we use pixels)
    dwg = svgwrite.Drawing(SAMPLE_SVG_PATH, profile='tiny')
    dwg.viewbox(width=200, height=100)  # Define the viewBox in the arbitrary units
    dwg.add(dwg.rect(insert=(0, 0), size=(200, 100), fill='green'))
    dwg.add(dwg.rect(insert=(10, 10), size=(100, 50), fill='blue'))
    dwg.add(dwg.rect(insert=(50, 50), size=(150, 50), fill='red'))

    # Set the preserveAspectRatio attribute to 'xMidYMid meet'
    # This will preserve the aspect ratio and scale the SVG to fit within the viewport,
    # aligning the midpoints of the SVG and viewport on the X and Y axes
    dwg.attribs['preserveAspectRatio'] = 'xMidYMid meet'

    # Save the SVG
    dwg.save()

    # Later, when you want to scale the SVG, you can change the width and height attributes
    # For example, to scale to 200mm by 100mm, you would do:
    dwg['width'] = '200mm'
    dwg['height'] = '100mm'

    # Save the scaled SVG
    dwg.saveas('test_scaled.svg')
