# Fork of better_poster_latex
The Latex version of Mike Morrison's "better poster" template.
Only portrait version for now.

Explanation here: https://www.youtube.com/watch?v=1RwJbhkCA58&t=1s

Overleaf template: https://www.overleaf.com/latex/templates/better-poster-for-scientific-presentation/xpcssnwsgwqp

Original powerpoint by Mike Morrison here https://osf.io/vxqr6/

## Compile

On ifi machines you can compile using:

```
$ latexmk -pdf -jobname=main -shell-escape main.tex
```

## Import to overleaf

Download project as `.zip` by pressing the *code* button on the main page of the repo.

In overleaf, select *new project* and import the `.zip`.

**WARNING:** Currently there is no way to link overleaf to Github enterprice, so once you are done in overleaf,
you need to add the pdf, main.tex and images in github.uio.no manually.

## QR code

Example on creating qr code:

```
$ qrencode "https://www.uio.no/studier/emner/matnat/ifi/IN5590/h24/portfolio/" -o images/qr-code.png
```

## Color

Chose a color from https://www.overleaf.com/learn/latex/Using_colors_in_LaTeX#Accessing_additional_named_colors and alter `./better_poster.sty` line 28:
`\colorlet{exp}{<your_new_color}`
