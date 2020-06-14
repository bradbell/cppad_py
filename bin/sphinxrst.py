#! /usr/bin/env python3
# vim: set expandtab:
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{begin_sphinxrst sphinxrst_py}
{spell_sphinxrst
    sphinxrst
    rst
    underbar
    conf
}

.. |space| unicode:: 0xA0

Extract Sphinx RST From Source Code
###################################

Syntax
======
``sphinxrst.py`` *sphinx_dir* *file_list* *spell_list*

.. _sphinxrst_py_sphinx_dir:

sphinx_dir
==========
The command line argument *sphinx_dir* is a sub-directory,
of the top git repository directory.
The  sphinx ``conf.py`` and ``index.rst`` files are located in this directory.
Any files that have names ending in ``.rst`` and that are
in the directory *sphinx_dir*:code:`/sphinxrst`,
are removed at the beginning of execution of ``sphinxrst.py``.
All the ``.rst`` files in *sphinx_dir*:code:`/sphinxrst`
were extracted from the source code the last time that ``sphinxrst.py``
was executed.

file_list
=========
The command line argument *file_list* is the name of a file
in the *sphinx_dir* directory containing a list of file names.
These file names are one per line and relative to the
top git repository directory.
A line that begins with :code:`#` is a comment (not included in the list).
Leading and trailing white space in a file name are ignored.
The sphinxrst files will be extracted from the files in this list
and placed in the *sphinx_dir*:code`/sphinxrst` directory.

.. _sphinxrst_py_spell_list:

spell_list
==========
The command line argument *spell_list* is the name of a file
in the *sphinx_dir* directory containing a list of words
that the spell checker will consider correct for all sections.
A line that begins with :code:`#` is a comment (not included in the list).
The words are one per line and
leading and trailing white space in a word are ignored.
Special words, for a particular section, are specified using the
:ref:`spell command<sphinxrst_py_spell_command>`.

.. _sphinxrst_py_start_section:

Begin Section
=============
The start of a sphinxrst section of the input file is indicated by the
following command at the start of a line
(not counting spaces used to indent the command):

