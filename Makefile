.PHONY: test

test:
	bash launcher.sh test/01_input.json > test/01_test_out.txt && \
	echo diff test/01_output.txt test/01_test_out.txt && \
	diff test/01_output.txt test/01_test_out.txt && \
	bash launcher.sh test/02_input.json > test/02_test_out.txt && \
	echo diff test/02_output.txt test/02_test_out.txt && \
	diff test/02_output.txt test/02_test_out.txt && \
\
	bash launcher.sh test/03_input.json > test/03_test_out.txt && \
	echo diff test/03_output.txt test/03_test_out.txt && \
	diff test/03_output.txt test/03_test_out.txt && \
\
	bash launcher.sh test/04_input.json > test/04_test_out.txt && \
	echo diff test/04_output.txt test/04_test_out.txt && \
	diff test/04_output.txt test/04_test_out.txt && \
	\
	python tests.py
