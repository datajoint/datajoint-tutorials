# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.5.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Working with automated computations: Imported tables

# Welcome back! In this session, we are going to continue working with the pipeline for the mouse electrophysiology example.
#
# In this session, we will learn to:
#
# * import neuron activity data from data files into an `Imported` table
# * automatically trigger computations for all missing entries with `populate`

# First thing first, let's import `datajoint` again.

import datajoint as dj

# As we are going to perform some computations, let's go ahead and import NumPy as well as Matplotlib.

import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

# Now we would like to continue working with the tables we defined in the previous notebook. To do so, we would need the classes for each table: `Mouse` and `Session`. We can either redefine it here, but for your convenience, we have included the schema and table class definitions in a package called `tutorial_pipeline.mouse_session`, from which you can import the classes as well as the schema object. We will use the schema object again to define more tables.

import sys
sys.path.append("..")
from tutorial_pipeline.mouse_session import schema, Mouse, Session

Mouse()

Session()

# The `mouse_session.py` also fills each table with data to make sure we are all on the same page.

# ## Importing data from data files

# Recall from the project description
# > * In each experimental session, you record electrical activity from a single neuron. You use recording equipment that produces separate data files for each neuron you recorded.
#
# Our recording equipment produces a data file for each neuron recorded. Since we record from one neuron per session, there should be one data file for each session.

# In the `data` directory, you will find `.npy` (saved NumPy array) files with names like `data_100_2017-05-25.npy`.

# As you might have guessed, these are the data for the recording sessions in the `Session` table, and each file are named according to the `mouse_id` and `session_date` - the attributes of the primary keys - in the format `data_{mouse_id}_{session_date}.npy`.
#
# So `data_100_2017-05-25.npy` is the data for session identified by `mouse_id = 100` and `session_date = "2017-05-25"`.

# ## Looking at the data

# Let's take a quick peak at the data file content.

# First, let's pick a session to load the data for. To do this we are going to first fetch the **primary key attributes** of `Session` as a list of dictionaries. We make use of the special `fetch('KEY')` syntax to achieve this.

keys = Session.fetch('KEY')
keys

# Any item in this list of keys can be used to uniquely identify a single session!

# ENTER YOUR CODE! - restrict session using keys and any element inside keys.


# Let's take the first key, and generate the file name that corresponds to this session. Remember the `data_{mouse_id}_{session_date}.npy` filename convetion!

key = keys[0]
key

filename = 'data/data_{mouse_id}_{session_date}.npy'.format(**key)
filename

# Here we have made use of Python's dictionary unpacking and `format` method on strings to generate the filename from the `key`.
#
# Finally, let's load the file.

data = np.load(filename)

# Look at its content...

data

# ...and check the shape of the data.

data.shape


# So this particular file contains a NumPy array of size 1 x 1000. This represents a (simulated) recording of raw electric activity from neuron(s) (1st dimension) over 1000 time bins (2nd dimesion).

# ## Defining the table for recorded neurons

# We now would like to have all these recorded `Neuron` represented and stored in our data pipeline.
#
# Since there may be multiple neurons recorded from each session, a `Neuron` can be uniquely identified by knowing the `Session` it was recorded in, as well as its `neuron_id`. For each `Neuron`, we want to store the neural activity found in the data file.

@schema
class Neuron(dj.Imported):
    definition = """
    -> Session
    neuron_id: int
    ---
    activity: longblob    # electric activity of the neuron
    """

# Let's check the state of our pipeline.

# ENTER YOUR CODE! - plot a Diagram of the schema


# We defined `activity` as a `longblob` so that it can store a NumPy array holding the electric activity over time. This NumPy array will be imported from the file corresponding to each neuron.

# Note that our `Neuron` class inherits from `dj.Imported` instead of `dj.Manual` like others. This is because **this table's content will depend on data imported from an external file**. The `Manual` vs `Imported` are said to specify the **tier of the table**.

# ## DataJoint table tiers

