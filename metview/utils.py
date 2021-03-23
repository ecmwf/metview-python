#
# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import getpass
import logging
import shutil
import os
import tempfile

LOG = logging.getLogger(__name__)


CACHE_DIR = os.path.join(tempfile.gettempdir(), f"mpy-{getpass.getuser()}")


def unpack(file_path, remove=False):
    if any(file_path.endswith(x) for x in [".tar", ".tar.gz", ".tar.bz2"]):
        target_dir = os.path.dirname(file_path)
        LOG.debug(f"file_path={file_path} target_dir={target_dir}")
        shutil.unpack_archive(file_path, target_dir)
        if remove:
            os.remove(file_path)


def download(url, target):
    from tqdm import tqdm
    import requests

    resp = requests.get(url, stream=True)
    total = int(resp.headers.get("content-length", 0))
    with open(target, "wb") as file, tqdm(
        desc=target,
        total=total,
        unit="iB",
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)


class Cache:
    ROOT_DIR = os.path.join(tempfile.gettempdir(), f"mpy_ds_{getpass.getuser()}")

    def all_exists(self, items, path):
        for name in items:
            p = os.path.join(path, name)
            # print(f"p={p}")
            if not os.path.exists(p):
                return False
            elif os.path.isdir(p):
                cnt_file = os.path.join(path, f".cnt_{name}")
                # print(f"cnt_file={cnt_file}")
                if os.path.exists(cnt_file):
                    with open(cnt_file, "r") as f:
                        try:
                            cnt_ref = int(f.read())
                            # print(f"cnt_ref={cnt_ref}")
                            if cnt_ref > sum(
                                [len(files) for r, d, files in os.walk(p)]
                            ):
                                return False
                        except:
                            return False
                else:
                    return False
        return True

    def make_reference(self, items, path):
        for name in items:
            p = os.path.join(path, name)
            if os.path.isdir(p):
                cnt_file = os.path.join(path, f".cnt_{name}")
                with open(cnt_file, "w") as f:
                    f.write(str(sum([len(files) for r, d, files in os.walk(p)])))


CACHE = Cache()
