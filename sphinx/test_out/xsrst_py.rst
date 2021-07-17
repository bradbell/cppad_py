!!!!!!!!
xsrst_py
!!!!!!!!

.. toctree::
   :maxdepth: 1
   :hidden:

   begin_cmd
   child_cmd
   spell_cmd
   suspend_cmd
   code_cmd
   file_cmd
   comment_ch_cmd
   heading_exam
   indent_exam
   configure

.. include:: ../preamble.rst

.. meta::
   :keywords: xsrst_py, extract, sphinx, rst

.. index:: xsrst_py, extract, sphinx, rst

.. _xsrst_py:

Extract Sphinx RST
##################
.. contents::
   :local:

.. The indentation examples are included by the child_cmd section.

.. meta::
   :keywords: syntax

.. index:: syntax

.. _xsrst_py.syntax:

Syntax
******
-   ``xsrst.py`` *target* *root_file* *sphinx_dir* *spelling* *keyword*
-   ``xsrst.py`` *target* *root_file* *sphinx_dir* *spelling* *keyword*
    *line_increment*

.. meta::
   :keywords: purpose

.. index:: purpose

.. _xsrst_py.purpose:

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

.. meta::
   :keywords: requirements

.. index:: requirements

.. _xsrst_py.requirements:

Requirements
************
-   ``pip install --user pyspellchecker``
-   ``pip install --user sphinx``
-   ``pip install --user sphinx-rtd-theme``
-   The directory *cmake_install_prefix*\ ``/bin`` must be in your execution
    path where *cmake_install_prefix* is the prefix used to instal cppad_py.

.. meta::
   :keywords: notation

.. index:: notation

.. _xsrst_py.notation:

Notation
********

.. meta::
   :keywords: white, space

.. index:: white, space

.. _xsrst_py.notation.white_space:

White Space
===========
We define white space to be a sequence of space characters; e.g.,
tabs are not consider white space by xsrst.

.. meta::
   :keywords: beginning, line

.. index:: beginning, line

.. _xsrst_py.notation.beginning_of_a_line:

Beginning of a Line
===================
We say that a string *text* is a the beginning of a line if
only white space, or nothing, comes before *text* in the line.

.. meta::
   :keywords: command, line, arguments

.. index:: command, line, arguments

.. _xsrst_py.command_line_arguments:

Command Line Arguments
**********************

.. meta::
   :keywords: target

.. index:: target

.. _xsrst_py.command_line_arguments.target:

target
======
The command line argument *target* must be ``html`` or ``pdf`` and
specifies the type of type output you plan to generate using sphinx.
If *target* is ``html`` you can generate the sphinx output using
the following command in the *sphinx_dir* directory:

.. code-block:: sh

        make html

If *target* is ``pdf``, you can use the following commands:

.. code-block:: sh

        sed -i preamble.rst -e '/BEGIN_LATEX_MACROS/,/END_LATEX_MACROS/d'
        sphinx-build -b latex . _build/latex
        git checkout preamble.rst
        cd _build/latex
        sed -i cppad_py.tex -e 's|\\chapter{|\\paragraph{|'
        make cppad_py.pdf

.. meta::
   :keywords: root_file

.. index:: root_file

.. _xsrst_py.command_line_arguments.root_file:

root_file
=========
The command line argument *root_file* is the name of a file,
relative to the top git repository directory.

.. meta::
   :keywords: root_section

.. index:: root_section

.. _xsrst_py.command_line_arguments.root_file.root_section:

root_section
------------
If there is only one section in the *root_file*,
the corresponding *section_name* is the *root_section* .
If there is more than one section in the *root_file*, the file must have a
:ref:`begin_cmd.parent_section` and the corresponding *section_name*
is the *root_section*.
The file *sphinx_dir* :code:`/index.rst` must contain the line

|tab| ``xsrst/`` *root_section*

.. meta::
   :keywords: sphinx_dir

.. index:: sphinx_dir

.. _xsrst_py.command_line_arguments.sphinx_dir:

sphinx_dir
==========
The command line argument *sphinx_dir* is a sub-directory,
of the top git repository directory.
The  sphinx ``conf.py``, ``index.rst``, *spelling*, and *keyword*
files are located in this directory.
The sub-directory *sphinx_dir* :code:`/xsrst` is managed by ``xsrst`` .
All the ``.rst`` files in *sphinx_dir* :code:`/xsrst`
were extracted from the source code and correspond to
last time that ``xsrst.py`` was executed.
Files that do not change are not updated (to speed up the processing).

.. meta::
   :keywords: example, configuration, files

.. index:: example, configuration, files

.. _xsrst_py.command_line_arguments.sphinx_dir.example_configuration_files:

Example Configuration Files
---------------------------

| |tab| conf.py: :ref:`conf_py`
| |tab| index.rst: :ref:`index_rst`
| |tab| keyword: :ref:`keyword`
| |tab| spelling: :ref:`spelling`

.. meta::
   :keywords: spelling

.. index:: spelling

.. _xsrst_py.command_line_arguments.spelling:

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

