module Main where

import Criterion.Main
import Fibonacci (fibonacci, fibonacci_fold)

fibBenchmarks :: [(String, Integer -> Integer, Integer)]
fibBenchmarks =
  [ ("Naive (n=20)", fibonacci, 20)
  , ("Fold (n=1000)", fibonacci_fold, 1000)
  ]

-- Benchmark Runner
main :: IO ()
main = defaultMain
  [ bgroup "Fibonacci" (map (\(name, func, input) -> bench name $ whnf func input) fibBenchmarks)
  ]
