(defun is_prime (num)
    "check if a number is prime"
    (if (eql num 1) (return-from is_prime nil))
    (dotimes (i (- (isqrt num) 2)) 
        (if (zerop (mod num (+ i 2))) (
            return-from is_prime nil)))
    (return-from is_prime t))

(let ((largest_prime_factor 0) (input_num 600851475143))

(loop 
    (progn 
        (dotimes (i input_num) 
            (if (and (zerop (mod input_num (+ i 1))) (is_prime (+ i 1)))
                (progn
                    (setq input_num (/ input_num (+ i 1)))
                    (if (> (+ i 1) largest_prime_factor)
                        (setq largest_prime_factor (+ i 1)))
                (return))))
        (if (eql input_num 1)(return))))

(write largest_prime_factor)
(write-line ""))