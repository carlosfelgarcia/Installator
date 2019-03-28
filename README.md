# Installator
A modular installator for python apps

## What it is?
This is a application to install python apps that need to be downloaded. It has only be tested on git hub repos but it can work for any URL.
It to work with a web authentication if need it. (Currently tested in Git private and public)

## Motivation
The idea of this project is to create a generic and dynamic module that can be used to install an app and/or also be part of the app to perform updates.

## How it works
The implementation is really simple...

### Use it to install
The repo have a generic UI that can be re-purpose for your needs or it can work as a command in a terminal.
It is recommended that you use a bake-in URL for installation purposes and a encrypted file to load your authentication key if need it.
To use it just need to use the install module and give it the url and destination folder. It will download the file and then copy it to the destination folder given.

It has a module "Checks" that can be modified to meet your needs for files that have been installed in the system.
*Currently supports zip compressed files but the idea is to extend it over time.*

### Use it to update
The update module will iterate over the current version that is passed in the parameters and the URL and return the first URL that exist.


## Important
This is a really open and generic module where is up to the developer to set the URLs that where the app will be download and update.

*It only supports versions in the form of Mayor.Minor.Patch*

**If you want to contribute to this project feel free to do so, for specs as this is a simple project, just follow the ones that these files have.**
