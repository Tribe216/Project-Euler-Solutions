top = 3
bot = 2
longer_top_count = 0

2.upto(1000) do |_|
    new_top = (2*bot + top)
    bot = (bot + top)
    top = new_top
    longer_top_count +=1 if top.to_s.length > bot.to_s.length
    puts longer_top_count
end
