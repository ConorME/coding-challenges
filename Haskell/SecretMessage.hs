{-# LANGUAGE UnicodeSyntax #-}
module SecretMessage where

import System.Random (randomRIO)

data FourLetterAlphabet = L1 | L2 | L3 | L4 deriving (Show, Enum, Bounded)

rotN :: (Bounded a, Enum a) => Int -> a -> a
rotN alphabetSize c = toEnum rotation
   where halfAlphabet = div alphabetSize 2
         offset = fromEnum c + halfAlphabet
	 rotation = mod offset alphabetSize
	
largestCharNumber :: Int
largestCharNumber = fromEnum (maxBound :: Char)

rotChar :: Char -> Char
rotChar charToEncrypt = rotN sizeOfAlphabet charToEncrypt
   where sizeOfAlphabet = 1 + largestCharNumber

rotString :: String -> String
rotString stringToEncrypt = map rotChar stringToEncrypt

-- Three Letter Alphabet
data ThreeLetterAlphabet = Ψ | Ω | Σ deriving (Show, Enum, Bounded)

randomThreeLetter :: IO ThreeLetterAlphabet
randomThreeLetter = do
    let min = fromEnum (minBound :: ThreeLetterAlphabet)
    let max = fromEnum (maxBound :: ThreeLetterAlphabet)
    randomNum <- randomRIO (min, max)
    return (toEnum randomNum)

randomThreeLetterList :: Int -> IO [ThreeLetterAlphabet]
randomThreeLetterList n = sequence (replicate n randomThreeLetter)

threeLetterEncoder :: [ThreeLetterAlphabet] -> [ThreeLetterAlphabet]
threeLetterEncoder vals = map rot3 vals
   where rot3 = rotN 3
