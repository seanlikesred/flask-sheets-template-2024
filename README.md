# flask-sheets-template-2024

A web application starter template, created in Python with the Flask framework. Allows users to login with their Google accounts (via OAuth). Interfaces with a Google Sheets database.

![](https://user-images.githubusercontent.com/1328807/160312385-7ffbbada-4363-4b48-873d-9eca868afef0.png)

## Prerequisites

This application requires a Python development environment with the following tools installed:

- Git
- Anaconda (comes with Python and PIP)

For beginners, here are some instructions for how to install Anaconda, and [set up your local Python development environment](https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/local-dev-setup/README.md#anaconda-python-and-pip).

## Repo Setup

1. Create a fork of this repository by clicking on the Fork button shown below. Name your repository the name of your new project.

![alt text](/.github/markdown-images/image-1.png)

2. Find your repo's URL by clicking on the Code button shown here. Copy this url to your clipboard.

![alt text](/.github/markdown-images/image-2.png)

2. Using `cd` on the command line, navigate to the folder on your computer where you want to store your project.

3. Clone your new repository onto your local machine by typing

```sh
git clone <URL of your new repo>
```

4. Run `cd <your-repo-name> ` to navigate into your new project.

## Anaconda Virtual Environment Setup

1. Once inside of your directory, run the following commands to create a new virtual environment

```sh
conda create -n flask-sheets-env-2024 python=3.10
conda activate flask-sheets-env-2024
```

2. Install the necessary python dependencies by running

```sh
pip install -r requirements.txt
```

## Services Setup

This app requires a few services, for user authentication and data storage. Follow the instructions below to setup these services.

### Google Cloud Project

1. Visit the [Google Cloud Console](https://console.cloud.google.com). Create a new project, and name it. After it is created, select it from the project selection dropdown menu.

![alt text](/.github/markdown-images/image-3.png)
![alt text](/.github/markdown-images/image-4.png)

### Google OAuth Client

Visit the [API Credentials](https://console.cloud.google.com/apis/credentials) page for your Google Cloud project. Click the button with the plus icon to "Create Credentials", and choose "Create OAuth Client Id".

Click to "Configure Consent Screen". Leave the domain info blank, and leave the defaults / skip lots of the setup for now. If/when you deploy your app to a production server, you can return to populating this info (or you will be using a different project).

You should see a screen like this after clicking through the Consent Screen settings.

![alt text](/.github/markdown-images/image-6.png)

Return to actually creating the "OAuth Client Id". Choose a "Web application" type, give it a name, and set the following "Authorized Redirect URIs" (for now, while the project is still in development):

#### http://localhost:5000/auth/google/callback

![alt text](/.github/markdown-images/image-7.png)

After the client is created, note the `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET` (right side of the screen below). You'll need these to set up your env file below.

![alt text](/.github/markdown-images/image-8.png)

### Google Cloud Service Account Credentials

To fetch data from the Google Sheets database (and use other Google APIs), the app will need access to a local "service account" credentials file.

From the [Google API Credentials](https://console.cloud.google.com/apis/credentials) page, create a new service account as necessary.

For the chosen service account, create new JSON credentials file as necessary from the "Keys" menu, then download the resulting JSON file into the root directory of this repo, specifically named "google-credentials.json".

![alt text](/.github/markdown-images/image-9.png)

### Google Sheets Database Setup

See the [Google Sheets Database Setup](/admin/SHEETS_DB.md) guide.

You'll need your Spreadsheet Document ID below, which can be found in the URL of your sheet after /d/ (highlighted below)

![alt text](/.github/markdown-images/image-11.png)

### Google Analytics Setup

If you would like to configure Google Analytics, consult the [Google Analytics Setup](/admin/GA.md) guide.

## Configuration

### Environment Variables

Create a file called ".env" in the root directory of this repository, and populate it with environment variables to specify your own credentials, as obtained in the "Setup" section above:

```sh
FLASK_APP="web_app"

#
# GOOGLE OAUTH
#
GOOGLE_CLIENT_ID="____________"
GOOGLE_CLIENT_SECRET="____________"

#
# GOOGLE SHEETS DATABASE
#
GOOGLE_SHEETS_DOCUMENT_ID="____________"

#
# GOOGLE ANALYTICS
#
GA_TRACKER_ID="UA-XXXXXXX-1"
```

## Usage

### Sheets Service

After configuring the Google Sheet database and populating it with products, you should be able to test out the app's ability to fetch products (and generate new orders):

```sh
python -m app.sheets_service
```

### Web Application

Run the local web server (then visit localhost:5000 in a browser):

```sh
FLASK_APP=web_app flask run
```

## Testing

Run tests:

```sh
pytest
```

> NOTE: we are using a live sheet for testing, so to avoid API rate limits, we are waiting / sleeping between each test, which makes the tests a bit slow for now

## CI

See more information about the [CI](/admin/CI.md) build process.

## Deploying

See the [Deployer's Guide](/admin/RENDER.md) for instructions on deploying to a production server hosted by Render.

## [License](/LICENSE.md)
