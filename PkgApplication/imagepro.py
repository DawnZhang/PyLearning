#!/usr/bin/python -tt

import os, sys
import Image

def roll(im, im_roll, delta):
    "Roll an image sideways"
    xsize, ysize = im.size
    delta = delta % xsize
    if delta == 0: return im

    part1 = im.crop((0, 0, delta, ysize))
    part2 = im.crop((delta, 0, xsize, ysize))
    im_roll.paste(part2, (0, 0, xsize-delta, ysize))
    im_roll.paste(part1, (xsize-delta, 0, xsize, ysize))

    return im_roll


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print 'usage: ./imagepro.py [--thumbnail][--convert][--roll][--modbands] file [file ...]'
        sys.exit(1)

    # Create JPEG Thumbnails
    if args[0] == '--thumbnail':
        size = 128, 128
        infile = args[1]
        outfile = os.path.splitext(infile)[0] + '.thumbnail'
        if infile != outfile:
            try:
                im = Image.open(infile)
                im.thumbnail(size)
                im.save(outfile, 'JPEG')
            except IOError:
                print 'cannot create thumbnail for', infile

    # Convert file to PNG
    if args[0] == '--convert':
        infile = args[1]
        f, e = os.path.splitext(infile)
        outfile = f + '.png'
        if infile != outfile:
            try:
                Image.open(infile).save(outfile)
            except IOError:
                print 'cannot convert', infile

    # Roll an Image
    if args[0] == '--roll':
        infile = args[1]
        f, e = os.path.splitext(infile)
        outfile = f + '_roll' + e
        try:
            im = Image.open(infile)
            im.save(outfile)
            im_roll = Image.open(outfile)
            roll(im, im_roll, im.size[0]/2).save(outfile)
        except IOError:
            print 'cannot roll', infile

    # Splitting and merging bands
    if args[0] == '--modbands':
        infile = args[1]
        f, e = os.path.splitext(infile)
        outfile = f + '_modbands' + e
        try:
            im = Image.open(infile)
            r, g, b = im.split()
            im = Image.merge('RGB', (b, g, r))
            im.save(outfile)
        except IOError:
            print 'cannot modify bands of', infile


if __name__ == '__main__':
    main()
