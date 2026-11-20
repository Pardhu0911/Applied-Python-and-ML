# Applied Python and machine-learning labs

These are shorter exercises from my graduate Python and machine-learning courses at the University of Cincinnati. To try one with data already included, start with outlier detection or the comparison of country-level education scores.

**Pardha Saradhi Edupalli**

## Run an exercise

Run these commands in PowerShell from this project folder with Python 3.12 installed.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python -m jupyter lab
```

Open a notebook and run its cells in order. For a Python script, change to its subfolder first so relative paths resolve. For the outlier exercise, start in the `applied-python-and-ml` folder and run these commands.

```powershell
cd outlier-detection
..\.venv\Scripts\python detect.py
```

| Folder | Experiment | Inputs or additional setup |
| --- | --- | --- |
| `outlier-detection` | Iteratively remove the most extreme observation using a leave-one-out standard deviation | A numeric sample is included |
| `education-scores` | Join three country-level score tables, compare their distributions and flag outliers | Three aggregate tables are included |
| `remote-access-regression` | Compare linear models, adjusted R² and Lasso feature selection | Included numeric application-usage table. Reported scores are in-sample |
| `remote-access-neural-networks` | Compare three Keras regressors on an 80/20 split of the usage table | Included usage table. Install `requirements-neural.txt` |
| `classifier-comparison` | Compare logistic regression, random forest, KNN, SVM and a decision tree on a classroom classification problem | Copy `data_diabetes.csv` from the original ML course ZIP into this folder. This is an educational modeling exercise |
| `movie-review-sentiment` | Train an embedding-based binary sentiment classifier | Install `requirements-neural.txt` and provide `data.csv` and `data_test.csv`, each with two headerless columns (review and label) |
| `gpt2-text-generation` | Interactive text generation with pretrained GPT-2 | Install `requirements-text-generation.txt`. First run downloads the public model. Enter `quit` to exit |
| `country-populations` | Filter the countries on a practice scraping page by population range | Requires network access to Scrapethissite.com |
| `literary-word-frequency` | Count words and character mentions in *Pride and Prejudice* and plot the distributions | Copy `pride_and_prejudice.txt` and `stopwords.txt` from the Grad Topics archive |
| `sqlite-basics` | Create, populate and query a sample table | Uses a temporary in-memory database and fictional student records |
| `python-practice` | Collections, matrices, recursion, OOP, exceptions, decorators, primes and a historical rotation cipher | For the rotation-cipher example, copy `dictionary.txt` from the original ML archive |

Install the optional neural-network and language-model requirements only for the exercises that use them. For the movie-review classifier, supply your own labeled training and test files. Validation uses a portion of the training file, and the test file is reserved for the final evaluation.
