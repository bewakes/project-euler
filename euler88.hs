module Main where

import           Control.Monad.State
import qualified Data.Map            as M
import           Data.Maybe
import qualified Data.Set            as S

type KMinsMap = M.Map Int Int

maxK :: Int
maxK = 12000

infinity = 999999999

nums :: [Int]
nums = [2..maxK]

-- Initial map of k and minProduct
minsForKs :: KMinsMap
minsForKs = M.fromList $ map (\x -> (x, infinity)) [1..maxK]

kForSet :: [Int] -> Int
kForSet numbers = product numbers - sum numbers + length numbers

generate :: KMinsMap -> [Int] -> [Int] -> KMinsMap
generate minMap currentList currentPool
  | k > maxK = minMap
  | otherwise = foldr run updatedMap filteredPoolElements
  where run itm accMap = generate accMap (itm: currentList) currentPool
        updatedMap = if prod <= fromJust (M.lookup k minMap) then M.insert k prod minMap else minMap
        filteredPoolElements = takeWhile appendedPoolLessThanMaxK (filter (>= head currentList) currentPool)
        appendedPoolLessThanMaxK = (<= maxK) . kForSet . (:currentList)
        prod = product currentList
        k = kForSet currentList

generateAll minMap [] = minMap
generateAll minMap ((lst, pool): xs) = generateAll (generate minMap lst pool) xs

allpools = map (\i -> ([nums !! i], drop i nums)) [0..length nums-1]

calculateUniqueSum minMap = (sum . S.toList) $ S.fromList $ M.elems minMap

main :: IO ()
main = do
    let sumK = calculateUniqueSum $ generateAll minsForKs allpools
    print $ sumK - 2  -- -2 because it includes minimum for k = 1 which we exclude
