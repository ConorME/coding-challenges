{-# LANGUAGE UnicodeSyntax #-}

module Symmetry3 where

data Symmetry3 = Γ | Δ | Ψ deriving (Show, Eq)

instance Semigroup Symmetry3 where
	(<>) Γ x  = x
	(<>) x Γ  = x
	(<>) Δ Δ  = Ψ
	(<>) Δ Ψ  = Γ
	(<>) Ψ Δ  = Γ
	(<>) Ψ Ψ  = Δ

instance Monoid Symmetry3 where
	mempty = Γ

(~) :: Symmetry3 -> Symmetry3
(~) Γ = Γ
(~) Δ = Ψ
(~) Ψ = Δ

