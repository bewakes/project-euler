module Main where

import Control.Monad.State.Strict
import System.Random
import Data.Array.IO
import Data.List (minimumBy, sortBy)
import Data.Ord (comparing)
import Data.Map hiding (map, take)

diceSides = 4
totalSquares = 40
numberRuns = 1000000

jail = 10
go = 0
c1 = 11
e3 = 24
h2 = 39
r1 = 5

rs = [5, 15, 25, 35]
us = [12, 28]

gtj = 30
cc = [2, 17, 33]
ch = [7, 22, 36]

nextR x = rs !! minind
    where diffs = map (\p -> (p - x) `mod` totalSquares) rs
          minind = fst $ minimumBy (comparing snd) $ zip [0..] diffs

nextU x = us !! minind
    where diffs = map (\p -> (p - x) `mod` totalSquares) us
          minind = fst $ minimumBy (comparing snd) $ zip [0..] diffs

-- Copied from: https://wiki.haskell.org/Random_shuffle
shuffle :: [a] -> IO [a]
shuffle xs = do
        ar <- newArray n xs
        forM [1..n] $ \i -> do
            j <- randomRIO (i,n)
            vi <- readArray ar i
            vj <- readArray ar j
            writeArray ar j vi
            return vj
  where
    n = length xs
    newArray :: Int -> [a] -> IO (IOArray Int a)
    newArray n xs =  newListArray (1,n) xs

data Monopoly = Monopoly
    { currentPosition :: Int
    , doublesCount :: Int
    , ccPile :: [Int]
    , chPile :: [Int]
    , positionFrequencies :: Map Int Int
    , currentGenerator :: StdGen
    }

shiftLeft :: [a] -> [a]
shiftLeft [] = []
shiftLeft (x:xs) = xs ++ [x]

run :: State Monopoly ()
run = state createState
    where createState (Monopoly p d cp chp f g) = ((), Monopoly newP newD newCp newChP newF newG)
            where (dice1, g') = randomR (1, diceSides) g
                  (dice2, newG) = randomR (1, diceSides) g'

                  obtainedP = (p + dice1 + dice2) `mod` totalSquares
                  doubles = if dice1 == dice2 then d + 1 else 0
                  newD = if doubles == 3 then 0 else doubles

                  (newP, newCp, newChP) = evalObtainedP doubles obtainedP
                  newF = insertWith (+) newP 1 f
                  evalObtainedP 3 _ = (jail, cp, chp)
                  evalObtainedP _ 30 = (jail, cp, chp) -- goto jail

                  evalObtainedP _ x
                    | x `elem` cc = case head cp of
                                        1 -> (go, shiftLeft cp, chp)
                                        2 -> (jail, shiftLeft cp, chp)
                                        _ -> (x, shiftLeft cp, chp)
                    | x `elem` ch = case head chp of
                                        1 -> (go, cp, shiftLeft chp)
                                        2 -> (jail, cp, shiftLeft chp)
                                        3 -> (c1, cp, shiftLeft chp)
                                        4 -> (e3, cp, shiftLeft chp)
                                        5 -> (h2, cp, shiftLeft chp)
                                        6 -> (r1, cp, shiftLeft chp)
                                        7 -> (nextR x, cp, shiftLeft chp)
                                        8 -> (nextR x, cp, shiftLeft chp)
                                        9 -> (nextU x, cp, shiftLeft chp)
                                        10 -> ((x - 3) `mod` totalSquares, cp, shiftLeft chp)
                                        _ -> (x, cp, shiftLeft chp)
                    | otherwise = (x, cp, chp)


main :: IO ()
main = do
    g <- getStdGen
    shuffledCC <- shuffle [1..16]
    shuffledCHC <- shuffle [1..16]
    let mstate = Monopoly 0 0 shuffledCC shuffledCHC empty g
        m = (execState (replicateM numberRuns run) mstate)
        sorted = sortBy (comparing ((\x -> -x) . snd)) (toList $ positionFrequencies m)
    print $ take 3 $ map fst sorted
