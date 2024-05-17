import datajoint as dj
import numpy as np
import pathlib

# import the mouse-session schema
from . import data_dir as ephys_data_dir
from .mouse_session import schema, Mouse, Session


# Table definitions


@schema
class Neuron(dj.Imported):
    definition = """
    -> Session
    neuron_id: int
    ---
    activity: longblob    # electric activity of the neuron
    """

    def make(self, key):
        # use key dictionary to determine the data file path
        data_file = ephys_data_dir / "data_{mouse_id}_{session_date}.npy".format(**key)

        # load the data
        data = np.load(data_file)

        print(
            "Populating neuron(s) for mouse_id={mouse_id} on session_date={session_date}".format(
                **key
            )
        )
        for idx, d in enumerate(data):
            # add the index of the 1st dimension as neuron_id
            key["neuron_id"] = idx

            # add the loaded data as the "activity" column
            key["activity"] = d

            # insert the key into self
            self.insert1(key)

            print("\tPopulated neuron {neuron_id}".format(**key))


Session.insert1(
    {
        "mouse_id": 100,
        "session_date": "2017-06-01",
        "experiment_setup": 1,
        "experimenter": "Jacob Reimer",
    },
    skip_duplicates=True,
)

Neuron.populate()
