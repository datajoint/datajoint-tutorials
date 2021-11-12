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

# # Working with automated computations: Computed tables

# Welcome back! In this session, we are going to continue working with the pipeline for the mouse electrophysiology example.
#
# In this session, we will learn to:
#
# * compute various statistics for each neuron by defining a `Computed` table
# * define a `Lookup` table to store parameters for computation
# * define another `Computed` table to perform spike detection and store the detected spikes
# * automatically trigger computations for all missing entries with `populate`
# * define a `Part` table to save the results computed with the master `Computed` table

# First thing first, let's import `datajoint` again.

import datajoint as dj

# As we are going to perform some computations, let's go ahead and import NumPy as well as Matplotlib.

import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

# Similarly as before, to continue working with the tables we defined in the previous notebook, we can either redefine the classes for each table `Mouse`, `Session`, `Neuron` and populate them. Or, again for your convenience, we can import them from the `tutorial_pipeline.ephys_cell_activity` module.

import sys
sys.path.append("..")
from tutorial_pipeline.ephys_cell_activity import schema, Mouse, Session, Neuron

Session()

Neuron()

# The `ephys_cell_activity.py` also fills each table with data and import the neuron activity data from `.npy` files to make sure we are all on the same page.

# # Computations in data pipeline

# Now we have successfully imported all data we have into our pipeline, it's time for us to start analyzing them!
#
# When you perform computations in the DataJoint data pipeline, you focus and design tables in terms of **what** is it that you are computing rather than the **how**. You should think in terms of the "things" that you are computing!

# Now, let's say that we want to compute the satististics, such as mean, standard deviation, and maximum value of each of our neuron's activity traces. Hence we want to compute the neuron's **activity statistics** for each neuron!

# So the new "thing" or entity here is `ActivityStatistics`, where each entry corresponds to the statistics of a single `Neuron`. Let's start designing the table, paying special attention to the dependencies.

# ### Statistics of neuron activities

# Before we create the table to store the statistics, let's think about how we might go about computing interesting statistics for a single neuron.
#
# Let's start by fetching one neuron to work with.

# +
keys = Neuron().fetch('KEY')

# pick one key
key = keys[0]
# -

Neuron() & key

# Lets go ahead and grab the `activity` data stored as numpy array. As we learned in the last session, we can `fetch` it!

activity = (Neuron() & key).fetch('activity')

activity

# It's a bit subtle, but `fetch` returns a NumPy array of the attribute, even if the attribute contains a NumPy array. So here, we actually got a NumPy array of NumPy array. We can of course just index into it,

activity[0]

# but if we knew that there was only one item, we can use `fetch1` instead to save some trouble

activity = (Neuron() & key).fetch1('activity')

activity

# Now we can compute some statistics:

# ENTER YOUR CODE! - compute the mean of the activity


# ENTER YOUR CODE! - compute the standard deviation of the activity


# ENTER YOUR CODE! - compute the maximum of the activity


# This gives us a good idea on how to:
# 1. fetch the activity of a neuron knowing its primary key, and
# 2. compute interesting statistics

# Armed with this knowledge, let's go ahead and define the table for `ActivityStatistics`

# ### Defining `ActivityStatistics` table

# Let's go ahead and work out the definition of the table.

@schema
class ActivityStatistics(dj.Computed):
    definition = """
    -> Neuron
    ---
    mean: float    # mean activity
    stdev: float   # standard deviation of activity
    max: float     # maximum activity
    """


# Did you notice that we are now inheriting from `dj.Computed`?  `Computed` is yet another table tier that signifies that **the entries of this table are computed using data in other tables**. `Computed` tables are represented as red circles in the Diagram   .

dj.Diagram (schema)


# Just like the `Imported` tables, `Computed` tables make use of the same `make` and `populate` logic for defining new entries in the table. Let's go ahead and implement `make` method.

# +
# ENTER YOUR CODE! - complete the `make` method

@schema
class ActivityStatistics(dj.Computed):
    definition = """
    -> Neuron
    ---
    mean: float    # mean activity
    stdev: float   # standard deviation of activity
    max: float     # maximum activity
    """

    def make(self, key):
        activity = (Neuron() & key).fetch1('activity')    # fetch activity as NumPy array

        # compute various statistics on activity
        key['mean'] =                 # compute mean
        key['stdev'] =                # compute standard deviation
        key['max'] =                  # compute max
        self.insert1(key)
        print('Computed statistics for mouse_id {mouse_id} session_date {session_date}'.format(**key))


# -

# Let's go ahead and populate the table.

ActivityStatistics.populate()

ActivityStatistics()

# Voila!! You have computed statistics for each neuron activity!

# # Spike detection

# Now, let's go ahead and tackle a more challenging computation. While having raw neural traces in itself can be quite interesting, nothing is as exciting as spikes! Let's take a look at the neurons activities and plot them.

# get all keys
keys = Neuron.fetch('KEY')

