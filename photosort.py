#!/usr/bin/env python

import os, sys

def main():
	import optparse
	
	# define and parse command-line options
	prog = os.path.basename(sys.argv[0])
	usage = "Usage: %s [options] action source dest" % prog
	
	parser = optparse.OptionParser(usage)
	parser.add_option("-c", "--copy",    dest="move",    action="store_true",  help="copy files to destination [default]")
	parser.add_option("-m", "--move",    dest="move",    action="store_false", help="move files to destination")
	parser.add_option("-v", "--verbose", dest="verbose", action="store_true")
	parser.add_option("-q", "--quiet",   dest="verbose", action="store_false")
	
	# sort action options
	group = optparse.OptionGroup(parser, "Sort Photos", "Usage: %s [options] sort source dest" % prog)
	group.add_option("-n", "--name",     dest="name",     help="specify a bucket name for this image source (default is the source directory name)", metavar="NAME")
	group.add_option("-p", "--preserve", dest="preserve", action="store_true",  help="keep all alternates including low-res and duplicates [default]")
	group.add_option("-d", "--discard",  dest="preserve", action="store_false", help="discard duplicates and low-res alternates.")
	parser.add_option_group(group)
	
	# restore action options
	group = optparse.OptionGroup(parser, "Restore Original Filenames", "Usage: %s [options] restore source [dest]" % prog)
	parser.add_option_group(group)
	
	# fix action options
	group = optparse.OptionGroup(parser, "Fix Photo Dates", "Usage: %s [options] fix source [dest]" % prog)
	parser.add_option_group(group)
	
	# parse our options
	parser.set_defaults(verbose=True, move=False, preserve=True)
	(options, args) = parser.parse_args()
	
	if len(args) == 0:
		parser.print_help()
		return
	elif args[0] not in ('sort','fix','restore'):
		parser.error("Invalid action provided")
	elif args[0] in ('fix','restore') and len(args) == 2:
		args.append(args[1])
	elif len(args) != 3:
		parser.error("Incorrect number of arguments")
	
	(action, src, dest) = args
	
	# handle sort action
	if action == 'sort':
		if not options.name:
			options.name = os.path.basename(os.path.abspath(src))
		sort_images(src, dest, options.name, options.move, options.verbose)
	
	# handle restore action
	if action == 'restore':
		restore_images(src, dest, options.move, options.verbose)
	
	# handle fix action
	if action == 'fix':
		fix_images(src, dest, options.move, options.verbose)
	
	print "\n\n...\n"


def sort_images(src, dest, src_bucket, move=False, verbose=True):
	print "Sorting Images..."


def restore_images(src, dest, move=False, verbose=True):
	print "Restoring Filenames..."


def fix_images(src, dest, move=False, verbose=True):
	print "Fixing Image Dates..."



if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print "\nOpteration Aborted\n"