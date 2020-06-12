#! /usr/bin/env python3
# vim: set expandtab:
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
# The extracted files are written to this sub-directory:
extract_dir = 'extract_rst'
#
# List of files that contain sphinxrst sections in them:
extract_list = [
    'extract_rst.py',
    'code_block.py',
]
#
# List of words that the spell checker will consider correct for all sections:
spell_list = [
    'covariates',
    'covariate',
    'dict',
    'dtype',
    'initialized',
    'initialize',
    'numpy',
    'py',
    'scipy',

    r'\begin',
    r'\cdot',
    r'\circ',
    r'\ell',
    r'\end',
    r'\exp',
    r'\frac',
    r'\int',
    r'\ldots',
    r'\log',
    r'\left',
    r'\mbox',
    r'\partial',
    r'\right',
    r'\sqrt',
    r'\sum',
]
# ----------------------------------------------------------------------------
'''
{begin_sphinxrst extract_rst_py}
{spell_sphinxrst
    sphinxrst
    rst
    underbar
}

.. |space| unicode:: 0xA0

Extract Sphinx RST From Source Code
###################################

Syntax
======
``extract_rst.py``

.. _extract_rst_py_extract_dir:

extract_dir
===========
The variable *extract_dir* at the top of ``extract_rst.py`` is a sub-directory
relative to the directory where ``extract_rst.py`` is executed..
Any files in this sub-directory, with names that end in ``.rst``,
are removed at the beginning of execution.
Thus all the files in this directory with names that end in ``.rst``,
were extracted from the source code the last time that ``extract_rst``
was executed.

extract_list
============
The variable *extract_list* at top of ``extract_rst.py``
is a list of file names that the sphinxrst files will be extracted from.
These names are relative to the directory where ``extract_rst.py``
is executed.

.. _extract_rst_py_spell_list:

spell_list
==========
The variable *spell_list* is a list of words that
the spell checker will consider correct for all sections.
Special words, for a particular section, are specified using the
:ref:`spell command<extract_rst_py_spell_command>`.

.. _extract_rst_py_start_section:

Start Section
=============
The start of a sphinxrst section of the input file is indicated by the
following text at the start of a line
(not counting spaces used to indent the text):

|space| |space| |space| |space|
``{begin_sphinxrst`` *section_name*:code:`}`

Here *section_name* is the name of output file corresponding to this section.
The possible characters in *section_name* are A-Z, a-z, 0-9, underbar ``_``,
and dot ``.``

End Section
===========
The end of a sphinxrst section of the input file is indicated by the following
text at the start of a line
(not counting spaces used to indent the text):

|space| |space| |space| |space|
``{end_sphinxrst`` *section_name*:code:`}`

Here *section_name* must be the same as in the corresponding
:ref:`start section<extract_rst_py_start_section>` command.

index.rst
=========
For each *section_name* in a
:ref:`start section<extract_rst_py_start_section>` command,
there must be a line in the ``index.rst`` with the following contents:

|space| |space| |space| |space|
:ref:`extract_dir<extract_rst_py_extract_dir>`/*section_name*.rst

where there can be any number of spaces before the text above.


Suspend Extraction
==================
It is possible do suspend the sphinxrst extraction during a section.
One begins the suspension with the following text at the start of a line
(not counting spaces used to indent the text):

|space| |space| |space| |space|
``{suspend_sphinxrst}``

One resumes the output with the following text at the start of a line
(not counting spaces used to indent the text):

|space| |space| |space| |space|
``{resume_sphinxrst}``

Note that this will also suspend the sphinxrst processing; e.g., spell checking.
Each suspend sphinxrst must have a corresponding resume sphinxrst in same
section (between the corresponding begin sphinxrst and end sphinxrst commands).

.. _extract_rst_py_spell_command:

Spell Command
=============
The list of words in
:ref:`spell_list<extract_rst_py_spell_list>` are consider correct spellings
for all sections. You can specify a special list of words for the current
section using the folowing text at the start of a line
(not counting spaces used to indent the text):

|space| |space| |space| |space|
``{spell_sphinxrst`` *word_1* ...  *word_n*:code:`}`

Here *word_1*, ..., *word_n* is the special list of words for this section.
In the syntax above the list of words is all in one line,
but they could be on different lines.
Each word starts with an upper case letter,
a lower case letter, or a back slash.
The rest of the characters in a word are lower case letters.
The case of the first letter does not matter when checking spelling;
e.g., if ``abcd`` is *word_1* then ``Abcd`` will be considered a valid word.
The back slash is included as a possible beginning of a word
so that latex commands can be included in the spelling list.
The latex commands corresponding to the letters in the greek alphabet
are automatically included in the spelling list.


Code Blocks
===========
A code block within a sphinxrst section begins and ends with three back quotes.

1. Thus there must be an even number of occurrences of three back quotes.
2. The first three back quotes, for each code block, must have a language name
   directly after it.  The language name must be a sequence of letters; e.g.,
   ``python``.
3. The other characters on the same line as the three back quotes
   are not included in the sphinxrst output. This enables one to begin or end
   a comment block without having those characters in the sphinxrst output.

Indentation
===========
If all of the extracted sphinxrst documentation for a section is indented
by the same number of space characters, those space characters
are not included in the sphinxrst output. This enables one to indent the
sphinxrst so it is grouped with the proper code block in the source.

Python Style Guide
==================
Use triple double quotes instead of triple single quotes at beginning
and end of comments so it is easier to distinguish from triple back quotes.


Wish List
=========
The following is a wish list for future improvements to ``extract_rst.py``:

Testing
-------
Include an optional command line argument that indicates test mode
and runs the extractor through some test files and makes sure the result
is correct.

Error Messaging
---------------
Improve the error messaging so that it include the line number of the
input file that the error occurred on.

Source File
-----------
Include the path to the source code file that the documentation was
extracted from (probably at the end of the section).

Double Word Errors
------------------
Detect double word errors and allow for exceptions by specifying them in a
``double_word_sphinxrst`` command.

Moving Code Blocks
------------------
Have a way to include code blocks that are not directly below and in the same
file; e.g., one my automatically transfer the prototype for a function,
in the same file or a different file, to the documentation for a section.

Module
------
Convert the extract program into a python module and provide a pip distribution for it.

{end_sphinxrst extract_rst_py}'''
# ----------------------------------------------------------------------------
import sys
import re
import os
import pdb
import spellchecker
# ---------------------------------------------------------------------------
# spell_checker
bad_words_in_spellchecker = [
    'thier',
]
greek_alphabet_latex_command = [
    r'\alpha',
    r'\beta',
    r'\gamma',
    r'\delta',
    r'\epsilon',
    r'\zeta',
    r'\eta',
    r'\theta',
    r'\iota',
    r'\kappa',
    r'\lamda',
    r'\mu',
    r'\nu',
    r'\xi',
    r'\omicron',
    r'\pi',
    r'\rho',
    r'\sigma',
    r'\tau',
    r'\upsilon',
    r'\phi',
    r'\chi',
    r'\psi',
    r'\omega',
]
#
spell_checker = spellchecker.SpellChecker(distance=1)
spell_checker.word_frequency.remove_words(bad_words_in_spellchecker)
spell_checker.word_frequency.load_words(greek_alphabet_latex_command)
spell_checker.word_frequency.load_words(spell_list)
# ---------------------------------------------------------------------------
#
# add program name to system error call
def sys_exit(msg, file_in=None, section_name=None) :
    if file_in != None :
        msg += '\nfile = ' + file_in
        if section_name != None :
            msg += ', section = ' + section_name
    sys.exit( 'extract_rst.py:\n' + msg )
