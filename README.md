# Installator
A modular installation for python apps

## What it is?
It is an application to install python apps that need to be downloaded. It has only be tested on git hub repositories, and it can also work for any URL.
It works with web authentication if is need it. (Currently tested in Git private and public)

## Motivation
The idea of this project is to create a generic and dynamic module that can be used to install an app and/or also be part of the app to perform updates.

## How it works
The implementation is straightforward...

### Use it to install
The repo has a generic UI that can be re-purposed for your needs, or it can work as a command in a terminal.
I do recommend to use a bake-in URL for installation purposes and to use an encrypted file for the authentication key.
The install module receives a URL and destination folder. It downloads the file and then copies it to the destination folder given.

It has a module "Checks" that can be modified to meet your needs for files that have been installed in the system.
*Currently supports zip compressed files but the idea is to extend it over time.*

### Use it to update
The update module iterates over the current version that is passed in the parameters and the URL and return the first URL that exists.


## Important
This project is an open and generic module where is up to the developer to set the URLs which the app downloads and updates.

*It only supports versions in the form of Mayor.Minor.Patch*

**If you want to contribute to this project feel free to do so, for specs as this is a simple project, please follow the ones that these files have.**
