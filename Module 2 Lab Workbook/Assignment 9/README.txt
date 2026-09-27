ASSIGNMENT 9 - PyTest + HTML REPORTING

Install:
pip install selenium pytest pytest-html

Run from this folder:
pytest --html=report.html --self-contained-html

Expected:
- 4 tests collected
- 3 PASS
- 1 intentional FAIL
- Screenshot created under screenshots/
- report.html generated
- Failed test screenshot embedded in the HTML report

The intentional failure exists only to demonstrate the assignment
requirement of showing PASS and FAIL in one execution.