# fetch all activities - returned as NumPy array of NumPy arrays
activities = (Neuron & keys).fetch('activity')

# +
fig, axs = plt.subplots(1, len(activities), figsize=(16, 4))
for activity, ax in zip(activities, axs.ravel()):
    ax.plot(activity)
    ax.set_xlabel('Time')
    ax.set_ylabel('Activity')

fig.tight_layout()
# -

# Let's now focus on one trace instead.

key = keys[0]

activity = (Neuron & key).fetch1('activity')

plt.plot(activity)
plt.xlabel('Time')
plt.ylabel('Activity')
plt.xlim([0, 300])

# Perhaps we can use threshold to detect when a spike occurs. Threshold of `0.5` may be a good start.

# +
threshold = 0.5

# find activity above threshold
above_thrs = (activity > threshold).astype(int)

plt.plot(activity)
plt.plot(above_thrs)
plt.xlabel('Time')
plt.xlim([0, 300])
# -

# We want to find out **when** it crossed the threshold. That is, find time bins where `above_thrs` goes from 0 (`False`) to 1 (`True`).

# +
rising = (np.diff(above_thrs) > 0).astype(int)   # find rising edge of crossing threshold
spikes = np.hstack((0, rising))    # prepend 0 to account for shortening due to np.diff

plt.plot(activity)
plt.plot(above_thrs)
plt.plot(np.where(spikes>0), 1,  'ro'); # plot only spike points
plt.xlabel('Time')
plt.xlim([0, 300])
# -

# Finally, let's also compute the spike counts

count = spikes.sum()   # compute total spike counts
count

# Here is our complete spike detection algorithm:

# +
# ENTER YOUR CODE! - try different values of threshold!

threshold =     # enter different threshold values here

# find activity above threshold
above_thrs = (activity > threshold).astype(int)

rising = (np.diff(above_thrs) > 0).astype(int)   # find rising edge of crossing threshold
spikes = np.hstack((0, rising))    # prepend 0 to account for shortening due to np.diff

count = spikes.sum()   # compute total spike counts


plt.plot(activity)
plt.plot(above_thrs)
plt.plot(np.where(spikes>0), 1,  'ro'); # plot only spike points
plt.xlabel('Time')
plt.title('Total spike counts: {}'.format(count));


# -

# Now notice that the exact spikes you detect depend on the value of the `threshold`. Therefore, the `threshold` is a parameter for our spike detection computation. Rather than fixing the value of the threshold, we might want to try different values and see what works well.
#
# In other words, you want to compute `Spikes` for a **combination** of `Neuron`s and different `threshold` values. To do this while still taking advantage of the `make` and `populate` logic, you would want to define a table to house parameters for spike detection in a `Lookup` table!

# ## Parameter `Lookup` table

# Let's define `SpikeDetectionParam` table to hold different parameter configuration for our spike detection algorithm. We are going to define this table as a `Lookup` table, rather than a `Manual` table. By now, you know that `Lookup` must be yet another **table tier** in DataJoint. `Lookup` tables are depicted by gray boxes in the Diagram .
#
# This tier indicates that the table will contain information:
# * that will be referenced by other tables
# * that doesn't change much - usually contains a few pre-known entries

@schema
class SpikeDetectionParam(dj.Lookup):
    definition = """
    sdp_id: int      # unique id for spike detection parameter set
    ---
    threshold: float   # threshold for spike detection
    """


dj.Diagram (schema)


# ### Defining `Spikes` table

# Now let's take everything together and define the `Spikes` table. Here each entry of the table will be *a set of spikes* for a single neuron, using a particular value of the `SpikeDetectionParam`. In other words, any particular entry of the `Spikes` table is determined by **a combination of a neuron and spike detection parameters**.
#
# We capture this by depending on both `Neuron` and `SpikeDetectionParam`. For each spike set, we want to store the detected spikes and the total number of spikes. The table definition will look something like:

@schema
class Spikes(dj.Computed):
    definition = """
    -> Neuron
    -> SpikeDetectionParam
    ---
    spikes: longblob     # detected spikes
    count: int           # total number of detected spikes
    """


# ### Define the `Waveform` part table

# We would also like to store the waveform at each detected spike, for a particular neuron. For simplicity, let's define the waveform to be 40 sample points before and after the onset of the detected spike.
# To accomplish this, we will define a `dj.Part` table `Waveform` which will contain the waveform per spike. The table definition is something like:

@schema
class Spikes(dj.Computed):
    definition = """
    -> Neuron
    -> SpikeDetectionParam
    ---
    spikes: longblob     # detected spikes
    count: int           # total number of detected spikes
    """

    class Waveform(dj.Part):
        definition = """
        -> master
        spike_id: int
        ---
        waveform: longblob  # waveform extracted from this spike
        """


