
pair_list = []
line_counter = 1
File.open('./input_files/P_099.txt').each.with_index(1) do |line, line_num| 
    pair = line.split(',')
    num = pair[0].to_i
    exp = pair[1].to_i
    pair_list << [num, exp, line_num]
end
pair_list.sort! {|a,b| (a[0].to_f**(a[1].to_f/b[1])) <=> b[0] }

largest_pair = pair_list[-1]
puts "#{largest_pair[2]} #{largest_pair[0]} #{largest_pair[1]}"
