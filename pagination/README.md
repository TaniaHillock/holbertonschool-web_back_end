# Pagination
## Resources
Read or watch:
* REST API Design: Pagination
* HATEOAS

## Learning Objectives
* How to paginate a dataset with simple page and page_size parameters
* How to paginate a dataset with hypermedia metadata
* How to paginate in a deletion-resilient manner

## Requirements
* All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/env python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle style (version 2.5.*)
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* All your functions and coroutines must be type-annotated.

## Setup
 *Popular_Baby_Names.csv : https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230909%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230909T112843Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=531c5e78bb5aa43b8985346c6f281e6c3547ef46d53f0a8c38e36c6a74eb11a5

## Files

|File Name | Description|
|----------|------------|
|0-simple_helper_function.py | Function named index_range that takes two integer arguments page and page_size. The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.|
|1-simple_pagination.py |  Method named get_page that takes two integer arguments page with default value 1 and page_size with default value 10.|
|2-hypermedia_pagination.py | get_hyper method that takes the same arguments (and defaults) as get_page and returns a dictionary.|
|3-hypermedia_del_pagination.py |  Two queries, certain rows are removed from the dataset, the user does not miss items from dataset when changing page.|

## Holberton Student

Tania Cauich
Github: @TaniaHillock