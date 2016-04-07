FILENAME = "input_files/p059_cipher.txt"

def get_input_array(filename)
    file_str = File.open(filename).read.strip
    char_list = file_str.strip.split(",")
    ascii_list = []
    char_list.each {|c| ascii_list << c.to_i}
    return ascii_list
end

def decrypt(message_ascii_a, key_ascii_a)
    output_message = ""
    l = key_ascii_a.length
    message_ascii_a.each.with_index do |char_i,i|
        output_message << (char_i ^ key_ascii_a[i % l]).chr
    end
    output_message
end

massage_ascii_list =  get_input_array(FILENAME)

97.upto(122) do |a|
    97.upto(122) do |b|
        97.upto(122) do |c|
            d_mes = decrypt(massage_ascii_list,[a,b,c])
            if d_mes.include?(" the ")
                puts "#{a} #{b} #{c}\t#{d_mes}"
                sum = 0
                d_mes.split("").each {|c| sum += c.ord}
                puts sum
            end
        end
    end
end
