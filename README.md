# PySpark GitHub Actions Example

A minimal repository demonstrating how to set up GitHub Actions for testing PySpark code with pytest and coverage across multiple platforms.

## Files

- `main.py` - Minimal PySpark example with a DataFrame row counting function
- `test_main.py` - Unit tests for main.py using pytest
- `test.yaml` - GitHub Actions workflow for running tests across OS/Python versions
- `coverage.yaml` - GitHub Actions workflow for coverage reporting

## Setup

### Local Development

```bash
# Install uv if you haven't already
pip install uv

# Install dependencies
uv pip install pytest pyspark coverage
```

### Running Tests Locally

```bash
# Run tests
pytest test_main.py -v

# Run tests with coverage
coverage run -m pytest test_main.py -v
coverage report -m
coverage html  # generates htmlcov/index.html
```

## GitHub Actions Workflows

### test.yaml - Multi-platform Testing

This workflow runs tests on:
- **Linux & macOS**: Python 3.9, 3.10, 3.11
- **Windows**: Python 3.11 only (with Java setup for PySpark)

Key features:
- Installs Java 17 on all platforms (required for PySpark)
- Uses `uv` for fast dependency installation
- Runs pytest with verbose output

### coverage.yaml - Coverage Reporting

This workflow provides **three coverage options** - choose the one that fits your needs:

#### Option 1: Codecov (Recommended for public repos)
- Uploads coverage to [Codecov.io](https://codecov.io)
- Provides detailed coverage visualization and PR comments
- **Setup**: 
  1. Sign up at codecov.io with your GitHub account
  2. Add your repository
  3. Add `CODECOV_TOKEN` to your repo secrets (Settings → Secrets → Actions)
  4. Keep the Codecov step in coverage.yaml

#### Option 2: Coverage PR Comments
- Posts coverage reports directly as PR comments
- No external service needed
- Uses `py-cov-action/python-coverage-comment-action`
- **Setup**: Already configured, just ensure GitHub Actions has write permissions

#### Option 3: Artifacts Only (Simplest)
- Saves coverage reports as workflow artifacts
- No external dependencies or tokens needed
- **Setup**: Replace the upload steps with:
  ```yaml
  - name: Upload coverage reports
    uses: actions/upload-artifact@v4
    with:
      name: coverage-report
      path: |
        coverage.xml
        htmlcov/
  ```

## Coverage CI/CD Recommendations

### For Learning (start here):
Use **Option 3** (artifacts only). Simply run coverage and view the HTML report in artifacts.

### For Open Source Projects:
Use **Option 1** (Codecov). It's free for public repos and provides the best visualization.

### For Private Projects:
Use **Option 2** (PR comments) if you want inline feedback, or **Option 3** if you just need the data.

### Enforcing Coverage Thresholds
Just readme change
Add a coverage check to fail the build if coverage drops:

```yaml
- name: Check coverage threshold
  run: |
    coverage report --fail-under=80
```

Add this after the `coverage report -m` step in coverage.yaml.

## Notes

- **Windows runners** require explicit Java installation for PySpark
- **uv** is used for faster dependency installation vs pip
- Coverage is run only on Linux with Python 3.11 to avoid redundant reporting
- The coverage workflow includes both Codecov upload and PR comment options - use whichever you prefer
