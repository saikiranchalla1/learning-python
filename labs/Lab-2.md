# Strings and Text

Almost every useful program involves some kind of text processing, whether it is
parsing data or generating output. This lab focuses on common ### Problems
involving text manipulation, such as pulling apart strings, searching,
substitution, lexing, and parsing. Many of these tasks can be easily solved
using built-in methods of strings. However, more complicated operations might
require the use of regular expressions or the creation of a full-fledged parser.
All of these topics are covered. In addition, a few tricky aspects of working
with Unicode are addressed.

## 2.1. Splitting Strings on Any of Multiple Delimiters

### Problem

You need to split a string into fields, but the delimiters (and spacing around
them) aren’t consistent throughout the string.

### Solution

The split() method of string objects is really meant for very simple cases, and
does not allow for multiple delimiters or account for possible whitespace around
the delimiters. In cases when you need a bit more flexibility, use the
re.split() method:

```
>>> line = 'asdf fjdk; afed, fjek,asdf,      foo'
>>> import re
>>> re.split(r'[;,\s]\s*', line)
['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
```

### Discussion

The re.split() function is useful because you can specify multiple patterns for
the separator. For example, as shown in the ### Solution, the separator is
either a comma (,), semicolon (;), or whitespace followed by any amount of extra
whitespace. Whenever that pattern is found, the entire match becomes the
delimiter between whatever fields lie on either side of the match. The result is
a list of fields, just as with str.split().

When using re.split(), you need to be a bit careful should the regular
expression pattern involve a capture group enclosed in parentheses. If capture
groups are used, then the matched text is also included in the result. For
example, watch what happens here:

```
>>> fields = re.split(r'(;|,|\s)\s*', line)
>>> fields
['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']
>>>
```

Getting the split characters might be useful in certain contexts. For example,
maybe you need the split characters later on to reform an output string:

```
>>> values = fields[::2]
>>> delimiters = fields[1::2] + ['']
>>> values
['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
>>> delimiters
[' ', ';', ',', ',', ',', '']

>>> # Reform the line using the same delimiters
>>> ''.join(v+d for v,d in zip(values, delimiters))
'asdf fjdk;afed,fjek,asdf,foo'
>>>
```

If you don’t want the separator characters in the result, but still need to use
parentheses to group parts of the regular expression pattern, make sure you use
a noncapture group, specified as (?:...). For example:

```
>>> re.split(r'(?:,|;|\s)\s*', line)
['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
>>>
```

## 2.2. Matching Text at the Start or End of a String

### Problem

You need to check the start or end of a string for specific text patterns, such
as filename extensions, URL schemes, and so on.

### Solution

A simple way to check the beginning or end of a string is to use the
str.startswith() or str.endswith() methods. For example:

```
>>> filename = 'spam.txt'
>>> filename.endswith('.txt')
True
>>> filename.startswith('file:')
False
>>> url = 'http://www.python.org'
>>> url.startswith('http:')
True
>>>
```

If you need to check against multiple choices, simply provide a tuple of
possibilities to startswith() or endswith():

```
>>> import os
>>> filenames = os.listdir('.')
>>> filenames
[ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h' ]
>>> [name for name in filenames if name.endswith(('.c', '.h')) ]
['foo.c', 'spam.c', 'spam.h' ]
>>> any(name.endswith('.py') for name in filenames)
True
>>>
```

Here is another example:

```
from urllib.request import urlopen

def read_data(name):
if name.startswith(('http:', 'https:', 'ftp:')):
return urlopen(name).read()
else:
with open(name) as f:
return f.read()
```

Oddly, this is one part of Python where a tuple is actually required as input.
If you happen to have the choices specified in a list or set, just make sure you
convert them using tuple() first. For example:

```
>>> choices = ['http:', 'ftp:']
>>> url = 'http://www.python.org'
>>> url.startswith(choices)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: startswith first arg must be str or a tuple of str, not list
>>> url.startswith(tuple(choices))
True
>>>
```

### Discussion

The startswith() and endswith() methods provide a very convenient way to perform
basic prefix and suffix checking. Similar operations can be performed with
slices, but are far less elegant. For example:

```
>>> filename = 'spam.txt'
>>> filename[-4:] == '.txt'
True
>>> url = 'http://www.python.org'
>>> url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:'
True
>>>
```

You might also be inclined to use regular expressions as an alternative. For
example:

```
>>> import re
>>> url = 'http://www.python.org'
>>> re.match('http:|https:|ftp:', url)
<_sre.SRE_Match object at 0x101253098>
>>>
```

This works, but is often overkill for simple matching. Using this recipe is
simpler and runs faster.

Last, but not least, the startswith() and endswith() methods look nice when
combined with other operations, such as common data reductions. For example,
this statement that checks a directory for the presence of certain kinds of
files:

```
if any(name.endswith(('.c', '.h')) for name in listdir(dirname)):
...
```

## 2.3. Matching Strings Using Shell Wildcard Patterns

### Problem

You want to match text using the same wildcard patterns as are commonly used
when working in Unix shells (e.g., *.py, Dat[0-9]*.csv, etc.).

### Solution

The fnmatch module provides two functions—fnmatch() and fnmatchcase()—that can
be used to perform such matching. The usage is simple:

```
>>> from fnmatch import fnmatch, fnmatchcase
>>> fnmatch('foo.txt', '*.txt')
True
>>> fnmatch('foo.txt', '?oo.txt')
True
>>> fnmatch('Dat45.csv', 'Dat[0-9]*')
True
>>> names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
>>> [name for name in names if fnmatch(name, 'Dat*.csv')]
['Dat1.csv', 'Dat2.csv']
>>>
```

Normally, fnmatch() matches patterns using the same case-sensitivity rules as
the system’s underlying filesystem (which varies based on operating system). For
example:

```
>>> # On OS X (Mac)
>>> fnmatch('foo.txt', '*.TXT')
False

>>> # On Windows
>>> fnmatch('foo.txt', '*.TXT')
True
>>>
```

If this distinction matters, use fnmatchcase() instead. It matches exactly based
on the lower- and uppercase conventions that you supply:

```
>>> fnmatchcase('foo.txt', '*.TXT')
False
>>>
```

An often overlooked feature of these functions is their potential use with data
processing of nonfilename strings. For example, suppose you have a list of
street addresses like this:

```
addresses = [
'5412 N CLARK ST',
'1060 W ADDISON ST',
'1039 W GRANVILLE AVE',
'2122 N CLARK ST',
'4802 N BROADWAY',
]
```

You could write list comprehensions like this:

```
>>> from fnmatch import fnmatchcase
>>> [addr for addr in addresses if fnmatchcase(addr, '* ST')]
['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']
>>> [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
['5412 N CLARK ST']
>>>
```

### Discussion

The matching performed by fnmatch sits somewhere between the functionality of
simple string methods and the full power of regular expressions. If you’re just
trying to provide a simple mechanism for allowing wildcards in data processing
operations, it’s often a reasonable ### Solution.

If you’re actually trying to write code that matches filenames, use the glob
module instead. See Recipe 5.13.

## 2.4. Matching and Searching for Text Patterns

### Problem

You want to match or search text for a specific pattern.

### Solution

If the text you’re trying to match is a simple literal, you can often just use
the basic string methods, such as str.find(), str.endswith(), str.startswith(),
or similar. For example:

```
>>> text = 'yeah, but no, but yeah, but no, but yeah'

>>> # Exact match
>>> text == 'yeah'
False

>>> # Match at start or end
>>> text.startswith('yeah')
True
>>> text.endswith('no')
False

>>> # Search for the location of the first occurrence
>>> text.find('no')
10
>>>
```

For more complicated matching, use regular expressions and the re module. To
illustrate the basic mechanics of using regular expressions, suppose you want to
match dates specified as digits, such as “11/27/2012.” Here is a sample of how
you would do it:

