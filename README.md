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

## Getting started

The easiest way to learn about the basics of DataJoint is to use these tutorial notebooks within a [GitHub Codespace](https://docs.github.com/en/codespaces/overview). Please follow the steps below for the best experience:

1. Fork this repository to your GitHub account.

2. Select the green `Code` button.

3. Within the dropdown menu, select the `Codespaces` tab.

4. Select the green `Create codespace on main` button.

5. The environment is ready when a Visual Studio Code window is rendered within your browser.  This takes ~5 minutes the first time being launched, and ~1 minute if you revisit this Codespace.

6. Navigate to the `00-Getting_Started` directory on the left panel and open the `00-Getting Started.ipynb` Jupyter notebook. Execute the cells in this notebook to begin your walk through the tutorials. We recommend finishing all notebooks in `00-Getting_Started` before proceeding to `01-Calcium_Imaging` and `02-Electrophysiology`.

7. Once you are done, GitHub will automatically stop the Codespace after 30 minutes of inactivity or you can manually stop the Codespace.

8. After stopping the Codespace, we recommend deleting the Codespace to save on storage costs, which are free for the first 15 GB-month.

+ If you are new to GitHub and run into any errors, please contact us via email at support@datajoint.com. If you are experienced with GitHub, please create an issue on the upstream repository or issue a pull request with a thorough explanation of the error and proposed solution.

+ **Please Note:** GitHub Codespaces are limited to 120 core-hours per month and 15 GB-month for free users. Once you exceed this limit, you will have to wait for the usage quota to reset or pay to use Codespaces.

## Run in Local Development Environment

- Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

- Install [Docker](https://docs.docker.com/get-docker/)

- Install [VSCode](https://code.visualstudio.com/)

- Install the VSCode [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

- `git clone` the codebase repository and open it in VSCode

- Use the `Dev Containers extension` to `Reopen in Container` (More info in the `Getting started` included with the extension.)

- You will know your environment has finished loading once you see a terminal open related to `Running postStartCommand` with a final message: `Done`.
