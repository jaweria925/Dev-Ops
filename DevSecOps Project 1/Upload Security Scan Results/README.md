Project:    Upload Security scan Results automatically to DefectDojo

UseCase:    Create python script that will automatically security scanning finding to vulnerability management tool using DefectDojo.

Techology used:

1. Pyhton
2. DefectDojo (via Rest API)
3. GitLab CI

Description:
1. Create a pyhton script that connect to DefectDojo via API key.
2. Create a Python script that upload njssan, semgrepscan and gitleaks scan files from Gitlab CI security scanning jobs to Defectdojo.
3. Add a new job into the Gitlab CI pipeline to run the python script to upload finding to Defectdojo as a part of pipeline execution.