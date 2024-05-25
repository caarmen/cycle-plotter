rm -rf reports
python -m pytest --cov=cycleplotter --cov-report=xml --cov-report=html --junitxml="reports/junit.xml" tests
mv coverage.xml htmlcov reports/.
