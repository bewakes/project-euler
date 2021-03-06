modulo :: Integer
modulo = 1000000007

fst3Tuple :: (a, a, a) -> a
fst3Tuple (x, _, _) = x

-- Get the value of number ^ power mod (modulo)
numberPowerMod :: Integer -> Integer -> Integer -> Integer
numberPowerMod number pow modulus
  | pow < 0 = numberPowerMod number (modulus - pow) modulus
  | otherwise = fst3Tuple $ until (\(_, y, _) -> y == 0) getModulusAndCount (1, pow, number `rem` modulus)
    where getModulusAndCount (result, c, prevPow) = if even c then (result, c `div` 2, currPow)
                                                              else ((result * prevPow) `rem` modulus, c `div` 2, currPow)
                                                  where currPow = prevPow * prevPow `rem` modulus

tenPowerMod :: Integer -> Integer -> Integer
tenPowerMod = numberPowerMod 10

fibs :: [Integer]
fibs = 0: 1: zipWith (+) fibs (tail fibs)

-- Very concise function to calculate inverse digit sum.
-- The idea is that, for a given number n, the number whose digit sums equal n will be
-- rem * (10 ^ q) + (10 ^ q - 1) where rem = n % 9 and q = n // 9(integer division)
--
-- To calculate sum of numbers each of which are the numbers which digit sums equal i
-- where i ranges from 1 to n,
-- We write the formula in sum terms and find a pattern that goes like this:
--    [(1 * 10^0)+(10^0- 1)] + [(2 * 10^0)+(10^0- 1)] + ... + [(0 * 10^0)+(10^1- 1)] + [(1 * 10^0)+(10^1- 1)]...
--  = [(0 * 10^0) + (1 * 10^0) + (2*10^0) + ... (8*10^0) + 9 * 10^0 - 9] + [(0 * 10^1) + (1 * 10^1) + (2*10^1) + ... (8*10^1) + 9 * 10^1 - 9] + ...
--
-- So, given the number n, and letting k = n // 9 and r = n % 9 the sum now becomes
-- [(0 + 1 + 2 + 3 + ... + 8) * 10^ i + 9 * 10 ^ i - 9] + [(0 + 1 + 2 + ... + r) * 10 ^ k + (r+1) * 10 ^ k, where i ranges from 0 to k - 1
--  = [sum(36*10^i + 8*10^i) where i ranges from 0 to k-1 ] + r(r+1)*10^k / 2 + (r+1) * 10^k
--  = 5 * (10^k-1) + (r+2)(r+1)*10^k /2  - n - 1
moduloSumInverseDigitsUpto :: Integer -> Integer -> Integer
moduloSumInverseDigitsUpto n md = 5 * (tenPowK - 1) + (r+2) * (r+1) * tenPowK `div` 2 - n - 1
    where k = n `div` 9
          r = n `rem` 9
          tenPowK = tenPowerMod k md


main :: IO ()
main = print $ (sum [moduloSumInverseDigitsUpto x modulo | x <- drop 2 (take 91 fibs)] `rem` modulo + modulo) `rem` modulo
