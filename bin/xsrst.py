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
{xsrst_begin_parent xsrst_py}
{xsrst_spell
    xsrst
    rst
    underbars
    conf
    toctree
    cmd
    html
    stackoverflow
    https
}

.. |space| unicode:: 0xA0

##################
Extract Sphinx RST
##################


.. The indentation examples are included by the child_cmd section.

{xsrst_children
   sphinx/test_in/heading.py
}

Syntax
======
``xsrst.py`` *sphinx_dir* *root_file* *spell_file*

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
and that are in the directory *sphinx_dir*:code:`/xsrst`,
are removed at the beginning of execution of ``xsrst.py``.
All the ``.rst`` files in *sphinx_dir*:code:`/xsrst`
were extracted from the source code the last time that ``xsrst.py``
was executed.

root_file
---------
The command line argument *root_file* is the name of a file,
relative to the top git repository directory.

root_section
............
If there is only one section in the *root_file* it is called
the *root_section*; i.e., it is the top section in that table of contents.
If there is more than one section in the *root_file*,
the file must have a
:ref:`begin_cmd.parent_section` and it is the *root_section*.
The file *sphinx_dir*:code`/index.rst` must contain the line

|space| |space| |space| |space|
``xsrst/`` *section_name*

where *section_name* is the name of the *root_section*.


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
for sections. The only such directive you should directly edit
is in the file *sphinx_dir*:code`/index.rst`.
One entry in this file specifies the
:ref:`root_section<xsrst_py.command_line_arguments.root_file.root_section>`.
Other entries are for ``.rst`` files that are not extracted by
``xsrst.py``.

Parent Section
--------------
A single input file may contain multiple
:ref:`sections<begin_cmd.section>`.
One (and at most one) of these sections may use begin with a
:ref:`parent begin<begin_cmd.parent_section>` command.
In this case, the other sections in the file are children of this section
and this section is a child of the section containing the
:ref:`child command<child_cmd>` that included this file.

If there is no parent section for a file,
all the sections in the file are children of the section containing the
child command that included the file.

Heading Links
=============
- For each word in a heading,
a link is included in the index from the word to the heading.

- Each word in a heading is added to the html keyword meta data.

- A cross reference label is defined for linking
  from anywhere to a heading. The details of how to use
  these labels are described below.

- Headings can also be used to help find links to children
  of the current section; see the heading
  :ref:`xsrst_py.heading_links.children` below.

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
paragraph is ``xsrst_py.headers_and_links.other_levels``.
This may seem verbose, but it helps keep the links up to date.
If a heading changes, all the links to that heading will break.
This identifies the links that should be checked
to make sure they are still valid.

Children
--------
If a xsrst input file has a
ref:`parent section<xsrst_py.table_of_contents.parent_section>`
the other sections in the file are children of the parent.

- If a section has a :ref:`child link command<child_cmd>`
  links to all the children of the section are place where the
  child link command is located.
- If a section has a :ref:`children command<child_cmd>`
  no automatic links to the children of the current section are generated.
- Otherwise, the links to the children of a section are placed
  at the end of the section.

You can place a heading directly before the links to make them easier to find.

Example
-------
:ref:`heading_exam`

Indentation
===========
If there are a number of spaces or tabs (but not both) before
all of the xsrst documentation for a section,
those characters are not included in the xsrst output.
This enables one to indent the
xsrst so it is grouped with the proper code block in the source.
An error message will result if
you mix spaces and tabs in this indentation.

Example
-------
- :ref:`indent_space_exam`
- :ref:`indent_tab_exam`

Wish List
=========
The following is a wish list for future improvements to ``xsrst.py``:

.. _stackoverflow: https://stackoverflow.com/questions/1686837/
   sphinx-documentation-tool-set-tab-width-in-output

Code Blocks
-----------
It would be nice to extend the :ref:`code_cmd` to have an optional
argument that specifies the languages (which might be different from
the file it appears in).

Tabs
----
Currently tabs in code blocks get expanded to 8 spaces; see stackoverflow_.
It would be nice to have a way to control the size of tabs in the code blocks
displayed by :ref:`code_cmd` and :ref:`file_cmd`.

