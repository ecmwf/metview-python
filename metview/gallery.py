# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

import zipfile

import metview as mv


def load_dataset(filename):
    base_url = "http://download.ecmwf.org/test-data/metview/gallery/"
    try:
        d = mv.download(url=base_url + filename, target=filename)
        if filename.endswith(".zip"):
            with zipfile.ZipFile(filename, "r") as f:
                f.extractall()
        return d
    except:
        raise Exception(
            "Could not download file " + filename + " from the download server"
        )
