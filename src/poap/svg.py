import svgwrite
import pandas as pd

from typing import Dict, List, Optional

from src.poap.config import SAMPLE_SVG_PATH, SAMPLE_SVG_SCALED_PATH


class Drawing:
    def __init__(self, dfs: List[pd.DataFrame] = None, file_path: str = SAMPLE_SVG_PATH):
        self.dwg = svgwrite.Drawing(file_path, profile='tiny')

        # self.scales = [df for df in dfs if df.name == 'scales'][0]

    def set_view_port(self, width: int, height: int, units: str = 'mm'):
        # viewPort is the visible area of the SVG
        # viewPort is defined using SVG element
        # Set unit identifiers on this element: px, em, cm, mm, in, pt, pc, %, etc.
        # Do not use unit identifiers for child elements
        self.dwg['width'] = f'{width}{units}'
        self.dwg['height'] = f'{height}{units}'

    def set_view_box(self, width: int, height: int, aspect_ratio: str = 'none'):
        # The viewPort determines how big the map looks on your screen
        # The viewBox determines which part of the map you are looking at and how zoomed in you are
        # The viewBox is defined using the viewBox attribute on the SVG element
        # We want viewBox to be the same as the view port
        # We want to the viewBox to scale with the viewPort (i.e. aspect ratio not preserved)
        self.dwg.viewbox(width=width, height=height)
        self.dwg.attribs['preserveAspectRatio'] = aspect_ratio

    def add_frame(self):
        self.dwg.add(self.dwg.rect(insert=(0, 0), size=(100, 100), fill='green'))

    def save_drawing(self):
        self.dwg.save()

    def save_drawing_as(self, file_path: str):
        self.dwg.saveas(file_path)

