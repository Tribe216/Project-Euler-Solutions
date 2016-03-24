FILENAME = "input_files/p042_words.txt"

def get_triangles(max_len)
    values = []
    n = 1
    while true
        tri_val = 0.5*(n**2 + n)
        if tri_val < max_len*26
            values << tri_val.to_i
            n += 1
        else
            break
        end
    end
    return values
end

def get_words_array(filename)
    file_str = File.open(filename).read.strip
    file_str.gsub!('"','')
    words = file_str.split(",")
    return words
end

words = get_words_array(FILENAME)

max_length = 0
words.each do |word|
    if word.length > max_length
        max_length = word.length
    end
end

tri_list = get_triangles(max_length)
tri_counter = 0

words.each do |word|
    word_sum = 0
    
    word.each_byte do |ascii_val|
        letter_value = ascii_val - 64
        word_sum += letter_value
    end

    if tri_list.include?(word_sum)
        tri_counter += 1
    end
end

p tri_counter
