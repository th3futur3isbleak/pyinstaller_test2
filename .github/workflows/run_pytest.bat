pytest tests/ --junitxml=test_results/junit/test-results.xml ^
        --json-report ^
        --json-report-file=test_results/pytest-reports/unit_tests.json ^
        --html=test_results/pytest-reports/unit_tests_report.html ^
        --self-contained-html ^
        --cov=pyinstaller_test ^
        --cov-report html:test_results/coverage/cov_html ^
        --cov-report xml:test_results/coverage/cov.xml ^
        --cov-report annotate:test_results/coverage/cov_annotate ^
        --cov=%PACKAGE_NAME% tests/