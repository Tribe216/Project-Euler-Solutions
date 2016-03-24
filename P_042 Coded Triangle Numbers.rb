FILENAME = "input_files/p042_words.txt"

def get_words_array(filename)
    file_str = File.open(filename).read.strip
    file_str.gsub!('"','')
    words = file_str.split(",")
    p words
end

get_words_array(FILENAME)



