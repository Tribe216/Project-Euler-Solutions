pent_set = []
best_result = [Float::INFINITY, nil, nil]
MAX_I = 3000

def gent_pent(n)
    return (n * (3*n - 1) / 2)
end

(MAX_I+1).times do |l|
    pent_set << gent_pent(l)
end

1.upto MAX_I do |i|
    (i+1).upto MAX_I do |j|
        diff = pent_set[j] - pent_set[i]
        break if diff > best_result[0]

        # puts" #{i}\t\t#{j}"

        sum = pent_set[i] + pent_set[j]
        
        if  (pent_set.include?(sum) && 
            pent_set.include?(diff) && 
            diff < best_result[0])

            best_result = diff, pent_set[i], pent_set[j]
            p best_result

        end

    end
end
