args = sys.argv

# further code of the script "process_four_numbers.py"
print([int(x) for i, x in enumerate(args) if i > 0])