```
>>> text1 = '11/27/2012'
>>> text2 = 'Nov 27, 2012'
>>>
>>> import re
>>> # Simple matching: \d+ means match one or more digits
>>> if re.match(r'\d+/\d+/\d+', text1):
...     print('yes')
... else:
...     print('no')
...
yes
>>> if re.match(r'\d+/\d+/\d+', text2):
...     print('yes')
... else:
...     print('no')
...
no
>>>
```

If you’re going to perform a lot of matches using the same pattern, it usually
pays to precompile the regular expression pattern into a pattern object first.
For example:

```
>>> datepat = re.compile(r'\d+/\d+/\d+')
>>> if datepat.match(text1):
...     print('yes')
... else:
...     print('no')
...
yes
>>> if datepat.match(text2):
...     print('yes')
... else:
...     print('no')
...
no
>>>
```

match() always tries to find the match at the start of a string. If you want to
search text for all occurrences of a pattern, use the findall() method instead.
For example:

```
>>> text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
>>> datepat.findall(text)
['11/27/2012', '3/13/2013']
>>>

```

When defining regular expressions, it is common to introduce capture groups by
enclosing parts of the pattern in parentheses. For example:

```
>>> datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
>>>

```

Capture groups often simplify subsequent processing of the matched text because
the contents of each group can be extracted individually. For example:

```
>>> m = datepat.match('11/27/2012')
>>> m
<_sre.SRE_Match object at 0x1005d2750>

>>> # Extract the contents of each group
>>> m.group(0)
'11/27/2012'
>>> m.group(1)
'11'
>>> m.group(2)
'27'
>>> m.group(3)
'2012'
>>> m.groups()
('11', '27', '2012')
>>> month, day, year = m.groups()
>>>

>>> # Find all matches (notice splitting into tuples)
>>> text
'Today is 11/27/2012. PyCon starts 3/13/2013.'
>>> datepat.findall(text)
[('11', '27', '2012'), ('3', '13', '2013')]
>>> for month, day, year in datepat.findall(text):
...     print('{}-{}-{}'.format(year, month, day))
...
2012-11-27
2013-3-13
>>>

```

The findall() method searches the text and finds all matches, returning them as
a list. If you want to find matches iteratively, use the finditer() method
instead. For example:

```
>>> for m in datepat.finditer(text):
...     print(m.groups())
...
('11', '27', '2012')
('3', '13', '2013')
>>>

```

### Discussion

A basic tutorial on the theory of regular expressions is beyond the scope of
this book. However, this recipe illustrates the absolute basics of using the re
module to match and search for text. The essential functionality is first
compiling a pattern using re.compile() and then using methods such as match(),
findall(), or finditer().

When specifying patterns, it is relatively common to use raw strings such as r'(
\d+)/(\d+)/(\d+)'. Such strings leave the backslash character uninterpreted,
which can be useful in the context of regular expressions. Otherwise, you need
to use double backslashes such as '(\\d+)/(\\d+)/(\\d+)'.

Be aware that the match() method only checks the beginning of a string. It’s
possible that it will match things you aren’t expecting. For example:

```
>>> m = datepat.match('11/27/2012abcdef')
>>> m
<_sre.SRE_Match object at 0x1005d27e8>
>>> m.group()
'11/27/2012'
>>>

```

If you want an exact match, make sure the pattern includes the end-marker ($),
as in the following:

```
>>> datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
>>> datepat.match('11/27/2012abcdef')
>>> datepat.match('11/27/2012')
<_sre.SRE_Match object at 0x1005d2750>
>>>
```

Last, if you’re just doing a simple text matching/searching operation, you can
often skip the compilation step and use module-level functions in the re module
instead. For example:

```
>>> re.findall(r'(\d+)/(\d+)/(\d+)', text)
[('11', '27', '2012'), ('3', '13', '2013')]
>>>
```

Be aware, though, that if you’re going to perform a lot of matching or
searching, it usually pays to compile the pattern first and use it over and over
again. The module-level functions keep a cache of recently compiled patterns, so
there isn’t a huge performance hit, but you’ll save a few lookups and extra
processing by using your own compiled pattern.

## 2.5. Searching and Replacing Text

### Problem

You want to search for and replace a text pattern in a string.

### Solution

For simple literal patterns, use the str.replace() method. For example:

```
>>> text = 'yeah, but no, but yeah, but no, but yeah'

>>> text.replace('yeah', 'yep')
'yep, but no, but yep, but no, but yep'
>>>
```

For more complicated patterns, use the sub() functions/methods in the re module.
To illustrate, suppose you want to rewrite dates of the form “11/27/2012” as
“2012-11-27.” Here is a sample of how to do it:

```
>>> text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
>>> import re
>>> re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
'Today is 2012-11-27. PyCon starts 2013-3-13.'
>>>
```

The first argument to sub() is the pattern to match and the second argument is
the replacement pattern. Backslashed digits such as \3 refer to capture group
numbers in the pattern.

If you’re going to perform repeated substitutions of the same pattern, consider
compiling it first for better performance. For example:

```
>>> import re
>>> datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
>>> datepat.sub(r'\3-\1-\2', text)
'Today is 2012-11-27. PyCon starts 2013-3-13.'
>>>

```

For more complicated substitutions, it’s possible to specify a substitution
callback function instead. For example:

```
>>> from calendar import month_abbr
>>> def change_date(m):
...     mon_name = month_abbr[int(m.group(1))]
...     return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
...
>>> datepat.sub(change_date, text)
'Today is 27 Nov 2012. PyCon starts 13 Mar 2013.'
>>>
```

As input, the argument to the substitution callback is a match object, as
returned by match() or find(). Use the .group() method to extract specific parts
of the match. The function should return the replacement text.

If you want to know how many substitutions were made in addition to getting the
replacement text, use re.subn() instead. For example:

```
>>> newtext, n = datepat.subn(r'\3-\1-\2', text)
>>> newtext
'Today is 2012-11-27. PyCon starts 2013-3-13.'
>>> n
2
>>>
```

### Discussion

There isn’t much more to regular expression search and replace than the sub()
method shown. The trickiest part is specifying the regular expression
pattern—something that’s best left as an exercise to the reader.

## 2.6. Searching and Replacing Case-Insensitive Text

### Problem

You need to search for and possibly replace text in a case-insensitive manner.

### Solution

To perform case-insensitive text operations, you need to use the re module and
supply the re.IGNORECASE flag to various operations. For example:

```
>>> text = 'UPPER PYTHON, lower python, Mixed Python'
>>> re.findall('python', text, flags=re.IGNORECASE)
['PYTHON', 'python', 'Python']
>>> re.sub('python', 'snake', text, flags=re.IGNORECASE)
'UPPER snake, lower snake, Mixed snake'
>>>
```

The last example reveals a limitation that replacing text won’t match the case
of the matched text. If you need to fix this, you might have to use a support
function, as in the following:

```
def matchcase(word):
def replace(m):
text = m.group()
if text.isupper():
return word.upper()
elif text.islower():
return word.lower()
elif text[0].isupper():
return word.capitalize()
else:
return word
return replace
```

Here is an example of using this last function:

```
>>> re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
'UPPER SNAKE, lower snake, Mixed Snake'
>>>
```

### Discussion

For simple cases, simply providing the re.IGNORECASE is enough to perform
case-insensitive matching. However, be aware that this may not be enough for
certain kinds of Unicode matching involving case folding. See Recipe 2.10 for
more details.

## 2.7. Specifying a Regular Expression for the Shortest Match

### Problem

You’re trying to match a text pattern using regular expressions, but it is
identifying the longest possible matches of a pattern. Instead, you would like
to change it to find the shortest possible match.

### Solution

This problem often arises in patterns that try to match text enclosed inside a
pair of starting and ending delimiters (e.g., a quoted string). To illustrate,
consider this example:

```
>>> str_pat = re.compile(r'\"(.*)\"')
>>> text1 = 'Computer says "no."'
>>> str_pat.findall(text1)
['no.']
>>> text2 = 'Computer says "no." Phone says "yes."'
>>> str_pat.findall(text2)
['no." Phone says "yes.']
>>>
```

