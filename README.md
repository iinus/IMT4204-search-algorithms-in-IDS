# IMT4204: Search Algorithms


## Usage 

<pre>
Usage: python3 fastsearch.py [options] [text] [pattern] 

Options:
  -h, --help  show this help message and exit
  --SO        Specify Shift-OR as alogorithm. Default is BNDM.
  --time      Print the execution time of algorithm.
  
 </pre>

### Example
<pre>
$ python3 fastsearch.py --SO  --time test.txt bra
*** Seraching for pattern bra ***
[*] Execution time: 3.826508186000865e-05
[+] Found pattern bra at pos 7
[+] Found pattern bra at pos 17
[+] Found pattern bra at pos 28
[+] Found pattern bra at pos 38
[+] Found pattern bra at pos 49
[+] Found pattern bra at pos 59
</pre> 
