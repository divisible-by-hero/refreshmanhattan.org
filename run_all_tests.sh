#!/bin/bash

echo "** Running Automated Tests **"


echo "** Blog **"
coverage -e 
coverage -x manage.py test blog --settings=settings.local


echo "** WRITING COVERAGE REPORTS **"
coverage html -d ./reports/coverage_html
coverage -r -m >./reports/coverage_report.txt