In this example, the pattern r'\"(.*)\"' is attempting to match text enclosed
inside quotes. However, the * operator in a regular expression is greedy, so
matching is based on finding the longest possible match. Thus, in the second
example involving text2, it incorrectly matches the two quoted strings.

To fix this, add the ? modifier after the * operator in the pattern, like this:

```
>>> str_pat = re.compile(r'\"(.*?)\"')
>>> str_pat.findall(text2)
['no.', 'yes.']
>>>
```

This makes the matching nongreedy, and produces the shortest match instead.

### Discussion

This recipe addresses one of the more common ### Problems encountered when
writing regular expressions involving the dot (.) character. In a pattern, the
dot matches any character except a newline. However, if you bracket the dot with
starting and ending text (such as a quote), matching will try to find the
longest possible match to the pattern. This causes multiple occurrences of the
starting or ending text to be skipped altogether and included in the results of
the longer match. Adding the ? right after operators such as * or + forces the
matching algorithm to look for the shortest possible match instead.

## 2.8. Writing a Regular Expression for Multiline Patterns

### Problem

You’re trying to match a block of text using a regular expression, but you need
the match to span multiple lines.

### Solution

This problem typically arises in patterns that use the dot (.) to match any
character but forget to account for the fact that it doesn’t match newlines. For
example, suppose you are trying to match C-style comments:

```
>>> comment = re.compile(r'/\*(.*?)\*/')
>>> text1 = '/* this is a comment */'
>>> text2 = '''/* this is a
...               multiline comment */
... '''
>>>
>>> comment.findall(text1)
[' this is a comment ']
>>> comment.findall(text2)
[]
>>>
```

To fix the problem, you can add support for newlines. For example:

```
>>> comment = re.compile(r'/\*((?:.|\n)*?)\*/')
>>> comment.findall(text2)
[' this is a\n              multiline comment ']
>>>
```

In this pattern, (?:.|\n) specifies a noncapture group (i.e., it defines a group
for the purposes of matching, but that group is not captured separately or
numbered).

### Discussion

The re.compile() function accepts a flag, re.DOTALL, which is useful here. It
makes the . in a regular expression match all characters, including newlines.
For example:

```
>>> comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
>>> comment.findall(text2)
[' this is a\n              multiline comment ']
```

Using the re.DOTALL flag works fine for simple cases, but might be ###
Problematic if you’re working with extremely complicated patterns or a mix of
separate regular expressions that have been combined together for the purpose of
tokenizing, as described in Recipe 2.18. If given a choice, it’s usually better
to define your regular expression pattern so that it works correctly without the
need for extra flags.

## 2.9. Normalizing Unicode Text to a Standard Representation

### Problem

You’re working with Unicode strings, but need to make sure that all of the
strings have the same underlying representation.

### Solution

In Unicode, certain characters can be represented by more than one valid
sequence of code points. To illustrate, consider the following example:

```
>>> s1 = 'Spicy Jalape\u00f1o'
>>> s2 = 'Spicy Jalapen\u0303o'
>>> s1
'Spicy Jalapeño'
>>> s2
'Spicy Jalapeño'
>>> s1 == s2
False
>>> len(s1)
14
>>> len(s2)
15
>>>
```

Here the text “Spicy Jalapeño” has been presented in two forms. The first uses
the fully composed “ñ” character (U+00F1). The second uses the Latin letter “n”
followed by a “~” combining character (U+0303).

Having multiple representations is a ### Problem for programs that compare
strings. In order to fix this, you should first normalize the text into a
standard representation using the unicodedata module:

```
>>> import unicodedata
>>> t1 = unicodedata.normalize('NFC', s1)
>>> t2 = unicodedata.normalize('NFC', s2)
>>> t1 == t2
True
>>> print(ascii(t1))
'Spicy Jalape\xf1o'

>>> t3 = unicodedata.normalize('NFD', s1)
>>> t4 = unicodedata.normalize('NFD', s2)
>>> t3 == t4
True
>>> print(ascii(t3))
'Spicy Jalapen\u0303o'
>>>
```

The first argument to normalize() specifies how you want the string normalized.
NFC means that characters should be fully composed (i.e., use a single code
point if possible). NFD means that characters should be fully decomposed with
the use of combining characters.

Python also supports the normalization forms NFKC and NFKD, which add extra
compatibility features for dealing with certain kinds of characters. For
example:

```
>>> s = '\ufb01'   # A single character
>>> s
'ﬁ'
>>> unicodedata.normalize('NFD', s)
'ﬁ'

# Notice how the combined letters are broken apart here
>>> unicodedata.normalize('NFKD', s)
'fi'
>>> unicodedata.normalize('NFKC', s)
'fi'
>>>
```

### Discussion

Normalization is an important part of any code that needs to ensure that it
processes Unicode text in a sane and consistent way. This is especially true
when processing strings received as part of user input where you have little
control of the encoding.

Normalization can also be an important part of sanitizing and filtering text.
For example, suppose you want to remove all diacritical marks from some text (
possibly for the purposes of searching or matching):

```
>>> t1 = unicodedata.normalize('NFD', s1)
>>> ''.join(c for c in t1 if not unicodedata.combining(c))
'Spicy Jalapeno'
>>>
```

This last example shows another important aspect of the unicodedata
module—namely, utility functions for testing characters against character
classes. The combining() function tests a character to see if it is a combining
character. There are other functions in the module for finding character
categories, testing digits, and so forth.

Unicode is obviously a large topic. For more detailed reference information
about normalization, visit Unicode’s page on the subject. Ned Batchelder has
also given an excellent presentation on Python Unicode handling issues at his
website.

## 2.10. Working with Unicode Characters in Regular Expressions

### Problem

You are using regular expressions to process text, but are concerned about the
handling of Unicode characters.

### Solution

By default, the re module is already programmed with rudimentary knowledge of
certain Unicode character classes. For example, \d already matches any unicode
digit character:

```
>>> import re
>>> num = re.compile('\d+')
>>> # ASCII digits
>>> num.match('123')
<_sre.SRE_Match object at 0x1007d9ed0>

>>> # Arabic digits
>>> num.match('\u0661\u0662\u0663')
<_sre.SRE_Match object at 0x101234030>
>>>
```

If you need to include specific Unicode characters in patterns, you can use the
usual escape sequence for Unicode characters (e.g., \uFFFF or \UFFFFFFF). For
example, here is a regex that matches all characters in a few different Arabic
code pages:

```
>>> arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')
>>>
```

When performing matching and searching operations, it’s a good idea to normalize
and possibly sanitize all text to a standard form first (see Recipe 2.9).
However, it’s also important to be aware of special cases. For example, consider
the behavior of case-insensitive matching combined with case folding:

```
>>> pat = re.compile('stra\u00dfe', re.IGNORECASE)
>>> s = 'straße'
>>> pat.match(s)              # Matches
<_sre.SRE_Match object at 0x10069d370>
>>> pat.match(s.upper())      # Doesn't match
>>> s.upper()                 # Case folds
'STRASSE'
>>>
```

### Discussion

Mixing Unicode and regular expressions is often a good way to make your head
explode. If you’re going to do it seriously, you should consider installing the
third-party regex library, which provides full support for Unicode case folding,
as well as a variety of other interesting features, including approximate
matching.

## 2.11. Stripping Unwanted Characters from Strings

### Problem

You want to strip unwanted characters, such as whitespace, from the beginning,
end, or middle of a text string.

### Solution

The strip() method can be used to strip characters from the beginning or end of
a string. lstrip() and rstrip() perform stripping from the left or right side,
respectively. By default, these methods strip whitespace, but other characters
can be given. For example:

```
>>> # Whitespace stripping
>>> s = '   hello world  \n'
>>> s.strip()
'hello world'
>>> s.lstrip()
'hello world  \n'
>>> s.rstrip()
'   hello world'
>>>

>>> # Character stripping
>>> t = '-----hello====='
>>> t.lstrip('-')
'hello====='
>>> t.strip('-=')
'hello'
>>>
```

### Discussion

