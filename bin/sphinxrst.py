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
    underbars
    conf
    toctree
}

.. |space| unicode:: 0xA0

###################################
Extract Sphinx RST From Source Code
###################################

Syntax
======
``sphinxrst.py`` *sphinx_dir* *file_list* *spell_list*

Notation
========

White Space
-----------
We define white space to be a sequence of space and tab characters.

Beginning of a Line
-------------------
We say that a string *text* is a the beginning of a line if
only white space, or nothing, comes before *text* in the line.

Command Line Arguments
======================

sphinx_dir
----------
The command line argument *sphinx_dir* is a sub-directory,
of the top git repository directory.
The  sphinx ``conf.py`` and ``index.rst`` files are located in this directory.
Any files that have names ending in ``.rst``,
and that are in the directory *sphinx_dir*:code:`/sphinxrst`,
are removed at the beginning of execution of ``sphinxrst.py``.
All the ``.rst`` files in *sphinx_dir*:code:`/sphinxrst`
were extracted from the source code the last time that ``sphinxrst.py``
was executed.

file_list
---------
The command line argument *file_list* is the name of a file
in the *sphinx_dir* directory containing a list of file names.
These file names are one per line and relative to the
top git repository directory.
A line that begins with :code:`#` is a comment (not included in the list).
Leading and trailing white space in a file name are ignored.
The sphinxrst files will be extracted from the files in this list
and placed in the *sphinx_dir*:code`/sphinxrst` directory.

spell_list
----------
The command line argument *spell_list* is the name of a file
in the *sphinx_dir* directory containing a list of words
that the spell checker will consider correct for all sections.
A line that begins with :code:`#` is a comment (not included in the list).
The words are one per line and
leading and trailing white space in a word are ignored.
Special words, for a particular section, are specified using the
:ref:`spell command<sphinxrst_py.spell.command>`.

Section
=======

Name
----
A *section_name* is a sequence of the following characters
a-z, 0-9, and underbar ``_``.
The corresponding sphinxrst output file is

|space| |space| |space| |space|
:ref:`sphinx_dir<sphinxrst_py.command_line_arguments.sphinx_dir>`
``/sphinxrst/`` *section_name* ``.rst``

Begin
-----
The start of a sphinxrst section of the input file is indicated by the
following command at the beginning of a line:

