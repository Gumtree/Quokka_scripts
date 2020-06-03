
proc doCount120 { } {
     newfile HISTOGRAM_XY
     histmem mode time
     histmem preset 120 
     histmem start block
     save
}

doCount120
