# WakaFont

Font consisting of 'missing' radicals for [WaniKani][wk].

## Process

1. (manual) Get the API key, then call the `/radicals` method with all levels enabled
2. Download all the radical PNGs
3. Convert them to a format suitable for [potrace][pt] (and invert), then to SVG
4. Use [FontCustom][fc] to make a webfont & preview page

## Prerequisites

* potrace
* ImageMagick
* FontCustom

## Usage

To make the font, run `./Shakefile.sh` and wait. If everything is OK, you'll get font, CSS and preview page in the `dist/` dir. If you just want to get PNGs or convert them to SVGs, you can run `python download.py` or `bash convert.sh`.

## License

All files except for `radicals.json` are licensed under WTFPL2. `radicals.json` is a modified WaniKani API output (personal info removed) and is subject to its Terms of Use.

[wk]: https://wanikani.com/
[pt]: http://potrace.sourceforge.net/
[fc]: http://fontcustom.com/