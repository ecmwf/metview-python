#
# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

import os
import re

from docutils import nodes
from docutils import statemachine
from docutils.parsers.rst import Directive
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter


class MvIncludeCode(Directive):
    """
    Custom directive to insert Python code block with hyperlinks
    to the Metview function documentation pages. Only supposed to be
    working for the Metview gallery examples!
    """

    RE_FUNCTION_PATTERN = re.compile(
        r"""mv<\/span><span class="o">\.<\/span><span class="n">(\w+)<\/span>"""
    )
    required_arguments = 1
    optional_arguments = 0

    def run(self):
        # Get the path to the python example file. All the paths have to be
        # relative to "docs"
        f_path = self.arguments[0]
        if f_path:
            if f_path[0] == "/":
                f_path = f_path[1:]
        else:
            raise self.warning(f"{self.name} empty path specified.")
            return []

        # read the example source and strip off the part
        # preceding the licence statement
        t = ""
        if os.path.exists(f_path):
            with open(f_path, "r") as f:
                t = f.read()
                pos = t.find("#")
                if pos >= 0:
                    t = t[pos:]
        else:
            raise self.warning(f"{self.name} source file={f_path} does not exist.")
            return []

        # generate syntax highlighted text using pygments (html)
        t = highlight(t, PythonLexer(), HtmlFormatter())

        # replace function calls with links to function documentation
        t = re.sub(self.RE_FUNCTION_PATTERN, self.insert_anchor, t)

        # add the resulting text as ".. raw:: html" node
        paragraph_node = nodes.raw("", t, format="html")
        return [paragraph_node]

    def insert_anchor(self, matchobj):
        """
        Replace the captured function name with an achored version
        """
        if matchobj:
            t = matchobj.group(0)
            if len(matchobj.groups()) == 1:
                # the first caputre group is the function name
                fn = matchobj.group(1)
                # check if the function has an rst documentation
                target = os.path.join("api", "functions", fn + ".rst")
                if not os.path.exists(target):
                    target = os.path.join("gen_files", "icon_functions", fn + ".rst")
                    if not os.path.exists(target):
                        return t

                # print(f"fn={fn}")
                # perform the acnhor insertion
                target = os.path.join("..", "..", os.path.dirname(target), fn + ".html")
                t_from = f"""<span class="n">{fn}</span>"""
                t_to = """<span class="n"><a class="reference internal" href="{}#id0" title="{}">{}</span></a>""".format(
                    target, fn, fn
                )
                t = t.replace(t_from, t_to)
            return t
        else:
            return ""

class MvMiniGallery(Directive):
    """
    Custom directive to insert a minigallery into documentation pages.
    """

    required_arguments = 1
    optional_arguments = 0

    def run(self):
        # Get the name of the function
        fn = self.arguments[0]
    
        has_file = False

        # if the notebook minigallery exists we include it with an include directive
        f_path = os.path.join("gen_files", "nb_backref", fn + ".rst")
        if os.path.exists(f_path):
            has_file = True
            t = f".. include:: /gen_files/nb_backref/{fn}.rst" 
            lines = statemachine.string2lines(t, convert_whitespace=True)                                   
            self.state_machine.insert_input(lines, "/" + f_path)
            # return []

        # if the gallery minigallery exists we include it with an include directive
        f_path = os.path.join("gen_files", "gallery_backref", fn + ".rst")
        if os.path.exists(f_path):
            has_file = True
            t = f".. include:: /gen_files/gallery_backref/{fn}.rst" 
            lines = statemachine.string2lines(t, convert_whitespace=True)                                   
            self.state_machine.insert_input(lines, "/" + f_path)
            # return []
        
        # if there is no minigallery we replace the directive with an empty string
        if not has_file:
            paragraph_node = nodes.paragraph(text="")
            return [paragraph_node]
        
        return []


def setup(app):
    app.add_directive("mv-include-code", MvIncludeCode)
    app.add_directive("mv-minigallery", MvMiniGallery)
   
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