The various strip() methods are commonly used when reading and cleaning up data
for later processing. For example, you can use them to get rid of whitespace,
remove quotations, and other tasks.

Be aware that stripping does not apply to any text in the middle of a string.
For example:

```
>>> s = '  hello       world   \n'
>>> s = s.strip()
>>> s
'hello       world'
>>>
```

If you needed to do something to the inner space, you would need to use another
technique, such as using the replace() method or a regular expression
substitution. For example:

```
>>> s.replace(' ', '')
'helloworld'
>>> import re
>>> re.sub('\s+', ' ', s)
'hello world'
>>>
```

It is often the case that you want to combine string stripping operations with
some other kind of iterative processing, such as reading lines of data from a
file. If so, this is one area where a generator expression can be useful. For
example:

```
with open(filename) as f:
lines = (line.strip() for line in f)
for line in lines:
...

```

Here, the expression lines = (line.strip() for line in f) acts as a kind of data
transform. It’s efficient because it doesn’t actually read the data into any
kind of temporary list first. It just creates an iterator where all of the lines
produced have the stripping operation applied to them.

For even more advanced stripping, you might turn to the translate() method. See
the next recipe on sanitizing strings for further details.

## 2.12. Sanitizing and Cleaning Up Text

### Problem

Some bored script kiddie has entered the text “pýtĥöñ” into a form on your web
page and you’d like to clean it up somehow.

### Solution

The problem of sanitizing and cleaning up text applies to a wide variety of ###
Problems involving text parsing and data handling. At a very simple level, you
might use basic string functions (e.g., str.upper() and str.lower()) to convert
text to a standard case. Simple replacements using str.replace() or re.sub() can
focus on removing or changing very specific character sequences. You can also
normalize text using unicodedata.normalize(), as shown in Recipe 2.9.

However, you might want to take the sanitation process a step further. Perhaps,
for example, you want to eliminate whole ranges of characters or strip
diacritical marks. To do so, you can turn to the often overlooked
str.translate() method. To illustrate, suppose you’ve got a messy string such as
the following:

```
>>> s = 'pýtĥöñ\fis\tawesome\r\n'
>>> s
'pýtĥöñ\x0cis\tawesome\r\n'
>>>
```

The first step is to clean up the whitespace. To do this, make a small
translation table and use translate():

```
>>> remap = {
...     ord('\t') : ' ',
...     ord('\f') : ' ',
...     ord('\r') : None      # Deleted
... }
>>> a = s.translate(remap)
>>> a
'pýtĥöñ is awesome\n'
>>>
```

As you can see here, whitespace characters such as \t and \f have been remapped
to a single space. The carriage return \r has been deleted entirely.

You can take this remapping idea a step further and build much bigger tables.
For example, let’s remove all combining characters:

```
>>> import unicodedata
>>> import sys
>>> cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
...                          if unicodedata.combining(chr(c)))
...
>>> b = unicodedata.normalize('NFD', a)
>>> b
'pýtĥöñ is awesome\n'
>>> b.translate(cmb_chrs)
'python is awesome\n'
>>>
```

In this last example, a dictionary mapping every Unicode combining character to
None is created using the dict.fromkeys().

The original input is then normalized into a decomposed form using
unicodedata.normalize(). From there, the translate function is used to delete
all of the accents. Similar techniques can be used to remove other kinds of
characters (e.g., control characters, etc.).

As another example, here is a translation table that maps all Unicode decimal
digit characters to their equivalent in ASCII:

```

>>> digitmap = { c: ord('0') + unicodedata.digit(chr(c))
...             for c in range(sys.maxunicode)
...             if unicodedata.category(chr(c)) == 'Nd' }
...
>>> len(digitmap)
460
>>> # Arabic digits
>>> x = '\u0661\u0662\u0663'
>>> x.translate(digitmap)
'123'
>>>
```

Yet another technique for cleaning up text involves I/O decoding and encoding
functions. The idea here is to first do some preliminary cleanup of the text,
and then run it through a combination of encode() or decode() operations to
strip or alter it. For example:

```
>>> a
'pýtĥöñ is awesome\n'
>>> b = unicodedata.normalize('NFD', a)
>>> b.encode('ascii', 'ignore').decode('ascii')
'python is awesome\n'
>>>
```

Here the normalization process decomposed the original text into characters
along with separate combining characters. The subsequent ASCII encoding/decoding
simply discarded all of those characters in one fell swoop. Naturally, this
would only work if getting an ASCII representation was the final goal.

### Discussion

A major issue with sanitizing text can be runtime performance. As a general
rule, the simpler it is, the faster it will run. For simple replacements, the
str.replace() method is often the fastest approach—even if you have to call it
multiple times. For instance, to clean up whitespace, you could use code like
this:

```
def clean_spaces(s):
s = s.replace('\r', '')
s = s.replace('\t', ' ')
s = s.replace('\f', ' ')
return s
```

If you try it, you’ll find that it’s quite a bit faster than using translate()
or an approach using a regular expression.

On the other hand, the translate() method is very fast if you need to perform
any kind of nontrivial character-to-character remapping or deletion.

In the big picture, performance is something you will have to study further in
your particular application. Unfortunately, it’s impossible to suggest one
specific technique that works best for all cases, so try different approaches
and measure it.

Although the focus of this recipe has been text, similar techniques can be
applied to bytes, including simple replacements, translation, and regular
expressions.

## 2.13. Aligning Text Strings

### Problem

You need to format text with some sort of alignment applied.

### Solution

For basic alignment of strings, the ljust(), rjust(), and center() methods of
strings can be used. For example:

```
>>> text = 'Hello World'
>>> text.ljust(20)
'Hello World         '
>>> text.rjust(20)
'         Hello World'
>>> text.center(20)
'    Hello World     '
>>>
```

All of these methods accept an optional fill character as well. For example:

```
>>> text.rjust(20,'=')
'=========Hello World'
>>> text.center(20,'*')
'****Hello World*****'
>>>
```

The format() function can also be used to easily align things. All you need to
do is use the <, >, or ^ characters along with a desired width. For example:

```

>>> format(text, '>20')
'         Hello World'
>>> format(text, '<20')
'Hello World         '
>>> format(text, '^20')
'    Hello World     '
>>>
```

If you want to include a fill character other than a space, specify it before
the alignment character:

```
>>> format(text, '=>20s')
'=========Hello World'
>>> format(text, '*^20s')
'****Hello World*****'
>>>
```

These format codes can also be used in the format() method when formatting
multiple values. For example:

```
>>> '{:>10s} {:>10s}'.format('Hello', 'World')
'     Hello      World'
>>>
```

One benefit of format() is that it is not specific to strings. It works with any
value, making it more general purpose. For instance, you can use it with
numbers:

```
>>> x = 1.2345
>>> format(x, '>10')
'    1.2345'
>>> format(x, '^10.2f')
'   1.23   '
>>>
```

### Discussion

In older code, you will also see the % operator used to format text. For
example:

```
>>> '%-20s' % text
'Hello World         '
>>> '%20s' % text
'         Hello World'
>>>
```

However, in new code, you should probably prefer the use of the format()
function or method. format() is a lot more powerful than what is provided with
the % operator. Moreover, format() is more general purpose than using the
jlust(), rjust(), or center() method of strings in that it works with any kind
of object.

For a complete list of features available with the format() function, consult
the online Python documentation.

## 2.14. Combining and Concatenating Strings

### Problem

You want to combine many small strings together into a larger string.

### Solution

If the strings you wish to combine are found in a sequence or iterable, the
fastest way to combine them is to use the join() method. For example:

```
>>> parts = ['Is', 'Chicago', 'Not', 'Chicago?']
>>> ' '.join(parts)
'Is Chicago Not Chicago?'
>>> ','.join(parts)
'Is,Chicago,Not,Chicago?'
>>> ''.join(parts)
'IsChicagoNotChicago?'
>>>
```

