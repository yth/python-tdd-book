python manage.py runserver &

if command -v xvfb-run 2>/dev/null; then
	xvfb-run -a python functional_tests.py
else
	python functional_test.py
fi

fg
