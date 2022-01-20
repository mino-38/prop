# What it can do
You can download files recursively, extract specific tags from html, etc.

# Install
```bash
# If you have the git command
$ pip install git+https://github.com/mino-38/prop

# If you don't have git command
$ pip install https://github.com/mino-38/prop/archive/refs/heads/main.zip
```

# Usage
```bash
$ prop [options] URL
```

# Options.
## -o, --output [path]
The -o, --output option allows you to specify the output file or directory.  
The -o and --output options can be used to specify the destination file or directory, and will save the file in the specified directory with the same name as the source file.  
Also, when using the -r option, please specify the destination directory with this option

## -O
Save the file with the same name as the original download.  
If -o, --output, or this option is not specified, the file will be output to standard output.

## -a, --fake-user-agent
Fake the UserAgent value.

## -U, --upgrade
Update prop.  
This is just running pip install --no-cache-dir --upgrade https://github.com/mino-38/prop/archive/refs/heads/main.zip, so you can run this directly.

## -s, --search-words [search-words]
You can search from the html code of the specified URL.  
The following is an example of what can be used as search words (you can also specify rel, alt, etc., but there are many, so only the main ones are used)

|  query  |  value  |
|  ----  |  ----  |
|  tags  |  tag name  |
|  class  |  class name  |
|  id |  id  |
|  text  |  value of tag  |
|  href  |  reference  |
|  src  |  reference to an image, etc  |
|  limit  |  number of retrievals (can also be specified with the -M option)  |

If you want to specify multiple values, separate them with ',' (no spaces).

Ex:

```bash
$ prop -s tags=a,script limit=5 URL

-> Get 5 tags from the URL source code.
Ex: ````bash $ prop -s tags=a,script limit=5

## -M, --limit [limit]
Specify the number of files to download recursively, or the number of results to retrieve with the -s, --search option.

## -R, --read-file [file]
Read from a file with pre-defined URLs and options.  
Also, since the session is retained, it is possible to access the file after logging in.

Ex:  
Contents of instruct.txt

````
-a -n -d name=hoge password=hogehoge -o /dev/null https://www.example.com/login.php
-O https://www.example.com/page.html
``` ``bash

```bash
$ prop -R instruct.txt
>>> Download https://www.example.com/page.html as page.html
```

## -r, --recursive [number of levels to go down]
Recursive download from the specified URL.  
If the number of descending levels is not specified, it is assumed to be 1.  
The target of the recursive download is the URL specified in the href attribute of the a tag and the src attribute of the img.  
If the -nE option is not specified, it will automatically replace the reference to the local file after downloading.  


If you use this option, please specify the destination directory with -o, --output option.


### Options available only with the -r option

#### -I, --interval [interval]
Specify the interval of the download.  
Recursive downloads can overload the target site, so it is recommended to specify at least 5 seconds.  
If a shorter time than the robots.txt directive is specified, it will be replaced by the robots.txt value.

#### -f, --format [format]
Allows you to specify the format of the file name of the file to be downloaded.  
The special format is as follows

|  format  |  value to be assigned  |
|  ----  |  ----  |
|  %(root)s  |  hostname of the download source  |
|  %(root)s  |  hostname of download source  |
|  %(file)s  |  file name of download source  |
|  %(num)d  |  sequential number starting from 0  |
|  %(ext)s   |  file extension  |


Ex:
```bash
$ prop -r -f "%(num)dtest-%(file)s" -o store_ directory URL

-> store_directory/0test-[filename], store_directory/1test-[filename] ... Download with the name

$ prop -r -f "test-%(num)d.%(ext)s" -o store_ directory URL

-> store_directory/test-0.[ext], store_directory/test-1[ext] ... Download as
````

Note that if the format does not include %(num)d or %(file)s, it will not be reflected (because the store name does not change dynamically).  
Also, there are some restrictions: %(file)s and %(ext)s formats can only be used at the end, more than one %(num)d cannot be used, and special formats such as %(num)d%(file)s cannot be used consecutively (because it is impossible to generate an exact sequential number for %(num)d).

## Option to restrict (extend) the download target
|  short option name  |  long option name  |  processing  |
|  ----  |  ----  |  ----  |
|  -np  |  --no-parent  |  option to ignore URLs in the hierarchy above the starting URL |
|  -nc  |  --no-content  | option to target only URLs with the href attribute of the a tag  |
|  -nc  |  --no-content  |  option to ignore URLs of href attribute of a tag  |
|  -nb  |  --no-body  |  option to ignore URLs of src attribute of img tag  |
|  -nd  |  --no-downloaded  |  Option to ignore files that have already been downloaded.
|  -nd  |  --no-downloaded  |  option to ignore already downloaded files  |
|  -dx  |  --download-external  | option to include URLs of external sites in the download  |
|  -st  |  --start  |  Option to specify a file name to start downloading  |

The -nc and -nb options cannot be used together.

## For options not listed here
Use the -h and --help options to display help.  
Please refer to the help page, which includes the options listed here.

# Where to save history, logs, and cache
You can see where the history is stored with --history-directory, where the logs are written with --log-file option, and where the cache is stored with --cache-directory

```bash
# A quick look at the logs
$ cat $(prop --log-file)

# History list
$ ls $(prop --history-directory)

# Where to store the cache
$ prop --cache-directory
````

You can also delete all logs with the --clear option (delete history and cache by hand or by deleting the history and cache directories)

```bash
# How to clear the logs
$ prop --clear

# How to delete the history
$ rm -r $(prop --history-directory)

# How to delete the cache
$ rm -r $(prop --cache-directory)
````

# New feature
- Add restrictions on formats that can be specified with -f and --format options.

# License
[MIT license](https://github.com/mino-38/prop/blob/main/LICENSE).
