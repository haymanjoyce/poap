import svgwrite
import pandas as pd

from typing import Dict, List, Optional

from src.poap import SAMPLE_SVG_PATH, SAMPLE_SVG_SCALED_PATH


class Drawing(svgwrite.Drawing):
    def __init__(self, file_path: str = SAMPLE_SVG_PATH):
        super().__init__(file_path, profile='basic')

    def set_view_port(self, width: int, height: int, units: str = 'mm'):
        # viewPort is the visible area of the SVG
        # viewPort is defined using SVG element
        # Set unit identifiers on this element: px, em, cm, mm, in, pt, pc, %, etc.
        # Do not use unit identifiers for child elements
        self['width'] = f'{width}{units}'
        self['height'] = f'{height}{units}'

    def set_view_box(self, width: int, height: int, aspect_ratio: str = 'none'):
        # The viewPort determines how big the map looks on your screen
        # The viewBox determines which part of the map you are looking at and how zoomed in you are
        # The viewBox is defined using the viewBox attribute on the SVG element
        # We want viewBox to be the same as the view port
        # We want to the viewBox to scale with the viewPort (i.e. aspect ratio not preserved)
        self.viewbox(width=width, height=height)
        self.attribs['preserveAspectRatio'] = aspect_ratio

    def print_svg(self):
        print(self.tostring())

    def add_drawing(self, drawing: svgwrite.Drawing):
        self.add(drawing)

    def save_drawing(self):
        self.save()

    def save_drawing_as(self, file_path: str):
        self.saveas(file_path)

