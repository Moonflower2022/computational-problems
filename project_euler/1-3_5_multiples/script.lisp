(let ((sum 0))
    
(dotimes (i 1000)(if (or (= (mod (+ i 1) 3) 0) (= (mod (+ i 1) 5) 0)) (incf sum (+ i 1))))
(write sum)
)

(write-line "") 