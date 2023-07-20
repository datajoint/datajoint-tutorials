# Welcome to DataJoint tutorials!

DataJoint is an open-source software and cloud platform to design, build and automate data analysis, pipelines and data sharing for neuroscience experiments. 

This document will guide you as a new DataJoint user through interactive tutorials organized in notebooks and written in Python.

*Please note that these hands-on tutorials are friendly to non-expert users and no prior programming knowledge is required.* 


## Key learnings from the tutorials

After completing this set of tutorials, you will gain real experience in the basics of the DataJoint framework. These skills will allow you to design, implement and manage data workflows effectively applied to your scientific research.

Here is a summary of the content that you can expect to have learned:

- Understanding DataJoint basics: concepts, design and structure (~1 hour)
    - Create schemas/tables
    - Table tiers (`Lookup`, `Manual`, `Imported`, `Computed`)
    - Insert entries and view entries in tables
    - Table dependency and data integrity
    - Query operations
        - Restriction - `&`
        - Join - `*`
        - Projection - `.proj()`
        - Aggregation - `.aggr()`
    - Fetch operations
        - Retrieve everything
        - Retrieve primary key - `.fetch("KEY")`
        - Retrieve selective attributes
    - Delete operations

- DataJoint advanced topics: workflow automation (~1 hour)
    - `Imported` and `Computed` tables
    - `make()` function 
    - `.populate()` for automated computation
    - `.populate(reserve_jobs=True)` for parallelization
    

## Quick start

The DataJoint tutorials are easily accessible using an **interactive environment** that contains all the software required to run the experiments. The environment is configured by [DevContainer] (https://containers.dev/). Here are two options to launch the interactive environment:

- **Cloud-based IDE: GitHub Codespaces**: (*recommended*) 
   - This is the easiest option for **tutorial users**. You will immediately start coding using DataJoint and Python, with no installation of software or environments, using built-in tools in the cloud. 
   
   - Instructions:
      - A codespace is a development environment hosted in the cloud. To use the DataJoint tutorials with [GitHub Codespaces](https://github.com/features/codespaces), you need a [GitHub](https://github.com/) account. Fork the [datajoint-tutorials](https://github.com/datajoint/datajoint-tutorials) repository into your repository.
      - From your `datajoint-tutorials` repository, click on `Code`, then click on `Codespaces` tab, and `+` option will `Create codespace on main` on your fork with default options. For more control, see the `...` where you may create `New with options...`.
      - The building time for a codespace is **~5m**. This is done infrequently and cached for convenience.
      - The start time for a codespace is **~30s**. This will pull the built codespace from the cache when you need it.
      - *Tip*: Each month, GitHub renews a [free-tier](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts) quota of computing and storage. Typically we run into the storage limits before anything else since Codespaces consume storage while stopped. It is best to delete Codespaces when not actively in use and recreate them when needed. We'll soon be creating prebuilds to avoid larger build times. Once any portion of your quota is reached, you will need to wait for it to be reset at the end of your cycle or add billing info to your GitHub account to handle overages.
      - *Tip*: GitHub auto names the codespace but you can rename the codespace so that it is easier to identify later.

- **Local IDE**:
   - We highly recommend this option for users seeking to apply DataJoint for **their own neuroscience experiments** and lab research. Additionally, this option is particularly advantageous for those who have a keen interest in **other modules of the DataJoint Elements Library** (e.g., Miniscope, DeepLabCut).

   - Instructions:
      - Ensure you have [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
      - Ensure you have [Docker](https://docs.docker.com/get-docker/)
      - Ensure you have [VSCode](https://code.visualstudio.com/)
      - Install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
      - `git clone` the codebase repository and open it in VSCode
      - Use the `Dev Containers extension` to `Reopen in Container` (More info in the `Getting started` included with the extension)

You will know your environment has finished loading once you see a terminal open related to `Running postStartCommand` with a final message: `Done` or the `README.md` is opened in `Preview`.

### Instructions

1. We recommend you start by navigating to the `notebooks` directory on the left panel and go through the `00-Getting_Started/01-DataJoint Basics - Interactive.ipynb` Jupyter notebook. Execute the cells in the notebooks to begin your walkthrough of the tutorial.

2. Once you are done, see the options available to you in the menu in the bottom-left corner. For example, in Codespace you will have the option to `Stop Current Codespace`, but when running DevContainer on your own machine the equivalent option is `Reopen folder locally`. By default, GitHub will also automatically stop the Codespace after 30 minutes of inactivity.

If you are new to GitHub and run into any errors, please contact us via email at support@datajoint.com. If you are experienced with GitHub, please create an issue on the upstream repository or if you'd like help contribute, feel free to create a pull request. Please include a thorough explanation of the error and/or proposed solution.

## Additional DataJoint Tutorials

- DataJoint Elements are a collection of curated modules for assembling data pipelines for several modalities of neurophysiology experiments.
  - [Element Calcium Imaging Tutorial](https://github.com/datajoint/element-calcium-imaging#interactive-tutorial)
  - [Element Array Electrophysiology Tutorial](https://github.com/datajoint/workflow-array-ephys#interactive-tutorial)
  - [Element Miniscope Calcium Imaging Tutorial](https://github.com/datajoint/workflow-miniscope#interactive-tutorial)

- [Machine Intelligence from Cortical Networks (MICrONS) program](https://www.microns-explorer.org/)
  - [MICrONS Tutorial](https://github.com/datajoint/microns_phase3_nda#interactive-environment)