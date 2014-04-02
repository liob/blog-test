Title: Scientific Blogging with Pelican and Pandoc
Date: 2014-04-01 18:40
Tags: "scientific writing"
Category: "scientific writing"
Slug: scientific_blogging_with_pelican_and_pandoc
Author: Hinrich B. Winther


> First of all a disclaimer: I am no expert in scientific blogging or even in blogging in general. I have only participated in one other blog and it failed miserably due to a lack of content.


What are the Formal Requirements for a Science Blog?
----------------------------------------------------

To my knowledge the term "science blog" is not defined. Furthermore, the exact format of scientific texts is highly dependant of your field as well as the medium you are publishing for. However, some prerequisite can be gathered by taking a look at traditional papers and abstracts:

**AMA Manual of Style?**

  (1) **Structure of Text**  
It should be possible to structure text logicly. This includes different types of headings, paragraphs as well as the ability to alter, to some degree, font characteristics.

  (2) **Support for Figures, Tables and Equations**  
There should be a simple way to create figures, tables and equations as well as their corresponding captions.

  (3) **Support for Citations**  
One of the most important parts of working scientificly is to not just state an opinion, but to back it up with your work or the preliminary work of others.

Currently [Pelican] (v.3.2) is able to statisfy the need for structured text as well as propper figures, tables and equations. However, it lacks support for citations, which is understandable, as this feature is usually not required for blogging. Nonetheless, it is required for scientific texts.


How Can Pelican Be Improved to Support Citations
------------------------------------------------

As Martin Fenner stated in his call for scholarly markdown [@fenner_call_2012] most of these features are already supported by [Pandoc]. This covers an excelent implementation for citations, including support for the [Citation Style Language (CSL)][CSL] which is espacilly useful when writing papers or abstracts. The natural fit is to use Pandoc as backend for Pelican. This can be achieved by creating a Pelican reader plugin, which is [fairly straight forward][How to create a new reader]. An implementation of such a reader plugin can be done in well under 50 lines of code: [Pandoc_Reader].

Yet, there is a lot of room for improvements. This includes fairly simple issues like cross referencing the references with the reference handles as well as more complex ones like [support for internal links for tables and figures][Pandoc issue 813].



References
----------

[CSL]: http://citationstyles.org/
[How to create a new reader]: http://pelican.readthedocs.org/en/latest/plugins.html#how-to-create-a-new-reader
[Pandoc]: http://johnmacfarlane.net/pandoc
[Pandoc issue 813]: https://github.com/jgm/pandoc/issues/813
[Pandoc_Reader]: https://github.com/liob/pandoc_reader
[Pelican]: http://getpelican.com

