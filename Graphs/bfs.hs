module Graph where

data Graph a b = Empty | Context a b & Graph a b

