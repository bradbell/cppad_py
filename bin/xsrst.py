#! /usr/bin/env python3
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
    underbars
    conf
    toctree
    stackoverflow
    pyspellchecker
    cmd
    cppad
    dir
    \chapter
    \paragraph
}

.. include:: ../preamble.rst

Extract Sphinx RST
##################


.. The indentation examples are included by the child_cmd section.

{xsrst_children
    sphinx/test_in/heading.py
    sphinx/configure.xsrst
}

Syntax
******
-   ``xsrst.py`` *target* *root_file* *sphinx_dir* *spelling* *keyword*
-   ``xsrst.py`` *target* *root_file* *sphinx_dir* *spelling* *keyword*
    *line_increment*

Purpose
*******
This is a pseudo sphinx extension that provides the following features:

#.  The file name for each section is also an abbreviated title used
    in the navigation bar and for linking to the section. This makes the
    navigation bar more useful while also having long descriptive titles.
    It also makes cross reference linking from other sections easier.
#.  Enables documentation in the comments for source code
    even when multiple computer languages are used for one package.
    Allows the documentation for one section to span multiple locations
    in the source code; see :ref:`suspend command<suspend_cmd>`.
#.  Allows for multiple sections (rst output files) to be specified by one
    input file. In addition, one section can be the parent for the
    other sections in a file.
#.  Generates the table of contents from the specification
    of which files are included; see :ref:`child commands<child_cmd>`.
    Generates a jump table to the headings for each section
    so that the navigation bar need not include this information.
#.  Includes a configurable :ref:`spell checker<spell_cmd>` and
    :ref:`index<genindex>`.
    Words in each heading are automatically included in the index.
#.  Makes it easy to include source code, that also executes, from
    directly below the :ref:`code command<code_cmd>` or from
    a different location in a :ref:`file<file_cmd>`.
    Uses tokens in the source, not line numbers in the source,
    to signify start and stop of inclusion from a file.

Requirements
************
-   ``pip install --user pyspellchecker``
-   ``pip install --user sphinx``
-   The directory *cppad_prefix* ``/bin`` must be in your execution path
    where *cppad_prefix* is the install prefix for cppad.

Notation
********

White Space
===========
We define white space to be a sequence of space characters; e.g.,
tabs are not consider white space by xsrst.

Beginning of a Line
===================
We say that a string *text* is a the beginning of a line if
only white space, or nothing, comes before *text* in the line.

Command Line Arguments
**********************

target
======
The command line argument *target* must be ``html`` or ``pdf`` and
specifies the type of type output you plan to generate using sphinx.
If *target* is ``html`` you can generate the sphinx output using
the following command in the *sphinx_dir* directory:
{xsrst_code sh}
    make html
{xsrst_code}
If *target* is ``pdf``, you can use the following commands:
{xsrst_code sh}
    sed -i preamble.rst -e '/BEGIN_LATEX_MACROS/,/END_LATEX_MACROS/d'
    sphinx-build -b latex . _build/latex
    git checkout preamble.rst
    cd _build/latex
    sed -i cppad_py.tex -e 's|\\chapter{|\\paragraph{|'
    make cppad_py.pdf
{xsrst_code}

root_file
=========
The command line argument *root_file* is the name of a file,
relative to the top git repository directory.

root_section
------------
If there is only one section in the *root_file* it is called
the *root_section*; i.e., it is the top section in that table of contents.
If there is more than one section in the *root_file*,
the file must have a
:ref:`begin_cmd.parent_section` and it is the *root_section*.
The file *sphinx_dir* :code:`/index.rst` must contain the line

|tab| ``xsrst/`` *section_name*

where *section_name* is the name of the *root_section*.

sphinx_dir
==========
The command line argument *sphinx_dir* is a sub-directory,
of the top git repository directory.
The  sphinx ``conf.py``, ``index.rst``, *spelling*, and *keyword*
files are located in this directory.
Any files that have names ending in ``.rst``,
and that are in the directory *sphinx_dir* :code:`/xsrst`,
are removed at the beginning of execution of ``xsrst.py``.
All the ``.rst`` files in *sphinx_dir* :code:`/xsrst`
were extracted from the source code the last time that ``xsrst.py``
was executed.

Example Configuration Files
---------------------------

| |tab| conf.py: :ref:`conf_py`
| |tab| index.rst: :ref:`index_rst`
| |tab| keyword: :ref:`keyword`
| |tab| spelling: :ref:`spelling`


spelling
========
The command line argument *spelling* is the name of a file,
relative to the *sphinx_dir* directory.
This file contains a list of words
that the spell checker will consider correct for all sections
(it can be an empty file).
A line that begins with :code:`#` is a comment (not included in the list).
The words are one per line and
leading and trailing white space in a word are ignored.
Special words, for a particular section, are specified using the
:ref:`spell command<spell_cmd>`.

keyword
=======
The command line argument *keyword* is the name of a file,
relative to the *sphinx_dir* directory.
This file contains a list of python regular expressions for heading tokens
that should not be included in the index (it can be an empty file).
A heading token is any sequence of non space or new line characters
with upper case letters converted to lower case.
For example, a heading might contain the token ``The`` but you
might not want to include ``the`` as a entry in the :ref:`genindex`.
In this case you could have a line containing just ``the`` in *keyword*.
For another example, you might want to exclude all tokens that are numbers.
In this case you could have a line containing just ``[0-9]*`` in *keyword*.
The regular expressions are one per line and
leading and trailing spaces are ignored.
A line that begins with :code:`#` is a comment
(not included in the list of python regular expressions).

line_increment
==============
This optional argument helps find the source of errors reported by sphinx.
If the argument *line_increment* is present,
a table is generated at the end of each output file.
This table maps line numbers in the output file to
line numbers in the corresponding xsrst input file.
The argument *line_increment* is a positive integer specifying the minimum
difference between xsrst input line numbers for entries in the table.
The value ``1`` will give the maximum resolution.
For example, the sphinx warning

| |tab| ... ``/xsrst/children_exam.rst:30: WARNING:`` ...

corresponds to line number 30 in the file ``children_exam.rst``.
The table at the bottom of that file maps line numbers in
``children_exam.rst`` to line numbers in the corresponding xsrst input file.

Table Of Contents
*****************

toctree
=======
The sphinx ``toctree`` directives are automatically generated
for sections. The only such directive you should directly edit
is in the file *sphinx_dir* :code:`/index.rst`.
One entry in this file specifies the
:ref:`root_section<xsrst_py.command_line_arguments.root_file.root_section>`.
Other entries are for ``.rst`` files that are not extracted by
``xsrst.py``.

Parent Section
==============
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
*************
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
=============
Each :ref:`section<begin_cmd.section>` can have only one header at
the first level which is a title for the section.
The :ref:`section_name<begin_cmd.section_name>`
is automatically used
as a label for linking the title for a section; i.e., the
following will link to the title for *section_name*:

|tab| ``:ref:``  ` *linking_text* :code:`<` *section_name* :code:`>` `

where *linking_text* is the text the user sees.

Other Levels
============
The label for linking a heading that is not at the first level
is the label for the heading directly above it plus a dot character :code:`.`,
plus a lower case version of the heading with spaces converted to
underbars :code:`_`. For example, the label for the heading for this
paragraph is

