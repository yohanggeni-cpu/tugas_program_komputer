# Exercise 8-15: Printing Models
# Fungsi berada di printing_functions.py dan diimpor ke program utama.
from ex_8_15.printing_functions import print_models, show_completed_models

unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
