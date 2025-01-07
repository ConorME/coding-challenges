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

rotEncoder :: String -> String
rotEncoder text = rotString text

xorBool :: Bool -> Bool -> Bool
xorBool x y = (x || y) && (not (x && y))

xorPair :: (Bool, Bool) -> Bool
xorPair (x, y) = xorBool x y

xor :: [Bool] -> [Bool] -> [Bool]
xor α β = map xorPair (zip α β)

type BitString = [Bool]

intToBitString' :: Int -> BitString
intToBitString' 0 = [False]
intToBitString' 1 = [True]
intToBitString' n = if (remainder == 0)
		      then False : intToBitString' nextVal
		      else True :  intToBitString' nextVal
   where remainder = mod n 2
         nextVal  = div n 2

maxBits :: Int
maxBits = length (intToBitString' maxBound)

intToBitString :: Int -> BitString
intToBitString n = leadingFalses ++ reversedBits
   where reversedBits = reverse (intToBitString' n)
         missingBits = maxBits - (length reversedBits)
	 leadingFalses = take missingBits (cycle [False])

charToBitString :: Char -> BitString 
charToBitString char = intToBitString (fromEnum char)

bitsToInt :: BitString -> Int
bitsToInt bits = sum (map (\x -> 2^(snd x)) trueLocations)
   where size = length bits
         indices = [size -1, size-2 .. 0]
         trueLocations = filter (\x -> fst x == True) (zip bits indices)

bitsToChar :: BitString -> Char
bitsToChar bits = toEnum (bitsToInt bits)

