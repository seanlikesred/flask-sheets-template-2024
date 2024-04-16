# flask-sheets-template-2024

A web application starter template, created in Python with the Flask framework. Allows users to login with their Google accounts (via OAuth). Interfaces with a Google Sheets database.

![](./docs/images/products-page-screenshot.png)

## Prerequisites

This application requires a Python development environment with the following tools installed:

- Git
- Anaconda (includes Python and Pip)

For beginners, here are some instructions for how to install Anaconda, and [set up your local Python development environment](https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/local-dev-setup/README.md#option-b-full-setup).

## Repo Setup

To make a copy of the prof's template repository, click "Use this template" to create a new copy of this repository under your own control.

Using GitHub Desktop or the command line, clone your copy of the repo to download it onto your local machine. Observe the location where you downloaded it (for example the Desktop).

Using GitHub Desktop or the command line, navigate to the local repo (for example if on the Desktop):

```sh
cd ~/Desktop/flask-sheets-template-2024
```


## Anaconda Virtual Environment Setup

Create a new virtual environment and activate it:

```sh
conda create -n flask-sheets-2024 python=3.10
conda activate flask-sheets-2024
```

After navigating to the local repo and activating the environment, install the necessary python dependencies:

```sh
pip install -r requirements.txt
```

## Services Setup

This app requires a few services, for user authentication and data storage. Follow the instructions below to setup these services:

1. Follow the [Google Cloud Setup Guide](./docs/GOOGLE_CLOUD.md) to configure a Google Cloud project to facilitate user logins and programmatic access to Google APIs. Obtain and configure client credentials (via environment variables) and service account credentials (via JSON file).

2. Follow the [Google Sheets Database Setup Guide](./docs/GOOGLE_SHEETS.md) to setup the Google Sheets database.

3. If you would like to configure Google Analytics, optionally consult the [Google Analytics Setup Guide](./docs/GOOGLE_ANALYTICS.md).


## Configuration

### Environment Variables

We will use environment variables to pass secret credentials to the app in a secure, indirect way.

Create a file called ".env" in the root directory of this repository, and add contents like the following (specifying your own credentials, as obtained during the "Setup" section):

```sh
FLASK_APP="web_app"

# GOOGLE OAUTH (see Google Cloud Setup Guide):
GOOGLE_CLIENT_ID="____________"
GOOGLE_CLIENT_SECRET="____________"

#
# GOOGLE SHEETS DATABASE (see Google Sheets Database Setup Guide)
#
GOOGLE_SHEETS_DOCUMENT_ID="____________"
#GOOGLE_SHEETS_TEST_DOCUMENT_ID="____________"

#
# GOOGLE ANALYTICS (see Google Analytics Setup Guide)
#
#GA_TRACKER_ID="____________"
```




## Usage

### Sheets Database

After you have set up the Google Sheets database, you should be able to use the spreadsheet service to interface with it at a low level (for example to list all the sheets in the document):

```sh
python -m app.spreadsheet_service
```

Assuming the "products" sheet has been setup properly, you can use the model class to interface with it at a higher level (for example to populate the sheet with example records):

```sh
python -m app.models.product
```

> NOTE: see the contents of the ["app/models/product.py"](/app/models/product.py) file for more details, and feel free to customize as desired.


### Web Application

Run the local web server (then visit http://localhost:5000 in a browser):

```sh
FLASK_APP=web_app flask run
```




## Testing

We will use a separate Google Sheet "test document" to use during testing. This keeps development data seprate from test data, and allows for experimentation when testing.

To setup the test document, follow a modified version of the Google Sheets Database Setup Guide:
  1. Create a copy of the Google Sheet "development document" you setup earlier (including the "products" and "orders" sheet with the proper column identifiers).
  2. Share this document with your service account's email address, giving it "Editor" priviges.
  3. Note the document's identifier from the URL bar, and set it as an environment variable called `GOOGLE_SHEETS_TEST_DOCUMENT_ID`, by adding this environment variable to the ".env" file.

After the test document has been setup, you should be able to run tests:

```sh
pytest
```

> NOTE: the "web_app_test" references specific content on certain pages, so as you update the page contents you may need to update the tests as well.

## Continuous Integration

See the [GitHub Actions Guide](/docs/GITHUB_ACTIONS.md) for more information about configuring the Continuous Integration (CI) build process.

## Deploying / Hosting

See the [Hosting Guide](/docs/RENDER.md) for instructions on deploying to a production server hosted by Render.



## [License](/LICENSE.md)
