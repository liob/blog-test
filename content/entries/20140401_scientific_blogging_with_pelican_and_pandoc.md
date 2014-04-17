Title: Scientific Blogging with Pelican and Pandoc
Date: 2014-04-17
Tags: "scientific writing"
Category: "scientific writing"
Slug: scientific_blogging_with_pelican_and_pandoc
Author: Hinrich B. Winther
Summary: The format of scientific texts is highly dependant of the respective field as well as the publishing media. However, there are some universal standards such as the IMRAD (Introduction, Methods, Results and Discussion) format for reports of original data. Prerequisite for scientific texts can be gathered by taking a look at traditional papers and abstracts


> First of all a disclaimer: I am no expert in scientific blogging or even in blogging in general. I have only participated in one other blog and it failed miserably due to a lack of content.


Formal Requirements for Scientific Texts
----------------------------------------

The format of scientific texts is highly dependant of the respective field as well as the publishing media. However, there are some universal standards such as the IMRAD (Introduction, Methods, Results and Discussion) format for reports of original data [@iverson_ama_2009]. Prerequisite for scientific texts can be gathered by taking a look at traditional papers and abstracts:

  (1) **Structure of Text**  
It should be possible to structure text logically. This includes different types of headings, paragraphs as well as the ability to alter font characteristics to some degree.

  (2) **Support for Citations**  
One of the most important parts of working scientifically is to not just state an opinion, but to back it up with the preliminary work of other parties.

  (3) **Support for Figures, Tables and Equations**  
There should be a simple way to create figures, tables and equations as well as their corresponding captions.

  (4) **Support for References**  
Automatic cross referencing as supported LaTex ("\\ref") and most word processors should be available.

Currently [Pelican] (v.3.2) is able to satisfy the requirement for structured text as well as proper figures, tables and equations. However, it lacks support for citations, which is comprehensible, as this feature is usually not required for blogging. Nonetheless, it is required for scientific texts.


Pelican and Pandoc
------------------

As Martin Fenner stated in his call for scholarly markdown [@fenner_call_2012] most of these features are already supported by [Pandoc]. This covers an excellent implementation for citations, including support for the [Citation Style Language (CSL)][CSL] which is especially useful when writing papers or abstracts. The natural fit is to use Pandoc as backend for Pelican. This can be achieved by creating a Pelican reader plugin, which is [fairly straight forward][How to create a new reader]. An implementation of such a reader plugin can be done in well under 50 lines of code: [Pandoc_Reader].


Lookout
-------

Although Pandoc has excellent support for structured text, figures, tables, equations and citations there is a lot of room for improvement. This includes fairly simple issues such as cross referencing support using html anchors as well as more complex ones such as [support for internal links for tables and figures][Pandoc issue 813].


References
----------

[CSL]: http://citationstyles.org/
[How to create a new reader]: http://pelican.readthedocs.org/en/latest/plugins.html#how-to-create-a-new-reader
[Pandoc]: http://johnmacfarlane.net/pandoc
[Pandoc issue 813]: https://github.com/jgm/pandoc/issues/813
[Pandoc_Reader]: https://github.com/liob/pandoc_reader
[Pelican]: http://getpelican.com

