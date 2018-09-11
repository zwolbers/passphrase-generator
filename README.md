# Passphrase Generator

Simple script to create passphrases.  It uses a cryptographically strong
random number generator.

```console
$ ./passphrase-generator.py
avoid luger dreg bloat kg fodder
```

## Motivation

There are a number of passphrase generators out there already - most of
which are more fully featured.  Sufficiently paranoid people may wish to
audit the code, however many of the top search results are hopelessly
complex.  Nobody is going to dig through hundreds of lines of code, or keep
up with hundreds of commits.  I realized it was far easier to write my own
script than to check for issues in another (accidental or otherwise).

`passphrase-generator.py` is roughly 30 lines long - 90% of it is dedicated
to argument parsing, print statements, and white space.  There is no
packaging.  The paranoid should find it fairly easy to audit.

## Usage

```console
$ ./passphrase-generator.py --help
usage: passphrase-generator.py [-h] [-n NUM] [-f FILE] [-v]

Generate a Passphrase

optional arguments:
  -h, --help            show this help message and exit
  -n NUM, --num NUM     number of words
  -f FILE, --file FILE  path to dictionary
  -v, --verbose         verbose output
```

I reference the [Diceware FAQ](http://world.std.com/~reinhold/dicewarefaq.html)
to determine a passphrase length:

```console
$ ./passphrase-generator.py -n 8
flit island avis berth sauce screw paris swept
```

Alternative wordlists can be used -
[the EFF maintains several](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases).
It is assumed each line contains a single word:

```console
$ head -n 3 eff_large_wordlist.txt
abacus
abdomen
abdominal
$ ./passphrase-generator.py -f eff_large_wordlist.txt
unselfish conflict gracious disdain nappy smolder
```

Additional stats can be printed:

```console
$ ./passphrase-generator.py -v

baud human gimbal fish spore trio

Number of words:    6
Number of letters:  33
```

## Acknowledgements

* This script uses a code snippet from the
  [Python docs](https://docs.python.org/3/library/secrets.html#recipes-and-best-practices).
* The default word list is based off of Arnold G. Reinhold's
  [Diceware](http://world.std.com/~reinhold/diceware.html).  In order to
  create a simpler format, the word list was modified under the
  [Creative Commons License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/):
    * The dice-number prefix was removed.
    * The PGP signature was removed.