# The `-> master` syntax denotes that the `Waveform` part table is foreign key constrained by `Spike` table - i.e. the master table. The master table drives the ***populate*** logic, and the content of the part table is generally ingested together with the content of the master table, all in one step (i.e. one `make()` call).

dj.Diagram (schema)


# In the Diagram   , we see that `Spikes` is a computed table (red circle) that depends on **both Neuron and SpikeDetectionParam**. Finally, let's go ahead and implement the `make` method for the `Spikes` table.

@schema
class Spikes(dj.Computed):
    definition = """
    -> Neuron
    -> SpikeDetectionParam
    ---
    spikes: longblob     # detected spikes
    count: int           # total number of detected spikes
    """

    class Waveform(dj.Part):
        definition = """
        -> master
        spike_id: int
        ---
        waveform: longblob  # waveform extracted from this spike
        """

    def make(self, key):
        print('Populating for: ', key)

        activity = (Neuron() & key).fetch1('activity')
        threshold = (SpikeDetectionParam() & key).fetch1('threshold')

        above_thrs = (activity > threshold).astype(int)   # find activity above threshold
        rising = (np.diff(above_thrs) > 0).astype(int)   # find rising edge of crossing threshold
        spikes = np.hstack((0, rising))    # prepend 0 to account for shortening due to np.diff

        count = spikes.sum()   # compute total spike counts
        print('Detected {} spikes!\n'.format(count))

        # create and insert a new dictionary containing `key` and additionally `spikes` and `count`
        self.insert1(dict(key, spikes=spikes, count=count))

        # extract waveform for the `Waveform` part-table
        before_spk, after_spk = 40, 40  # extract 40 sample points before and after a spike as the waveform
        for spk_id, spk in enumerate(np.where(spikes==1)[0]):

            # For simplicity, skip the spikes too close to the beginning or the end
            if spk - before_spk < 0 or spk + after_spk > len(activity) + 1:
                continue

            wf = activity[spk - before_spk: spk + after_spk]

            # create and insert a new dictionary containing `key` and additionally `spike_id` and `waveform`
            self.Waveform.insert1(dict(key, spike_id=spk_id, waveform=wf))


# The implementation of the spike detection is pretty much what we had above, except that we now fetch the value of `threshold` from the `SpikeDetectionParam` table.

# Looking at the `Spikes` table, we see that it indeed inherits the primary key attributes from **both Neuron (`mouse_id`, `session_date`) and SpikeDetectionParam (`sdp_id`)**.

Spikes()

# ### Populating `Spikes` table

# We are now ready to populate! When we call `populate` on `Spikes`, DataJoint will automatically call `make` on **every valid combination of the parent tables - Neuron and SpikeDetectionParam**.

# ENTER YOUR CODE! - populate the Spikes table


# Hm... `populate` doesn't seem to be doing anything... What could be the cause?

# Looking at `SpikeDetectionParam` reveals the issue:

SpikeDetectionParam()

# That's right! We have not added a detection parameter set yet. Let's go ahead and add one.

SpikeDetectionParam.insert1((0, 0.5))

SpikeDetectionParam()

# Now we should really be ready to perform the computation...

# ENTER YOUR CODE! - populate the Spikes table for real!


Spikes()

# ...and we now have spike detection running!

# Checking the waveform(s) from the Waveform part table

# ENTER YOUR CODE! - Now, build a query for the waveforms from mouse 100, session on "2017-05-25", with detection param 0


# ENTER YOUR CODE! - try fetching all the waveforms


# ENTER YOUR CODE! - and plot the average waveform


# ### Trying out other parameter values

# Let's see how different thresholds affect the results.

SpikeDetectionParam.insert1((1, 0.9))  # add another threshold

SpikeDetectionParam()

# ENTER YOUR CODE! - populate the "missing" entry in Spikes table


Spikes()

# You can see that the results of spike detection under different parameter settings can live happily next to each other, without any confusion as to what is what.

# ## Deleting entries "upstream"

# Now let's say that we decided that we don't like the first spike threshold of `0.5`. While there is really nothing wrong keeping those results around, you might decide that you'd rather delete all computations performed with that threshold to keep your tables clean.

# While you can restrict `Spikes` table to the specific parameter id (i.e. `sdp_id = 0`) and delete the entries:

(Spikes & 'sdp_id = 0').delete()

# We can simply delete the unwanted paramter from the `SpikeDetectionParam` table, and let DataJoint cascade the deletion:

SpikeDetectionParam() & 'sdp_id = 0'

(SpikeDetectionParam() & 'sdp_id = 0').delete()

Spikes()

# # Summary

# Congratulations! You have successfully extended your pipeline with a table to represent recorded data (`Neuron` as `Imported` table), tables that performs and represents computation results (`ActivityStatistics` and `Spikes` as `Computed` tables) and a table to hold computation parameters (`SpikeDetectionParam` as `Lookup` table).

dj.Diagram (schema)

# Our pipeline is still fairly simple but completely capable of handling analysis!