At first glance, this syntax might look really odd, but the join() operation is
specified as a method on strings. Partly this is because the objects you want to
join could come from any number of different data sequences (e.g., lists,
tuples, dicts, files, sets, or generators), and it would be redundant to have
join() implemented as a method on all of those objects separately. So you just
specify the separator string that you want and use the join() method on it to
glue text fragments together.

If you’re only combining a few strings, using + usually works well enough:

```
>>> a = 'Is Chicago'
>>> b = 'Not Chicago?'
>>> a + ' ' + b
'Is Chicago Not Chicago?'
>>>
```

The + operator also works fine as a substitute for more complicated string
formatting operations. For example:

```
>>> print('{} {}'.format(a,b))
Is Chicago Not Chicago?
>>> print(a + ' ' + b)
Is Chicago Not Chicago?
>>>
```

If you’re trying to combine string literals together in source code, you can
simply place them adjacent to each other with no + operator. For example:

```
>>> a = 'Hello' 'World'
>>> a
'HelloWorld'
>>>
```

### Discussion

Joining strings together might not seem advanced enough to warrant an entire
recipe, but it’s often an area where programmers make programming choices that
severely impact the performance of their code.

The most important thing to know is that using the + operator to join a lot of
strings together is grossly inefficient due to the memory copies and garbage
collection that occurs. In particular, you never want to write code that joins
strings together like this:

```
s = ''
for p in parts:
s += p
```

This runs quite a bit slower than using the join() method, mainly because each
+= operation creates a new string object. You’re better off just collecting all
of the parts first and then joining them together at the end.

One related (and pretty neat) trick is the conversion of data to strings and
concatenation at the same time using a generator expression, as described in
Recipe 1.19. For example:

```

>>> data = ['ACME', 50, 91.1]
>>> ','.join(str(d) for d in data)
'ACME,50,91.1'
>>>
```

Also be on the lookout for unnecessary string concatenations. Sometimes
programmers get carried away with concatenation when it’s really not technically
necessary. For example, when printing:

```
print(a + ':' + b + ':' + c)       # Ugly
print(':'.join([a, b, c]))         # Still ugly

print(a, b, c, sep=':')            # Better
```

Mixing I/O operations and string concatenation is something that might require
study in your application. For example, consider the following two code
fragments:

```
# Version 1 (string concatenation)
f.write(chunk1 + chunk2)

# Version 2 (separate I/O operations)
f.write(chunk1)
f.write(chunk2)
```

If the two strings are small, the first version might offer much better
performance due to the inherent expense of carrying out an I/O system call. On
the other hand, if the two strings are large, the second version may be more
efficient, since it avoids making a large temporary result and copying large
blocks of memory around. Again, it must be stressed that this is something you
would have to study in relation to your own data in order to determine which
performs best.

Last, but not least, if you’re writing code that is building output from lots of
small strings, you might consider writing that code as a generator function,
using yield to emit fragments. For example:

```

def sample():
yield 'Is'
yield 'Chicago'
yield 'Not'
yield 'Chicago?'
```

The interesting thing about this approach is that it makes no assumption about
how the fragments are to be assembled together. For example, you could simply
join the fragments using join():

```
text = ''.join(sample())
```

Or you could redirect the fragments to I/O:

```
for part in sample():
f.write(part)
```

Or you could come up with some kind of hybrid scheme that’s smart about
combining I/O operations:

```
def combine(source, maxsize):
parts = []
size = 0
for part in source:
parts.append(part)
size += len(part)
if size > maxsize:
yield ''.join(parts)
parts = []
size = 0
yield ''.join(parts)

for part in combine(sample(), 32768):
f.write(part)
```

The key point is that the original generator function doesn’t have to know the
precise details. It just yields the parts.

## 2.15. Interpolating Variables in Strings

### Problem

You want to create a string in which embedded variable names are substituted
with a string representation of a variable’s value.

### Solution

Python has no direct support for simply substituting variable values in strings.
However, this feature can be approximated using the format() method of strings.
For example:

```
>>> s = '{name} has {n} messages.'
>>> s.format(name='Guido', n=37)
'Guido has 37 messages.'
>>>
```

Alternatively, if the values to be substituted are truly found in variables, you
can use the combination of format_map() and vars(), as in the following:

```
>>> name = 'Guido'
>>> n = 37
>>> s.format_map(vars())
'Guido has 37 messages.'
>>>
```

One subtle feature of vars() is that it also works with instances. For example:

```
>>> class Info:
...     def __init__(self, name, n):
...         self.name = name
...         self.n = n
...
>>> a = Info('Guido',37)
>>> s.format_map(vars(a))
'Guido has 37 messages.'
>>>
```

One downside of format() and format_map() is that they do not deal gracefully
with missing values. For example:

```
>>> s.format(name='Guido')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
KeyError: 'n'
>>>
```

One way to avoid this is to define an alternative dictionary class with a __
missing__() method, as in the following:

```
class safesub(dict):
def __missing__(self, key):
return '{' + key + '}'
```

Now use this class to wrap the inputs to format_map():

```
>>> del n     # Make sure n is undefined
>>> s.format_map(safesub(vars()))
'Guido has {n} messages.'
>>>
```

If you find yourself frequently performing these steps in your code, you could
hide the variable substitution process behind a small utility function that
employs a so-called “frame hack.” For example:

```
import sys

def sub(text):
return text.format_map(safesub(sys._getframe(1).f_locals))
```

Now you can type things like this:

```
>>> name = 'Guido'
>>> n = 37
>>> print(sub('Hello {name}'))
Hello Guido
>>> print(sub('You have {n} messages.'))
You have 37 messages.
>>> print(sub('Your favorite color is {color}'))
Your favorite color is {color}
>>>
```

### Discussion

The lack of true variable interpolation in Python has led to a variety of ###
Solutions over the years. As an alternative to the ### Solution presented in
this recipe, you will sometimes see string formatting like this:

```
>>> name = 'Guido'
>>> n = 37
>>> '%(name) has %(n) messages.' % vars()
'Guido has 37 messages.'
>>>
```

You may also see the use of template strings:

```
>>> import string
>>> s = string.Template('$name has $n messages.')
>>> s.substitute(vars())
'Guido has 37 messages.'
>>>
```

However, the format() and format_map() methods are more modern than either of
these alternatives, and should be preferred. One benefit of using format() is
that you also get all of the features related to string formatting (alignment,
padding, numerical formatting, etc.), which is simply not possible with
alternatives such as Template string objects.

Parts of this recipe also illustrate a few interesting advanced features. The
little-known __missing__() method of mapping/dict classes is a method that you
can define to handle missing values. In the safesub class, this method has been
defined to return missing values back as a placeholder. Instead of getting a
KeyError exception, you would see the missing values appearing in the resulting
string (potentially useful for debugging).

The sub() function uses sys._getframe(1) to return the stack frame of the
caller. From that, the f_locals attribute is accessed to get the local
variables. It goes without saying that messing around with stack frames should
probably be avoided in most code. However, for utility functions such as a
string substitution feature, it can be useful. As an aside, it’s probably worth
noting that f_locals is a dictionary that is a copy of the local variables in
the calling function. Although you can modify the contents of f_locals, the
modifications don’t actually have any lasting effect. Thus, even though
accessing a different stack frame might look evil, it’s not possible to
accidentally overwrite variables or change the local environment of the caller.

## 2.16. Reformatting Text to a Fixed Number of Columns

### Problem

You have long strings that you want to reformat so that they fill a
user-specified number of columns.

### Solution

Use the textwrap module to reformat text for output. For example, suppose you
have the following long string:

```
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
Here’s how you can use the textwrap module to reformat it in various ways:

>>> import textwrap
>>> print(textwrap.fill(s, 70))
Look into my eyes, look into my eyes, the eyes, the eyes, the eyes,
not around the eyes, don't look around the eyes, look into my eyes,
you're under.

>>> print(textwrap.fill(s, 40))
Look into my eyes, look into my eyes,
the eyes, the eyes, the eyes, not around
the eyes, don't look around the eyes,
look into my eyes, you're under.

>>> print(textwrap.fill(s, 40, initial_indent='    '))
Look into my eyes, look into my
eyes, the eyes, the eyes, the eyes, not
around the eyes, don't look around the
eyes, look into my eyes, you're under.

>>> print(textwrap.fill(s, 40, subsequent_indent='    '))
Look into my eyes, look into my eyes,
the eyes, the eyes, the eyes, not
around the eyes, don't look around
the eyes, look into my eyes, you're
under.
```

