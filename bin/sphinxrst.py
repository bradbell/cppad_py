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
{sphinxrst_begin sphinxrst_py}
{sphinxrst_spell
    sphinxrst
    rst
    underbars
    conf
    toctree
    cmd
}

.. |space| unicode:: 0xA0

###################################
Extract Sphinx RST From Source Code
###################################

Syntax
======
``sphinxrst.py`` *sphinx_dir* *root_file* *spell_file*

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

root_file
---------
The command line argument *root_file* is the name of a file,
relative to the top git repository directory.
The first sphinxrst section in this file will be the *root section*
(top section), in the table of contents for this documentation.
The file *sphinx_dir*:code`/index.rst` must contain the line

|space| |space| |space| |space|
``sphinxrst/`` *section_name*

where *section_name* is the name
of the first section in *root_file*.


spell_file
----------
The command line argument *spell_file* is the name of a file,
relative to the top git repository directory.
This file contains a list of words
that the spell checker will consider correct for all sections.
A line that begins with :code:`#` is a comment (not included in the list).
The words are one per line and
leading and trailing white space in a word are ignored.
Special words, for a particular section, are specified using the
:ref:`spell command<spell_cmd>`.

Table Of Contents
=================

toctree
-------
The sphinx ``toctree`` directives are automatically generated
for sections. The only such directive you nedd to enter is in the
file *sphinx_dir*:code`/index.rst`.
One entry is for the first section in the
:ref:`root_file<sphinxrst_py.command_line_arguments.root_file>`.
Other entries are for ``.rst`` files that are not extracted by
``sphinxrst.py``.


Parent Section
--------------
A single input file may contain multiple sections.
The first section in a file is called the file's parent section.
Other sections in a file are children of the parent section.

Headings and Links
==================

Section Level
-------------
Each :ref:`section<begin_cmd.section>` can have only one header at
the first level which is a title for the section.
The :ref:`section_name<begin_cmd.section_name>`
is automatically used
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
If a sphinxrst input file has more than one section,
the :ref:`parent section<sphinxrst_py.table_of_contents.parent_section>`
has children.

- If this section has a :ref:`child link command<child_cmd>`
  links to all the children of the current section are place where the
  child link command is located.
- If this section has a :ref:`children command<child_cmd>`
  no automatic links to the children of the current section are generated.
- Otherwise, the links to the children of the current section are placed
  at the end of the section.

You can place a heading directly before the links to make them easier to find.

Indentation
===========
If all of the extracted sphinxrst documentation for a section is indented
by the same white space characters, those characters
are not included in the sphinxrst output. This enables one to indent the
sphinxrst so it is grouped with the proper code block in the source.

Wish List
=========
The following is a wish list for future improvements to ``sphinxrst.py``:

Error Messaging
---------------
Improve the error messaging so that it include the line number of the
input file that the error occurred on.

Module
------
Convert the program into a python module and provide a pip distribution for it.


Children
========
{sphinxrst_child_link%
   %sphinx/test_in/heading.py
%}

{sphinxrst_end sphinxrst_py}
"""
# ---------------------------------------------------------------------------
"""
{sphinxrst_begin begin_cmd}
{sphinxrst_spell
    underbar
    rst
}

.. |space| unicode:: 0xA0

======================
Begin and End Commands
======================

