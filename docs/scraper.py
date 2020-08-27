from glob import glob
import logging
from pathlib import Path
import shutil
import os
import subprocess

# from pdf2image import convert_from_path
from sphinx_gallery.scrapers import figure_rst

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)


class PNGScraper(object):
    def __init__(self):
        self.seen = set()

    def __repr__(self):
        return "PNGScraper"

    def __call__(self, block, block_vars, gallery_conf):
        # Find all PNG files in the directory of this example.
        path_current_example = os.path.dirname(block_vars["src_file"])
        current_name = Path(block_vars["src_file"]).stem
        pdfs = sorted(
            glob(os.path.join(path_current_example, "{}*.pdf".format(current_name)))
        )
        pngs = []

        LOG.debug("pdfs={}".format(pdfs))
        for pdf in pdfs:
            png = pdf.replace(".pdf", ".png")
            # try:
            #     pages = convert_from_path(pdf, 800)
            #     pages[0].save(png, 'PNG')
            # except Exception as e:
            #     print(e)
            # pngs.append(png)

            cmd = "convert -trim -border 8x8 -bordercolor white {} {}".format(pdf, png)
            try:
                os.system(cmd)
            except Exception as e:
                print(e)
            pngs.append(png)

        # Iterate through PNGs, copy them to the sphinx-gallery output directory
        image_names = list()
        image_path_iterator = block_vars["image_path_iterator"]
        for png in pngs:
            if png not in self.seen:
                self.seen |= set(png)
                this_image_path = image_path_iterator.next()
                image_names.append(this_image_path)
                LOG.debug("generate: {} -> {}".format(png, this_image_path))
                shutil.move(png, this_image_path)
        # Use the `figure_rst` helper function to generate rST for image files
        return figure_rst(image_names, gallery_conf["src_dir"])