Error Messaging
---------------
Improve the error messaging so that it include the line number of the
input file that the error occurred on.

Module
------
Convert the program into a python module and provide a pip distribution for it.


.. All the children of this section are commands except for heading_exam.

Commands
========
- :ref:`begin_cmd`
- :ref:`child_cmd`
- :ref:`spell_cmd`
- :ref:`suspend_cmd`
- :ref:`code_cmd`
- :ref:`file_cmd`
- :ref:`comment_ch_cmd`

{xsrst_end xsrst_py}
"""
# ---------------------------------------------------------------------------
"""
{xsrst_begin begin_cmd}
{xsrst_spell
    underbar
    rst
    cmd
}

.. |space| unicode:: 0xA0

======================
Begin and End Commands
======================

Syntax
------
- ``{xsrst_begin``        *section_name*:code:`}`
- ``{xsrst_begin_parent`` *section_name*:code:`}`
- ``{xsrst_end``          *section_name*:code:`}`

Section
-------
The start (end) of a section of the input file is indicated by a
begin (end) command at the
:ref:`beginning of a line<xsrst_py.notation.beginning_of_a_line>`.

section_name
------------
The *section_name* is a non-empty sequence of the following characters:
a-z, 0-9, and underbar ``_``.
A link is included in the index under the section name
to the first heading the section.
The section name is also added to the html keyword meta data.


Output File
-----------
The output file corresponding to *section_name* is

|space| |space| |space| |space|
:ref:`sphinx_dir<xsrst_py.command_line_arguments.sphinx_dir>`
``/xsrst/`` *section_name* ``.rst``

Parent Section
--------------
There can be at most one begin parent command in an input file.
In this case there must be other sections in the file
and they are child of the parent section.
The parent section is a child
of the section that included this file using a :ref:`child command<child_cmd>`.

If there is no parent command in an input file,
all the sections in the file are children
of the section that included this file using a :ref:`child command<child_cmd>`.

{xsrst_end begin_cmd}
"""
# ---------------------------------------------------------------------------
"""
{xsrst_begin child_cmd}
{xsrst_spell
    cmd
}

=================================
Children and Child Links Commands
=================================

Syntax
------

| ``{xsrst_children``
|   *file_1*
|   ...
|   *file_n*
| :code:`}`
|
| ``{xsrst_child_link``
|   *file_1*
|   ...
|   *file_n*
| :code:`}`


Purpose
-------
A section can specify a set of files for which the
:ref:`parent section<begin_cmd.parent_section>` of each file
is a child of the current section.
(If there is not parent section in a file,
all the sections in the file are children of the current section.)
This is done using the commands above at the
:ref:`beginning of a line<xsrst_py.notation.beginning_of_a_line>`.

File Names
----------
A new line character must precede and follow each
of the file names *file_1* ... *file_n*.
Leading and trailing white space is not included in the names
The file names are  relative to the directory where ``xsrst.py``
is executed; i.e., the top directory for this git repository.
This may seem verbose, but it makes it easier to write scripts
that move files and automatically change references to them.

Links
-----
The child link command also places
links to all the children of the current at the location of the command.
You can place a heading directly before the links to make them easier to find.

Example
-------
{xsrst_child_link
   sphinx/test_in/no_parent.xsrst
}

{xsrst_end child_cmd}
"""
# ---------------------------------------------------------------------------
"""
{xsrst_begin spell_cmd}

=============
Spell Command
=============

Syntax
------
``{xsrst_spell`` *word_1* ...  *word_n*:code:`}`

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
:ref:`beginning of a line<xsrst_py.notation.beginning_of_a_line>`.

spell_file
----------
The list of words in
:ref:`spell_file<xsrst_py.command_line_arguments.spell_file>`
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
{xsrst_child_link
   sphinx/test_in/spell.py
}

{xsrst_end spell_cmd}
"""
# ---------------------------------------------------------------------------
"""
{xsrst_begin suspend_cmd}

==========================
Suspend and Resume Command
==========================

Syntax
------
- ``{xsrst_suspend}``
- ``{xsrst_resume}``

Purpose
-------
It is possible to suspend (resume) the xsrst extraction during a section.
One begins (ends) the suspension with a suspend command (resume command)
at the
:ref:`beginning of a line<xsrst_py.notation.beginning_of_a_line>`.
Note that this will also suspend all other xsrst processing; e.g.,
spell checking.

Example
-------
{xsrst_child_link
   sphinx/test_in/suspend.py
}

{xsrst_end suspend_cmd}
"""
# ---------------------------------------------------------------------------
"""
{xsrst_begin code_cmd}
{xsrst_spell
    cmd
}

============
Code Command
============

Syntax
------
``{xsrst_code`` *language* :code:`}`
``{xsrst_code}``

Purpose
-------
A code block, directly below in the current input file, begins with
a line containing the first version ( *language* included version)
of the command above.

Requirements
------------
Each code command ends with
a line containing the second version of the command; i.e., ``{xsrst_code}``.
Hence there must be an even number of code commands.
The back quote character \` can't be in the same line as the commands.

language
--------
A *language* is a non-empty sequence of non-space the characters.
It is used to determine the source code language
for highlighting the code block.

Rest of Line
------------
Other characters on the same line as a code command
are not included in the xsrst output.
This enables one to begin or end a comment block
without having the comment characters in the xsrst output.

Spell Checking
--------------
Code blocks as usually small and
spell checking is done for these code blocks.
(Spell checking is not done for code blocks included using the
:ref:`file command<file_cmd>` .)

Example
-------
{xsrst_child_link
   sphinx/test_in/code_block.py
}

{xsrst_end code_cmd}
"""
# ---------------------------------------------------------------------------
"""
{xsrst_begin file_cmd}

.. |space| unicode:: 0xA0

============
File Command
============

Syntax
------

| ``{xsrst_file`` |space| *start*
|   *stop*
| :code:`}`
|
| ``{xsrst_file`` |space| *start*
|   *stop*
|   *file_name*
| :code:`}`

Purpose
-------
A code block, from any where in any file,
is included by the command above at the
:ref:`beginning of a line<xsrst_py.notation.beginning_of_a_line>`.

White Space
-----------
Leading and trailing white space is not included in
*start*, *stop* or *file_name*.
The new line character terminates these tokens.

file_name
---------
If *file_name* is not in the syntax,
the code block is in the current input file.
Otherwise, the code block is in *file_name*,
which is relative to the directory where ``xsrst.py``
is executed; i.e., the top directory for this git repository.
This may seem verbose, but it makes it easier to write scripts
that move files and automatically change references to them.

start
-----
The code block starts with the occurence
of the text *start* at the beginning of a line in *file_name*.
There can only be one occurence of *start* at the beginning
of a line in *file_name*.
Note that the *start* pattern in the command does not
occur at the beginning of a line.
Hence it will not match the scan for the start of the code block
when the code block is in the current input file.

stop
----
The code block ends with the first occurence
of the text *stop* at the beginning of a line and after *start*.
The lines containing *start* and *stop* in *file_name* are not included in
the code block.

Spell Checking
--------------
Spell checking is **not** done for these code blocks.


Example
-------
{xsrst_child_link
   sphinx/test_in/file_block.py
}

{xsrst_end file_cmd}
"""
# ----------------------------------------------------------------------------
"""
{xsrst_begin comment_ch_cmd}
{xsrst_spell
    rst
    cmd
}

==================
Comment Ch Command
==================

Syntax
------
``{xsrst_comment_ch`` *ch*:code:`}`

Purpose
-------
Some languages have a special character that
indicates the rest of the line is a comment.
If you embed sphinx documentation in this type of comment,
you need to inform xsrst of the special character so it does
not end up in your ``.rst`` output file.

ch
--
The value of *ch* must be one non white space character.
There must be at least one white space character
between `xsrst_comment_ch`` and *ch*.
Leading and trailing white space around *ch* is ignored.
There can be only one occurence of this command within a file,
it's effect lasts for the entire file, and
it must come before the first :ref:`begin_cmd` in the file.


Beginning of a Line
-------------------
A sequence of characters *text* is at the beginning of a line if there
are only spaces and tab characters
between the previous new line character and *text*.
In addition, the special character *ch* can be the first character
after the new line and before *text*.

Indentation
-----------
The special character (and one space if present directly after)
is removed from the input stream before calculating the amount of
:ref:`xsrst_py.Indentation` for the current section.
For example, if :code:`#` is the special character,
the following input has the heading Factorial
and the ``def`` token indented the same amount:

.. code-block:: py

    # Factorial
    # ---------
    def factorial(n) :
        if n == 1 :
            return 1
        return n * factorial(n-1)


Example
-------
{xsrst_child_link
    sphinx/test_in/comment_ch.py
}

{xsrst_end comment_ch_cmd}
"""
# ---------------------------------------------------------------------------
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
def get_code_file_extensions() :
    import pygments.lexers
    code_file_extensions = list()
    for lexer in pygments.lexers.get_all_lexers() :
        for extension in lexer[2] :
            extension = extension.replace('*.', '')
            code_file_extensions.append( extension )
    return code_file_extensions
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
            j -= 1
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
def pattern_begin_end(file_data, file_in) :
    #
    # comment_ch
    pattern_comment_ch = re.compile(r'{xsrst_comment_ch\s+([^}])\s*\}')
    match_comment_ch   = pattern_comment_ch.search(file_data)
    if not match_comment_ch :
        comment_ch = None
    else :
        comment_ch = match_comment_ch.group(1)
        data_rest  = file_data[ match_comment_ch.end() : ]
        match      = pattern_comment_ch.search(file_in)
        if match :
            msg = 'There are multiple command_ch commands in this file'
            sys_exit(msg, file_in)
        if comment_ch == ']' :
            msg  = 'Cannot use "]" as the speical comment charater\n'
            msg += 'in a comment_ch command.'
            sys_exit(msg, file_in)
    #
    # pattern_begin
    ch = comment_ch
    if ch :
        pattern_begin = re.compile(
        r'\n[' + ch + r']?[ \t]*\{xsrst_(begin|begin_parent)\s+([a-z0-9_]+)\}'
        )
    else :
        pattern_begin = re.compile(
            r'\n[ \t]*\{xsrst_(begin|begin_parent)\s+([a-z0-9_]+)\}'
        )
    #
    # pattern_end
    if ch :
        pattern_end = re.compile(
            r'\n[' + ch + r']?[ \t]*\{xsrst_end\s+([a-z0-9_]+)\}'
        )
    else :
        pattern_end = re.compile(
            r'\n[ \t]*\{xsrst_end\s+([a-z0-9_]+)\}'
        )
    return pattern_begin, pattern_end, match_comment_ch

# ----------------------------------------------------------------------------
# find all the section names and corresponding data in the specified file
# The returned data does not include the begin and end section commands
def file2file_info(
        section_info,
        file_in
) :
    #
    # file_data
    file_ptr   = open(file_in, 'r')
    file_data  = file_ptr.read()
    file_ptr.close()
    #
    # initialize return value
    file_info = list()
    #
    pattern_begin_command, pattern_end_command, match_comment_ch = \
        pattern_begin_end(file_data, file_in)
    #
    if match_comment_ch :
        comment_ch       = match_comment_ch.group(1)
        comment_ch_index = match_comment_ch.end()
    else :
        comment_ch       = None
        comment_ch_index = 0
    #
    # index to start search for next pattern in file_data
    file_index  = 0
    #
    while file_index < len(file_data) :
        #
        # match_xsrst_begin
        data_rest   = file_data[file_index : ]
        match_xsrst_begin = pattern_begin_command.search(data_rest)
        #
        if match_xsrst_begin == None :
            if file_index == 0 :
                msg  = 'can not find followng at start of a line:\n'
                msg += '    {xsrst_begin section_name}\n'
                sys_exit(msg, file_in)
            file_index = len(file_data)
        else :
            # section_name
            section_name = match_xsrst_begin.group(2)
            is_parent    = match_xsrst_begin.group(1) == 'begin_parent'
            if section_name == '' :
                msg  = 'section_name after xsrst_begin is empty'
                sys_exit(msg, file_in)
            #
            begin_index = file_index + match_xsrst_begin.start()
            if begin_index < comment_ch_index :
                msg = 'A begin command comes before the comment_ch command'
                sys_exit(msg, file_in, section_name)
            #
            # check if section appears multiple times
            for info in file_info :
                if section_name == info['section_name'] :
                    msg  = 'xsrst_begin ' + section_name
                    msg += ' appears twice in file\n' + file_in
                    sys_exit(msg)
            for info in section_info :
                if section_name == info['section_name'] :
                    msg  = 'xsrst_begin ' + section_name
                    msg += ' appears twice\n'
                    msg += 'Once in file ' + file_in + '\n'
                    msg += 'And again in file ' + info['file_in'] + '\n'
                    sys_exit(msg)
            #
            # check if two parent sections in this file
            if is_parent :
                for info in file_info :
                    if info['is_parent'] :
                        msg  = 'xsrst_begin_parent'
                        msg += ' appears twice in file\n' + file_in
                        sys_exit(msg)
            #
            # file_index
            file_index += match_xsrst_begin.end()
            #
            # match_xsrst_end
            data_rest = file_data[file_index : ]
            match_xsrst_end = pattern_end_command.search(data_rest)
            #
            if match_xsrst_end == None :
                msg  = 'can not find followig at start of a line:\n'
                msg += '    {xsrst_end section_name}'
                sys_exit(msg, file_in, section_name)
            if match_xsrst_end.group(1) != section_name :
                msg = 'in file ' + file_in + '\nsection names do not match\n'
                msg += 'xsrst_begin section name = '+section_name + '\n'
                msg += 'xsrst_end section name   = '
                msg += match_xsrst_end.group(1) + '\n'
                sys_exit(msg)
            #
            # section_data
            section_start = file_index
            section_end   = file_index + match_xsrst_end.start() + 1
            section_data  = file_data[ section_start : section_end ]
            #
            # remove comments at start of lines
            if comment_ch :
                assert len(comment_ch) == 1
                pattern = re.compile( r'\n[' + comment_ch + r'] ?' )
                section_data = pattern.sub(r'\n', section_data)
            #
            # file_info
            file_info.append( {
                'section_name' : section_name,
                'section_data' : section_data,
                'is_parent'    : is_parent,
            } )
            #
            # place to start search for next section
            file_index += match_xsrst_end.end()
    return file_info
# ----------------------------------------------------------------------------
def indent_to_remove(section_data, file_in, section_name) :
    #
    # len_data
    len_data   = len(section_data)
    #
    # newline_list
    pattern_newline  = re.compile( r'\n')
    newline_itr      = pattern_newline.finditer(section_data)
    newline_list     = list()
    for itr in newline_itr :
        newlist = itr.start()
        newline_list.append( newlist )
    #
    # num_remove
    num_remove = len(section_data)
    for newline in newline_list :
        next_ = newline + 1
        if next_ < len_data and 0 < num_remove :
            ch = section_data[next_]
            while ch in ' \t' and next_ + 1 < len_data :
                next_ += 1
                ch     = section_data[next_]
            if ch not in ' \t\n' :
                num_remove = min(num_remove, next_ - newline - 1)
    if num_remove == 0 :
        return num_remove
    #
    # check indent_ch
    line      = 0
    indent_ch = section_data[ newline_list[line] + 1 ]
    while indent_ch == '\n' :
        line += 1
        indent_ch = section_data[ newline_list[line] + 1 ]
    #
    check_ch  = indent_ch + '\n'
    for newline in newline_list :
        next_ = newline + 1
        end   = min( len_data, next_ + num_remove )
        while next_ < end :
            if section_data[next_] not in check_ch :
                msg  = 'mixing both spaces and tabs for '
                msg += 'white space that indents this section.'
                sys_exit(msg, file_in, section_name)
            next_ += 1
    #
    return num_remove
# ----------------------------------------------------------------------------
# process xsrst_suspend commands
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
            msg  = 'there is a {xsrst_suspend} without a '
            msg += 'corresponding {xsrst_resume}'
            sys_exit(msg, file_in, section_name)
        if match_suspend != None :
            if match_suspend.start() < match_resume.start() :
                msg  = 'there are two {xsrst_suspend} without a '
                msg += '{xsrst_resume} between them'
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
    replace = '\n{xsrst_' + command + '}\n'
    #
    # section_data
    data_left  = section_data[ : match.start() ]
    data_right = section_data[ match.end() : ]
    section_data = data_left + replace + data_right
    #
    # file_list
    for child_file in match.group(2).split('\n') :
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
        #
        pattern_begin, pattern_end, comment_ch = \
            pattern_begin_end(file_data, child_file)
        #
        match  = pattern_begin.search(file_data)
        offset = 0
        if match is None :
            msg  = 'The file ' + child_file + '\n'
            msg += 'in the ' + command + ' command does not contain any '
            msg += 'begin commands'
            sys_exit(msg, file_in, section_name)
        #
        child_list     = list()
        found_parent = False
        while match and not found_parent:
            found_parent  = match.group(1) == 'begin_parent'
            child_name    = match.group(2)
            #
            if found_parent :
                child_list = [ child_name ]
            else :
                child_list.append( child_name )
            #
            offset  = offset + match.end()
            match   = pattern_begin.search(file_data[offset :])
        #
        section_list += child_list
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
            msg  = 'there are two spell xsrst commands'
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
    command_pattern = re.compile( r'\{[a-z]+_xsrst[^}]*\}' )
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
# remove characters on same line as {xsrst_code}
def isolate_code_command(pattern, section_data, file_in, section_name) :
    section_index  = 0
    match_begin_code = pattern['code'].search(section_data)
    while match_begin_code != None :
        language       = match_begin_code.group(1).strip()
        if language == '' :
            msg = 'missing language in first comamnd of a code block pair'
            sys_exit(msg, file_in, section_name)
        for ch in language :
            if ch < 'a' or 'z' < ch :
                msg = 'code block language character not in a-z.'
                sys_exit(msg, file_in, section_name)
        begin_start    = match_begin_code.start() + section_index
        begin_end      = match_begin_code.end()   + section_index
        section_rest   = section_data[ begin_end : ]
        match_end_code = pattern['code'].search( section_rest )
        if match_end_code == None :
            msg = 'xsrst_code start does not have a corresponding stop'
            sys_exit(msg, file_in, section_name)
        if match_end_code.group(1).strip() != '' :
            msg ='xsrst_code stop command has language argument'
            sys_exit(msg, file_in, section_name)
        end_start = match_end_code.start() + begin_end
        end_end   = match_end_code.end()   + begin_end
        #
        code_section = section_data[ begin_end : end_start + 1]
        #
        data_left   = section_data[: begin_start + 1 ]
        data_left  += '{xsrst_code ' + language + '}'
        data_left  += code_section
        data_left  += '{xsrst_code}'
        data_right  = section_data[ end_end : ]
        #
        section_data  = data_left + data_right
        section_index = len(data_left)
        match_begin_code  = pattern['code'].search(data_right)
    return section_data
# -----------------------------------------------------------------------------
# convert file command start and stop from patterns to line numbers
def convert_file_command(file_pattern, section_data, file_in, section_name) :
    assert file_pattern.groups == 2 or file_pattern.groups == 3
    section_index  = 0
    match_file     = file_pattern.search(section_data)
    while match_file != None :
        #
        # start
        start     = match_file.group(1).strip()
        if start == '' :
            msg = 'xsrst_file command: start text is empty'
            sys_exit(msg, file_in, section_name)
        #
        # stop
        stop      = match_file.group(2) .strip()
        if stop == '' :
            msg = 'xsrst_file command: stop text is empty'
            sys_exit(msg, file_in, section_name)
        #
        # file_name
        if file_pattern.groups == 2 :
            file_name = file_in
        else :
            file_name = match_file.group(3).strip()
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
            msg  = 'xsrst_file command: can not find start = '
            msg += '"' + start + '"'
            msg += '\nat beginning of a line in file_name = "'
            msg += file_name + '"'
            sys_exit(msg, file_in, section_name)
        offset     = start_index + len(start)
        if 0 <= find_at_start_of_line(offset, data, start) :
            msg  = 'xsrst_file command: found more than one '
            msg += 'start = "' + start + '"'
            msg += '\nat beginning of a line in file_name = "'
            msg += file_name + '"'
            sys_exit(msg, file_in, section_name)
        #
        # stop_index
        stop_index = find_at_start_of_line(offset, data, stop)
        if stop_index < 0 :
            msg  = 'xsrst_file command: can not find'
            msg += '\nstop = "' + stop + '"'
            msg += ' after start = "' + start + '"'
            msg += '\nin file_name = "' + file_name + '"'
            sys_exit(msg, file_in, section_name)
        offset     = stop_index + len(stop)
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
        cmd  = f'xsrst__file {file_name} {start_line} {stop_line} '
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
def add_label_and_index_for_headings(
        section_data, num_remove, file_in, section_name
) :
    punctuation      = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
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
                    assert label == section_name
                else :
                    heading = heading_list[level]
                    label += '.' + heading['text'].lower().replace(' ', '_')
            # include section link as link to first heading
            if len(heading_list) == 1 :
                index = section_name
            else :
                index = ''
            for word in heading_list[-1]['text'].lower().split() :
                if index == '' :
                    index = word
                else :
                    index += ',' + word
            #
            cmd  = '\n{xsrst_label '
            cmd += index + ' '
            cmd += label + ' }'
            #
            # place label and index entry in output before the heading
            data_left   = section_data[: candidate_start]
            data_left  += cmd
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
    sphinx_dir,
    file_in,
    section_data,
    section_info,
    child_list,
    output_dir,
    section_name,
    spell_checker,
) :
    # If file_path is relative to top git repo directory,
    # xsrst_dir2top_dir/file_path is relative to sphinx_dir/xsrst directory.
    depth   =  sphinx_dir.count('/') + 2
    top_dir =  depth * '../'
    top_dir = top_dir[:-1]
    #
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
        code_command       = line.startswith('{xsrst_code')
        file_command       = line.startswith('{xsrst__file')
        label_command      = line.startswith('{xsrst_label')
        children_command   = line.startswith('{xsrst_children')
        child_link_command = line.startswith('{xsrst_child_link')
        if label_command :
            # --------------------------------------------------------
            # label command
            line  = line.split(' ')
            index = line[1].replace(',', ', ')
            label = line[2]
            line  = '.. meta::\n'
            line += '   :keywords: ' + index + '\n\n'
            line += '.. index:: ' + index + '\n\n'
            line += '.. _' + label + ':\n\n'
            file_ptr.write(line)
            previous_empty = True
        elif code_command :
            # --------------------------------------------------------
            # code command
            inside_code = not inside_code
            if inside_code :
                assert line[-2:] == '}\n'
                language = line[ len('{xsrst_code') : -2 ].strip()
                line     = '.. code-block:: ' + language + '\n\n'
                if not previous_empty :
                    line = '\n' + line
            else :
                line = '\n'
            file_ptr.write(line)
            previous_empty = True
        elif file_command :
            line       = line.split()
            file_name  = line[1]
            start_line = line[2]
            stop_line  = line[3]
            #
            file_ptr.write('\n')
            line = f'.. literalinclude:: {top_dir}/{file_name}\n'
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
            # replace tabs with 4 spaces
            line = line.replace('\t', 4 * ' ' )
            if inside_code :
                line = 4 * ' ' + line
            #
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
    file_ptr.write( f'xsrst input file: ``{file_in}``\n')
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
    usage = 'bin/xsrst.py sphinx_dir root_file spell_file'
    sys_exit(usage)
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
output_dir = sphinx_dir + '/xsrst'
if os.path.isdir(output_dir) :
    for file_name in os.listdir(output_dir) :
        if file_name.endswith('.rst') :
            file_path = output_dir + "/" + file_name
            os.remove(file_path)
else :
    os.mkdir(output_dir)
#
# spell_checker
spell_list           = file2list(spell_file)
spell_checker        = init_spell_checker(spell_list)
code_file_extensions = get_code_file_extensions()
#
# converting over to using a single dictionary for all patterns
pattern = dict()
pattern['code'] = re.compile(
    r'\n[^\n`]*\{xsrst_code([^}]*)\}[^\n`]*'
)
#
# define some pytyon regular expression patterns
pattern_suspend_command = re.compile( r'\n[ \t]*\{xsrst_suspend\}' )
pattern_resume_command  = re.compile( r'\n[ \t]*\{xsrst_resume\}' )
pattern_end_command     = re.compile(
    r'\n[ \t]*\{xsrst_end\s+([a-z0-9_]+)\}'
)
pattern_spell_command   = re.compile(
    r'\n[ \t]*\{xsrst_spell([^}]*)\}'
)
pattern_file_command_2    = re.compile(
    r'\n[ \t]*\{xsrst_file[ \t]([^}\n]*)\n([^}\n]*)\n[ \t]*\}'
)
pattern_file_command_3    = re.compile(
    r'\n[ \t]*\{xsrst_file[ \t]([^}\n]*)\n([^}\n]*)\n([^}\n]+)\n[ \t]*\}'
)
pattern_child_command = re.compile(
    r'\n[ \t]*\{xsrst_(children|child_link)([^}]*)\}'
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
    file_in              = info['file_in']
    parent_file          = info['parent_file']
    grand_parent_section = info['parent_section']
    assert os.path.isfile(file_in)
    #
    # get xsrst docuemntation in this file
    this_file_info = file2file_info(
        section_info,
        file_in,
    )
    #
    # determine index of parent section for this file
    file_parent_section_index = None
    file_parent_section_name  = None
    for i in range( len(this_file_info) ) :
        if this_file_info[i]['is_parent'] :
            file_parent_section_index = len(section_info) + i
            file_parent_section_name  = this_file_info[i]['section_name']
    if file_parent_section_index :
        if len(this_file_info) < 2 :
            msg  = 'xsrst_begin_parent appreas in a file with only one section'
            sys_exit(msg, file_in, section_name)
    #
    # add this files sections to section_info
    for i_file in range( len(this_file_info) ) :
        # ----------------------------------------------------------------
        # section_name, section_data
        section_name = this_file_info[i_file]['section_name']
        section_data = this_file_info[i_file]['section_data']
        is_parent    = this_file_info[i_file]['is_parent']
        if is_parent :
            parent_section = grand_parent_section
        elif file_parent_section_index is not None :
            parent_section = file_parent_section_index
        else :
            parent_section = grand_parent_section
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
        # ---------------------------------------------------------------
        # num_remove, indent_ch
        num_remove = indent_to_remove(
            section_data,
            file_in,
            section_name
        )
        # ----------------------------------------------------------------
        # process spell commands
        section_data = spell_command(
            pattern_spell_command,
            section_data,
            file_in,
            section_name,
        )
        # ----------------------------------------------------------------
        # remove characters on same line as {xsrst_code}
        section_data = isolate_code_command(
            pattern,
            section_data,
            file_in,
            section_name,
        )
        # ---------------------------------------------------------------
        # file command: convert start and stop to line numbers
        section_data = convert_file_command(
            pattern_file_command_2,
            section_data,
            file_in,
            section_name,
        )
        section_data = convert_file_command(
            pattern_file_command_3,
            section_data,
            file_in,
            section_name,
        )
        index = find_at_start_of_line(0, section_data, '{xsrst_file')
        if 0 <= index :
            eol  = section_data.find('\n', index)
            line = section_data[index : eol]
            assert 0 < eol
            msg  = 'syntax error in xsrst_file command in line\n'
            msg += line
            sys_exit(msg, file_in, section_name)
        # ---------------------------------------------------------------
        # add labels corresponding to headings
        section_data = add_label_and_index_for_headings(
            section_data,
            num_remove,
            file_in,
            section_name
        )
        # ----------------------------------------------------------------
        # child_list
        # first section in each file may need to add to child list
        child_list = list()
        if is_parent :
            for i in range( len(this_file_info) ) :
                if i != i_file :
                    child_list.append(  this_file_info[i]['section_name'] )
        child_list = child_list + child_section
        # ---------------------------------------------------------------
        # write file for this section
        write_file(
            sphinx_dir,
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
pattern  = r'\n[ \t]*xsrst/'
pattern += section_name.replace('.', '[.]')
match_line = re.search(pattern, file_data)
if match_line == None :
    msg  = 'The first section in the root_file is ' + section_name + '\n'
    msg += 'The following line:\n'
    msg += '    xsrst/' + section_name + '\n'
    msg += 'is missing from the toctree command in\n'
    msg += index_file
    sys_exit(msg)
#
print('xsrst.py: OK')
sys.exit(0)
