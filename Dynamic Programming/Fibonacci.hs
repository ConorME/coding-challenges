module Fibonacci where

fibonacci :: Integer -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n - 1) + fibonacci (n - 2)

fibonacci_fold :: Integer -> Integer
fibonacci_fold n = fst $ foldl (\(a, b) _ -> (b, a + b)) (0, 1) [1..n]

