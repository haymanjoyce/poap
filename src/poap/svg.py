import svgwrite

from src.poap.config import SAMPLE_SVG_PATH, SAMPLE_SVG_SCALED_PATH


def create_sample_svg(page_width=200, page_height=200):
    # Create an SVG with arbitrary units (here we use pixels)
    dwg = svgwrite.Drawing(SAMPLE_SVG_PATH, profile='tiny')
    dwg.viewbox(width=page_width, height=page_height)  # Define the viewBox in the arbitrary units
    dwg.add(dwg.rect(insert=(0, 0), size=(page_width, page_height), fill='green'))
    half_width = page_width / 2
    half_height = page_height / 2
    dwg.add(dwg.rect(insert=(0, 0), size=(half_width, half_height), fill='blue'))
    dwg.add(dwg.rect(insert=(half_width, half_height), size=(half_width, half_height), fill='red'))

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
    dwg.saveas(SAMPLE_SVG_SCALED_PATH)
