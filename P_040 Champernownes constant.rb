
def get_champ_digit(pn)
    if pn < 10
        return pn
    end

    i = 1
    place_counter = 10
    while true
        if (place_counter + ( (10**(i+1)) - (10**i)) * (i+1) ) <= pn
            place_counter += ( (10**(i+1)) - (10**i)) * (i+1)
            i += 1
        else
            rem = pn - place_counter
            start_num = 10**i
            digit_places = i+1
            the_num = start_num + (rem/digit_places)

            num_str = the_num.to_s
            d = num_str[rem % (i+1)]
            return d.to_i
        end
    end
end

mult_val = 1
0.upto 6 do |i|
    the_digit = get_champ_digit(10**i)
    puts i.to_s + " " + the_digit.to_s
    mult_val *= the_digit
    puts mult_val.to_s
end
