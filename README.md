## Binary Lattice
I included 3 programs which in turn vary `sigma`, `number of steps`, and `strike value`. These prgrams can print the lattice to stdout for visualization. Thsi can be enabled/disabled by toggling the 'print_tree' boolean. As submitted, this feature is disabled, as its more useful at smaller numbers of steps.

### Monte Carlo
By default, this program will output a matplot chart of all the random walks, as well as a `.csv` file containing the same results. Both of these features can be disabled by changing the booleans `plot` and `csv_out` to False.

![Random Walks](monte-carlo/plots/1.1.png)

### Run
Make sure you have Python3.6 or higher installed, then:

`$ pip3 install -r requirements.txt`  
`$ python3 <q1|q2>py`

### Clean
`$ pip3 uninstall -r requirements.txt`