.. meta::
   :keywords: keyword

.. index:: keyword

.. _xsrst_py.command_line_arguments.keyword:

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

.. meta::
   :keywords: line_increment

.. index:: line_increment

.. _xsrst_py.command_line_arguments.line_increment:

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

.. meta::
   :keywords: table, contents

.. index:: table, contents

.. _xsrst_py.table_of_contents:

Table of Contents
*****************

.. meta::
   :keywords: toctree

.. index:: toctree

.. _xsrst_py.table_of_contents.toctree:

toctree
=======
The sphinx ``toctree`` directives are automatically generated
for sections. The only such directive you should directly edit
is in the file *sphinx_dir*\ ``/index.rst``

.. meta::
   :keywords: index.rst

.. index:: index.rst

.. _xsrst_py.table_of_contents.toctree.index.rst:

index.rst
---------
First entry below ``toctree`` in the *sphinx_dir*\ ``/index.rst``
file should be ``xsrst/xsrst_automatic``.
This includes the automatically generated table of contents
for the files extracted by xsrst.
(The link anchor ``xsrst_table_of_contents``
can be used to link to this section.)
The second entry below ``toctree`` should be the
:ref:`root_section<xsrst_py.command_line_arguments.root_file.root_section>`.
You may have other entries for ``.rst`` files that are not extracted by
``xsrst.py``.

.. meta::
   :keywords: parent, section

.. index:: parent, section

.. _xsrst_py.table_of_contents.parent_section:

Parent Section
==============
A single input file may contain multiple
:ref:`sections<begin_cmd.section>`.
The first of these sections may use a
:ref:`parent begin<begin_cmd.parent_section>` command.
In this case, the other sections in the file are children of this section
and this section is a child of the section containing the
:ref:`child command<child_cmd>` that included this file.

If there is no begin parent command in a file,
all the sections in the file are children of the section containing the
child command that included the file.

.. meta::
   :keywords: heading, links

.. index:: heading, links

.. _xsrst_py.heading_links:

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

.. meta::
   :keywords: section, level

.. index:: section, level

.. _xsrst_py.heading_links.section_level:

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

.. meta::
   :keywords: other, levels

.. index:: other, levels

.. _xsrst_py.heading_links.other_levels:

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

.. meta::
   :keywords: children

.. index:: children

.. _xsrst_py.heading_links.children:

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

.. meta::
   :keywords: example

.. index:: example

.. _xsrst_py.heading_links.example:

Example
=======
:ref:`heading_exam`

.. meta::
   :keywords: indentation

.. index:: indentation

.. _xsrst_py.indentation:

Indentation
***********
If there are a number of spaces before
all of the xsrst documentation for a section,
those characters are not included in the xsrst output.
This enables one to indent the
xsrst so it is grouped with the proper code block in the source.
An error message will result if
you use tabs in the indentation.

.. meta::
   :keywords: example

.. index:: example

.. _xsrst_py.indentation.example:

Example
=======
- :ref:`indent_exam`

.. meta::
   :keywords: wish, list

.. index:: wish, list

.. _xsrst_py.wish_list:

Wish List
*********
The following is a wish list for future improvements to ``xsrst.py``:

.. _stackoverflow: https://stackoverflow.com/questions/1686837/
   sphinx-documentation-tool-set-tab-width-in-output

.. meta::
   :keywords: subset, documentation

.. index:: subset, documentation

.. _xsrst_py.wish_list.subset_documentation:

Subset Documentation
====================
Have a way to specify subsets of the documentation by a group name.
For example ``{xsrst_begin`` `section_name group_1 group_2}` would say that
this documentation should be included if `group_1` or `group_2`
is specified by the ``xsrst`` command line.
If not groups were specified, all groups would be included.

.. meta::
   :keywords: spelling

.. index:: spelling

.. _xsrst_py.wish_list.spelling:

Spelling
========
Automatically ignore more words that are sphinx or latex commands.

.. meta::
   :keywords: tabs

.. index:: tabs

.. _xsrst_py.wish_list.tabs:

Tabs
====
Tabs in a code blocks get expanded to 8 spaces; see stackoverflow_.
It would be nice to have a way to control the size of tabs in the code blocks
displayed by :ref:`code_cmd` and :ref:`file_cmd`.
Perhaps it would be good to support tabs as a method for
indenting xsrst input sections.

.. meta::
   :keywords: module

.. index:: module

.. _xsrst_py.wish_list.module:

Module
======
Convert the program into a python module and provide a pip distribution for it.
It would at least be nice for cppad_py to install the ``xsrst.py`` program
so that users would not have to copy it to a directory in
their execution path.

.. All the children of this section are commands except for heading_exam.

.. meta::
   :keywords: commands

.. index:: commands

.. _xsrst_py.commands:

Commands
********
- :ref:`begin_cmd`
- :ref:`child_cmd`
- :ref:`spell_cmd`
- :ref:`suspend_cmd`
- :ref:`code_cmd`
- :ref:`file_cmd`
- :ref:`comment_ch_cmd`

----

xsrst input file: ``bin/xsrst.py``