|tab| ``xsrst_py.headers_and_links.other_levels``.

This may seem verbose, but it helps keep the links up to date.
If a heading changes, all the links to that heading will break.
This identifies the links that should be checked
to make sure they are still valid.

Children
========
If a xsrst input file has a
:ref:`parent section<xsrst_py.table_of_contents.parent_section>`
the other sections in the file are children of the parent.

- If a section has a :ref:`child link or list command<child_cmd>`
  links to all the children of the section are placed where the
  child link command is located.
- If a section has a :ref:`children command<child_cmd>`
  no automatic links to the children of the current section are generated.
- Otherwise, the links to the children of a section are placed
  at the end of the section.

You can place a heading directly before the links to make them easier to find.

Example
=======
:ref:`heading_exam`

Indentation
***********
If there are a number of spaces before
all of the xsrst documentation for a section,
those characters are not included in the xsrst output.
This enables one to indent the
xsrst so it is grouped with the proper code block in the source.
An error message will result if
you use tabs in the indentation.

Example
=======
- :ref:`indent_exam`

Wish List
*********
The following is a wish list for future improvements to ``xsrst.py``:

.. _stackoverflow: https://stackoverflow.com/questions/1686837/
   sphinx-documentation-tool-set-tab-width-in-output

Tabs
====
Tabs in a code blocks get expanded to 8 spaces; see stackoverflow_.
It would be nice to have a way to control the size of tabs in the code blocks
displayed by :ref:`code_cmd` and :ref:`file_cmd`.
Perhaps it would be good to support tabs as a method for
indenting xsrst input sections.

Module
======
Convert the program into a python module and provide a pip distribution for it.
It would at least be nice for cppad_py to install the ``xsrst.py`` program
so that users would not have to copy it to a directory in
their execution path.


.. All the children of this section are commands except for heading_exam.

Commands
********
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
    dir
}

.. include:: ../preamble.rst

Begin and End Commands
######################

