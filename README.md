# Growth Mindset Dashboard

A Streamlit application to help you track and visualize your personal growth journey.

## Features

- **Dashboard**: Visualize your learning progress with interactive charts and metrics
- **Progress Tracker**: Log your daily learning activities and challenges
- **Resources**: Access curated resources on developing a growth mindset

## Installation

This project uses Python 3.13+ and requires the following packages:

- streamlit
- pandas
- numpy

### Setting up with uv (recommended)

```bash
# Navigate to the project directory
cd growth-mindset

# Install dependencies with uv
uv pip install -e .
```

### Alternative: Setting up with conda

```bash
# Create and activate conda environment
conda create -n growth-mindset python=3.13
conda activate growth-mindset

# Install required packages
conda install -c conda-forge streamlit pandas numpy
```

## Running the Application

```bash
# Start the Streamlit app
streamlit run main.py
```

The application will be available at http://localhost:8501.

## Customization

Modify the application to track your own growth metrics by editing the `main.py` file:

- Change the metrics in the dashboard
- Add new pages to the application
- Customize the resources section with your favorite learning materials

## Project Structure

- `main.py`: Main application file
- `pyproject.toml`: Project configuration and dependencies
- `README.md`: Project documentation

## License

This project is open source and available under the MIT License.
