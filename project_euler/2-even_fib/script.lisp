(
    let ((i 0) (a 0) (b 1) (total 0))

    (loop (progn
        (if (= (mod i 2) 0) 
            (progn
                (setq a (+ a b))
                (if (>= a 4000000) (return))
                (if (eql (mod a 2) 0) (incf total a)))
            (progn 
                (setq b (+ a b)) 
                (if (>= b 4000000) (return))
                (if (eql (mod b 2) 0) (incf total b))))
        (incf i 1)
    ))

    (write total)
    (write-line "") 
)