### Discussion

The textwrap module is a straightforward way to clean up text for
printing—especially if you want the output to fit nicely on the terminal. On the
subject of the terminal size, you can obtain it using os.get_terminal_size().
For example:

```
>>> import os
>>> os.get_terminal_size().columns
80
>>>
```

The fill() method has a few additional options that control how it handles tabs,
sentence endings, and so on. Look at the documentation for the
textwrap.TextWrapper class for further details.

## 2.17. Handling HTML and XML Entities in Text

### Problem

You want to replace HTML or XML entities such as &entity; or &#code; with their
corresponding text. Alternatively, you need to produce text, but escape certain
characters (e.g., <, >, or &).

### Solution

If you are producing text, replacing special characters such as < or > is
relatively easy if you use the html.escape() function. For example:

```
>>> s = 'Elements are written as "<tag>text</tag>".'
>>> import html
>>> print(s)
Elements are written as "<tag>text</tag>".
>>> print(html.escape(s))
Elements are written as &quot;&lt;tag&gt;text&lt;/tag&gt;&quot;.

>>> # Disable escaping of quotes
>>> print(html.escape(s, quote=False))
Elements are written as "&lt;tag&gt;text&lt;/tag&gt;".
>>>
```

If you’re trying to emit text as ASCII and want to embed character code entities
for non-ASCII characters, you can use the errors='xmlcharrefreplace' argument to
various I/O-related functions to do it. For example:

```
>>> s = 'Spicy Jalapeño'
>>> s.encode('ascii', errors='xmlcharrefreplace')
b'Spicy Jalape&#241;o'
>>>
```

To replace entities in text, a different approach is needed. If you’re actually
processing HTML or XML, try using a proper HTML or XML parser first. Normally,
these tools will automatically take care of replacing the values for you during
parsing and you don’t need to worry about it.

If, for some reason, you’ve received bare text with some entities in it and you
want them replaced manually, you can usually do it using various utility
functions/methods associated with HTML or XML parsers. For example:

```

>>> s = 'Spicy &quot;Jalape&#241;o&quot.'
>>> from html.parser import HTMLParser
>>> p = HTMLParser()
>>> p.unescape(s)
'Spicy "Jalapeño".'
>>>
>>> t = 'The prompt is &gt;&gt;&gt;'
>>> from xml.sax.saxutils import unescape
>>> unescape(t)
'The prompt is >>>'
>>>
```

### Discussion

Proper escaping of special characters is an easily overlooked detail of
generating HTML or XML. This is especially true if you’re generating such output
yourself using print() or other basic string formatting features. Using a
utility function such as html.escape() is an easy ### Solution.

If you need to process text in the other direction, various utility functions,
such as xml.sax.saxutils.unescape(), can help. However, you really need to
investigate the use of a proper parser. For example, if processing HTML or XML,
using a parsing module such as html.parser or xml.etree.ElementTree should
already take care of details related to replacing entities in the input text for
you.

## 2.18. Tokenizing Text

### Problem

You have a string that you want to parse left to right into a stream of tokens.

### Solution

Suppose you have a string of text such as this:

```
text = 'foo = 23 + 42 * 10'
```

To tokenize the string, you need to do more than merely match patterns. You need
to have some way to identify the kind of pattern as well. For instance, you
might want to turn the string into a sequence of pairs like this:

```
tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
```

To do this kind of splitting, the first step is to define all of the possible
tokens, including whitespace, by regular expression patterns using named capture
groups such as this:

```
import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM  = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ    = r'(?P<EQ>=)'
WS    = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
```

In these re patterns, the ?P<TOKENNAME> convention is used to assign a name to
the pattern. This will be used later.

Next, to tokenize, use the little-known scanner() method of pattern objects.
This method creates a scanner object in which repeated calls to match() step
through the supplied text one match at a time. Here is an interactive example of
how a scanner object works:

```
>>> scanner = master_pat.scanner('foo = 42')
>>> scanner.match()
<_sre.SRE_Match object at 0x100677738>
>>> _.lastgroup, _.group()
('NAME', 'foo')
>>> scanner.match()
<_sre.SRE_Match object at 0x100677738>
>>> _.lastgroup, _.group()
('WS', ' ')
>>> scanner.match()
<_sre.SRE_Match object at 0x100677738>
>>> _.lastgroup, _.group()
('EQ', '=')
>>> scanner.match()
<_sre.SRE_Match object at 0x100677738>
>>> _.lastgroup, _.group()
('WS', ' ')
>>> scanner.match()
<_sre.SRE_Match object at 0x100677738>
>>> _.lastgroup, _.group()
('NUM', '42')
>>> scanner.match()
>>>
```

To take this technique and put it into code, it can be cleaned up and easily
packaged into a generator like this:

```
from collections import namedtuple

Token = namedtuple('Token', ['type','value'])

def generate_tokens(pat, text):
scanner = pat.scanner(text)
for m in iter(scanner.match, None):
yield Token(m.lastgroup, m.group())

# Example use
for tok in generate_tokens(master_pat, 'foo = 42'):
print(tok)

# Produces output
# Token(type='NAME', value='foo')
# Token(type='WS', value=' ')
# Token(type='EQ', value='=')
# Token(type='WS', value=' ')
# Token(type='NUM', value='42')
```

If you want to filter the token stream in some way, you can either define more
generator functions or use a generator expression. For example, here is how you
might filter out all whitespace tokens.

```
tokens = (tok for tok in generate_tokens(master_pat, text)
if tok.type != 'WS')
for tok in tokens:
print(tok)
```

### Discussion

Tokenizing is often the first step for more advanced kinds of text parsing and
handling. To use the scanning technique shown, there are a few important details
to keep in mind. First, you must make sure that you identify every possible text
sequence that might appear in the input with a correponding re pattern. If any
nonmatching text is found, scanning simply stops. This is why it was necessary
to specify the whitespace (WS) token in the example.

The order of tokens in the master regular expression also matters. When
matching, re tries to match pattens in the order specified. Thus, if a pattern
happens to be a substring of a longer pattern, you need to make sure the longer
pattern goes first. For example:

```
LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'

master_pat = re.compile('|'.join([LE, LT, EQ]))    # Correct
# master_pat = re.compile('|'.join([LT, LE, EQ]))  # Incorrect
```

The second pattern is wrong because it would match the text <= as the token LT
followed by the token EQ, not the single token LE, as was probably desired.

Last, but not least, you need to watch out for patterns that form substrings.
For example, suppose you have two pattens like this:

```
PRINT = r'(P<PRINT>print)'
NAME  = r'(P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'

master_pat = re.compile('|'.join([PRINT, NAME]))

for tok in generate_tokens(master_pat, 'printer'):
print(tok)

# Outputs :
#  Token(type='PRINT', value='print')
#  Token(type='NAME', value='er')
```

For more advanced kinds of tokenizing, you may want to check out packages such
as PyParsing or PLY. An example involving PLY appears in the next recipe.

## 2.19. Writing a Simple Recursive Descent Parser

### Problem

You need to parse text according to a set of grammar rules and perform actions
or build an abstract syntax tree representing the input. The grammar is small,
so you’d prefer to just write the parser yourself as opposed to using some kind
of framework.

### Solution

In this ### Problem, we’re focused on the ### Problem of parsing text according
to a particular grammar. In order to do this, you should probably start by
having a formal specification of the grammar in the form of a BNF or EBNF. For
example, a grammar for simple arithmetic expressions might look like this:

```
    expr ::= expr + term
         |   expr - term
         |   term

    term ::= term * factor
         |   term / factor
         |   factor

    factor ::= ( expr )
           |   NUM
```

