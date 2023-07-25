# Welcome to DataJoint tutorials!

DataJoint is an open-source library for science labs to design and build data pipelines for automated data analysis and sharing.

This document will guide you as a new DataJoint user through interactive tutorials organized in [Jupyter notebooks](https://jupyter-notebook.readthedocs.io/en/stable/) and written in [Python](https://www.python.org/).

*Please note that these hands-on DataJoint tutorials are friendly to non-expert users, and advanced programming skills are not required.* 

## Table of contents 
- In the `tutorials` folder are interactive Jupyter notebooks to learn DataJoint. The Calcium Imaging and Electrophysiology tutorials are relevant examples of data structure and analysis. In addition, some fill-in-the-blank sections are included for you to code yourself!
    - 01-DataJoint Basics
    - 02-Calcium Imaging Imported Tables
    - 03-Calcium Imaging Computed Tables
    - 04-Electrophysiology Imported Tables
    - 05-Electrophysiology Computed Tables

- Completed exercises: notebooks with the code sections completed and solved.

- Short tutorials:
    - DataJoint in 30min
    - University

- Tutorial pipeline
    - Ephys cell activity
    - Imaging
    - Mouse session

## Key learnings from the tutorials

After completing this set of tutorials, you will gain real experience in the basics of the DataJoint framework. These skills will allow you to design, implement and manage data pipelines effectively applied to your scientific research.

Here is a summary of the content that you can expect to have learned:

- Understanding DataJoint basics: concepts, design, and structure (~1 hour)
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

### User installation 
DataJoint tutorials are easily accessible using an **interactive environment** that contains all the software required to run the experiments. The setting is configured by [DevContainer] (https://containers.dev/). Here are two options to launch the interactive environment. 

*Please note that to use the DataJoint Python package with an interactive environment, you need a [GitHub](https://github.com/) account.*

- **Cloud-based environment: GitHub Codespaces**: (*recommended*) 
   - This is the easiest option for **tutorial users**. You will immediately start coding using DataJoint and Python, without installing software or local environments. Cloud-based environments (IDEs), such as [GitHub Codespaces](https://github.com/features/codespaces), use built-in tools directly connected to the cloud and work on the browser.
   
   - Instructions:
      - Fork the [datajoint-tutorials](https://github.com/datajoint/datajoint-tutorials) repository into your repository.
      - From your `datajoint-tutorials` repository, click on `Code`, then click on `Codespaces` tab, and `+` option will `Create codespace on main` on your fork with default options. For more control, see the `...` where you may create `New with options...`.
      - The building time for Codespaces is **~5m**. This is done infrequently and cached for convenience.
      - The start time for Codespaces is **~30s**. This will pull the built codespace from the cache when you need it.
      - *Tip*: Each month, GitHub renews a [free-tier](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts) quota of computing and storage. Typically we run into the storage limits before anything else since Codespaces consume storage while stopped. It is best to delete Codespaces when not actively in use and recreate them when needed. We'll soon be creating prebuilds to avoid larger build times. Once any portion of your quota is reached, you will need to wait for it to be reset at the end of your cycle or add billing info to your GitHub account to handle overages.
      - *Tip*: GitHub auto names the Codespaces, but you can rename the Codespaces so that it is easier to identify later.

- **Local environment**:
   - We highly recommend this option for users that who want to apply DataJoint to **their own neuroscience experiments** and lab research after exploring the tutorials. Additionally, this option is particularly advantageous for those who have a keen interest in **other modules of the DataJoint Elements Library** (e.g., Miniscope, DeepLabCut). For this option, ensure you have the following:
    - [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
    - [Docker](https://docs.docker.com/get-docker/)
    - [Microsoft's Visual Studio Code (VS Code)](https://code.visualstudio.com/)
    - [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). 
    
    For more detailed instructions, please check out the [User Guide in DataJoint Documentation](https://datajoint.com/docs/elements/user-guide/).

Before we start, remember that all the edits you make in these tutorial notebooks are ***not persistent*** - they will be reset to the original content every time you restart the server. However, you can easily download the notebooks that interest you in keeping the changes.

### Instructions
- To begin, navigate to the notebooks directory located in the left panel and proceed through the sequentially organized Jupyter notebooks, labeled by numbers. Execute the cells in the notebooks to begin your walkthrough of the tutorial.

- Once you are done, see the options in the menu in the bottom-left corner. For example, in Codespaces you can `Stop Current Codespace`, but when running DevContainer on your machine the equivalent option is `Reopen folder locally`. By default, GitHub will also automatically stop the Codespaces after 30 minutes of inactivity.

## Support
If you need help getting started or run into any errors, please open a GitHub Issue or contact our team by email at support@datajoint.com.

## Additional DataJoint Tutorials

- DataJoint Elements is a collection of curated modules for assembling data pipelines for several modalities of neurophysiology experiments.
  - [Element Calcium Imaging Tutorial](https://github.com/datajoint/element-calcium-imaging#interactive-tutorial)
  - [Element Array Electrophysiology Tutorial](https://github.com/datajoint/workflow-array-ephys#interactive-tutorial)

- [Machine Intelligence from Cortical Networks (MICrONS) program](https://www.microns-explorer.org/)
  - [MICrONS Tutorial](https://github.com/datajoint/microns_phase3_nda#interactive-environment)