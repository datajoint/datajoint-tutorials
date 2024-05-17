import datajoint as dj
from . import data_dir


# fail-safe user name retrieval
username = dj.conn().conn_info["user"]
schema = dj.schema("{}_tutorial_pipeline".format(username))


# Table definitions


@schema
class Mouse(dj.Manual):
    definition = """
    # Experimental animals
    mouse_id             : int                          # Unique animal ID
    ---
    dob=null             : date                         # date of birth
    sex="unknown"        : enum('M','F','unknown')      # sex
    """


@schema
class Session(dj.Manual):
    definition = """
    # Experiment session
    -> Mouse
    session_date               : date                         # date
    ---
    experiment_setup           : int                          # experiment setup ID
    experimenter               : varchar(100)                 # experimenter name
    data_path=''               : varchar(255)                 #
    """


# Insert the following data into the table

mouse_data = [
    {"dob": "2017-03-01", "mouse_id": 0, "sex": "M"},
    {"dob": "2016-11-19", "mouse_id": 1, "sex": "M"},
    {"dob": "2016-11-20", "mouse_id": 2, "sex": "unknown"},
    {"dob": "2016-12-25", "mouse_id": 5, "sex": "F"},
    {"dob": "2017-01-01", "mouse_id": 10, "sex": "F"},
    {"dob": "2017-01-03", "mouse_id": 11, "sex": "F"},
    {"dob": "2017-05-12", "mouse_id": 100, "sex": "F"},
]

session_data = [
    {
        "experiment_setup": 0,
        "experimenter": "Edgar Y. Walker",
        "mouse_id": 0,
        "session_date": "2017-05-15",
        "data_path": data_dir.as_posix(),
    },
    {
        "experiment_setup": 0,
        "experimenter": "Edgar Y. Walker",
        "mouse_id": 0,
        "session_date": "2017-05-19",
        "data_path": data_dir.as_posix(),
    },
    {
        "experiment_setup": 1,
        "experimenter": "Fabian Sinz",
        "mouse_id": 5,
        "session_date": "2017-01-05",
        "data_path": data_dir.as_posix(),
    },
    {
        "experiment_setup": 100,
        "experimenter": "Jacob Reimer",
        "mouse_id": 100,
        "session_date": "2017-05-25",
        "data_path": data_dir.as_posix(),
    },
]

Mouse.insert(mouse_data, skip_duplicates=True)
Session.insert(session_data, skip_duplicates=True)
