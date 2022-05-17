# Welcome to the UwUinator!

## What It Does

The UwUinator fills a specified path with UwU Files until the script is either stopped or the drive runs out of storage space. 

I always get asked, "what is the point of this?" There isn't one.

The UwUinator is just a script I made bored in school after I took a classmate's drive and he asked, "are you going to fill my drive with UwUs?"

## What's New in v1.5.5
- The UwUinator now takes command line arguments! These can be used to customize the way it works.
    - `path` - A required positional argument that specifies the path to fill with UwUs. 
    - `-a`, `--amount` - The amount of space, in megabytes, to have the UwUinator fill. If not specified, it goes until the drive is full.
    - `-f`, `--file` - The file to copy. If not specified, the default image is used.
    - `-h`, `--help` - Displays the help message.
- The UwUinator no longer breaks when you use ctrl+c to stop it. This is now the recommended way to stop the UwUinator.

## About the UwUinator

The UwUinator is a Python script that fills a specified path with a file we like to call an "UwU File." An UwU File is any file that says UwU in it anywhere, as long as it's noticeable. The early versions of the UwUinator created massive text files with "UwU." Now, it copies an image to your specified path. If it can't find the image, you can even specify your own file.

Throughout the files, you'll find docstrings with my personal tests. You'll see names of people you'll never meet and drive types you never thought would be filled with UwUs.

Do what you want with this, have fun. That's what the UwUinator was made for.


## Running the UwUinator

To run the UwUinator, you must have Python 3 installed. 
The UwUinator does not use any libraries that do not come with Python.

```
py uwuinator.py [path] [--args]
```

An example:

```
py uwuinator.py E:\UwU --amount 1000 
```

To view a list of arguments, run the UwUinator with the `--help` argument.

```
py uwuinator.py --help
```

## Contributing

If you can't tell already, the UwUinator is not very well optimized and is somewhat messy. Fortunately, the UwUinator relies on the drive it's writing to for its speed. If there is any way you can think of making it faster or more optimized, feel free to fork it, make a PR, whatever.