Or, alternatively, in EBNF form:

```
    expr ::= term { (+|-) term }*

    term ::= factor { (*|/) factor }*

    factor ::= ( expr )
           |   NUM
```

In an EBNF, parts of a rule enclosed in { ... }* are optional. The * means zero
or more repetitions (the same meaning as in a regular expression).

Now, if you’re not familiar with the mechanics of working with a BNF, think of
it as a specification of substitution or replacement rules where symbols on the
left side can be replaced by the symbols on the right (or vice versa).
Generally, what happens during parsing is that you try to match the input text
to the grammar by making various substitutions and expansions using the BNF. To
illustrate, suppose you are parsing an expression such as 3 + 4 * 5. This
expression would first need to be broken down into a token stream, using the
techniques described in Recipe 2.18. The result might be a sequence of tokens
like this:

```
    NUM + NUM * NUM
```

From there, parsing involves trying to match the grammar to input tokens by
making substitutions:

```
    expr
    expr ::= term { (+|-) term }*
    expr ::= factor { (*|/) factor }* { (+|-) term }*
    expr ::= NUM { (*|/) factor }* { (+|-) term }*
    expr ::= NUM { (+|-) term }*
    expr ::= NUM + term { (+|-) term }*
    expr ::= NUM + factor { (*|/) factor }* { (+|-) term }*
    expr ::= NUM + NUM { (*|/) factor}* { (+|-) term }*
    expr ::= NUM + NUM * factor { (*|/) factor }* { (+|-) term }*
    expr ::= NUM + NUM * NUM { (*|/) factor }* { (+|-) term }*
    expr ::= NUM + NUM * NUM { (+|-) term }*
    expr ::= NUM + NUM * NUM
```

Following all of the substitution steps takes a bit of coffee, but they’re
driven by looking at the input and trying to match it to grammar rules. The
first input token is a NUM, so substitutions first focus on matching that part.
Once matched, attention moves to the next token of + and so on. Certain parts of
the righthand side (e.g., { (*/) factor }*) disappear when it’s determined that
they can’t match the next token. In a successful parse, the entire righthand
side is expanded completely to match the input token stream.

With all of the preceding background in place, here is a simple recipe that
shows how to build a recursive descent expression evaluator:

```
import re
import collections

# Token specification
NUM    = r'(?P<NUM>\d+)'
PLUS   = r'(?P<PLUS>\+)'
MINUS  = r'(?P<MINUS>-)'
TIMES  = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS     = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES,
DIVIDE, LPAREN, RPAREN, WS]))

# Tokenizer
Token = collections.namedtuple('Token', ['type','value'])

def generate_tokens(text):
scanner = master_pat.scanner(text)
for m in iter(scanner.match, None):
tok = Token(m.lastgroup, m.group())
if tok.type != 'WS':
yield tok

# Parser
class ExpressionEvaluator:
'''
Implementation of a recursive descent parser.   Each method
implements a single grammar rule.  Use the ._accept() method
to test and accept the current lookahead token.  Use the ._expect()
method to exactly match and discard the next token on the input
(or raise a SyntaxError if it doesn't match).
'''

    def parse(self,text):
        self.tokens = generate_tokens(text)
        self.tok = None             # Last symbol consumed
        self.nexttok = None         # Next symbol tokenized
        self._advance()             # Load first lookahead token
        return self.expr()

    def _advance(self):
        'Advance one token ahead'
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

    def _accept(self,toktype):
        'Test and consume the next token if it matches toktype'
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False

    def _expect(self,toktype):
        'Consume next token if it matches toktype or raise SyntaxError'
        if not self._accept(toktype):
            raise SyntaxError('Expected ' + toktype)

    # Grammar rules follow

    def expr(self):
        "expression ::= term { ('+'|'-') term }*"

        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval += right
            elif op == 'MINUS':
                exprval -= right
        return exprval

    def term(self):
        "term ::= factor { ('*'|'/') factor }*"

        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval *= right
            elif op == 'DIVIDE':
                termval /= right
        return termval

    def factor(self):
        "factor ::= NUM | ( expr )"

        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUMBER or LPAREN')
```

Here is an example of using the ExpressionEvaluator class interactively:

```
>>> e = ExpressionEvaluator()
>>> e.parse('2')
2
>>> e.parse('2 + 3')
5
>>> e.parse('2 + 3 * 4')
14
>>> e.parse('2 + (3 + 4) * 5')
37
>>> e.parse('2 + (3 + * 4)')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "exprparse.py", line 40, in parse
return self.expr()
File "exprparse.py", line 67, in expr
right = self.term()
File "exprparse.py", line 77, in term
termval = self.factor()
File "exprparse.py", line 93, in factor
exprval = self.expr()
File "exprparse.py", line 67, in expr
right = self.term()
File "exprparse.py", line 77, in term
termval = self.factor()
File "exprparse.py", line 97, in factor
raise SyntaxError("Expected NUMBER or LPAREN")
SyntaxError: Expected NUMBER or LPAREN
>>>
```

If you want to do something other than pure evaluation, you need to change the
ExpressionEvaluator class to do something else. For example, here is an
alternative implementation that constructs a simple parse tree:

```
class ExpressionTreeBuilder(ExpressionEvaluator):
def expr(self):
"expression ::= term { ('+'|'-') term }"

        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval = ('+', exprval, right)
            elif op == 'MINUS':
                exprval = ('-', exprval, right)
        return exprval

    def term(self):
        "term ::= factor { ('*'|'/') factor }"

        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval = ('*', termval, right)
            elif op == 'DIVIDE':
                termval = ('/', termval, right)
        return termval

    def factor(self):
        'factor ::= NUM | ( expr )'

        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUMBER or LPAREN')
The following example shows how it works:

>>> e = ExpressionTreeBuilder()
>>> e.parse('2 + 3')
('+', 2, 3)
>>> e.parse('2 + 3 * 4')
('+', 2, ('*', 3, 4))
>>> e.parse('2 + (3 + 4) * 5')
('+', 2, ('*', ('+', 3, 4), 5))
>>> e.parse('2 + 3 + 4')
('+', ('+', 2, 3), 4)
>>>
```

### Discussion

Parsing is a huge topic that generally occupies students for the first three
weeks of a compilers course. If you are seeking background knowledge about
grammars, parsing algorithms, and other information, a compilers book is where
you should turn. Needless to say, all of that can’t be repeated here.

Nevertheless, the overall idea of writing a recursive descent parser is
generally simple. To start, you take every grammar rule and you turn it into a
function or method. Thus, if your grammar looks like this:

```
    expr ::= term { ('+'|'-') term }*

    term ::= factor { ('*'|'/') factor }*

    factor ::= '(' expr ')'
           |   NUM
```

You start by turning it into a set of methods like this:

```
class ExpressionEvaluator:
...
def expr(self):
...

    def term(self):
        ...

    def factor(self):
        ...
```

The task of each method is simple—it must walk from left to right over each part
of the grammar rule, consuming tokens in the process. In a sense, the goal of
the method is to either consume the rule or generate a syntax error if it gets
stuck. To do this, the following implementation techniques are applied:

