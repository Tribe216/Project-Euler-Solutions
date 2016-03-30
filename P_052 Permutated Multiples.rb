def factorial(num) 
    return num.downto(1).inject(:*) 
end

def combos(n,r)
    return (factorial(n) / (factorial(r) * factorial(n-r)))
end


master_counter = 0
2.upto 100 do |n|
    (n/2).downto(1) do |r|
        if combos(n,r) > 1000000
            if r*2 == n
                master_counter += 1
            else
                master_counter += 2
            end
        else
            break
        end
    end
end

puts master_counter