Syntax
------
- ``{sphinxrst_begin`` *section_name*:code:`}`
- ``{sphinxrst_end`` *section_name*:code:`}`

Section
-------
The start (end) of a section of the input file is indicated by a
begin (end) command at the
:ref:`beginning of a line<sphinxrst_py.notation.beginning_of_a_line>`.

section_name
------------
A *section_name* is a non-empty sequence of the following characters:
a-z, 0-9, and underbar ``_``.

Output File
-----------
The output file corresponding to *section_name* is

|space| |space| |space| |space|
:ref:`sphinx_dir<sphinxrst_py.command_line_arguments.sphinx_dir>`
``/sphinxrst/`` *section_name* ``.rst``

{sphinxrst_end begin_cmd}
"""
# ---------------------------------------------------------------------------
"""
{sphinxrst_begin child_cmd}

=================================
Children and Child Links Commands
=================================

Syntax
------
- ``{sphinxrst_children%``
  *file_1* :code:`%` ... :code:`%` *file_n* :code:`%}`
- ``{sphinxrst_child_link%``
  *file_1* :code:`%` ... :code:`%` *file_n* :code:`%}`


Purpose
-------
A section can specify a set of files for which
the first section in each file (parent section for each file)
is a child of the current section.
This is done using the commands above at the
:ref:`beginning of a line<sphinxrst_py.notation.beginning_of_a_line>`.

White Space
-----------
Leading and trailing white space is not included in the file names.
In addition, and empty file name is ignored.
This enables one to put the command on multiple input lines.

Links
-----
The child link command also places
links to all the children of the current at the location of the command.
You can place a heading directly before the links to make them easier to find.

Example
-------
{sphinxrst_child_link%
   %sphinx/test_in/children.py
%}

{sphinxrst_end child_cmd}
"""
# ---------------------------------------------------------------------------
"""
{sphinxrst_begin spell_cmd}

=============
Spell Command
=============

Syntax
------
``{sphinxrst_spell`` *word_1* ...  *word_n*:code:`}`

Here *word_1*, ..., *word_n* is the special list of words for this section.
In the syntax above the list of words is all in one line,
but they could be on different lines.
Each word starts with an upper case letter,
a lower case letter, or a back slash.
The back slash is included as a possible beginning of a word
so that latex commands can be included in the spelling list.
The rest of the characters in a word are lower case letters.


Purpose
-------
You can specify a special list of words
(not normally considered correct spelling)
for the current section using the command above at the
:ref:`beginning of a line<sphinxrst_py.notation.beginning_of_a_line>`.

spell_file
----------
The list of words in
:ref:`spell_file<sphinxrst_py.command_line_arguments.spell_file>`
are considered correct spellings for all sections.
The latex commands corresponding to the letters in the greek alphabet
are automatically added to this list.


Capitalized Words
-----------------
The case of the first letter does not matter when checking spelling;
e.g., if ``abcd`` is *word_1* then ``Abcd`` will be considered a valid word.

Double Words
------------
It is considered an error to have only white space between two occurrences
of the same word.

Example
-------
{sphinxrst_child_link%
   %sphinx/test_in/spell.py
%}

{sphinxrst_end spell_cmd}
"""
# ---------------------------------------------------------------------------
"""
{sphinxrst_begin suspend_cmd}

==========================
Suspend and Resume Command
==========================

Syntax
------
- ``{sphinxrst_suspend}``
- ``{sphinxrst_resume}``

Purpose
-------
It is possible to suspend (resume) the sphinxrst extraction during a section.
One begins (ends) the suspension with a suspend command (resume command)
at the
:ref:`beginning of a line<sphinxrst_py.notation.beginning_of_a_line>`.
Note that this will also suspend all other sphinxrst processing; e.g.,
spell checking.

Example
-------
{sphinxrst_child_link%
   %sphinx/test_in/suspend.py
%}

{sphinxrst_end suspend_cmd}
"""
# ---------------------------------------------------------------------------
"""
{sphinxrst_begin code_cmd}
{sphinxrst_spell
    cmd
}

============
Code Command
============

Syntax
------
``{sphinxrst_code}``

Purpose
-------
A code block, directly below in the current input file, begins with
a line containing the command above.

Requirements
------------
Each code command ends with
a line containing another code command.
Hence there must be an even number of code commands.
The back quote character \` can't be in the same line as the commands.

Rest of Line
------------
Other characters on the same line as a code command
are not included in the sphinxrst output.
This enables one to begin or end a comment block
without having the comment characters in the sphinxrst output.
The file extension in the name of the current input file is used to
determine the source code language for highlighting the code block.
Code blocks as usually small and

Spell Checking
--------------
Spell checking is done for these code blocks,
but not for code blocks included using the
:ref:`file command<file_cmd>`.

Example
-------
{sphinxrst_child_link%
   %sphinx/test_in/code_block.py
%}

{sphinxrst_end code_cmd}
"""
# ---------------------------------------------------------------------------
"""
{sphinxrst_begin file_cmd}

============
File Command
============

Syntax
------
``{sphinxrst_file%`` *file_name* :code:`%` *start* :code:`%` *stop* :code:`%}`

Purpose
-------
A code block, from any file, is included by the command above at the
:ref:`beginning of a line<sphinxrst_py.notation.beginning_of_a_line>`.

White Space
-----------
Leading and trailing white space is not included in
*file_name*, *start*, or *end*.
This enables one to put the command on multiple input lines.

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

Spell Checking
--------------
Spell checking is **not** done for these code blocks.


Example
-------
{sphinxrst_child_link%
   %sphinx/test_in/file_block.py
%}

{sphinxrst_end file_cmd}
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
    sys.exit(msg )
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
        pattern_begin_command,
        pattern_end_command,
        section_info,
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
        # match_sphinxrst_begin
        data_rest   = file_data[file_index : ]
        match_sphinxrst_begin = pattern_begin_command.search(data_rest)
        #
        if match_sphinxrst_begin == None :
            if file_index == 0 :
                msg  = 'can not find followng at start of a line:\n'
                msg += '    {sphinxrst_begin section_name}\n'
                sys_exit(msg, file_in)
            file_index = len(file_data)
        else :
            # section_name
            section_name = match_sphinxrst_begin.group(1)
            if section_name == '' :
                msg  = 'section_name after sphinxrst_begin is empty'
                sys_exit(msg, file_in)
            #
            # check if section appears multiple times
            for info in file_info :
                if section_name == info['section_name'] :
                    msg  = 'sphinxrst_begin ' + section_name
                    msg += ' appears twice in file\n' + file_in
                    sys_exit(msg)
            for info in section_info :
                if section_name == info['section_name'] :
                    msg  = 'sphinxrst_begin ' + section_name
                    msg += ' appears twice\n'
                    msg += 'Once in file ' + file_in + '\n'
                    msg += 'And again in file ' + info['file_in'] + '\n'
                    sys_exit(msg)
            #
            # file_index
            file_index += match_sphinxrst_begin.end()
            #
            # match_sphinxrst_end
            data_rest = file_data[file_index : ]
            match_sphinxrst_end = pattern_end_command.search(data_rest)
            #
            if match_sphinxrst_end == None :
                msg  = 'can not find followig at start of a line:\n'
                msg += '    {sphinxrst_end section_name}'
                sys_exit(msg, file_in, section_name)
            if match_sphinxrst_end.group(1) != section_name :
                msg = 'in file ' + file_in + '\nsection names do not match\n'
                msg += 'sphinxrst_begin section name = '+section_name + '\n'
                msg += 'sphinxrst_end section name   = '
                msg += match_sphinxrst_end.group(1) + '\n'
                sys_exit(msg)
            #
            # section_data
            section_start = file_index
            section_end   = file_index + match_sphinxrst_end.start()
            section_data  = file_data[ section_start : section_end ]
            #
            # file_info
            file_info.append( {
                'section_name' : section_name,
                'section_data' : section_data,
            } )
            #
            # place to start search for next section
            file_index += match_sphinxrst_end.end()
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
# process sphinxrst_suspend commands
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
            msg  = 'there is a {sphinxrst_suspend} without a '
            msg += 'corresponding {sphinxrst_resume}'
            sys_exit(msg, file_in, section_name)
        if match_suspend != None :
            if match_suspend.start() < match_resume.start() :
                msg  = 'there are two {sphinxrst_suspend} without a '
                msg += '{sphinxrst_resume} between them'
                sys_exit(msg, file_in, section_name)
        resume_end   = match_resume.end() + suspend_end
        section_rest = section_data[ resume_end :]
        section_data = section_data[: suspend_start] + section_rest
        #
        # redo match_suppend so relative to new section_data
        match_suspend = suspend_pattern.search(section_data)
    return section_data
# -----------------------------------------------------------------------------
# process child commands
def child_commands(
    pattern_child,
    pattern_begin,
    pattern_end,
    section_data,
    file_in,
    section_name,
) :
    file_list    = list()
    section_list = list()
    match        = pattern_child.search(section_data)
    if match is None :
        return section_data, file_list, section_list
    match_tmp    = pattern_child.search(section_data[match.end() :] )
    if match_tmp is not None :
        msg = 'There is more than one children or child_link commands in'
        sys_exit(msg, file_in, section_name)
    #
    assert match.group(1) == 'children' or match.group(1) == 'child_link'
    command = match.group(1)
    replace = '\n{sphinxrst_' + command + '}\n'
    #
    # section_data
    data_left  = section_data[ : match.start() ]
    data_right = section_data[ match.end() : ]
    section_data = data_left + replace + data_right
    #
    # file_list
    for child_file in match.group(2).split('%') :
        child_file = child_file.strip()
        if child_file != '' :
            file_list.append(child_file)
    #
    # section_list
    for child_file in file_list :
        if not os.path.isfile(child_file) :
            msg  = 'The file ' + child_file + '\n'
            msg += 'in the ' + command + ' command does not exist'
            sys_exit(msg, file_in, section_name)
        #
        # errors in the begin and end commands will be detected later
        # when this file is processed.
        file_ptr    = open(child_file, 'r')
        file_data   = file_ptr.read()
        file_ptr.close()
        file_index  = 0
        match       = pattern_begin.search(file_data)
        if match is None :
            msg  = 'The file ' + child_file + '\n'
            msg += 'in the ' + command + ' command does not contain any '
            msg += 'begin commands'
            sys_exit(msg, file_in, section_name)
        #
        child_name  = match.group(1)
        if child_name != '' :
            section_list.append(child_name)
    #
    return section_data, file_list, section_list
# -----------------------------------------------------------------------------
# process spell command
def spell_command(
    spell_pattern, section_data, file_in, section_name
) :
    word_pattern  = re.compile( r'[\\A-Za-z][a-z]*' )
    match_spell   = spell_pattern.search(section_data)
    special_list  = list()
    if match_spell != None :
        section_rest   = section_data[ match_spell.end() : ]
        match_another  = pattern_spell_command.search(section_rest)
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
# remove characters on same line as {sphinxrst_code}
def isolate_code_command(code_pattern, section_data, file_in, section_name) :
    section_index  = 0
    match_begin_code = code_pattern.search(section_data)
    while match_begin_code != None :
        begin_start    = match_begin_code.start() + section_index
        begin_end      = match_begin_code.end()   + section_index
        section_rest   = section_data[ begin_end : ]
        match_end_code = code_pattern.search( section_rest )
        if match_end_code == None :
            msg  = 'number of sphinxrst_code commands is not even'
            sys_exit(msg, file_in, section_name)
        end_start = match_end_code.start() + begin_end
        end_end   = match_end_code.end()   + begin_end
        #
        data_left   = section_data[: begin_start + 1 ]
        data_left  += '{sphinxrst_code}'
        data_left  += section_data[ begin_end : end_start + 1]
        data_left  += '{sphinxrst_code}'
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
            msg = 'sphinxrst_file command: start text is empty'
            sys_exit(msg, file_in, section_name)
        #
        # stop
        stop      = match_file.group(3) .strip()
        if stop == '' :
            msg = 'sphinxrst_file command: stop text is empty'
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
            msg  = 'sphinxrst_file command: can not find start = '
            msg += '"' + start + '"'
            msg += '\nin file_name = "' + file_name + '"'
            sys_exit(msg, file_in, section_name)
        offset     = start_index + len(start)
        if 0 <= find_at_start_of_line(offset, data, start) :
            msg  = 'sphinxrst_file command: found more than one '
            msg += 'start = "' + start + '"'
            msg += '\nin file_name = "' + file_name + '"'
            sys_exit(msg, file_in, section_name)
        #
        # stop_index
        stop_index = find_at_start_of_line(offset, data, stop)
        if stop_index < 0 :
            msg  = 'sphinxrst_file command: can not find'
            msg += '\nstop = "' + stop + '"'
            msg += ' after start = "' + start + '"'
            msg += '\nin file_name = "' + file_name + '"'
            sys_exit(msg, file_in, section_name)
        offset     = stop_index + len(stop)
        if 0 <= find_at_start_of_line(offset, data, stop) :
            msg  = 'sphinxrst_file command: found more than one '
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
        cmd  = f'sphinxrst_file%{file_name}%{start_line}%{stop_line}%'
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
            data_left  += '\n{sphinxrst_label ' + label + ' }'
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
    return section_data
# -----------------------------------------------------------------------------
# write file corresponding to a section
# (and finish processing that has been delayed to this point)
def write_file(
    file_in,
    section_data,
    section_info,
    child_list,
    output_dir,
    section_name,
    spell_checker,
) :
    # split section data into lines
    newline_pattern = re.compile( r'\n')
    newline_itr     = newline_pattern.finditer(section_data)
    newline_list    = list()
    for itr in newline_itr :
        newlist = itr.start()
        newline_list.append( newlist )
    #
    # open output file
    file_out          = output_dir + '/' + section_name + '.rst'
    file_ptr          = open(file_out, 'w')
    #
    # links to ancestors and position in website
    section_index = len(section_info) - 1
    assert section_info[section_index]['section_name'] == section_name
    line  = section_name + '\n'
    ancestor_index = section_info[section_index]['parent_section']
    while ancestor_index != None :
        ancestor_name  = section_info[ancestor_index]['section_name']
        ancestor_index = section_info[ancestor_index]['parent_section']
        line  = f':ref:`{ancestor_name}<{ancestor_name}>`' + ' > ' + line
    file_ptr.write('|\n\n') # vertical space needed by bootstrap theme
    file_ptr.write(line)
    file_ptr.write('\n')
    #
    # now output the section data
    startline         = 0
    inside_code       = False
    previous_empty    = True
    has_child_command = False
    for newline in newline_list :
        line  = section_data[startline : newline + 1]
        # commands that delay some processing to this point
        code_command       = line.startswith('{sphinxrst_code')
        file_command       = line.startswith('{sphinxrst_file')
        label_command      = line.startswith('{sphinxrst_label')
        children_command   = line.startswith('{sphinxrst_children')
        child_link_command = line.startswith('{sphinxrst_child_link')
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
        elif children_command or child_link_command :
            assert not has_child_command
            assert len(child_list) > 0
            has_child_command = True
            #
            file_ptr.write('.. toctree::\n')
            file_ptr.write('   :maxdepth: 1\n')
            if children_command :
                file_ptr.write('   :hidden:\n')
            file_ptr.write('\n')
            for child in child_list :
                file_ptr.write('   ' + child + '\n')
            file_ptr.write('\n')
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
    if len(child_list) > 0 and not has_child_command :
        file_ptr.write('.. toctree::\n')
        file_ptr.write('   :maxdepth: 1\n\n')
        for child in child_list :
            file_ptr.write('   ' + child + '\n')
        file_ptr.write('\n')
    #
    file_ptr.write('----\n\n') # sphinx transition
    file_ptr.write( f'sphinxrst input file: ``{file_in}``\n')
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
# root_file
root_file = sys.argv[2]
if not os.path.isfile(root_file) :
    msg  = 'root_file = ' + root_file + '\n'
    msg += 'is not a file'
    sys_exit(msg)
#
# spell_file
spell_file = sys.argv[3]
if not os.path.isfile(spell_file) :
    msg  = 'spell_file = ' + spell_file + '\n'
    msg += 'is not a file'
    sys_exit(msg)
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
spell_list    = file2list(spell_file)
spell_checker = init_spell_checker(spell_list)
#
# define some pytyon regular expression patterns
pattern_code_command    = re.compile( r'\n[^\n`]*\{sphinxrst_code\}[^\n`]*')
pattern_suspend_command = re.compile( r'\n[ \t]*\{sphinxrst_suspend\}' )
pattern_resume_command  = re.compile( r'\n[ \t]*\{sphinxrst_resume\}' )
pattern_begin_command   = re.compile(
    r'\n[ \t]*\{sphinxrst_begin\s+([a-z0-9_]+)\}'
)
pattern_end_command     = re.compile(
    r'\n[ \t]*\{sphinxrst_end\s+([a-z0-9_]+)\}'
)
pattern_spell_command   = re.compile(
    r'\n[ \t]*\{sphinxrst_spell([^}]*)\}'
)
pattern_file_command    = re.compile(
    r'\n[ \t]*\{sphinxrst_file%([^%]*)%([^%]*)%([^%]*)%\}'
)
pattern_child_command = re.compile(
    r'\n[ \t]*\{sphinxrst_(children|child_link)%([^}]*)%\}'
)
# -----------------------------------------------------------------------------
# process each file in the list
section_info     = list()
file_info_stack  = list()
file_info_done   = list()
info = {
    'file_in'        : root_file,
    'parent_file'    : None,
    'parent_section' : None,
}
file_info_stack.append(info)
while 0 < len(file_info_stack) :
    info  = file_info_stack.pop()
    #
    for info_tmp in file_info_done :
        if info_tmp['file_in'] == info['file_in'] :
            msg  = 'The file ' + info['file_in'] + ' is included twice\n'
            msg += 'Once in ' + info_tmp['parent_file'] + '\n'
            msg += 'and again in ' + info['parent_file'] + '\n'
            sys_exit(msg)
    file_info_done.append(info)
    #
    file_in        = info['file_in']
    parent_file    = info['parent_file']
    parent_section = info['parent_section']
    assert os.path.isfile(file_in)
    #
    # get sphinxrst docuemntation in this file
    this_file_info = file2file_info(
        pattern_begin_command,
        pattern_end_command,
        section_info,
        file_in,
    )
    #
    # first section for this file (is parent for this file)
    first_section_index = len(section_info)
    for i in range( len(this_file_info) ) :
        # ----------------------------------------------------------------
        # section_name, section_data
        section_name = this_file_info[i]['section_name']
        section_data = this_file_info[i]['section_data']
        if 0 < i :
            parent_section = first_section_index
        #
        section_info.append( {
            'section_name'   : section_name,
            'file_in'        : file_in,
            'parent_section' : parent_section
        } )
        # ----------------------------------------------------------------
        # process suspend commands
        section_data = suspend_command(
            pattern_suspend_command,
            pattern_resume_command,
            section_data,
            file_in,
            section_name,
        )
        # ----------------------------------------------------------------
        # process child command
        section_data, child_file, child_section = child_commands(
            pattern_child_command,
            pattern_begin_command,
            pattern_end_command,
            section_data,
            file_in,
            section_name,
        )
        section_index = len(section_info) - 1
        for file_tmp in child_file :
            file_info_stack.append( {
                'file_in'        : file_tmp,
                'parent_file'    : file_in,
                'parent_section' : section_index,
            } )
        # ----------------------------------------------------------------
        # process spell commands
        section_data = spell_command(
            pattern_spell_command,
            section_data,
            file_in,
            section_name,
        )
        # ----------------------------------------------------------------
        # remove characters on same line as {sphinxrst_code}
        section_data = isolate_code_command(
            pattern_code_command,
            section_data,
            file_in,
            section_name,
        )
        # ---------------------------------------------------------------
        # file command: convert start and stop to line numbers
        section_data = convert_file_command(
            pattern_file_command,
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
                cmd  = section_data[next_:].startswith('{sphinxrst_code')
                cmd += section_data[next_:].startswith('{sphinxrst_file')
                cmd += section_data[next_:].startswith('{sphinxrst_child')
                if ch not in ' \t\n' and not cmd :
                    num_remove = min(num_remove, next_ - newline - 1)
        # ---------------------------------------------------------------
        # add labels corresponding to headings
        section_data = add_labels_for_headings(
            section_data,
            num_remove,
            white_space,
            file_in,
            section_name
        )
        # ----------------------------------------------------------------
        # child_list
        # first section in each file may need to add to child list
        parent   = section_name == this_file_info[0]['section_name']
        child_list = list()
        if parent :
            for i in range( len(this_file_info) - 1 ) :
                child_list.append(  this_file_info[i+1]['section_name'] )
        child_list = child_list + child_section
        # ---------------------------------------------------------------
        # write file for this section
        write_file(
            file_in,
            section_data,
            section_info,
            child_list,
            output_dir,
            section_name,
            spell_checker,
        )
# -----------------------------------------------------------------------------
# read index.rst
index_file   = sphinx_dir + '/index.rst'
file_ptr     = open(index_file, 'r')
file_data    = file_ptr.read()
file_ptr.close()
#
# section_info[0] corresponds to the root section
assert section_info[0]['file_in'] == root_file
assert section_info[0]['parent_section'] is None
section_name = section_info[0]['section_name']
#
# check section_name is in index file
pattern  = r'\n[ \t]*sphinxrst/'
pattern += section_name.replace('.', '[.]')
match_line = re.search(pattern, file_data)
if match_line == None :
    msg  = 'The first section in the root_file is ' + section_name + '\n'
    msg += 'The following line:\n'
    msg += '    sphinxrst/' + section_name + '\n'
    msg += 'must is missing from the toctree command in\n'
    msg += index_file
    sys_exit(msg)
#
print('sphinxrst.py: OK')
sys.exit(0)
