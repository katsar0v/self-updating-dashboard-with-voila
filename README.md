[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/katsar0v/self-updating-dashboard-with-voila/master?urlpath=voila%2Frender%2Fdashboard.ipynb)

![Screenshot](screenshot.png?raw=true "Screenshot")


# Self-updating Voila Dashboard Example

This is an example to create a self-updating dashboard, which gets data from an api interface.

This example contains `requiremements.txt` for dependencies.

## Local Setup

To test locally (with venv):

```
python -m venv venv
source activate venv/bin/activate
pip install -r requirements.txt
gunicorn api:app -b 127.0.0.1:9999 --daemon
voila dashboard.ipynb
```

To test locally (with conda):

```
conda env create self-updating-dashboard
conda activate create self-updating-dashboard
pip install -r requirements.txt
gunicorn api:app -b 127.0.0.1:9999 --daemon
voila dashboard.ipynb
```

This will open a new browser tab at http://localhost:8866 serving the dashboard.