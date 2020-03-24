modulo = 1000000007

digitSum :: Integer -> Integer
digitSum num = snd $ until numEqualsZero divideAndAddRem (num, 0)
    where divideAndAddRem (nm, sm) = (nm `div` 10, sm + nm `rem` 10)
          numEqualsZero = (== 0) . fst

-- Smallest Number with given sum is always in the format (reminder)(all 9s) such
-- that reminder + all 9s add up to the given sum
smallestNumWithSum :: Integer -> Integer
smallestNumWithSum sm = rm * (10 ^ q) + (10 ^ q - 1)
    where q = sm `div` 9
          rm = sm `rem` 9

fst3Tuple :: (a, a, a) -> a
fst3Tuple (x, _, _) = x

-- Get the value of 10 ^ number mod (modulo)
tenPowerMod :: Integer -> Integer -> Integer
tenPowerMod pow modulus = fst3Tuple $ until (\(_, y, _) -> y == 0) getModulusAndCount (1, pow, 10 `rem` modulus)
    where getModulusAndCount (result, c, prevPow) = if even c then (result, c `div` 2, currPow)
                                                              else ((result * prevPow) `rem` modulus, c `div` 2, currPow)
                                                  where currPow = prevPow * prevPow `rem` modulus

-- for large numbers the result becomes very very big so use modulo
smallestNumWithSumModulo :: Integer -> Integer -> Integer
smallestNumWithSumModulo sm modulus = rm * powerMod + (powerMod -1)
    where q = sm `div` 9
          rm = sm `rem` 9
          powerMod = tenPowerMod q modulus


sumUpto :: Integer -> (Integer -> Integer) -> Integer
sumUpto n f = sum $ map f [1..n]

fibs :: [Integer]
fibs = 0: 1: zipWith (+) fibs (tail fibs)

fibsFrom2 = drop 2 fibs

main :: IO ()
main = do
    print $ sum $ map (`smallestNumWithSumModulo` modulo) (take 90 fibsFrom2)
