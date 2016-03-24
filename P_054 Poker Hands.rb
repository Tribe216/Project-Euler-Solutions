FILENAME = "input_files/p054_poker.txt"

def get_next_hand_set(filename)
    File.open(filename).each.with_index do |line, i| 
        card_strings = line.split()

        num = pair[0].to_i
        exp = pair[1].to_i
        pair_list << [i, num, exp]

        puts pair_list
    end
end

get_next_hand_set(FILENAME)



