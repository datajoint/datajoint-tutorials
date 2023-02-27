# DataJoint interactive tutorial with GitHub Codespace

Interactive tutorials on the DataJoint framework, in python. Throughout this set of tutorials, you will learn

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

The easiest way to start this interactive tutorial on DataJoint basics is to use [GitHub Codespace](https://docs.github.com/en/codespaces/overview). Please follow the steps below for the best experience:

1. Fork this repository to your own GitHub account.

2. Click on the green `Code` button where you would typically click to clone a repository.

3. Within the dropdown menu, click on the `Codespaces` tab.

4. If this is your first time using Codespaces with this repository, please click on the green `Create codespace on master` button.

5. Wait for the environment to be created. This step takes ~5 minutes the very first time being launched, and typically around ~1 minute if you revisit this codespace again in the future. 

6. You will know the environment is ready when a Visual Studio Code window is rendered within your browser. If you are new to Visual Studio Code, please take a minute to familiarize yourself with the layout. The directories you will need to navigate are on the left side of the screen by default.

7. Navigate to the 00-Getting_started directory and open the `00-Getting started.ipynb` Jupyter Notebook. Execute the cells in this notebook to begin your walk through the tutorials.

We recommend finishing all notebooks in `00-Getting_started` before proceeding to `01-Calcium_imaging` and `02-Electrophysiology`. Once you are done, GitHub will automatically terminate the Codespace after 30 minutes of inactivity or you can manually terminate the Codespace.

If you are new to GitHub and run into any errors, please contact us via email at support@datajoint.com. If you are experienced with GitHub, please create an issue on the upstream repository or issue a pull request with a thorough explanantion of the error and proposed solution. 

**Please Note:** 

```GitHub Codespaces are limited to 120 core hours per month for free users. Once you exceed this limit, you will have to wait for the hours to reset or pay to use Codespaces.```

