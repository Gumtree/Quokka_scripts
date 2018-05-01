proc doCount { } {
     newfile HISTOGRAM_XY
     histmem mode time
     histmem preset 300 
     histmem start block
     save
}

for {set i 0} {$i < 1000} { incr i} {
doCount
} 
