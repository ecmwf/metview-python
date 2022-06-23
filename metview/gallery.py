# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

import os
import zipfile

import metview as mv


def load_dataset(filename, check_local=False):
    def _simple_download(url, target):
        import requests

        r = requests.get(url, allow_redirects=True)
        r.raise_for_status()
        open(target, "wb").write(r.content)

    if check_local and os.path.exists(filename):
        try:
            return mv.read(filename)
        except:
            return None

    base_url = "https://get.ecmwf.int/test-data/metview/gallery/"
    try:
        # d = mv.download(url=base_url + filename, target=filename)
        _simple_download(os.path.join(base_url, filename), filename)
    except Exception as e:
        raise Exception(
            f"Could not download file={filename} from the download server. {e}"
        )

    d = None
    if filename.endswith(".zip"):
        with zipfile.ZipFile(filename, "r") as f:
            f.extractall()
    else:
        try:
            d = mv.read(filename)
        except:
            pass
    return d