# In DataJoint, the tier of the table indicates **the nature of the data and the data source for the table**. So far we have encountered two table tiers: `Manual` and `Imported`, and we will encounter the two other major tiers in this session.
#
# DataJoint tables in `Manual` tier, or simply **Manual tables** indicate that its contents are **manually** entered by either experimenters or a recording system, and its content **do not depend on external data files or other tables**. This is the most basic table type you will encounter, especially as the tables at the beggining of the pipeline. In the Diagram, `Manual` tables are depicted by green rectangles.
#
# On the other hand, **Imported tables** are understood to pull data (or *import* data) from external data files, and come equipped with functionalities to perform this importing process automatically, as we will see shortly! In the Diagram, `Imported` tables are depicted by blue ellipses.

dj.Diagram(schema)

# ## Importing data into the `Imported` table

# Rather than filling out the content of the table manually using `insert1` or `insert` methods, we are going to make use of the `make` and `populate` logic that comes with `Imported` tables to automatically figure out what needs to be imported and perform the import!

# ## `make` and `populate` methods

# `Imported` table comes with a special method called `populate`. Let's try calling it.

# ENTER YOUR CODE! - call `populate` on the table


# Notice that `populate` call complained that a method called `make` is not implemented. Let me show a simple `make` method that will help elucidate what this is all about.

@schema
class Neuron(dj.Imported):
    definition = """
    -> Session
    neuron_id: int
    ---
    activity: longblob    # electric activity of the neuron
    """
    def make(self, key): # `make` takes a single argument `key`
        print('key is', key)

# Now, let's call `populate` again!

# ENTER YOUR CODE! - call `populate` on the table


# When you call `populate` on an `Imported` table, this triggers DataJoint to look up all tables that the `Imported` table depends on.
#
# For **every unique combination of entries in the depended or "parent" tables**, DataJoint calls `make` function, passing in the primary key of the parent(s).

# Because `Neuron` depends on `Session`, `Neuron`'s `make` method was called for each entry of `Session`

Session()


# Note that `make` only receives the *primary key attributes* of `Session` (`mouse_id` and `session_date`) but not the other attributes.

# ## Implementing `make`

# Now we have a better understanding of `make`, let's implement `make` to perform the importing of data from file.

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
        data_file = "data/data_{mouse_id}_{session_date}.npy".format(**key)

        # load the data
        data = np.load(data_file)

        for idx, d in enumerate(data):
            # add the index of the 1st dimension as neuron_id
            key['neuron_id'] = idx

            # add the loaded data as the "activity" column
            key['activity'] = d

            # insert the key into self
            self.insert1(key)

            print('Populated neuron={neuron_id} for mouse_id={mouse_id} on session_date={session_date}'.format(**key))


# Notice that we added the missing attribute information `activity` into the `key` dictionary, and finally **inserted the entry** into `self` = `Neuron` table. The `make` method's job is to create and insert a new entry corresponding to the `key` into this table!

# Finally, let's go ahead and call `populate` to actually populate the `Neuron` table, filling it with data loaded from data files!

Neuron.populate()

Neuron()

# As you can obviously see, in these example datasets, we only have data for one neuron per session.

# What happens if we call `Neuron.populate` again?

Neuron.populate()

# That's right - nothing! This makes sense, because we have imported `Neuron` for all entries in `Session` and nothing is left to be imported.

# Now what happens if we insert a new entry into `Session`?

Session.insert1({
    "mouse_id": 100,
    "session_date": "2017-06-01",
    "experiment_setup": 1,
    "experimenter": "Jacob Reimer"
})

# We can find all `Session` without corresponding `Neuron` entry with the **negative restriction operator** `-`

# select all Session entries *without* a corresponding entry in Neuron
Session - Neuron

Neuron.populate()

Neuron()

# # Summary

# Congratulations! You have successfully extended your pipeline with a table to represent recorded data (`Neuron` as `Imported` table), learned and implemented the `make()` and `populate()` call to load external data to your tables.

dj.Diagram(schema)

# At this point, our pipeline contains the core elements with data populated, ready for further downstream analysis.
#
# In the next [session](./03-Computed%20Table%2C%20Lookup%20Table%2C%20and%20Part%20Table%20-%20Interactive.ipynb), we are going to introduce the concept of `Computed` table, and `Lookup` table, as well as learning to set up a automated computation routine.
