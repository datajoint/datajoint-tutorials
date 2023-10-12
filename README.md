# Welcome to DataJoint tutorials!

DataJoint is an open-source library for scientific research labs to design and build
data pipelines for automated data analysis and sharing.

This document will guide you through interactive tutorials written in
[Python](https://www.python.org/) and organized in [Jupyter
notebooks](https://jupyter-notebook.readthedocs.io/en/stable/).

*Please note that these hands-on DataJoint tutorials are friendly to non-expert users, and advanced programming skills are not required.* 


## Table of contents 
- The [tutorials](./tutorials) folder contains interactive Jupyter notebooks designed to teach DataJoint. The calcium imaging and electrophysiology tutorials provide examples of defining and interacting with data pipelines. In addition, some fill-in-the-blank sections are included for you to code yourself!
    - 01-DataJoint Basics
    - 02-Calcium Imaging Imported Tables
    - 03-Calcium Imaging Computed Tables
    - 04-Electrophysiology Imported Tables
    - 05-Electrophysiology Computed Tables

- The [completed_tutorials](./completed_tutorials) folder contains Jupyter notebooks with all code sections completed and solved.

- You will find the following notebooks in the [short_tutorials](./short_tutorials) folder:
    - DataJoint in 30min
    - University


## Key learnings from the tutorials

After completing this set of tutorials, you will gain real experience in the basics of the DataJoint framework. These skills will allow you to design, implement and manage data pipelines effectively applied to your scientific research.

Here is a summary of the content that you can expect to have learned:

- Understanding DataJoint basics: concepts, design, and structure (~1 hour)
    - Create schemas/tables
    - Table tiers (`Lookup`, `Manual`, `Imported`, `Computed`)
    - Insert entries and view entries in tables
    - Table dependency and data integrity
    - Basic operations
        - Restriction - `&`
        - Join - `*`
        - Projection - `.proj()`
        - Fetch - `.fetch()`
        - Deletion - `.delete()`
        - Drop - `.drop()`

- DataJoint advanced topics: pipeline automation (~1 hour)
    - `Imported` and `Computed` tables
    - `make()` function 
    - `.populate()` for automated computation
    - `.populate(reserve_jobs=True)` for parallelization
    

## Interactive Environment

- These interactive DataJoint tutorials can be accessed through a cloud-based environment on [GitHub Codespaces](https://github.com/features/codespaces).  The following instructions will provide you with an environment that is configured with DataJoint for Python so that you can immediately begin to build and run a data pipeline.
- Instructions
  - Sign up for a free a [GitHub](https://github.com/) account.
  - Fork this repository.
  - Launch the environment using GitHub Codespaces on your fork with the default options by selecting the green `Code` button, then the `Codespaces` tab, and then the green `Create codespace on main` button. For more control, under the `Codespaces` tab select the `...` button where you may create `New with options....`.
  - The launch time for the Codespace is less that 2 minutes.
  - You will know your environment has finished loading once the `pip install -e .` command has run and the terminal prompt is clear.
  - To begin, navigate to the `tutorials` directory located in the left panel and proceed through the sequentially organized Jupyter notebooks. Execute the cells in the notebooks to begin your walkthrough of the tutorial.
  - Once you are done, see the options in the menu in the bottom-left corner. In Codespaces, you can `Stop Current Codespace`. By default, GitHub will also automatically stop the Codespaces after 30 minutes of inactivity.
- *Tip*: Each month, GitHub renews a [free-tier](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts) quota of computing and storage. Typically we run into the storage limits before anything else since Codespaces consume storage while stopped. It is best to delete [Codespaces](https://github.com/codespaces) when not actively in use and recreate them when needed. Once any portion of your quota is reached, you will need to wait for it to be reset at the end of your cycle or add billing info to your GitHub account to handle overages.
- *Tip*: GitHub auto names the Codespaces, but you can rename the Codespace so that it is easier to identify later.
- *Tip*: All the edits you make in these tutorial notebooks are ***not persistent***.  Edits will be reset to the original content every time you restart the server.  However, you can easily commit the changes to your fork.


## Documentation

- For more information on DataJoint Python, please refer to the [documentation](https://datajoint.com/docs/core/datajoint-python/).


## Support
If you need help getting started or run into any errors, please open a GitHub Issue or contact our team by email at support@datajoint.com.


## Additional DataJoint Tutorials

- DataJoint Elements is a collection of curated modules for assembling data pipelines for several modalities of neurophysiology experiments.
  - [Element Calcium Imaging Tutorial](https://github.com/datajoint/element-calcium-imaging#interactive-tutorial)
  - [Element Array Electrophysiology Tutorial](https://github.com/datajoint/workflow-array-ephys#interactive-tutorial)

- [Machine Intelligence from Cortical Networks (MICrONS) program](https://www.microns-explorer.org/)
  - [MICrONS Tutorial](https://github.com/datajoint/microns_phase3_nda#interactive-environment)


## Developer Instructions
- Local environment instructions
    - Install the following:
        - [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
        - [Docker](https://docs.docker.com/get-docker/)
            - On M1/M2 Mac:
                - Enable Rosetta 2 on Docker advanced/experimental settings
                - Ensure Rosetta is installed by typing `softwareupdate --install-rosetta` at a shell prompt
                - `export DOCKER_DEFAULT_PLATFORM=linux/amd64` in .zshrc or at a shell prompt
        - [Microsoft's Visual Studio Code (VS Code)](https://code.visualstudio.com/)
        - VSCode [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
    - `git clone` your fork of the repository and open it in VSCode.
    - Use the `Dev Containers extension` to `Reopen in Container`. (More info in the `Getting started` included with the extension.)
    - To begin, navigate to the [tutorials](./tutorials) directory located in the left panel and proceed through the sequentially organized Jupyter notebooks. Execute the cells in the notebooks to begin your walkthrough of the tutorial.
    - Once you are done, you can stop the container by closing the `VS Code` window.