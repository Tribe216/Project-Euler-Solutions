require 'set'

1.upto 100000000 do |num|
    num = ("1" + num.to_s).to_i
    perm = true
    2.upto 6 do |mult|
        if (num*mult).to_s.split("").sort != num.to_s.split("").sort
            perm = false
            break
        end
    end

    if perm
        puts num
        break
    end
end