(defun is_prime (num)
    "check if a number is prime"
    (if (eql num 1) (return-from is_prime nil))
    (dotimes (i (- (isqrt num) 2)) 
        (if (zerop (mod num (+ i 2))) (
            return-from is_prime nil)))
    (return-from is_prime t))

(let ((total 0) (threshold 2000000))

(dotimes (i (- threshold 2))
    (if (is_prime (+ i 2))
    (incf total (+ i 2)))
)

(write total)
(write-line "")
)