#
# check working directory
if not os.path.isdir('CVS') :
    msg = 'must be executed from CVS directory\n'
    sys_exit(msg)
#
# remove all *.rst files from output directory (so only new ones remain)
output_dir = extract_dir
if os.path.isdir(output_dir) :
    for file_name in os.listdir(output_dir) :
        if file_name.endswith('.rst') :
            file_path = output_dir + "/" + file_name
            os.remove(file_path)
else :
    os.mkdir(output_dir)
#
# initialize list of section names and corresponding file names
section_list       = list()
corresponding_file = list()
#
# define some pytyon regular expression patterns
pattern_suspend_sphinxrst = re.compile( r'\n *\{suspend_sphinxrst\}' )
pattern_resume_sphinxrst  = re.compile( r'\n *\{resume_sphinxrst\}' )
pattern_begin_sphinxrst   = re.compile( r'\n *\{begin_sphinxrst\s+(\w*)\}' )
pattern_end_sphinxrst     = re.compile( r'\n *\{end_sphinxrst\s+(\w*)\}' )
pattern_spell_sphinxrst   = re.compile( r'\n *\{spell_sphinxrst([^}]*)\}' )
pattern_begin_3quote      = re.compile( r'[^\n]*(```([a-zA-Z]*))[^\n]*' )
pattern_end_3quote        = re.compile( r'[^\n]*(```)[^\n]*' )
pattern_newline           = re.compile( r'\n')
pattern_word              = re.compile( r'[\\A-Za-z][a-z]*' )
# -----------------------------------------------------------------------------
# process each file in the list
for file_in in extract_list :
    #
    # file_data
    file_ptr   = open(file_in, 'r')
    file_data  = file_ptr.read()
    file_ptr.close()
    #
    # file_index is where to start search for next pattern in file_data
    file_index  = 0
    #
    while file_index < len(file_data) :
        #
        # match_begin_sphinxrst
        data_rest   = file_data[file_index : ]
        match_begin_sphinxrst = pattern_begin_sphinxrst.search(data_rest)
        #
        if match_begin_sphinxrst == None :
            if file_index == 0 :
                # Use @ so does not match pattern_begin_sphinxrst in this file.
                msg  = 'can not find followng at start of a line:\n'
                msg += '    {begin_sphinxrst section_name}\n'
                sys_exit(msg, file_in)
            file_index = len(file_data)
        else :
            # section_name
            section_name = match_begin_sphinxrst.group(1)
            if section_name == '' :
                msg  = 'section_name after begin_sphinxrst is empty'
                sys_exit(msg, file_in)
            #
            if section_name in section_list :
                # this section appears multiple times
                index = section_list.index(section_name)
                msg  = 'begin_sphinxrst ' + section_name
                msg += ' appears twice; see files\n' + file_in + ' and '
                msg += corresponding_file[index]
                sys_exit(msg)
            section_list.append( section_name )
            corresponding_file.append( file_in )
            #
            # file_index
            file_index += match_begin_sphinxrst.end()
            #
            # match_end_sphinxrst
            data_rest = file_data[file_index : ]
            match_end_sphinxrst = pattern_end_sphinxrst.search(data_rest)
            #
            if match_end_sphinxrst == None :
                msg  = 'can not find followig at start of a line:\n'
                msg += '    {end_sphinxrst section_name}'
                sys_exit(msg, file_in, section_name)
            if match_end_sphinxrst.group(1) != section_name :
                msg = 'in file ' + file_in + '\nsection names do not match\n'
                msg += 'begin_sphinxrst section name = '+section_name + '\n'
                msg += 'end_sphinxrst section name   = '
                msg += match_end_sphinxrst.group(1) + '\n'
                sys_exit(msg)
            #
            # output_data
            output_start = file_index
            output_end   = file_index + match_end_sphinxrst.start()
            output_data  = file_data[ output_start : output_end ]
            # ----------------------------------------------------------------
            # process suspend sphinxrst commands
            match_suspend = pattern_suspend_sphinxrst.search(output_data)
            while match_suspend != None :
                suspend_start = match_suspend.start()
                suspend_end   = match_suspend.end()
                output_rest   = output_data[ suspend_end : ]
                match_resume  = pattern_resume_sphinxrst.search(output_rest)
                match_suspend = pattern_suspend_sphinxrst.search(output_rest)
                if match_resume == None :
                    msg  = 'there is a {suspend_sphinxrst} without a '
                    msg += 'corresponding {resume_sphinxrst}'
                    sys_exit(msg, file_in, section_name)
                if match_suspend != None :
                    if match_suspend.start() < match_resume.start() :
                        pdb.set_trace()
                        msg  = 'there are two {suspend_sphinxrst} without a '
                        msg += '{resume_sphinxrst} between them'
                        sys_exit(msg, file_in, section_name)
                resume_end  = match_resume.end() + suspend_end
                output_rest = output_data[ resume_end :]
                output_data = output_data[: suspend_start] + output_rest
                # redo match_suppend so relative to new output_data
                match_suspend = pattern_suspend_sphinxrst.search(output_data)
            # ----------------------------------------------------------------
            # process spell command
            match_spell = pattern_spell_sphinxrst.search(output_data)
            special_list  = list()
            if match_spell != None :
                output_rest   = output_data[ match_spell.end() : ]
                match_another = pattern_spell_sphinxrst.search(output_rest)
                if match_another :
                    msg  = 'there are two spell sphinxrst commands'
                    sys_exit(msg, file_in, section_name)
                for itr in pattern_word.finditer( match_spell.group(1) ) :
                    special_list.append( itr.group(0).lower() )
                start       = match_spell.start()
                end         = match_spell.end()
                output_data = output_data[: start] + output_data[end :]
            # ----------------------------------------------------------------
            # remove characters on same line as triple back quote
            output_index  = 0
            match_begin_3quote = pattern_begin_3quote.search(output_data)
            while match_begin_3quote != None :
                if match_begin_3quote.group(2) == '' :
                    msg  = 'language missing directly after first'
                    msg += ' ``` for a code block'
                    sys_exit(msg, file_in, section_name)
                begin_start = match_begin_3quote.start() + output_index
                begin_end   = match_begin_3quote.end()   + output_index
                output_rest = output_data[ begin_end : ]
                match_end_3quote   = pattern_end_3quote.search( output_rest )
                if match_end_3quote == None :
                    msg  = 'number of triple backquotes is not even'
                    sys_exit(msg, file_in, section_name)
                end_start = match_end_3quote.start() + begin_end
                end_end   = match_end_3quote.end()   + begin_end
                #
                data_left   = output_data[: begin_start ]
                data_left  += match_begin_3quote.group(1)
                data_left  += output_data[ begin_end : end_start ]
                data_left  += match_end_3quote.group(1)
                data_right  = output_data[ end_end : ]
                #
                output_data  = data_left + data_right
                output_index = len(data_left)
                match_begin_3quote  = pattern_begin_3quote.search(data_right)
            # ---------------------------------------------------------------
            # num_remove (for indented documentation)
            len_output   = len(output_data)
            num_remove   = len(output_data)
            newline_itr  = pattern_newline.finditer(output_data)
            newline_list = list()
            for itr in newline_itr :
                start = itr.start()
                newline_list.append( start )
                next_ = start + 1
                if next_ < len_output and num_remove != 0 :
                    ch = output_data[next_]
                    while ch == ' ' and next_ + 1 < len_output :
                        next_ += 1
                        ch = output_data[next_]
                    if ch == '\t' :
                        msg  = 'tab in white space at begining of a line'
                        sys_exit(msg, file_in, section_name)
                    tripple_back_quote = output_data[next_:].startswith('```')
                    if ch != '\n' and ch != ' ' and not tripple_back_quote :
                        num_remove = min(num_remove, next_ - start - 1)
            # ---------------------------------------------------------------
            # write file for this section
            file_out          = output_dir + '/' + section_name + '.rst'
            file_ptr          = open(file_out, 'w')
            start_line        = 0
            first_spell_error = True # for this section
            inside_3quote     = False
            for newline in newline_list :
                tripple_back_quote = output_data[start_line:].startswith('```')
                if tripple_back_quote :
                    inside_3quote = not inside_3quote
                    if inside_3quote :
                        end_line = start_line + \
                            output_data[start_line:].find('\n')
                        language = output_data[start_line + 3 : end_line]
                        line     = '.. code-block:: ' + language + '\n\n'
                        file_ptr.write(line)
                    else :
                        file_ptr.write('\n')
                elif start_line + num_remove <= newline :
                    start_line += num_remove
                    line        = output_data[start_line : newline + 1]
                    # ------------------------------------------------------
                    # check spelling
                    word_list = list()
                    for itr in pattern_word.finditer( line ) :
                        word = itr.group(0)
                        if len( spell_checker.unknown( [word] ) ) > 0 :
                            if not word.lower() in special_list :
                                if first_spell_error :
                                    msg  = 'warning: file = ' + file_in
                                    msg += ', section = ' + section_name
                                    print(msg)
                                    first_spell_error = False
                                msg  = 'spelling = ' + word
                                suggest = spell_checker.correction(word)
                                if suggest != word :
                                    msg += ', suggest = ' + suggest
                                print(msg)
                                special_list.append(word.lower())
                    # ------------------------------------------------------
                    if inside_3quote :
                        line = '    ' + line
                    file_ptr.write( line )
                else :
                    file_ptr.write( "\n" )
                start_line = newline + 1
            file_ptr.close()
            #
            # file_index
            file_index += match_end_sphinxrst.end()
# -----------------------------------------------------------------------------
# read index.rst
file_in   = 'index.rst'
file_ptr  = open(file_in, 'r')
file_data = file_ptr.read()
file_ptr.close()
#
for section_name in section_list :
    # There should be an line in index.rst with the following contents:
    #     extract_rst/section_name.rst'
    # where the spaces are optional
    pattern  = r'\n[ \t]*extract_rst/'
    pattern += section_name.replace('.', '[.]')
    #
    match_line = re.search(pattern, file_data)
    if match_line == None :
        msg   = 'Can not find following line in ' + file_in + ':\n'
        msg  += '    extract_rst/' + section_name + '\n'
        msg  += 'Spaces before the text above are options.'
        sys_exit(msg)
#
print('extract.py: OK')
sys.exit(0)
