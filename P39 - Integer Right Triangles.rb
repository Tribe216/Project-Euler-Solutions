def check_right(s1,s2,h)
    return s1**2 + s2**2 == h**2
end

def loop_thru_total(num)
    counter = 0
    1.upto(num/3) do |s1|
        s1.upto((num - s1)/2) do |s2|
            if check_right(s1,s2,num-s1-s2)
                # puts s1.to_s + " " + s2.to_s + "    " + (num-s1-s2).to_s
                counter += 1
            end
        end
    end
    return counter
end

max_tri = 0
1000.times do |i|
    num_tri = loop_thru_total(i)
    if num_tri > 0 and num_tri > max_tri
        puts i.to_s + " " + num_tri.to_s
        max_tri = num_tri
    end
end