|space| |space| |space| |space|
``{begin_sphinxrst`` *section_name*:code:`}`

Here *section_name* is the name of output file corresponding to this section.
The possible characters in *section_name* are A-Z, a-z, 0-9, underbar ``_``,
and dot ``.``

End Section
===========
The end of a sphinxrst section of the input file is indicated by the following
command at the start of a line
(not counting spaces used to indent the command):

|space| |space| |space| |space|
``{end_sphinxrst`` *section_name*:code:`}`

Here *section_name* must be the same as in the corresponding
:ref:`start section<sphinxrst_py_start_section>` command.

index.rst
=========
The file ``index.rst`` must exist in the directory
:ref:`sphinx_dir<sphinxrst_py_sphinx_dir>`.
For each *section_name* in a
:ref:`start section<sphinxrst_py_start_section>` command,
there must be a line in ``index.rst`` with the following text:

|space| |space| |space| |space|
``sphinxrst/`` *section_name*:code:`.rst`

where there can be any number of spaces before the text above.


Suspend Extraction
==================
It is possible do suspend the sphinxrst extraction during a section.
One begins the suspension with the following command at the start of a line
(not counting spaces used to indent the command):

|space| |space| |space| |space|
``{suspend_sphinxrst}``

One resumes the output with the following command at the start of a line
(not counting spaces used to indent the command):

|space| |space| |space| |space|
``{resume_sphinxrst}``

Note that this will also suspend the sphinxrst processing; e.g., spell checking.
Each suspend sphinxrst must have a corresponding resume sphinxrst in same
section (between the corresponding begin sphinxrst and end sphinxrst commands).

.. _sphinxrst_py_spell_command:

Spell Command
=============
The list of words in
:ref:`spell_list<sphinxrst_py_spell_list>` are consider correct spellings
for all sections. You can specify a special list of words for the current
section using the following command at the start of a line
(not counting spaces used to indent the command):

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


Code Block
==========
A code block, directly below in the current input file, begins with
a line containing the following command:

|space| |space| |space| |space|
``{code_sphinxrst`` *language*:code:`}`

Here *language* is sequence of letters; e.g., ``python``,
that specify the language used to highlight the code block.
Each code block must end with
a line containing the following command:

|space| |space| |space| |space|
``{code_sphinxrst}``

The back quote character \` can't be in the same line as either
of the commands above.
Other characters on the same line as the two command above
are not included in the sphinxrst output.
This enables one to begin or end a comment block
without having the comment characters in the sphinxrst output.

File Block
==========
A file code block, from any file, is included by the following command
at the start of a line
(not counting spaces used to indent the command):

|space| |space| |space| |space|
``{file_sphinxrst%`` *file_name* :code:`%` *start* :code:`%` *stop*:code:`%}`

The back quote character \` can't be in the same lines as the command above.
Leading and trailing white space is not included in
*file_name*, *start*, or *end*.
This enables on to put the command on multiple input lines.

Notation
--------
We say that a string *text* is a the beginning of a line if
only space characters come before *text* in the line.


file_name
---------
If *file_name* is empty, the current input file is used.
Otherwise *file_name* is relative to the directory where ``sphinxrst.py``
is executed; i.e., the top directory for this git repository.

start
-----
The code block starts with the occurence
of the text *start* at the beginning of a line in *file_name*.
There can only be one occurence of *start* at the beginning
of a line in *file_name*.

stop
----
The code block ends with the first occurence
of the text *stop* at the beginning of a line and after the *start*.
The lines containing *start* and *stop* in *file_name* are not included in
the code block.

Indentation
===========
If all of the extracted sphinxrst documentation for a section is indented
by the same number of space characters, those space characters
are not included in the sphinxrst output. This enables one to indent the
sphinxrst so it is grouped with the proper code block in the source.

Python Style Guide
==================
Use triple double quotes instead of triple single quotes at beginning
and end of comments so it is easier to distinguish from back quotes.

Wish List
=========
The following is a wish list for future improvements to ``sphinxrst.py``:

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

{end_sphinxrst sphinxrst_py}
"""
# ----------------------------------------------------------------------------
import sys
import re
import os
import pdb
import spellchecker
# ---------------------------------------------------------------------------
def init_spell_checker(spell_list) :
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
    #
    return spell_checker
# ---------------------------------------------------------------------------
# search for raw text at start of line (ignoring white space)
def find_at_start_of_line(offset, data, text) :
    index = offset
    while index < len(data) :
        index = data.find(text, index)
        if index <= 0 :
            return index
        j = index - 1
        while j >= 0 and data[j] == ' ' :
            --j
        if j < 0 :
            return index
        if data[j] == '\n' :
            return index
        index = index + 1
# ---------------------------------------------------------------------------
# add file name, section name, and program name to system exit call
def sys_exit(msg, file_in=None, section_name=None) :
    if file_in != None :
        msg += '\nfile = ' + file_in
        if section_name != None :
            msg += ', section = ' + section_name
    sys.exit( 'bin/sphinxrst.py sphinx_dir file_list spell_list\n' + msg )
# ---------------------------------------------------------------------------
def file2list(file_name) :
    file_ptr  = open(file_name, 'r')
    result    = list()
    for line in file_ptr :
        if not line.startswith('#') :
            line = line.strip()
            if not line == '' :
                result.append(line)
    file_ptr.close()
    return result
# =============================================================================
# main program
# =============================================================================
# check working directory
if not os.path.isdir('.git') :
    msg = 'must be executed from to top directory for this git repository\n'
    sys_exit(msg)
#
# check number of comamnd line arguments
if len(sys.argv) != 4 :
    sys_exit('expected three command line argument')
#
# sphinx_dir
sphinx_dir      = sys.argv[1]
if not os.path.isdir(sphinx_dir) :
    msg  = 'sphinx_dir = ' + sphinx_dir + '\n'
    msg += 'is not a sub-directory of current working directory'
    sys_exit(msg)
#
# file_list
file_path = sphinx_dir + '/' + sys.argv[2]
if not os.path.isfile(file_path) :
    msg  = 'sphinx_dir/file_list = ' + sphinx_dir + '/' + sys.argv[2] + '\n'
    msg += 'is not a file'
    sys_exit(msg)
file_list  = file2list(file_path)
#
# spell_list
file_path = sphinx_dir + '/' + sys.argv[3]
if not os.path.isfile(file_path) :
    msg  = 'sphinx_dir/spell_list = ' + sphinx_dir + '/' + sys.argv[3] + '\n'
    msg += 'is not a file'
    sys_exit(msg)
spell_list  = file2list(file_path)
#
# check for conf.y, index.rst
for file_name in ['conf.py', 'index.rst'] :
    file_path = sphinx_dir + '/' + file_name
    if not os.path.isfile( file_path ) :
        msg  = 'can not find the file ' + file_name + '\n'
        msg += 'in sphinx_dir = ' + sphinx_dir
        sys_exit(msg)
#
# remove all *.rst files from output directory so only new ones remain aftet
# this program finishes
output_dir = sphinx_dir + '/sphinxrst'
if os.path.isdir(output_dir) :
    for file_name in os.listdir(output_dir) :
        if file_name.endswith('.rst') :
            file_path = output_dir + "/" + file_name
            os.remove(file_path)
else :
    os.mkdir(output_dir)
#
# spell_checker
spell_checker = init_spell_checker(spell_list)
#
# initialize list of section names and corresponding file names
section_list       = list()
corresponding_file = list()
#
# define some pytyon regular expression patterns
pattern_newline           = re.compile( r'\n')
pattern_word              = re.compile( r'[\\A-Za-z][a-z]*' )
pattern_suspend_sphinxrst = re.compile( r'\n *\{suspend_sphinxrst\}' )
pattern_resume_sphinxrst  = re.compile( r'\n *\{resume_sphinxrst\}' )
pattern_begin_sphinxrst   = re.compile( r'\n *\{begin_sphinxrst\s+(\w*)\}' )
pattern_end_sphinxrst     = re.compile( r'\n *\{end_sphinxrst\s+(\w*)\}' )
pattern_spell_sphinxrst   = re.compile( r'\n *\{spell_sphinxrst([^}]*)\}' )
pattern_file_sphinxrst    = re.compile(
    r'\n[^\n`]*\{file_sphinxrst%([^%]*)%([^%]*)%([^%]*)%[^\n`]*\}'
)
pattern_begin_code        = re.compile(
    r'\n[^\n`]*(\{code_sphinxrst\s+(\w*)\})[^\n`]*'
)
pattern_end_code          = re.compile(
    r'\n[^\n`]*(\{code_sphinxrst\})[^\n`]*'
)
# -----------------------------------------------------------------------------
# process each file in the list
for file_in in file_list :
    if not os.path.isfile(file_in) :
        msg  = 'can not file the file: ' + file_in + '\n'
        msg += 'which is located in sphinx_dir/file_list\n'
        msg += 'sphinx_dir = ' + sphinx_dir + '\n'
        msg += 'file_list  = ' + sys.argv[2] + '\n'
        sys_exit(msg)
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
            # remove characters on same line as {code_sphinxrst
            output_index  = 0
            match_begin_code = pattern_begin_code.search(output_data)
            while match_begin_code != None :
                if match_begin_code.group(2) == '' :
                    msg  = 'language missing directly after first'
                    msg += ' code_sphinxrst for a code block'
                    sys_exit(msg, file_in, section_name)
                begin_start = match_begin_code.start() + output_index
                begin_end   = match_begin_code.end()   + output_index
                output_rest = output_data[ begin_end : ]
                match_end_code   = pattern_end_code.search( output_rest )
                if match_end_code == None :
                    msg  = 'number of code_sphinxrst commands is not even'
                    sys_exit(msg, file_in, section_name)
                end_start = match_end_code.start() + begin_end
                end_end   = match_end_code.end()   + begin_end
                #
                data_left   = output_data[: begin_start + 1 ]
                data_left  += match_begin_code.group(1)
                data_left  += output_data[ begin_end : end_start + 1]
                data_left  += match_end_code.group(1)
                data_right  = output_data[ end_end : ]
                #
                output_data  = data_left + data_right
                output_index = len(data_left)
                match_begin_code  = pattern_begin_code.search(data_right)
            # ---------------------------------------------------------------
            # file command: convert start and stop to line numbers
            output_index     = 0
            match_file = pattern_file_sphinxrst.search(output_data)
            while match_file != None :
                #
                # file_name
                file_name = match_file.group(1).strip()
                if file_name == '' :
                    file_name = file_in
                #
                # start
                start     = match_file.group(2).strip()
                if start == '' :
                    msg = 'file_sphinxrst command: start text is empty'
                    sys_exit(msg, file_in, section_name)
                #
                # stop
                stop      = match_file.group(3) .strip()
                if stop == '' :
                    msg = 'file_sphinxrst command: stop text is empty'
                    sys_exit(msg, file_in, section_name)
                #
                # data
                file_ptr  = open(file_name, 'r')
                data      = file_ptr.read()
                file_ptr.close()
                #
                # start_index
                offset      = 0
                start_index = find_at_start_of_line(offset, data ,start)
                if start_index < 0 :
                    msg  = 'file_sphinxrst command: can not find start = '
                    msg += '"' + start + '"'
                    msg += '\nin file_name = "' + file_name + '"'
                    sys_exit(msg, file_in, section_name)
                offset     = start_index + len(start)
                if 0 <= find_at_start_of_line(offset, data, start) :
                    msg  = 'file_sphinxrst command: found more than one '
                    msg += 'start = "' + start + '"'
                    msg += '\nin file_name = "' + file_name + '"'
                    sys_exit(msg, file_in, section_name)
                #
                # stop_index
                stop_index = find_at_start_of_line(offset, data, stop)
                if stop_index < 0 :
                    msg  = 'file_sphinxrst command: can not find'
                    msg += '\nstop = "' + stop + '"'
                    msg += ' after start = "' + start + '"'
                    msg += '\nin file_name = "' + file_name + '"'
                    sys_exit(msg, file_in, section_name)
                #
                # start_line
                start_line = data[: start_index].count('\n') + 2
                #
                # stop_line
                stop_line = data[: stop_index].count('\n')
                #
                # beginning of lines with command in it
                begin_line = match_file.start() + output_index;
                #
                # end of lines with command in it
                end_line = match_file.end() + output_index;
                #
                # converted version of the command
                cmd  = f'file_sphinxrst%{file_name}%{start_line}%{stop_line}%'
                cmd  = '\n{' + cmd  + '}'
                #
                data_left  = output_data[: begin_line]
                data_left += cmd
                data_right = output_data[ end_line : ]
                #
                output_data  = data_left + data_right
                output_index = len(data_left)
                match_file  = pattern_begin_code.search(data_right)
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
                    cmd  = output_data[next_:].startswith('{code_sphinxrst')
                    cmd += output_data[next_:].startswith('{file_sphinxrst')
                    if ch != '\n' and ch != ' ' and not cmd :
                        num_remove = min(num_remove, next_ - start - 1)
            # ---------------------------------------------------------------
            # write file for this section
            file_out          = output_dir + '/' + section_name + '.rst'
            file_ptr          = open(file_out, 'w')
            start_line        = 0
            first_spell_error = True # for this section
            inside_code       = False
            for newline in newline_list :
                code_command = \
                    output_data[start_line:].startswith('{code_sphinxrst')
                file_command = \
                    output_data[start_line:].startswith('{file_sphinxrst')
                if code_command :
                    # --------------------------------------------------------
                    # code command
                    inside_code = not inside_code
                    if inside_code :
                        end_cmd = start_line + \
                            output_data[start_line:].find('}')
                        language = output_data[start_line + 16 : end_cmd]
                        line     = '.. code-block:: ' + language + '\n\n'
                        file_ptr.write(line)
                    else :
                        file_ptr.write('\n')
                elif file_command :
                        line       = output_data[start_line : newline + 1]
                        line       = line.split('%')
                        file_name  = line[1]
                        start_line = line[2]
                        stop_line  = line[3]
                        #
                        file_ptr.write('\n')
                        line = f'.. literalinclude:: ../../{file_name}\n'
                        file_ptr.write(line)
                        line = f'    :lines: {start_line}-{stop_line}\n'
                        file_ptr.write(line)
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
                    if inside_code :
                        # indent code block
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
file_in   = sphinx_dir + '/index.rst'
file_ptr  = open(file_in, 'r')
file_data = file_ptr.read()
file_ptr.close()
#
for section_name in section_list :
    # There should be an line in index.rst with the following contents:
    #     sphinxrst/section_name.rst'
    # where the spaces are optional
    pattern  = r'\n[ \t]*sphinxrst/'
    pattern += section_name.replace('.', '[.]')
    #
    match_line = re.search(pattern, file_data)
    if match_line == None :
        msg   = 'Can not find following line in ' + file_in + ':\n'
        msg  += '    sphinxrst/' + section_name + '\n'
        msg  += 'Spaces before the text above are optional.'
        sys_exit(msg)
#
print('sphinxrst.py: OK')
sys.exit(0)
