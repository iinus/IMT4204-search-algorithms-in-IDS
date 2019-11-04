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

## About BNDM
The BNDM (Backward Non-deterministic DAWG Matching) (DAWG –Directed Acyclic Word Graph) is an ultra-fast bit-parallel exact search algorithm first published in 2000 by Navarroet al. The algorithm belongs to the class of so-called skip algorithms. These algorithms are capable of skipping the regions of the search string where the search pattern is impossible to be located. This capability makes them faster on average than search algorithms from the non-skip category. However, the skipping capability introduces a weakness in IDS application of this algorithm. An attacker can deliberately launch specially crafted traffic against a victim employing an IDS with such an algorithm implemented that would make the skip algorithm run slower than expected (so-called algorithmic attack).

## About Shift-OR
Shift-Or is an exact search algorithm, and is very similar to the Shift-And algorithm. Shift-Or uses bit parallelism to simulate the operation of a non-deterministic automaton that searches the pattern in the text. It complements both the bit mask for each symbol, and the search status word, D. If di = 0, there is an active machine. In that case, OR-ing with 1 is not necessary. Shift-or is slower on average than BNDM, however, it is resistant to algorithm attacks. 

## Execution time comparison 
![Alt text](/figures/PatternLength.png?raw=true)

![Alt text](/figures/TextLength.png?raw=true)
