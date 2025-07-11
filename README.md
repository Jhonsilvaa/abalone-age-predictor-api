# Abalone Age Prediction API


This is a RESTful Flask API to predict the age of abalone using physical measurements. The prediction is made by a pre-trained LightGBM regression model, and the API includes validation, preprocessing, and documentation.

## Prerequisites

* **Python >= 3.12.3** (Recommended: use [pyenv](https://github.com/pyenv/pyenv))

* **Poetry** (Dependency manager - [installation guide](https://python-poetry.org/docs/))

* **Git** (Version control system - [installation guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))

* **GNU Make** (Required for build automation):
   - **Linux**:  Usually pre-installed. If not, install it via your package manager (e.g., `sudo apt install make` on Debian/Ubuntu).
   - **macOS**: Install via  [Homebrew](https://brew.sh)  (`brew install make`)
   - **Windows**: Install via [Chocolatey](https://chocolatey.org/install) (`choco install make`).

## Installation

1. **Clone this repository**:
```bash
   git clone https://github.com/Jhonsilvaa/abalone-age-prediction-api.git
```

2.  **Navigate to project directory**:
```bash
   cd abalone-age-prediction-api
```
3. **Install dependencies with Make**:
```bash
    make install
```

## Running the API

Start the development server using Make:
```bash
    make run
```
> The API will be available at: `http://localhost:5000`

## API Endpoints

### GET /health

> Checks the health status of the API.

**Response**:

```json
{
  "status": "ok",
  "message": "API is running."
}
```
### POST /predict

> Predicts the age of an abalone from physical measurements.



**Request Body**:

```json
{
  "Diameter": 0.365,
  "Height": 0.095,
  "Length": 0.455,
  "Sex": "M",
  "Shell weight": 0.15,
  "Shucked weight": 0.2245,
  "Viscera weight": 0.101,
  "Whole weight": 0.514
}
```
**Successful Response**:
```json
{"prediction":9}
```
## API Documentation

Automatically generated OpenAPI documentation is available when the server is running:

- Redoc: `http://localhost:5000/apidoc/redoc`
- Swagger UI: `http://localhost:5000/apidoc/swagger`
- OpenAPI JSON: `http://localhost:5000/openapi.json`


## License

This project is licensed under the GNU General Public License v3.0, as indicated by the LICENSE file in the repository. 

