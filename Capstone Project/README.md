# Selenium Python E-Commerce Automation Framework

A maintainable UI automation framework for the TutorialsNinja OpenCart demo store. It demonstrates Selenium WebDriver, Page Object Model (POM), pytest, unittest, CSV-driven test data, configuration management, failure screenshots, and HTML reporting.

**Application under test:** https://tutorialsninja.com/demo/  
**Scope:** login validation (negative/invalid credentials) and product search.


## 1. Framework structure

```text
capstone_project_selenium_ecommerce_framework/
├── config/
│   └── config.ini
├── framework/
│   ├── base_page.py
│   ├── config_reader.py
│   ├── data_reader.py
│   ├── driver_factory.py
│   └── screenshot_util.py
├── pages/
│   ├── home_page.py
│   ├── login_page.py
│   └── search_results_page.py
├── reports/
├── screenshots/
├── testdata/
│   ├── login_data.csv
│   └── search_data.csv
├── tests/
│   ├── pytest/
│   │   ├── conftest.py
│   │   ├── test_login.py
│   │   └── test_product_search.py
│   └── unittest/
│       └── test_login_unittest.py
├── pytest.ini
└── requirements.txt
```

## 2. Prerequisites

- Python 3.10 or newer
- Google Chrome
- Internet access to the demo site
- A terminal such as PowerShell, Command Prompt, or bash

Selenium 4 uses Selenium Manager to resolve the browser driver in typical environments. If your organization blocks driver downloads, install and configure the matching driver through its approved process.

## 3. Installation (Windows PowerShell)

```powershell
cd capstone_project_selenium_ecommerce_framework
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 4. Configuration

Edit `config/config.ini`:

- `base_url`: target application URL
- `browser`: `chrome` or `firefox`
- `headless`: `true` or `false`
- `explicit_wait`: explicit wait in seconds
- `page_load_timeout`: page load timeout in seconds

Set `headless = true` for CI execution. Do not commit real credentials or secrets. The supplied CSV uses invalid synthetic login data.

## 5. Execute tests

### pytest suite

```powershell
pytest tests/pytest -v
```

Generate a standalone HTML report:

```powershell
pytest tests/pytest -v --html=reports/pytest-report.html --self-contained-html
```

### unittest suite

```powershell
python -m unittest discover -s tests/unittest -p "test_*.py" -v
```

The unittest test is intentionally separate from pytest and can be run independently.

## 6. Test coverage

| ID | Framework | Scenario | Expected result |
|---|---|---|---|
| LGN-001 | pytest, CSV-driven | Submit invalid credentials | Login remains unsuccessful and validation warning is displayed |
| LGN-002 | unittest | Submit invalid credentials | Validation warning is displayed |
| SRCH-001 | pytest, CSV-driven | Search for `iphone` | Search heading and at least one matching product are displayed |
| SRCH-002 | pytest, CSV-driven | Search for `macbook` | Search heading and at least one matching product are displayed |

Search terms and login test data are maintained in `testdata/*.csv`. Update the search CSV if the demo catalogue changes.

## 7. Failure handling and reporting

- pytest: `tests/pytest/conftest.py` captures a PNG on a failed test and attaches it to the HTML report when the pytest-html plugin supports the attachment API.
- unittest: `tearDown()` captures a screenshot when the test reports an error or failure.
- Screenshots are written to `screenshots/`; reports are written to `reports/`.
- These output folders are excluded from version control except for their `.gitkeep` placeholders.

## 8. Design notes

- **POM:** page-specific locators and user actions are encapsulated in page classes; tests assert business outcomes.
- **BasePage:** centralizes explicit waits and common browser interactions.
- **DriverFactory:** centralizes browser creation and configuration.
- **ConfigReader:** reads environment-independent settings from INI.
- **CSVDataReader:** provides reusable data-driven test inputs.
- **Test isolation:** each test receives a fresh browser session.
- **Maintainability:** selectors are centralized in page objects, so UI changes can be updated in one place.

## 9. Troubleshooting

1. **Browser does not launch:** update Chrome/Firefox and confirm the machine can obtain a compatible driver.
2. **Site is unavailable:** verify connectivity and retry; this project depends on a third-party demo website.
3. **Search assertion fails:** inspect the current catalogue and update `testdata/search_data.csv` with products that exist.
4. **No screenshot appears:** confirm the test actually failed after browser creation and that the `screenshots/` directory is writable.
5. **HTML report is missing:** run the pytest command with `--html=reports/pytest-report.html --self-contained-html`.