Syntax
******
- ``{xsrst_begin``        *section_name* :code:`}`
- ``{xsrst_begin_parent`` *section_name* :code:`}`
- ``{xsrst_end``          *section_name* :code:`}`

Section
*******
The start (end) of a section of the input file is indicated by a
begin (end) command at the
:ref:`beginning of a line<xsrst_py.notation.beginning_of_a_line>`.

section_name
************
The *section_name* is a non-empty sequence of the following characters:
a-z, 0-9, and underbar ``_``.
It can not begin with the characters ``xsrst_``.
A link is included in the index under the section name
to the first heading the section.
The section name is also added to the html keyword meta data.


Output File
***********
The output file corresponding to *section_name* is

|tab| :ref:`sphinx_dir<xsrst_py.command_line_arguments.sphinx_dir>`
``/xsrst/`` *section_name* ``.rst``

Parent Section
**************
There can be at most one begin parent command in an input file.
In this case there must be other sections in the file
and they are children of the parent section.
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

Children Commands
#################

Syntax
******

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
|
| ``{xsrst_child_list``
|   *file_1*
|   ...
|   *file_n*
| :code:`}`


Purpose
*******
A section can specify a set of files for which the
:ref:`parent section<begin_cmd.parent_section>` of each file
is a child of the current section.
(If there is not parent section in a file,
all the sections in the file are children of the current section.)
This is done using the commands above at the
:ref:`beginning of a line<xsrst_py.notation.beginning_of_a_line>`.

File Names
**********
A new line character must precede and follow each
of the file names *file_1* ... *file_n*.
Leading and trailing white space is not included in the names
The file names are  relative to the directory where ``xsrst.py``
is executed; i.e., the top directory for this git repository.
This may seem verbose, but it makes it easier to write scripts
that move files and automatically change references to them.

Links
*****
The child link and list commands also place
links to all the children of the current at the location of the command.
The links are displayed using the title for each section.
The child list command includes the section name next to the title.
You can place a heading directly before the links to make them easier to find.

Example
*******
{xsrst_child_list
   sphinx/test_in/no_parent.xsrst
}

{xsrst_end child_cmd}
"""
# ---------------------------------------------------------------------------
"""
{xsrst_begin spell_cmd}

Spell Command
#############

Syntax
******
``{xsrst_spell`` *word_1* ...  *word_n* :code:`}`

Here *word_1*, ..., *word_n* is the special list of words for this section.
In the syntax above the list of words is all in one line,
but they could be on different lines.
Each word starts with an upper case letter,
a lower case letter, or a back slash.
The back slash is included as a possible beginning of a word
so that latex commands can be included in the spelling list.
The rest of the characters in a word are lower case letters.


Purpose
*******
You can specify a special list of words
(not normally considered correct spelling)
for the current section using the command above at the
:ref:`beginning of a line<xsrst_py.notation.beginning_of_a_line>`.

spelling
********
The list of words in
:ref:`spelling<xsrst_py.command_line_arguments.spelling>`
are considered correct spellings for all sections.
The latex commands corresponding to the letters in the greek alphabet
are automatically added to this list.


Capital Letters
***************
The case of the first letter does not matter when checking spelling;
e.g., if ``abcd`` is *word_1* then ``Abcd`` will be considered a valid word.
Each capital letter starts a new word; e.g., `CamelCase` is considered to
be the two words 'camel' and 'case'.
Single letter words are always correct and not included in the
special word list; e.g., the word list entry ``CppAD`` is the same as ``Cpp``.

Double Words
************
It is considered an error to have only white space between two occurrences
of the same word. You can make an exception for this by entering
the same word twice (next to each other) in the special word list.

Example
*******
{xsrst_child_link
   sphinx/test_in/spell.py
}

{xsrst_end spell_cmd}
"""
# ---------------------------------------------------------------------------
"""
{xsrst_begin suspend_cmd}

Suspend and Resume Commands
###########################

Syntax
******
- ``{xsrst_suspend}``
- ``{xsrst_resume}``

Purpose
*******
It is possible to suspend (resume) the xsrst extraction during a section.
One begins (ends) the suspension with a suspend command (resume command)
at the
:ref:`beginning of a line<xsrst_py.notation.beginning_of_a_line>`.
Note that this will also suspend all other xsrst processing; e.g.,
spell checking.

Example
*******
{xsrst_child_link
   sphinx/test_in/suspend.py
}

{xsrst_end suspend_cmd}
"""
# ---------------------------------------------------------------------------
"""
{xsrst_begin code_cmd}

Code Command
############

Syntax
******
- ``{xsrst_code`` *language* :code:`}`
- ``{xsrst_code}``

Purpose
*******
A code block, directly below in the current input file, begins with
a line containing the first version ( *language* included version)
of the command above.

Requirements
************
Each code command ends with
a line containing the second version of the command; i.e., ``{xsrst_code}``.
Hence there must be an even number of code commands.
The back quote character \` can't be in the same line as the commands.

language
********
A *language* is a non-empty sequence of non-space the characters.
It is used to determine the source code language
for highlighting the code block.

Rest of Line
************
Other characters on the same line as a code command
are not included in the xsrst output.
This enables one to begin or end a comment block
without having the comment characters in the xsrst output.

Spell Checking
**************
Code blocks as usually small and
spell checking is done for these code blocks.
(Spell checking is not done for code blocks included using the
:ref:`file command<file_cmd>` .)

Example
*******
{xsrst_child_link
   sphinx/test_in/code.py
}

{xsrst_end code_cmd}
"""
# ---------------------------------------------------------------------------
"""
{xsrst_begin file_cmd}

.. include:: ../preamble.rst

File Command
############

Syntax
******

| ``{xsrst_file``
| |tab| *start*
| |tab| *stop*
| :code:`}`
|
| ``{xsrst_file``
| |tab| *start*
| |tab| *stop*
| |tab| *file_name*
| :code:`}`

Purpose
*******
A code block, from any where in any file,
is included by the command above at the
:ref:`beginning of a line<xsrst_py.notation.beginning_of_a_line>`.

White Space
***********
Leading and trailing white space is not included in
*start*, *stop* or *file_name*.
The new line character separates these tokens.

file_name
*********
If *file_name* is not in the syntax,
the code block is in the current input file.
Otherwise, the code block is in *file_name*.
This file name is relative to the directory where ``xsrst.py``
is executed; i.e., the top directory for this git repository.
This may seem verbose, but it makes it easier to write scripts
that move files and automatically change references to them.

start
*****
The code block starts with the line following the occurence
of the text *start* in *file_name*.
If this is the same as the file containing the command,
the text *start* will not match any text in the command.
There must be one and only one occurence of *start* in *file_name*,
not counting the command itself when the files are the same.

stop
****
The code block ends with the line before the occurence
of the text *start* in *file_name*.
If this is the same as the file containing the command,
the text *stop* will not match any text in the command.
There must be one and only one occurence of *stop* in *file_name*,
not counting the command itself when the files are the same.

Spell Checking
**************
Spell checking is **not** done for these code blocks.


Example
*******
{xsrst_child_link
   sphinx/test_in/file.cpp
}

{xsrst_end file_cmd}
"""
# ----------------------------------------------------------------------------
"""
{xsrst_begin comment_ch_cmd}

Comment Character Command
#########################

Syntax
******
``{xsrst_comment_ch`` *ch* :code:`}`

Purpose
*******
Some languages have a special character that
indicates the rest of the line is a comment.
If you embed sphinx documentation in this type of comment,
you need to inform xsrst of the special character so it does
not end up in your ``.rst`` output file.

ch
--
The value of *ch* must be one non white space character.
There must be at least one white space character
between ``xsrst_comment_ch`` and *ch*.
Leading and trailing white space around *ch* is ignored.
There can be only one occurence of this command within a file,
it's effect lasts for the entire file, and
it must come before the first :ref:`begin_cmd` in the file.


Beginning of a Line
*******************
A sequence of characters *text* is at the beginning of a line if there
are only space characters
between the previous new line character and *text*.
In addition, the special character *ch* can be the first character
after the new line and before *text*.

Input Stream
************
The special character (and one space if present directly after)
is removed from the input stream before any xsrst processing; e.g.,
calculating the amount of
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
*******
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
def replace_section_number(file_data, section_number) :
    pattern   = '\n{xsrst_section_number}'
    if section_number == '' :
        # This is the root section
        return file_data.replace(pattern,'')
    #
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    # start of section_number command
    start_cmd = file_data.find(pattern)
    assert 0 <= start_cmd
    # first character after command
    ch  = file_data[start_cmd + len(pattern)]
    assert ch == '\n'
    # second and third newline after command
    second_index = file_data.index('\n', start_cmd + len(pattern) + 1)
    third_index  = file_data.index('\n', second_index + 1)
    # first and second line after comman
    first_line   = file_data[start_cmd + len(pattern) + 1 : second_index ]
    second_line  = file_data[ second_index + 1 : third_index ]
    # check for overline
    overline = False
    if first_line[0] * len(first_line) == first_line :
        if first_line[0] in punctuation :
            overline = True
    if not overline :
        assert second_line[0] in punctuation
        first_line   = section_number + ' ' + first_line
        second_line += second_line[0] * ( len(section_number) + 1 )
        data  = file_data[: start_cmd] + '\n'
        data += first_line + '\n'
        data += second_line + '\n'
        data += file_data[third_index :]
    else :
        # fourth newline after command
            fourth_index = file_data.index('\n', third_index + 1)
            third_line   = file_data[third_index + 1 : fourth_index]
            assert first_line == third_line
            first_line += first_line[0] * ( len(section_number) + 1 )
            third_line  = first_line
            second_line = section_number + ' ' + second_line
    data  = file_data[: start_cmd] + '\n'
    data += first_line + '\n'
    data += second_line + '\n'
    if not overline :
        data += file_data[third_index :]
    else :
        data += third_line
        data += file_data[fourth_index:]
    #
    return data
    #
# ---------------------------------------------------------------------------
# create table of contents and replace '{xsrst_section_number}' commands
# in *.rst files.
def table_of_contents(target, section_info, level, count, section_index) :
    assert level >= 1
    assert len(count) == level-1
    #
    section_name = section_info[section_index]['section_name']
    if level == 1 :
        assert section_index == 0
        content  = '\n'
        content += 'Table of Contents\n'
        content += '*****************\n'
        content += ':ref:`' + section_name + '`\n\n'
        section_number = ''
    else :
        assert section_index != 0
        content  = '| '
        assert level > 1
        for i in range(level - 2 ) :
            content += ' |space| '
        section_number = ''
        for i in range(level - 1) :
            section_number += str(count[i])
            if i + 1 < level - 1 :
                section_number += '.'
        content  += ' :ref:`'
        content  += section_name + '`\n'
    # --------------------------------------------------------------------
    # replace {xsrst_section_number} in output_dir/section_name.rst
    file_name = output_dir + '/' + section_name + '.rst'
    file_ptr  = open(file_name, 'r')
    file_data = file_ptr.read()
    file_ptr.close()
    if target == 'pdf' :
        file_data = replace_section_number(file_data, section_number)
    else :
        file_data = replace_section_number(file_data, '')
    file_ptr  = open(file_name, 'w')
    file_ptr.write(file_data)
    file_ptr.close()
    #
    child_count   = count + [0]
    child_content = ''
    for child_index in range( len( section_info ) ) :
        if section_info[child_index]['parent_section'] == section_index :
            child_count[-1] += 1
            child_content += table_of_contents(
                target, section_info, level + 1, child_count, child_index
            )
    #
    # if the number of children greater than one, put a blank line before
    # and after the child table of contents
    number_children = child_count[-1]
    if 1 < number_children :
        if not child_content.startswith('|\n') :
            child_content = '|\n' + child_content
        if not child_content.endswith('|\n') :
            child_content = child_content + '|\n'
    #
    return content + child_content
# ---------------------------------------------------------------------------
def newline_indices(data) :
    pattern_newline  = re.compile( r'\n')
    newline_itr      = pattern_newline.finditer(data)
    newline_list     = list()
    for itr in newline_itr :
        newlist = itr.start()
        newline_list.append( newlist )
    return newline_list
# ---------------------------------------------------------------------------
def add_line_numbers(data) :
    newline_list = newline_indices(data)
    result       = ""
    previous     = 0
    for i in range( len(newline_list) ) :
        current = newline_list[i]
        line    = data[previous : current]
        if previous == current :
            assert i == 0
        elif line[-1] != '\n' :
            line += '{xsrst_line ' + str(i + 1) + '@'
        result  += line
        previous = current
    #
    assert previous == len(data) - 1
    result += '\n'
    return result
# ---------------------------------------------------------------------------
def remove_line_numbers(pattern, data_in) :
    match     = pattern['line'].search(data_in)
    offset_in = 0
    line_out  = 1
    data_out  = ''
    line_pair = list()
    while match :
        start      = offset_in + match.start()
        end        = offset_in + match.end()
        before     = data_in[offset_in : start]
        line_xsrst = match.group(1)
        line_out  += before.count('\n')
        #
        line_pair.append( ( line_out, int(line_xsrst) ) )
        data_out += before
        #
        offset_in   = end
        match       = pattern['line'].search(data_in[end :])
    data_out += data_in[offset_in :]
    return data_out, line_pair
# ---------------------------------------------------------------------------
def init_spell_checker(spell_list) :
    remove_from_dictionary = [
        'af',
        'anl',
        'ap',
        'av',
        'bv',
        'dv',
        'cg',
        'cpp',
        'dep',
        'dir',
        'exp',
        'gcc',
        'hes',
        'hess',
        'ind',
        'jac',
        'len',
        'mcs',
        'nr',
        'nc',
        'nd',
        'op',
        'prt',
        'ptr',
        'rel',
        'rc',
        'sim',
        'std',
        'thier',
        'var',
        'vec',
        'yi',
        'xp',
    ]
    add_to_dictionary = [
        'aborts',
        'covariate',
        'covariates',
        'debug',
        'exponentiation',
        'identifiability',
        'initialize',
        'initialized',
        'jacobian',
        'jacobians',
        'hessians',
        'initialization',
        'invertible',
        'likelihoods',
        'messaging',
        'modeled',
        'modeling',
        'optimizes',
        'partials',
        'piecewise',
        'unary',
        'unicode',
        'wikipedia',
        'wiki',
        #
        # greek letter latex commands
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
        r'\lambda',
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
    spell_checker.word_frequency.remove_words(remove_from_dictionary)
    spell_checker.word_frequency.load_words(add_to_dictionary)
    spell_checker.word_frequency.load_words(spell_list)
    #
    return spell_checker
# ---------------------------------------------------------------------------
def find_text_line(data, text, exclude=None) :
    assert len(text) > 0
    result = list()
    #
    if exclude == None :
        exclude = (0, 0)
    #
    index = data.find(text)
    while 0 <= index :
        line_number = data[: index].count('\n') + 1
        if line_number < exclude[0] or exclude[1] < line_number :
            result.append( line_number )
        index = data.find(text, index + len(text))
    return result
# ---------------------------------------------------------------------------
# add file name, section name, and program name to system exit call
def sys_exit(msg, fname=None, sname=None, match=None, data=None, line=None) :
    extra = ''
    if sname :
        extra += 'section = ' + sname
    if fname :
        if extra != '' :
            extra += ', '
        extra += 'file = ' + fname
    if match :
        assert fname != None
        assert data != None
        assert line == None
        match_line  = pattern['line'].search( data[match.start() :] )
        assert match_line
        line = match_line.group(1)
    if line != None :
        if extra != '' :
            extra += ', '
        extra += 'line = ' + str(line)
    if extra != '' :
        msg += '\n' + extra
    sys.exit('\n' + msg)
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
        match      = pattern_comment_ch.search(data_rest)
        if match :
            msg = 'There are multiple command_ch commands in this file'
            # This error is detected during a child command and file_data
            # does not have line numbers in it
            sys_exit(msg, fname=file_in)
        if comment_ch == ']' :
            msg  = 'Cannot use "]" as the speical comment charater\n'
            msg += 'in a comment_ch command.'
            sys_exit(msg, fname=file_in)
    #
    # pattern_begin
    ch = comment_ch
    if ch :
        pattern_begin = re.compile(
        r'(^|\n)[' + ch +
            r']?[ \t]*\{xsrst_(begin|begin_parent)\s+([a-z0-9_]*)\}'
        )
    else :
        pattern_begin = re.compile(
            r'(^|\n)[ \t]*\{xsrst_(begin|begin_parent)\s+([a-z0-9_]*)\}'
        )
    #
    # pattern_end
    if ch :
        pattern_end = re.compile(
            r'\n[' + ch + r']?[ \t]*\{xsrst_end\s+([a-z0-9_]*)\}'
        )
    else :
        pattern_end = re.compile(
            r'\n[ \t]*\{xsrst_end\s+([a-z0-9_]*)\}'
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
    file_data = add_line_numbers(file_data)
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
                sys_exit(msg, fname=file_in)
            file_index = len(file_data)
        else :
            # section_name
            section_name = match_xsrst_begin.group(3)
            is_parent    = match_xsrst_begin.group(2) == 'begin_parent'
            if section_name == '' :
                msg  = 'section_name after xsrst_begin is empty'
                sys_exit(msg,
                    fname=file_in, match=match_xsrst_begin, data=data_rest
                )
            if section_name.startswith('xsrst_') :
                # section name xsrst_py is used to document this program
                if section_name != 'xsrst_py' :
                    msg = 'section_name cannot start with xsrst_'
                    sys_exit(msg,
                        fname=file_in, match=match_xsrst_begin, data=data_rest
                    )
            #
            begin_index = file_index + match_xsrst_begin.start()
            if begin_index < comment_ch_index :
                msg = 'A begin command comes before the comment_ch command'
                sys_exit(msg,
                    fname=file_in,
                    sname=section_name,
                    match=match_xsrst_begin,
                    data=data_rest,
                )
            #
            # check if section appears multiple times
            for info in file_info :
                if section_name == info['section_name'] :
                    msg  = 'xsrst_begin: section appears multiple times'
                    sys_exit(msg,
                        fname=file_in,
                        sname=section_name,
                        match=match_xsrst_begin,
                        data=data_rest
                    )
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
                        msg += ' appears twice in same file'
                        sys_exit(msg,
                            fname=file_in,
                            sname=section_name,
                            match=match_xsrst_begin,
                            data=data_rest
                        )
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
                sys_exit(msg, fname=file_in, sname=section_name)
            if match_xsrst_end.group(1) != section_name :
                msg = 'begin and end section names do not match\n'
                msg += 'begin name = ' + section_name + '\n'
                msg += 'end name   = ' + match_xsrst_end.group(1)
                sys_exit(msg,
                    fname=file_in,
                    match=match_xsrst_end,
                    data=data_rest
                )
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
    newline_list = newline_indices(section_data)
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
                sys_exit(msg, fname=file_in, sname=section_name)
            next_ += 1
    #
    return num_remove
# ----------------------------------------------------------------------------
# process xsrst_suspend commands
def suspend_command(
    pattern, section_data, file_in, section_name
) :
    match_suspend = pattern['suspend'].search(section_data)
    while match_suspend != None :
        suspend_start = match_suspend.start()
        suspend_end   = match_suspend.end()
        section_rest  = section_data[ suspend_end : ]
        match_resume  = pattern['resume'].search(section_rest)
        if match_resume == None :
            msg  = 'there is a {xsrst_suspend} without a '
            msg += 'corresponding {xsrst_resume}'
            sys_exit(msg,
                fname=file_in,
                sname=section_name,
                match=match_suspend,
                data=section_data
            )
        match_suspend = pattern['suspend'].search(section_rest)
        if match_suspend != None :
            if match_suspend.start() < match_resume.start() :
                msg  = 'there are two {xsrst_suspend} without a '
                msg += '{xsrst_resume} between them'
                sys_exit(msg,
                    fname=file_in,
                    sname=section_name,
                    match=match_suspend,
                    data=section_rest
                )
        resume_end   = match_resume.end() + suspend_end
        section_rest = section_data[ resume_end :]
        section_data = section_data[: suspend_start] + section_rest
        #
        # redo match_suppend so relative to new section_data
        match_suspend = pattern['suspend'].search(section_data)
    return section_data
# -----------------------------------------------------------------------------
# process child commands
def child_commands(
    pattern,
    section_data,
    file_in,
    section_name,
) :
    file_list    = list()
    file_line    = list()
    section_list = list()
    match        = pattern['child'].search(section_data)
    if match is None :
        return section_data, file_list, section_list
    match_tmp    = pattern['child'].search(section_data[match.end() :] )
    if match_tmp is not None :
        msg = 'More than one children or child_link command in a section.'
        sys_exit(msg,
            fname=file_in,
            sname=section_name,
            match=match_tmp,
            data=section_data[match.end():]
        )
    #
    assert match.group(1) in [ 'children', 'child_link', 'child_list']
    command = match.group(1)
    replace = '\n{xsrst_' + command + '}\n'
    #
    # section_data
    data_left  = section_data[ : match.start() ]
    data_right = section_data[ match.end() : ]
    section_data = data_left + replace + data_right
    #
    # file_list, file_line
    for child_pair in match.group(2).split('\n') :
        match_line = pattern['line'].search(child_pair)
        if match_line :
            line_number = match_line.group(1)
        child_file  = pattern['line'].sub('', child_pair).strip()
        if child_file != '' :
            assert match_line
            file_list.append(child_file)
            file_line.append(line_number)
    #
    # section_list
    for i in range( len(file_list) ) :
        child_file = file_list[i]
        child_line = file_line[i]
        if not os.path.isfile(child_file) :
            msg  = 'The file ' + child_file + '\n'
            msg += 'in the ' + command + ' command does not exist'
            sys_exit(msg,
                fname=file_in, sname=section_name, line=child_line
            )
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
            sys_exit(msg,
                fname=file_in, sname=section_name, line=child_line
            )
        #
        list_children     = list()
        found_parent = False
        while match and not found_parent:
            found_parent  = match.group(2) == 'begin_parent'
            child_name    = match.group(3)
            #
            if found_parent :
                list_children = [ child_name ]
            else :
                list_children.append( child_name )
            #
            offset  = offset + match.end()
            match   = pattern_begin.search(file_data[offset :])
        #
        section_list += list_children
    #
    return section_data, file_list, section_list
# -----------------------------------------------------------------------------
# process spell command
def spell_command(
    pattern, section_data, file_in, section_name, spell_checker
) :
    match_spell   = pattern['spell'].search(section_data)
    special_used  = dict()
    double_used   = dict()
    if match_spell != None :
        section_rest   = section_data[ match_spell.end() : ]
        match_another  = pattern['spell'].search(section_rest)
        if match_another :
            msg  = 'there are two spell xsrst commands'
            sys_exit(msg, fname=file_in, sname=section_name)
        previous_word = ''
        spell_arg = match_spell.group(1)
        spell_arg = pattern['line'].sub('', spell_arg)
        for itr in pattern['word'].finditer( spell_arg ) :
            word_lower = itr.group(0).lower()
            if len(word_lower) > 1 :
                special_used[ word_lower ] = False
                if word_lower == previous_word :
                    double_used[ word_lower ] = False
            previous_word = word_lower
        #
        # remove spell command
        start        = match_spell.start()
        end          = match_spell.end()
        section_data = section_data[: start] + section_data[end :]
    #
    # version of section_data with certain commands removed
    section_tmp = section_data
    #
    # commands with file names as arugments
    section_tmp = pattern['file_2'].sub('', section_tmp)
    section_tmp = pattern['file_3'].sub('', section_tmp)
    section_tmp = pattern['child'].sub('', section_tmp)
    #
    # command with section names and headings as arguments
    section_tmp = pattern['ref_1'].sub('', section_tmp)
    section_tmp = pattern['ref_2'].sub(r'\1', section_tmp)
    section_tmp = pattern['code'].sub('', section_tmp)
    #
    # commands with external urls as arguments
    section_tmp = pattern['url_1'].sub('', section_tmp)
    section_tmp = pattern['url_2'].sub(r'\1', section_tmp)
    #
    # check for spelling errors
    first_spell_error = True
    for itr in pattern['word'].finditer( section_tmp ) :
        word = itr.group(0)
        if len( spell_checker.unknown( [word] ) ) > 0 :
            word_lower = word.lower()
            if not word_lower in special_used :
                if first_spell_error :
                    msg  = '\nwarning: file = ' + file_in
                    msg += ', section = ' + section_name
                    print(msg)
                    first_spell_error = False
                # line_number
                offset = itr.start()
                match  = pattern['line'].search(section_tmp[offset :] )
                assert match
                line_number = match.group(1)
                #
                # msg
                msg  = 'spelling = ' + word
                suggest = spell_checker.correction(word)
                if suggest != word :
                    msg += ', suggest = ' + suggest
                msg += ', line ' + line_number
                #
                print(msg)
            special_used[word_lower] = True
    #
    # check for double word errors
    for itr in pattern['double_word'].finditer(section_data) :
        word_lower = itr.group(1).lower()
        if not word_lower in double_used :
            if first_spell_error :
                msg  = 'warning: file = ' + file_in
                msg += ', section = ' + section_name
                print(msg)
                first_spell_error = False
            double_word = itr.group(0).strip()
            msg         = 'double word error: "' + double_word + '"'
            print(msg)
        double_used[word_lower]  = True
        special_used[word_lower] = True
    #
    # check for words that were not used
    for word_lower in special_used :
        if not special_used[word_lower] :
            if first_spell_error :
                msg  = '\nwarning: file = ' + file_in
                msg += ', section = ' + section_name
                print(msg)
                first_spell_error = False
            msg = 'spelling word "' + word_lower + '" not needed'
            print(msg)
    for word_lower in double_used :
        if not double_used[word_lower] :
            if first_spell_error :
                msg  = '\nwarning: file = ' + file_in
                msg += ', section = ' + section_name
                print(msg)
                first_spell_error = False
            msg  = 'double word "' + word_lower + ' ' + word_lower
            msg += '" not needed'
            print(msg)
    #
    return section_data
# -----------------------------------------------------------------------------
# remove characters on same line as {xsrst_code}
def isolate_code_command(pattern, section_data, file_in, section_name) :
    section_index    = 0
    data_right       = section_data
    match_begin_code = pattern['code'].search(section_data)
    while match_begin_code != None :
        language       = match_begin_code.group(1).strip()
        if language == '' :
            msg = 'missing language in first command of a code block pair'
            sys_exit(msg,
                fname=file_in,
                sname=section_name,
                match=match_begin_code,
                data=data_right
            )
        for ch in language :
            if ch < 'a' or 'z' < ch :
                msg = 'code block language character not in a-z.'
                sys_exit(msg,
                    fname=file_in,
                    sname=section_name,
                    match=match_begin_code,
                    data=data_right
                )
        begin_start    = match_begin_code.start() + section_index
        begin_end      = match_begin_code.end()   + section_index
        section_rest   = section_data[ begin_end : ]
        match_end_code = pattern['code'].search( section_rest )
        if match_end_code == None :
            msg = 'xsrst_code start does not have a corresponding stop'
            sys_exit(msg,
                fname=file_in,
                sname=section_name,
                match=match_begin_code,
                data=data_right
            )
        if match_end_code.group(1).strip() != '' :
            msg ='xsrst_code stop command has language argument'
            sys_exit(msg,
                fname=file_in,
                sname=section_name,
                match=match_end_code,
                data=section_rest
            )
        # pygments does not recognize hpp ?
        if language == 'hpp' :
            language = 'cpp'
        #
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
def convert_file_command(pattern, section_data, file_in, section_name) :
    assert pattern['file_2'].groups == 6
    assert pattern['file_3'].groups == 8
    for key in [ 'file_2', 'file_3' ] :
        file_offset = 0
        match_file  = pattern[key].search(section_data)
        while match_file != None :
            #
            # exclude
            cmd_start = int( match_file.group(1) )
            if key == 'file_2' :
                cmd_end = int( match_file.group(6) )
            else :
                cmd_end = int( match_file.group(8) )
            exclude = (cmd_start, cmd_end)
            #
            # start, start_line
            start      = match_file.group(2).strip()
            start_line = int( match_file.group(3) )
            if start == '' :
                msg = 'xsrst_file command: start text is empty'
                sys_exit(msg,
                    fname=file_in, sname=section_name, line=start_line
                )
            #
            # stop, stop_line
            stop      = match_file.group(4) .strip()
            stop_line = int( match_file.group(5) )
            if stop == '' :
                msg = 'xsrst_file command: stop text is empty'
                sys_exit(msg,
                    fname=file_in, sname=section_name, line=stop_line
                )
            #
            # file_name, same_file
            if key == 'file_2' :
                file_name = file_in
                same_file = True
            else :
                file_name  = match_file.group(6).strip()
                same_file  = os.path.samefile(file_name, file_in)
            #
            # data
            file_ptr  = open(file_name, 'r')
            data      = file_ptr.read()
            file_ptr.close()
            #
            # start_list
            if same_file :
                start_list = find_text_line(data ,start, exclude)
            else :
                start_list = find_text_line(data ,start)
            if len(start_list) == 0 :
                msg  = 'xsrst_file command: can not find'
                msg += '\nstart = "' + start + '"'
                msg += ' in file '+ file_name
                sys_exit(msg,
                    fname=file_in, sname=section_name, line=start_line
                )
            if 1 < len(start_list) :
                msg  = 'xsrst_file command: found more than one'
                msg += '\nstart = "' + start + '"'
                msg += ' in file '+ file_name
                sys_exit(msg,
                    fname=file_in, sname=section_name, line=start_line
                )
            #
            # stop_list
            if same_file :
                stop_list = find_text_line(data, stop, exclude)
            else :
                stop_list = find_text_line(data, stop)
            if len(stop_list) == 0 :
                msg  = 'xsrst_file command: can not find'
                msg += '\nstop = "' + stop + '"'
                msg += ' in file '+ file_name
                sys_exit(msg,
                    fname=file_in, sname=section_name, line=stop_line
                )
            if 1 < len(stop_list) :
                msg  = 'xsrst_file command: found more than one'
                msg += '\nstop = "' + stop + '"'
                msg += ' in file '+ file_name
                sys_exit(msg,
                    fname=file_in, sname=section_name, line=stop_line
                )
            #
            if stop_list[0] <= start_list[0] :
                msg  = 'xsrst_file command: stop does not come after start'
                msg += ' in file '+ file_name
                msg += '\nstart = "' + start + '"'
                msg += '\nstop = "' + stop + '"'
                sys_exit(msg,
                    fname=file_in, sname=section_name, line=stop_line
                )
            #
            # locations in file_name
            start_line  = start_list[0] + 1
            stop_line   = stop_list[0] - 1
            #
            #
            # beginning of lines with command in it
            begin_line = match_file.start() + file_offset;
            #
            # end of lines with command in it
            end_line = match_file.end() + file_offset;
            #
            # converted version of the command
            cmd  = f'xsrst__file {file_name} {start_line} {stop_line} '
            cmd  = '\n{' + cmd  + '}\n'
            #
            data_left  = section_data[: begin_line]
            data_left += cmd
            data_right = '\n' + section_data[ end_line : ]
            #
            section_data  = data_left + data_right
            file_offset   = len(data_left)
            match_file  = pattern[key].search(data_right)
    return section_data
# -----------------------------------------------------------------------------
# add labels and indices for headings
def process_headings(
        pattern, section_data, num_remove, file_in, section_name, index_list
) :
    punctuation      = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    assert len(punctuation) == 34 - 2 # two escape sequences
    #
    punctuation_used = set()
    heading_list     = list()
    next_start       = 0
    next_newline     = section_data.find('\n', next_start)
    candidate_start  = None
    candidate_state  = 'empty'
    jump_table       = ''
    while 0 <= next_newline :
        next_line = section_data[next_start : next_newline]
        next_line = pattern['line'].sub('', next_line)
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
            if overline :
                punctuation_used.add(character)
            #
            # check for first heading
            if len( heading_list ) == 0 :
                heading_list.append( heading )
            else :
                same_level = overline == heading_list[0]['overline']
                if same_level :
                    same_level = character == heading_list[0]['character']
                if same_level :
                    msg = 'There are multiple titles for this section'
                    sys_exit(msg, fname=file_in, sname=section_name)
                level = 1
                while level < len(heading_list) and not same_level :
                    same_level = overline == heading_list[level]['overline']
                    if same_level :
                        same_level = \
                            character == heading_list[level]['character']
                    if same_level :
                        heading_list = heading_list[: level ]
                        heading_list.append(heading)
                    else :
                        level += 1
                if not same_level :
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
                skip = False
                for regexp in index_list :
                    match = regexp.search(word)
                    if match :
                        if match.group(0) == word :
                            skip = True
                if not skip :
                    if index == '' :
                        index = word
                    else :
                        index += ',' + word
            #
            # jump_table entry for this heading
            level       = len(heading_list) - 1
            if 0 < level :
                line        = (4 * (level - 1)) * ' ' + '- '
                line       += ':ref:`' + label + '`\n'
                jump_table += line
            #
            cmd  = '\n{xsrst_label '
            cmd += index + ' '
            cmd += label + ' }'
            #
            # place label and index entry in output before the heading
            data_left   = section_data[: candidate_start]
            if len(heading_list) == 1 :
                cmd += '\n{xsrst_section_number}'
            data_left  += cmd
            data_left  += section_data[candidate_start : next_newline]
            if len(heading_list) == 1 :
                data_left += '\n{xsrst_jump_table}'
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
    i = 0
    while punctuation[i] in punctuation_used :
        i += 1
        if i == len(punctuation) :
            msg  = 'more than ' + len(punctuation) - 1
            msg += ' overlined heading levels'
            sys_exit(msg, fname = file_in, sname = section_name)
    line           = len(section_name) * punctuation[i] + '\n'
    pseudo_heading = line + section_name + '\n' + line + '\n'
    #
    return section_data, pseudo_heading, jump_table
# -----------------------------------------------------------------------------
# Compute output corresponding to a section.
# This finishes all the xsrst processing that has been delayed to this point
# with the exception of {xsrst_section_number}. The seciton number is computed
# after all the sections have been output and replaced during the
# table_of_contents computation.
def compute_output(
    pattern,
    sphinx_dir,
    file_in,
    section_data,
    list_children,
    pseudo_heading,
    jump_table,
    output_dir,
    section_name,
    line_increment,
) :
    # If file_path is relative to top git repo directory,
    # xsrst_dir2top_dir/file_path is relative to sphinx_dir/xsrst directory.
    depth   =  sphinx_dir.count('/') + 2
    top_dir =  depth * '../'
    top_dir = top_dir[:-1]
    #
    # split section data into lines
    newline_list = newline_indices(section_data)
    #
    # put pseudo heading at beginning of output
    rst_output = pseudo_heading
    #
    # now output the section data
    startline         = 0
    inside_code       = False
    previous_empty    = True
    has_child_command = False
    for newline in newline_list :
        line  = section_data[startline : newline + 1]
        # commands that delay some processing to this point
        section_number_command = line.startswith('{xsrst_section_number}')
        jump_table_command     = line.startswith('{xsrst_jump_table')
        code_command           = line.startswith('{xsrst_code')
        file_command           = line.startswith('{xsrst__file')
        label_command          = line.startswith('{xsrst_label')
        children_command       = line.startswith('{xsrst_children')
        child_link_command     = line.startswith('{xsrst_child_link')
        child_list_command     = line.startswith('{xsrst_child_list')
        if section_number_command :
            rst_output += line
        elif jump_table_command :
            rst_output += jump_table + '\n'
            previous_empty = True
        elif label_command :
            # --------------------------------------------------------
            # label command
            line  = line.split(' ')
            index = line[1].replace(',', ', ')
            label = line[2]
            line  = ''
            if index != '' :
                # index is empty if keyword file ingnores all words in heading
                line += '.. meta::\n'
                line += '   :keywords: ' + index + '\n\n'
                line += '.. index:: ' + index + '\n\n'
            line += '.. _' + label + ':\n\n'
            rst_output += line
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
            rst_output += line
            previous_empty = True
        elif file_command :
            line       = line.split()
            file_name  = line[1]
            start_line = line[2]
            stop_line  = line[3]
            #
            rst_output += '\n'
            line = f'.. literalinclude:: {top_dir}/{file_name}\n'
            rst_output += line
            line = f'    :lines: {start_line}-{stop_line}\n'
            rst_output += line
            #
            # Add language to literalinclude, sphinx seems to be brain
            # dead and does not do this automatically.
            index = file_name.rfind('.')
            if 0 <= index and index + 1 < len(file_name) :
                extension = file_name[index + 1 :]
                if extension == 'xsrst' :
                    extension = 'rst'
                elif extension == 'hpp' :
                    extension = 'cpp' # pygments does not recognize hpp ?
                line = f'    :language: {extension}\n'
                rst_output += line
            #
            rst_output += '\n'
            previous_empty = True
        elif children_command or child_link_command or child_list_command :
            assert not has_child_command
            assert len(list_children) > 0
            has_child_command = True
            #
            rst_output += '.. toctree::\n'
            rst_output += '   :maxdepth: 1\n'
            if children_command or child_list_command :
                rst_output += '   :hidden:\n'
            rst_output += '\n'
            for child in list_children :
                rst_output += '   ' + child + '\n'
            rst_output += '\n'
            #
            if child_list_command :
                for child in list_children :
                    rst_output += '#. ' + child + ': :ref:`'+ child + '`\n'
                rst_output += '\n'
            previous_empty = True
        else :
            match = pattern['line'].search(line)
            if match :
                empty_line = match.start() <= num_remove
            else :
                empty_line = len(line) <= num_remove
            if empty_line :
                    line = '\n'
            else :
                    line = line[num_remove :]
            if inside_code :
                line = 4 * ' ' + line
            #
            if line != '\n' :
                rst_output += line
            elif not previous_empty :
                rst_output += line
            #
            previous_empty = line == '\n'
        startline = newline + 1
    #
    # The last step in converting xsrst commands is removing line numbers
    # (done last so mapping from output to input line number is correct)
    rst_output, line_pair = remove_line_numbers(pattern, rst_output)
    # -----------------------------------------------------------------------
    if not previous_empty :
        rst_output += '\n'
    #
    if len(list_children) > 0 and not has_child_command :
        rst_output += '.. toctree::\n'
        rst_output += '   :maxdepth: 1\n\n'
        for child in list_children :
            rst_output += '   ' + child + '\n'
        rst_output += '\n'
    #
    # sphinx transition
    rst_output += '----\n\n'
    rst_output += f'xsrst input file: ``{file_in}``\n'
    #
    if line_increment > 0 :
        rst_output += '\n.. csv-table:: Line Number Mapping\n'
        rst_output += 4 * ' ' + ':header: rst file, xsrst input\n'
        rst_output += 4 * ' ' + ':widths: 10, 10\n\n'
        previous_line = None
        for pair in line_pair :
            if previous_line is None :
                rst_output   += f'    {pair[0]}, {pair[1]}\n'
                previous_line = pair[1]
            elif pair[1] - previous_line >= line_increment :
                rst_output   += f'    {pair[0]}, {pair[1]}\n'
                previous_line = pair[1]
    #
    return rst_output
# -----------------------------------------------------------------------------
# write file corresponding to a section
def write_file(
    section_name,
    rst_output,
) :
    # open output file
    file_out = output_dir + '/' + section_name + '.rst'
    file_ptr = open(file_out, 'w')
    file_ptr.write(rst_output)
    file_ptr.close()
# =============================================================================
# main program
# =============================================================================
# check working directory
if not os.path.isdir('.git') :
    msg = 'must be executed from to top directory for this git repository\n'
    sys_exit(msg)
#
# check number of command line arguments
if len(sys.argv) != 5 and len(sys.argv) != 6 :
    usage  = 'bin/xsrst.py root_file sphinx_dir spelling keyword'
    usage += ' [line_increment]'
    sys_exit(usage)
#
# target
target = sys.argv[1]
if target != 'html' and target != 'pdf' :
    msg  = 'target = ' + target + '\n'
    msg += 'is not "html" or "pdf"'
    sys_exit(msg)
#
# root_file
root_file = sys.argv[2]
if not os.path.isfile(root_file) :
    msg  = 'root_file = ' + root_file + '\n'
    msg += 'is not a file'
    sys_exit(msg)
#
# sphinx_dir
sphinx_dir      = sys.argv[3]
if not os.path.isdir(sphinx_dir) :
    msg  = 'sphinx_dir = ' + sphinx_dir + '\n'
    msg += 'is not a sub-directory of current working directory'
    sys_exit(msg)
#
# spelling
spelling   = sys.argv[4]
spell_path = sphinx_dir + '/' + spelling
if not os.path.isfile(spell_path) :
    msg  = 'sphinx_dir/spelling = ' + spell_path + '\n'
    msg += 'is not a file'
    sys_exit(msg)
#
# keyword
keyword      = sys.argv[5]
keyword_path = sphinx_dir + '/' + keyword
if not os.path.isfile(keyword_path) :
    msg  = 'sphinx_dir/keyword = ' + keyword_path + '\n'
    msg += 'is not a file'
    sys_exit(msg)
#
# line_increment
if len(sys.argv) == 6 :
    line_increment = 0
else :
    line_increment = int(sys.argv[7])
    if line_increment < 1 :
        msg += 'line_increment is not a positive integer'
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
spell_list           = file2list(spell_path)
spell_checker        = init_spell_checker(spell_list)
#
# index_list
index_list = list()
for regexp in file2list(keyword_path) :
    index_list.append( re.compile( regexp ) )
#
# regular expresssions used for spell command
pattern = dict()
pattern['word']        = re.compile( r'[\\A-Za-z][a-z]*' )
pattern['double_word'] = re.compile( r'\s+([\\A-Za-z][a-z]*)\s+\1[^a-z]' )
pattern['ref_1']       = re.compile( r':ref:`[^\n<`]+`' )
pattern['url_1']       = re.compile( r'`<[^\n>`]+>`_' )
pattern['ref_2']       = re.compile( r':ref:`([^\n<`]+)<[^\n>`]+>`' )
pattern['url_2']       = re.compile( r'`([^\n<`]+)<[^\n>`]+>`_' )
#
# regular expressions corresponding to xsrst commands
pattern['line']    = re.compile(r'\{xsrst_line ([0-9]+)@')
pattern['suspend'] = re.compile( r'\n[ \t]*\{xsrst_suspend\}' )
pattern['resume']  = re.compile( r'\n[ \t]*\{xsrst_resume\}' )
pattern['code']    = re.compile(
    r'\n[^\n`]*\{xsrst_code([^}]*)\}[^\n`]*'
)
pattern['spell']   = re.compile(
    r'\n[ \t]*\{xsrst_spell([^}]*)\}'
)
arg = r'([^{]*)\{xsrst_line ([0-9]+)@\n'
lin = r'[ \t]*\{xsrst_line ([0-9]+)@\n'
pattern['file_2']  = re.compile(
    r'\n[ \t]*\{xsrst_file' + lin + arg + arg + r'[ \t]*\}' + lin
)
pattern['file_3']  = re.compile(
    r'\n[ \t]*\{xsrst_file' + lin + arg + arg + arg + r'[ \t]*\}' + lin
)
pattern['child']   = re.compile(
    r'\n[ \t]*\{xsrst_(children|child_link|child_list)([^}]*)\}'
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
    # pop first element is stack so that order in pdf file and
    # table of contents is correct
    info  = file_info_stack.pop(0)
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
    parent_file_section  = info['parent_section']
    assert os.path.isfile(file_in)
    #
    # get xsrst docuemntation in this file
    this_file_info = file2file_info(
        section_info,
        file_in,
    )
    #
    # determine index of parent section for this file
    this_file_parent_section_index = None
    for i in range( len(this_file_info) ) :
        if this_file_info[i]['is_parent'] :
            this_file_parent_section_index = len(section_info) + i
    if this_file_parent_section_index :
        if len(this_file_info) < 2 :
            msg  = 'xsrst_begin_parent appreas in a file with only one section'
            sys_exit(msg, fname=file_in, sname=section_name)
    #
    # add this files sections to section_info
    for i_file in range( len(this_file_info) ) :
        # ----------------------------------------------------------------
        # section_name, section_data
        section_name = this_file_info[i_file]['section_name']
        section_data = this_file_info[i_file]['section_data']
        is_parent    = this_file_info[i_file]['is_parent']
        if is_parent or this_file_parent_section_index is None :
            parent_section = parent_file_section
        else :
            parent_section = this_file_parent_section_index
        #
        section_info.append( {
            'section_name'   : section_name,
            'file_in'        : file_in,
            'parent_section' : parent_section
        } )
        # ----------------------------------------------------------------
        # process suspend commands
        section_data = suspend_command(
            pattern,
            section_data,
            file_in,
            section_name,
        )
        # ----------------------------------------------------------------
        # process spell commands
        # do after suspend and before other commands to help ignore sections
        # of text that do not need spell checking
        section_data = spell_command(
            pattern,
            section_data,
            file_in,
            section_name,
            spell_checker,
        )
        # ----------------------------------------------------------------
        # process child command
        section_data, child_file, child_section = child_commands(
            pattern,
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
            pattern,
            section_data,
            file_in,
            section_name,
        )
        # ---------------------------------------------------------------
        # add labels and indices corresponding to headings
        section_data, pseudo_heading, jump_table = process_headings(
            pattern,
            section_data,
            num_remove,
            file_in,
            section_name,
            index_list,
        )
        # ----------------------------------------------------------------
        # list_children
        # first section in each file may need to add to child list
        list_children = list()
        if is_parent :
            for i in range( len(this_file_info) ) :
                if i != i_file :
                    list_children.append(  this_file_info[i]['section_name'] )
        list_children = list_children + child_section
        # ---------------------------------------------------------------
        rst_output = compute_output(
            pattern,
            sphinx_dir,
            file_in,
            section_data,
            list_children,
            pseudo_heading,
            jump_table,
            output_dir,
            section_name,
            line_increment,
        )
        # ---------------------------------------------------------------
        write_file(
            section_name,
            rst_output,
        )
# -----------------------------------------------------------------------------
# xstst_automatic.rst
output_data = '.. include:: ../preamble.rst\n'
#
if target == 'pdf' :
    # The top level heading is not included in pdf output
    output_data += '\n'
    output_data += 'Dummy Heading\n'
    output_data += '#############\n'
#
# Table of Contents
level         = 1
count         = list()
section_index = 0
output_data  += table_of_contents(
    target, section_info, level, count, section_index
)
if target == 'html' :
    # Link to Index
    output_data += '\n'
    output_data += 'Link to Index\n'
    output_data += '*************\n'
    output_data += '* :ref:`genindex`\n'
#
file_out    = output_dir + '/' + 'xsrst_automatic.rst'
file_ptr    = open(file_out, 'w')
file_ptr.write(output_data)
file_ptr.close()
# -----------------------------------------------------------------------------
# check section_name is in index.rst
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
# table
print('xsrst.py: OK')
sys.exit(0)
