import datajoint as dj
import numpy as np
import os
from skimage import io

# import the mouse-session schema
from .mouse_session import schema, Mouse, Session


# Table definitions


@schema
class Scan(dj.Manual):
    definition = """
    -> Session
    scan_idx    : int           # scan index
    ---
    depth       : float         # depth of this scan
    wavelength  : float         # wavelength used
    laser_power : float         # power of the laser used
    fps         : float         # frames per second
    file_name    : varchar(128) # name of the tif file
    """


@schema
class AverageFrame(dj.Imported):
    definition = """
    -> Scan
    ---
    average_frame   : longblob     # average fluorescence across frames
    """

    def make(
        self, key
    ):  # key is the primary key of one of the entries in the table `Scan`
        # fetch data directory from table Session
        data_path = (Session & key).fetch1("data_path")

        # fetch data file name from table Scan
        file_name = (Scan & key).fetch1("file_name")

        # load the file
        im = io.imread(os.path.join(data_path, file_name))
        # compute the average image across the frames
        avg_image = np.mean(im, axis=0)

        # Now prepare the entry as a dictionary with all fields defined in the table.
        key["average_frame"] = avg_image  # inherit the primary key from the table Scan

        # insert entry with the method `insert1()`
        self.insert1(key)

        print("\tPopulated Scan {mouse_id} - {session_date} - {scan_idx}".format(**key))


Scan.insert(
    [
        {
            "mouse_id": 0,
            "session_date": "2017-05-15",
            "scan_idx": 1,
            "depth": 150,
            "wavelength": 920,
            "laser_power": 26,
            "fps": 15,
            "file_name": "example_scan_01.tif",
        },
        {
            "mouse_id": 0,
            "session_date": "2017-05-15",
            "scan_idx": 2,
            "depth": 200,
            "wavelength": 920,
            "laser_power": 24,
            "fps": 15,
            "file_name": "example_scan_02.tif",
        },
        {
            "mouse_id": 100,
            "session_date": "2017-05-25",
            "scan_idx": 1,
            "depth": 150,
            "wavelength": 920,
            "laser_power": 25,
            "fps": 15,
            "file_name": "example_scan_03.tif",
        },
    ],
    skip_duplicates=True,
)

AverageFrame.populate()
