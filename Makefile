OUTPUT_DIR = out

site : clean
	# make output directory
	mkdir $(OUTPUT_DIR)

	# run generation script
	./make_index.py > $(OUTPUT_DIR)/index.html

clean :
	rm -rf $(OUTPUT_DIR)
