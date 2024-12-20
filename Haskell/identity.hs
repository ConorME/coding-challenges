 {-# LANGUAGE UnicodeSyntax #-}

module Main where

identity :: Show a ⇒ a → a
identity x = x

main :: IO ()
main = do
	input ← getLine
	putStrLn $ identity input
