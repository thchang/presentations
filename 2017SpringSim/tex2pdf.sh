tex "$1".tex
dvips "$1".dvi -t landscape
ps2pdf14 "$1".ps
# -dSubsetFonts=true -dEmbedAllFonts=true
