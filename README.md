# DataJoint interactive tutorial with GitHub Codespace

Interactive tutorials on the DataJoint framework, in Python. Throughout this set of tutorials, you will learn

- DataJoint basics (~1 hour)
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

- DataJoint advanced topics (~1 hour)
    - `Imported` and `Computed` tables
    - `make()` function 
    - `.populate()` for automated computation
    - `.populate(reserve_jobs=True)` for parallelization

## Interactive Tutorial

The easiest way to learn DataJoint is to use the tutorial notebooks within the included interactive environment configured using [DevContainer](https://containers.dev/).

### Launch Environment

Here are some options that provide a great experience:

- **Cloud-based IDE**: (*recommended*)
  - Launch using [GitHub Codespaces](https://github.com/features/codespaces) using the `+` option which will `Create codespace on main` in the codebase repository on your fork with default options. For more control, see the `...` where you may create `New with options...`.
  - Build time for a codespace is **~5m**. This is done infrequently and cached for convenience.
  - Start time for a codespace is **~30s**. This will pull the built codespace from cache when you need it.
  - *Tip*: Each month, GitHub renews a [free-tier](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts) quota of compute and storage. Typically we run into the storage limits before anything else since Codespaces consume storage while stopped. It is best to delete Codespaces when not actively in use and recreate when needed. We'll soon be creating prebuilds to avoid larger build times. Once any portion of your quota is reached, you will need to wait for it to be reset at the end of your cycle or add billing info to your GitHub account to handle overages.
  - *Tip*: GitHub auto names the codespace but you can rename the codespace so that it is easier to identify later.
- **Local IDE**:
  - Ensure you have [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
  - Ensure you have [Docker](https://docs.docker.com/get-docker/)
    - On M1/M2 Mac, you have to:
      - enable Rosetta 2 on Docker advanced/experimental settings
      - ensure Rosetta is installed by typing `softwareupdate --install-rosetta` at a shell prompt
      - `export DOCKER_DEFAULT_PLATFORM=linux/amd64` in .zshrc or at a shell prompt
  - Ensure you have [VSCode](https://code.visualstudio.com/)
  - Install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
  - `git clone` the codebase repository and open it in VSCode
  - Use the `Dev Containers extension` to `Reopen in Container` (More info in the `Getting started` included with the extension)

You will know your environment has finished loading once you either see a terminal open related to `Running postStartCommand` with a final message: `Done` or the `README.md` is opened in `Preview`.

### Instructions

1. We recommend you start by navigating to the `notebooks` directory on the left panel and go through the `00-Getting_Started/01-DataJoint Basics - Interactive.ipynb` Jupyter notebook. Execute the cells in the notebooks to begin your walk through of the tutorial.

1. Once you are done, see the options available to you in the menu in the bottom-left corner. For example, in Codespace you will have an option to `Stop Current Codespace` but when running DevContainer on your own machine the equivalent option is `Reopen folder locally`. By default, GitHub will also automatically stop the Codespace after 30 minutes of inactivity.

If you are new to GitHub and run into any errors, please contact us via email at support@datajoint.com. If you are experienced with GitHub, please create an issue on the upstream repository or if you'd like help contribute, feel free to create a pull request. Please include a thorough explanantion of the error and/or proposed solution.

## Additional DataJoint Tutorials

- DataJoint Elements are a collection of curated modules for assembling data pipelines for several modalities of neurophysiology experiments.
  - [Element Calcium Imaging Tutorial](https://github.com/datajoint/element-calcium-imaging#interactive-tutorial)
  - [Element Array Electrophysiology Tutorial](https://github.com/datajoint/workflow-array-ephys#interactive-tutorial)

- [Machine Intelligence from Cortical Networks (MICrONS) program](https://www.microns-explorer.org/)
  - [MICrONS Tutorial](https://github.com/datajoint/microns_phase3_nda#interactive-environment)