If the next symbol in the rule is the name of another grammar rule (e.g., term
or factor), you simply call the method with the same name. This is the “descent”
part of the algorithm—control descends into another grammar rule. Sometimes
rules will involve calls to methods that are already executing (e.g., the call
to expr in the factor ::= '(' expr ')' rule). This is the “recursive” part of
the algorithm. If the next symbol in the rule has to be a specific symbol (
e.g., (), you look at the next token and check for an exact match. If it doesn’t
match, it’s a syntax error. The _expect() method in this recipe is used to
perform these steps. If the next symbol in the rule could be a few possible
choices (e.g., + or -), you have to check the next token for each possibility
and advance only if a match is made. This is the purpose of the _accept() method
in this recipe. It’s kind of like a weaker version of the _expect() method in
that it will advance if a match is made, but if not, it simply backs off without
raising an error (thus allowing further checks to be made). For grammar rules
where there are repeated parts (e.g., such as in the rule expr ::= term { ('+'|'
-') term }*), the repetition gets implemented by a while loop. The body of the
loop will generally collect or process all of the repeated items until no more
are found. Once an entire grammar rule has been consumed, each method returns
some kind of result back to the caller. This is how values propagate during
parsing. For example, in the expression evaluator, return values will represent
partial results of the expression being parsed. Eventually they all get combined
together in the topmost grammar rule method that executes. Although a simple
example has been shown, recursive descent parsers can be used to implement
rather complicated parsers. For example, Python code itself is interpreted by a
recursive descent parser. If you’re so inclined, you can look at the underlying
grammar by inspecting the file Grammar/Grammar in the Python source. That said,
there are still numerous pitfalls and limitations with making a parser by hand.

One such limitation of recursive descent parsers is that they can’t be written
for grammar rules involving any kind of left recursion. For example, suppose you
need to translate a rule like this:

```
    items ::= items ',' item
           |  item
```

To do it, you might try to use the items() method like this:

```
def items(self):
itemsval = self.items()
if itemsval and self._accept(','):
itemsval.append(self.item())
else:
itemsval = [ self.item() ]
```

The only problem is that it doesn’t work. In fact, it blows up with an infinite
recursion error.

You can also run into tricky issues concerning the grammar rules themselves. For
example, you might have wondered whether or not expressions could have been
described by this more simple grammar:

```
    expr ::= factor { ('+'|'-'|'*'|'/') factor }*

    factor ::= '(' expression ')'
           |   NUM
```

This grammar technically “works,” but it doesn’t observe the standard arithmetic
rules concerning order of evaluation. For example, the expression “3 + 4 * 5”
would get evaluated as “35” instead of the expected result of “23.” The use of
separate “expr” and “term” rules is there to make evaluation work correctly.

For really complicated grammars, you are often better off using parsing tools
such as PyParsing or PLY. This is what the expression evaluator code looks like
using PLY:

```
from ply.lex import lex
from ply.yacc import yacc

# Token list
tokens = [ 'NUM', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN' ]

# Ignored characters

t_ignore = ' \t\n'

# Token specifications (as regexs)
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Token processing functions
def t_NUM(t):
r'\d+'
t.value = int(t.value)
return t

# Error handler
def t_error(t):
print('Bad character: {!r}'.format(t.value[0]))
t.skip(1)

# Build the lexer
lexer = lex()

# Grammar rules and handler functions
def p_expr(p):
'''
expr : expr PLUS term
| expr MINUS term
'''
if p[2] == '+':
p[0] = p[1] + p[3]
elif p[2] == '-':
p[0] = p[1] - p[3]

def p_expr_term(p):
'''
expr : term
'''
p[0] = p[1]

def p_term(p):
'''
term : term TIMES factor
| term DIVIDE factor
'''
if p[2] == '*':
p[0] = p[1] * p[3]
elif p[2] == '/':
p[0] = p[1] / p[3]

def p_term_factor(p):
'''
term : factor
'''
p[0] = p[1]

def p_factor(p):
'''
factor : NUM
'''
p[0] = p[1]

def p_factor_group(p):
'''
factor : LPAREN expr RPAREN
'''
p[0] = p[2]

def p_error(p):
print('Syntax error')

parser = yacc()
```

In this code, you’ll find that everything is specified at a much higher level.
You simply write regular expressions for the tokens and high-level handling
functions that execute when various grammar rules are matched. The actual
mechanics of running the parser, accepting tokens, and so forth is implemented
entirely by the library.

Here is an example of how the resulting parser object gets used:

```
>>> parser.parse('2')
2
>>> parser.parse('2+3')
5
>>> parser.parse('2+(3+4)*5')
37
>>>
```

If you need a bit more excitement in your programming, writing parsers and
compilers can be a fun project. Again, a compilers textbook will have a lot of
low-level details underlying theory. However, many fine resources can also be
found online. Python’s own ast module is also worth a look.

## 2.20. Performing Text Operations on Byte Strings

### Problem

You want to perform common text operations (e.g., stripping, searching, and
replacement) on byte strings.

### Solution

Byte strings already support most of the same built-in operations as text
strings. For example:

```
>>> data = b'Hello World'
>>> data[0:5]
b'Hello'
>>> data.startswith(b'Hello')
True
>>> data.split()
[b'Hello', b'World']
>>> data.replace(b'Hello', b'Hello Cruel')
b'Hello Cruel World'
>>>
```

Such operations also work with byte arrays. For example:

```
>>> data = bytearray(b'Hello World')
>>> data[0:5]
bytearray(b'Hello')
>>> data.startswith(b'Hello')
True
>>> data.split()
[bytearray(b'Hello'), bytearray(b'World')]
>>> data.replace(b'Hello', b'Hello Cruel')
bytearray(b'Hello Cruel World')
>>>
```

You can apply regular expression pattern matching to byte strings, but the
patterns themselves need to be specified as bytes. For example:

```
>>>
>>> data = b'FOO:BAR,SPAM'
>>> import re
>>> re.split('[:,]',data)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "/usr/local/lib/python3.3/re.py", line 191, in split
return _compile(pattern, flags).split(string, maxsplit)
TypeError: can't use a string pattern on a bytes-like object

>>> re.split(b'[:,]',data)     # Notice: pattern as bytes
[b'FOO', b'BAR', b'SPAM']
>>>
```

### Discussion

For the most part, almost all of the operations available on text strings will
work on byte strings. However, there are a few notable differences to be aware
of. First, indexing of byte strings produces integers, not individual
characters. For example:

```

>>> a = 'Hello World'     # Text string
>>> a[0]
'H'
>>> a[1]
'e'
>>> b = b'Hello World'    # Byte string
>>> b[0]
72
>>> b[1]
101
>>>
```

This difference in semantics can affect programs that try to process
byte-oriented data on a character-by-character basis.

Second, byte strings don’t provide a nice string representation and don’t print
cleanly unless first decoded into a text string. For example:

```
>>> s = b'Hello World'
>>> print(s)
b'Hello World'               # Observe b'...'
>>> print(s.decode('ascii'))
Hello World
>>>
```

Similarly, there are no string formatting operations available to byte strings.

```
>>> b'%10s %10d %10.2f' % (b'ACME', 100, 490.1)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for %: 'bytes' and 'tuple'

>>> b'{} {} {}'.format(b'ACME', 100, 490.1)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'bytes' object has no attribute 'format'
>>>
```

If you want to do any kind of formatting applied to byte strings, it should be
done using normal text strings and encoding. For example:

```
>>> '{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii')
b'ACME              100     490.10'
>>>
```

Finally, you need to be aware that using a byte string can change the semantics
of certain operations—especially those related to the filesystem. For example,
if you supply a filename encoded as bytes instead of a text string, it usually
disables filename encoding/decoding. For example:

```
>>> # Write a UTF-8 filename
>>> with open('jalape\xf1o.txt', 'w') as f:
...     f.write('spicy')
...

>>> # Get a directory listing
>>> import os
>>> os.listdir('.')          # Text string (names are decoded)
['jalapeño.txt']

>>> os.listdir(b'.')         # Byte string (names left as bytes)
[b'jalapen\xcc\x83o.txt']
>>>
```

Notice in the last part of this example how giving a byte string as the
directory name caused the resulting filenames to be returned as undecoded bytes.
The filename shown in the directory listing contains raw UTF-8 encoding. See
Recipe 5.15 for some related issues concerning filenames.

As a final comment, some programmers might be inclined to use byte strings as an
alternative to text strings due to a possible performance improvement. Although
it’s true that manipulating bytes tends to be slightly more efficient than
text (due to the inherent overhead related to Unicode), doing so usually leads
to very messy and nonidiomatic code. You’ll often find that byte strings don’t
play well with a lot of other parts of Python, and that you end up having to
perform all sorts of manual encoding/decoding operations yourself to get things
to work right. Frankly, if you’re working with text, use normal text strings in
your program, not byte strings.
