error=0
for project in cycleplotter tests
do
  black $project --check || error=$?
  ruff check $project --output-format=github || error=$?
  isort --profile black $project || error=$?
done
exit $error
