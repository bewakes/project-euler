
g_all = generateAll k []
    where 
          generateAll:: (Integral a) => a -> [[a]] -> [[a]]
          generateAll n lst
            | n>8 = lst
            | otherwise = generateAll (n+1) $ lst++[generate n 1 []]
          k = 3

generate:: (Integral a) => a-> a-> [a] -> [a]
generate pol n lst 
    | val>=10000 = lst
    | val<=999 = generate pol (n+1) lst
    | otherwise = generate pol (n+1) (lst++ [val])
    where val = get_nth pol n
          get_nth pol n
            | pol==3 = quot (n*(n+1)) 2
            | pol==4 = n*n
            | pol==5 = quot (n*(3*n-1)) 2
            | pol==6 = n*(2*n -1)
            | pol==7 = quot (n*(5*n-3)) 2
            | pol==8 = n*(3*n-2)
            | otherwise = -1

checkChain :: (Integral a) => a -> a -> Bool
checkChain a b = (rem a 100) == (quot b 100)

findSet :: (Integral a) => [[a]] -> [a]
findSet allpolys = fillCycle [] allpolys
    where fillCycle lst polys 
                | checkChain (last lst) (head $ take 1 polys) = 

main = do
    putStrLn $ show answer
    where answer = findSet g_all