|space| |space| |space| |space|
``{begin_sphinxrst`` *section_name*:code:`}`

End
---
The end of a sphinxrst section of the input file is indicated by the following
command at the beginning of a line:

|space| |space| |space| |space|
``{end_sphinxrst`` *section_name*:code:`}`

Here *section_name* must be the same as in the corresponding
begin section command.

Table Of Contents
=================

Parent Section
--------------
A single input file may contain multiple sections.
The first section in a file is called the file's parent section.
Other sections in a file are children of the parent section.

index.rst
---------
The file ``index.rst`` must exist in the directory
:ref:`sphinx_dir<sphinxrst_py.command_line_arguments.sphinx_dir>`.
For each parent *section_name* in a
:ref:`begin section<sphinxrst_py.section.begin>` command,
there must be a line in ``index.rst`` with the following text:

|space| |space| |space| |space|
``sphinxrst/`` *section_name*:code:`.rst`

There can white space before the text above.

Suspend Extraction
==================
It is possible to suspend the sphinxrst extraction during a section.
One begins the suspension with the following command
at the beginning of a line:

|space| |space| |space| |space|
``{suspend_sphinxrst}``

Note that this will also suspend the sphinxrst processing; e.g., spell checking.
One resumes the output with the following command at the beginning of a line:

|space| |space| |space| |space|
``{resume_sphinxrst}``

Each suspend sphinxrst must have a corresponding resume sphinxrst in same
section (between the corresponding begin sphinxrst and end sphinxrst commands).

Example
-------
:ref:`suspend_py`

Spell
=====

spell_list
----------
The list of words in
:ref:`spell_list<sphinxrst_py.command_line_arguments.spell_list>`
are considered correct spellings
for all sections.
The latex commands corresponding to the letters in the greek alphabet
are automatically included in this list

Command
-------
You can specify a special list of words for the current
section using the following command at the beginning of a line:

|space| |space| |space| |space|
``{spell_sphinxrst`` *word_1* ...  *word_n*:code:`}`

Here *word_1*, ..., *word_n* is the special list of words for this section.
In the syntax above the list of words is all in one line,
but they could be on different lines.
Each word starts with an upper case letter,
a lower case letter, or a back slash.
The back slash is included as a possible beginning of a word
so that latex commands can be included in the spelling list.
The rest of the characters in a word are lower case letters.

Checking
--------
The case of the first letter does not matter when checking spelling;
e.g., if ``abcd`` is *word_1* then ``Abcd`` will be considered a valid word.

Double Word
-----------
It is considered an error to have only white space between two occurrences
of the same word.

Example
-------
:ref:`spell_exam`

Code Block
==========
A code block, directly below in the current input file, begins with
a line containing the following command:

|space| |space| |space| |space|
``{code_sphinxrst}``

Each code block must end with
a line containing the same command above.

The back quote character \` can't be in the same line as the two commands.
Other characters on the same line as the commands
are not included in the sphinxrst output.
This enables one to begin or end a comment block
without having the comment characters in the sphinxrst output.
The name of the current input file is used to determine the source code
language for highlighting the code block.
Code blocks as usually small and spell check is done inside of them.

Example
-------
:ref:`code_block_exam`

File Block
==========
A code block, from any file, is included by the following command
at the beginning of a line:

|space| |space| |space| |space|
``{file_sphinxrst%`` *file_name* :code:`%` *start* :code:`%` *stop*:code:`%}`

The back quote character \` can not be in the same lines as the command above.
Leading and trailing white space is not included in
*file_name*, *start*, or *end*.
This enables one to put the command on multiple input lines.
File blocks can be large and spell check is NOT done inside of them.

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
The code block ends with the occurence
of the text *stop* at the beginning of a line and after *start*.
There can only be one occurence of *stop* at the beginning of a line
and after *start* and it must come after *start*.
The lines containing *start* and *stop* in *file_name* are not included in
the code block.

Example
-------
:ref:`file_block_exam`

Headings and Links
==================

Section Level
-------------
Each :ref:`section<sphinxrst_py.section>` can have only one header at
the first level which is a title for the section.
The *section_name* is automatically used
as a label for linking the title for a section; i.e., the
following will link to the title for *section_name*:

|space| |space| |space| |space|
``:ref:`` \\`  *linking_text* :code:`<` *section_name* :code:`>` \\`

where *linking_text* is the text the user sees.

Other Levels
------------
The label for linking a heading that is not at the first level
is the label for the heading directly above it plus a dot character :code:`.`,
plus a lower case version of the heading with spaces converted to
underbars :code:`_`. For example, the label for the heading for this
paragraph is ``sphinxrst_py.headers_and_links.other_levels``.
This may seem verbose, but it helps keep the links up to date.
If a heading changes, all the links to that heading will break.
This identifies the links that should be checked
to make sure they are still valid.

Children
--------
If a :ref:`parent section<sphinxrst_py.table_of_contents.parent_section>`
has children, a ``toctree`` command that provides links to the children
is included at the end of the section.
You can place a heading at the end of section to make these
links easier to find.

Example
-------
:ref:`heading_exam`

Indentation
===========
If all of the extracted sphinxrst documentation for a section is indented
by the same white space characters, those characters
are not included in the sphinxrst output. This enables one to indent the
sphinxrst so it is grouped with the proper code block in the source.

Example
-------
:ref:`indent_space_exam`, :ref:`indent_tab_exam`

Python Style Guide
==================
Use triple double quotes instead of triple single quotes at beginning
and end of comments so it is easier to distinguish from back quotes.

Wish List
=========
The following is a wish list for future improvements to ``sphinxrst.py``:

Error Messaging
---------------
Improve the error messaging so that it include the line number of the
input file that the error occurred on.

Module
------
Convert the extract program into a python module and provide a pip distribution for it.

Indexing
--------
Add indexing so that there are search links to headings at all levels.

Contents
--------
Have a section specify its child sections.
Sections that are not in ``index.rst`` must be the child of one
and only one section.

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
# search for raw text at beginning of a line
def find_at_start_of_line(offset, data, text) :
    index = offset
    while index < len(data) :
        index = data.find(text, index)
        if index <= 0 :
            return index
        j = index - 1
        while j >= 0 and data[j] in ' \t' :
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
            line = line.strip(' \t\n')
            if not line == '' :
                result.append(line)
    file_ptr.close()
    return result
# ----------------------------------------------------------------------------
# find all the section names and corresponding data in the specified file
# The returned data does not include the begin and end section commands
def file2file_info(
        pattern_begin_sphinxrst,
        pattern_end_sphinxrst,
        section_list,
        correspnding_file,
        file_in
) :
    #
    # file_data
    file_ptr   = open(file_in, 'r')
    file_data  = file_ptr.read()
    file_ptr.close()
    #
    # Initialize return value
    file_info = list()
    #
    # index to start search for next pattern in file_data
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
            # check if section appears multiple times
            for info in file_info :
                if section_name == info['section_name'] :
                    msg  = 'begin_sphinxrst ' + section_name
                    msg += ' appears twice in file\n' + file_in
                    sys_exit(msg)
            if section_name in section_list :
                # this section appears multiple times
                index = section_list.index(section_name)
                msg  = 'begin_sphinxrst ' + section_name
                msg += ' appears twice; see files\n' + file_in + ' and '
                msg += corresponding_file[index]
                sys_exit(msg)
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
            # section_data
            section_start = file_index
            section_end   = file_index + match_end_sphinxrst.start()
            section_data  = file_data[ section_start : section_end ]
            #
            # file_info
            file_info.append( {
                'section_name' : section_name,
                'section_data' : section_data,
            } )
            #
            # place to start search for next section
            file_index += match_end_sphinxrst.end()
    return file_info
# ----------------------------------------------------------------------------
def start_line_white_space(data, file_in, section_name) :
    data_index  = 0
    white_space = None
    #
    # find first line with a space or tab as first character in the line
    while white_space == None :
        if data[data_index] in ' \t' :
            white_space = data[data_index]
        else :
            index = data[data_index :].find('\n')
            if index < 0 :
                return ' '
            data_index = data_index + index + 1
            if data_index >= len(data) :
                return ' '
    # check that white space at beginning of line is same for all lines
    while data_index < len(data) :
        while data[data_index] == white_space and data_index < len(data) :
            data_index += 1
        if data_index == len(data) :
            return white_space
        if data[data_index] in ' \t' :
            msg  = 'mixing both spaces and tabs for white space at '
            msg += 'beginning of lines.'
            sys_exit(msg, file_in, section_name)
        index = data[data_index :].find('\n')
        if index < 0 :
            return white_space
        data_index = data_index + index + 1
    return white_space
# ----------------------------------------------------------------------------
# process suspend_sphinxrst commands
def suspend_command(
    suspend_pattern, resume_pattern, section_data, file_in, section_name
) :
    match_suspend = suspend_pattern.search(section_data)
    while match_suspend != None :
        suspend_start = match_suspend.start()
        suspend_end   = match_suspend.end()
        section_rest  = section_data[ suspend_end : ]
        match_resume  = resume_pattern.search(section_rest)
        match_suspend = suspend_pattern.search(section_rest)
        if match_resume == None :
            msg  = 'there is a {suspend_sphinxrst} without a '
            msg += 'corresponding {resume_sphinxrst}'
            sys_exit(msg, file_in, section_name)
        if match_suspend != None :
            if match_suspend.start() < match_resume.start() :
                msg  = 'there are two {suspend_sphinxrst} without a '
                msg += '{resume_sphinxrst} between them'
                sys_exit(msg, file_in, section_name)
        resume_end   = match_resume.end() + suspend_end
        section_rest = section_data[ resume_end :]
        section_data = section_data[: suspend_start] + section_rest
        #
        # redo match_suppend so relative to new section_data
        match_suspend = suspend_pattern.search(section_data)
    return section_data
# -----------------------------------------------------------------------------
# process spell_sphinx commands
def spell_command(
    spell_pattern, section_data, file_in, section_name
) :
    word_pattern  = re.compile( r'[\\A-Za-z][a-z]*' )
    match_spell   = spell_pattern.search(section_data)
    special_list  = list()
    if match_spell != None :
        section_rest   = section_data[ match_spell.end() : ]
        match_another  = pattern_spell_sphinxrst.search(section_rest)
        if match_another :
            msg  = 'there are two spell sphinxrst commands'
            sys_exit(msg, file_in, section_name)
        for itr in word_pattern.finditer( match_spell.group(1) ) :
            special_list.append( itr.group(0).lower() )
        #
        # remove spell command
        start        = match_spell.start()
        end          = match_spell.end()
        section_data = section_data[: start] + section_data[end :]
    #
    # data = section_data with commands removed
    command_pattern = re.compile( r'\{[a-z]+_sphinxrst[^}]*\}' )
    data            = ''
    previous_end    = 0
    for itr in command_pattern.finditer( section_data ) :
        start        = itr.start()
        data        += section_data[previous_end : start ]
        previous_end = itr.end()
    data += section_data[previous_end :]
    #
    # check for spelling errors
    first_spell_error = True
    for itr in word_pattern.finditer( data ) :
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
    #
    # check for double word errors
    double_pattern  = re.compile( r'\s+([\\A-Za-z][a-z]*)\s+\1' )
    for itr in double_pattern.finditer(data) :
        ok   = False
        word = itr.group(1)
        if word in special_list :
            index = special_list.index(word)
            if index + 1 < len(special_list) :
                if special_list[index+1] == word :
                    ok = True
        if not ok :
            if first_spell_error :
                msg  = 'warning: file = ' + file_in
                msg += ', section = ' + section_name
                print(msg)
                first_spell_error = False
            double_word = itr.group(0).strip()
            msg         = 'double word error: "' + double_word + '"'
            print(msg)
    #
    return section_data
# -----------------------------------------------------------------------------
# remove characters on same line as {code_sphinxrst}
def isolate_code_command(code_pattern, section_data, file_in, section_name) :
    section_index  = 0
    match_begin_code = code_pattern.search(section_data)
    while match_begin_code != None :
        begin_start    = match_begin_code.start() + section_index
        begin_end      = match_begin_code.end()   + section_index
        section_rest   = section_data[ begin_end : ]
        match_end_code = code_pattern.search( section_rest )
        if match_end_code == None :
            msg  = 'number of code_sphinxrst commands is not even'
            sys_exit(msg, file_in, section_name)
        end_start = match_end_code.start() + begin_end
        end_end   = match_end_code.end()   + begin_end
        #
        data_left   = section_data[: begin_start + 1 ]
        data_left  += '{code_sphinxrst}'
        data_left  += section_data[ begin_end : end_start + 1]
        data_left  += '{code_sphinxrst}'
        data_right  = section_data[ end_end : ]
        #
        section_data  = data_left + data_right
        section_index = len(data_left)
        match_begin_code  = code_pattern.search(data_right)
    return section_data
# -----------------------------------------------------------------------------
# convert file command start and stop from patterns to line numbers
def convert_file_command(file_pattern, section_data, file_in, section_name) :
    section_index  = 0
    match_file    = file_pattern.search(section_data)
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
        offset     = stop_index + len(stop)
        if 0 <= find_at_start_of_line(offset, data, stop) :
            msg  = 'file_sphinxrst command: found more than one '
            msg += 'stop = "' + stop + '"'
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
        begin_line = match_file.start() + section_index;
        #
        # end of lines with command in it
        end_line = match_file.end() + section_index;
        #
        # converted version of the command
        cmd  = f'file_sphinxrst%{file_name}%{start_line}%{stop_line}%'
        cmd  = '\n{' + cmd  + '}'
        #
        data_left  = section_data[: begin_line]
        data_left += cmd
        data_right = section_data[ end_line : ]
        #
        section_data  = data_left + data_right
        section_index = len(data_left)
        match_file  = file_pattern.search(data_right)
    return section_data
# -----------------------------------------------------------------------------
# labels for headings
def add_labels_for_headings(
        section_data, num_remove, white_space, file_in, section_name
) :
    punctuation      = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
    indent           = num_remove * white_space
    heading_list     = list()
    next_start       = 0
    next_newline     = section_data.find('\n', next_start)
    candidate_start  = None
    candidate_state  = 'empty'
    while 0 <= next_newline :
        next_line = section_data[next_start : next_newline]
        next_line = next_line[num_remove :].rstrip(' \t')
        next_len  = len(next_line)
        if next_len == 0 :
            candidate_start = next_start
            candidate_state = 'before_overline'
        elif candidate_state == 'before_overline' :
            ch = next_line[0]
            if ch in punctuation and next_line == ch * next_len :
                candidate_state = 'before_heading'
                overline        = next_line
            else :
                candidate_state = 'before_underline'
                overline        = None
                heading_text    = next_line
        elif candidate_state == 'before_heading' :
            candidate_state = 'before_underline'
            heading_text    = next_line
        elif candidate_state == 'before_underline' :
            ch = next_line[0]
            if len(next_line) < len(heading_text) :
                candidate_state = 'empty'
            elif overline is not None and overline != next_line:
                candidate_state = 'empty'
            elif next_line[0] not in punctuation :
                candidate_state = 'empty'
            elif next_line != next_line[0] * next_len :
                candidate_state = 'empty'
            else :
                candidate_state = 'end'
                underline       = next_line
        if candidate_state == 'end' :
            # overline, character, and text for this heading
            character = underline[0]
            overline  =  overline is not None
            heading   = {
                'overline' : overline,
                'character': character,
                'text':      heading_text
            }
            #
            # check for first heading
            if len( heading_list ) == 0 :
                heading_list.append( heading )
            else :
                match = overline == heading_list[0]['overline']
                if match :
                    match = character == heading_list[0]['character']
                if match :
                    msg = 'There are multiple titles for this section'
                    sys_exit(msg, file_in, section_name)
                level = 1
                while level < len(heading_list) and not match :
                    match = overline == heading_list[level]['overline']
                    if match :
                        match = character == heading_list[level]['character']
                    if match :
                        heading_list = heading_list[: level ]
                        heading_list.append(heading)
                    else :
                        level += 1
                if not match :
                    # this heading at a deeper level
                    heading_list.append( heading )

            label = ''
            for level in range( len(heading_list) ) :
                if level == 0 :
                    label = section_name.lower().replace(' ', '_')
                else :
                    heading = heading_list[level]
                    label += '.' + heading['text'].lower().replace(' ', '_')
            #
            # place label in output before the heading
            data_left   = section_data[: candidate_start]
            data_left  += '\n{label_sphinxrst ' + label + ' }'
            data_left  += section_data[candidate_start : next_newline]
            data_right  = section_data[next_newline : ]
            section_data = data_left + data_right
            #
            # setup of for next heading
            candidate_state = 'empty'
            next_start      = len(data_left) + 1
            next_newline    = section_data.find('\n', next_start )
        else :
            next_start   = next_newline + 1
            next_newline = section_data.find('\n', next_start)
    #
    # children_heading_info
    if len(heading_list) == 0 :
        msg = 'There is no titles for this section'
        sys_exit(msg, file_in, section_name)
    #
    if len(heading_list) == 1 :
        if heading_list[0]['character'] != '=' :
            character = '='
        else :
            character = '-'
    else :
        overline  = heading_list[1]['overline']
        character = heading_list[1]['character']
    children_heading_info = { 'overline' : overline, 'character' : ch }
    #
    return section_data, children_heading_info
# -----------------------------------------------------------------------------
# write file corresponding to a section
# (and finish processing that has been delayed to this point)
def write_file(
    file_in,
    section_data,
    child_list,
    children_heading_info,
    output_dir,
    section_name,
    spell_checker,
) :
    #
    newline_pattern = re.compile( r'\n')
    newline_itr     = newline_pattern.finditer(section_data)
    newline_list    = list()
    for itr in newline_itr :
        newlist = itr.start()
        newline_list.append( newlist )
    file_out          = output_dir + '/' + section_name + '.rst'
    file_ptr          = open(file_out, 'w')
    startline         = 0
    inside_code       = False
    previous_empty    = True
    for newline in newline_list :
        line  = section_data[startline : newline + 1]
        # commands that delay some processing to this point
        code_command  = line.startswith('{code_sphinxrst')
        file_command  = line.startswith('{file_sphinxrst')
        label_command = line.startswith('{label_sphinxrst')
        if label_command :
            # --------------------------------------------------------
            # label command
            line  = line.split(' ')
            label = line[1]
            line  = '.. _' + label + ':\n\n'
            file_ptr.write(line)
            previous_empty = True
        elif code_command :
            # --------------------------------------------------------
            # code command
            inside_code = not inside_code
            if inside_code :
                index = file_in.rfind('.')
                if index < 0 :
                    extension = ''
                else :
                    extension = file_in[index + 1 : ]
                line     = '.. code-block:: ' + extension + '\n\n'
            else :
                line = '\n'
            file_ptr.write(line)
            previous_empty = True
        elif file_command :
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
            previous_empty = True
        elif newline <= startline + num_remove :
            if not previous_empty :
                file_ptr.write( "\n" )
                previous_empty = True
        else :
            line = line[num_remove : newline + 1]
            if inside_code :
                # indent code block
                if white_space == ' ' :
                    line = '    ' + line
                else :
                    line = '\t' + line
            previous_empty = line == '\n'
            file_ptr.write( line )
        startline = newline + 1
    # -----------------------------------------------------------------------
    if not previous_empty :
        file_ptr.write('\n')
    #
    if len(child_list) > 0 :
        file_ptr.write('.. toctree::\n')
        file_ptr.write('   :maxdepth: 1\n\n')
        for child in child_list :
            file_ptr.write('   ' + child + '\n')
        file_ptr.write('\n')
    #
    file_ptr.write( f'sphinxrst_input_file: ``{file_in}``\n')
    file_ptr.close()
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
pattern_code_sphinxrst    = re.compile( r'\n[^\n`]*\{code_sphinxrst\}[^\n`]*')
pattern_suspend_sphinxrst = re.compile( r'\n[ \t]*\{suspend_sphinxrst\}' )
pattern_resume_sphinxrst  = re.compile( r'\n[ \t]*\{resume_sphinxrst\}' )
pattern_begin_sphinxrst   = re.compile(
    r'\n[ \t]*\{begin_sphinxrst\s+([a-z0-9_]+)\}'
)
pattern_end_sphinxrst     = re.compile(
    r'\n[ \t]*\{end_sphinxrst\s+([a-z0-9_]+)\}'
)
pattern_spell_sphinxrst   = re.compile(
    r'\n[ \t]*\{spell_sphinxrst([^}]*)\}'
)
pattern_file_sphinxrst    = re.compile(
    r'\n[^\n`]*\{file_sphinxrst%([^%]*)%([^%]*)%([^%]*)%[^\n`]*\}'
)
# -----------------------------------------------------------------------------
# process each file in the list
for file_in in file_list :
    if not os.path.isfile(file_in) :
        msg  = 'can not find the file: ' + file_in + '\n'
        msg += 'which is located in sphinx_dir/file_list\n'
        msg += 'sphinx_dir = ' + sphinx_dir + '\n'
        msg += 'file_list  = ' + sys.argv[2] + '\n'
        sys_exit(msg)
    #
    # get sphinxrst docuemntation in this file
    file_info = file2file_info(
        pattern_begin_sphinxrst,
        pattern_end_sphinxrst,
        section_list,
        corresponding_file,
        file_in,
    )
    #
    for info in file_info :
        #
        # section_name, section_data
        section_name = info['section_name']
        section_data = info['section_data']
        #
        section_list.append(section_name)
        corresponding_file.append(file_in)
        #
        #
        # process suspend commands
        section_data = suspend_command(
            pattern_suspend_sphinxrst,
            pattern_resume_sphinxrst,
            section_data,
            file_in,
            section_name,
        )
        # ----------------------------------------------------------------
        # process spell commands
        section_data = spell_command(
            pattern_spell_sphinxrst,
            section_data,
            file_in,
            section_name,
        )
        # ----------------------------------------------------------------
        # remove characters on same line as {code_sphinxrst}
        section_data = isolate_code_command(
            pattern_code_sphinxrst,
            section_data,
            file_in,
            section_name,
        )
        # ---------------------------------------------------------------
        # file command: convert start and stop to line numbers
        section_data = convert_file_command(
            pattern_file_sphinxrst,
            section_data,
            file_in,
            section_name,
        )
        # ---------------------------------------------------------------
        # white_space
        white_space = start_line_white_space(
            section_data,
            file_in,
            section_name
        )
        # ---------------------------------------------------------------
        # num_remove (for indented documentation)
        pattern_newline  = re.compile( r'\n')
        newline_itr      = pattern_newline.finditer(section_data)
        newline_list     = list()
        for itr in newline_itr :
            newlist = itr.start()
            newline_list.append( newlist )
        len_data   = len(section_data)
        num_remove   = len(section_data)
        for newline in newline_list :
            next_ = newline + 1
            if next_ < len_data and num_remove != 0 :
                ch = section_data[next_]
                while ch in ' \t\n' and next_ + 1 < len_data :
                    next_ += 1
                    ch = section_data[next_]
                cmd  = section_data[next_:].startswith('{code_sphinxrst')
                cmd += section_data[next_:].startswith('{file_sphinxrst')
                if ch not in ' \t\n' and not cmd :
                    num_remove = min(num_remove, next_ - newline - 1)
        # ---------------------------------------------------------------
        # add labels corresponding to headings
        section_data, children_heading_info = add_labels_for_headings(
            section_data,
            num_remove,
            white_space,
            file_in,
            section_name
        )
        # ----------------------------------------------------------------
        # child_list
        child_list = list()
        parent     =  section_name == file_info[0]['section_name']
        if parent :
            for i in range( len(file_info) - 1 ) :
                child_list.append(  file_info[i+1]['section_name'] )
        # ---------------------------------------------------------------
        # write file for this section
        write_file(
            file_in,
            section_data,
            child_list,
            children_heading_info,
            output_dir,
            section_name,
            spell_checker,
        )
# -----------------------------------------------------------------------------
# read index.rst
file_in   = sphinx_dir + '/index.rst'
file_ptr  = open(file_in, 'r')
file_data = file_ptr.read()
file_ptr.close()
#
for i in range( len(section_list) ) :
    section_name = section_list[i]
    file_in      = corresponding_file[i]
    parent       = True
    if i > 0 :
        parent = file_in != corresponding_file[i-1]
    if parent :
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
