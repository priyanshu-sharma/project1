with buy_data as (
    select stock_name, sum(price) as buy_price from Stocks group by stock_name, operation having operation = 'Buy' 
), sell_data as (
    select stock_name, sum(price) as sell_price from Stocks group by stock_name, operation having operation = 'Sell' 
) select s.stock_name, s.sell_price - b.buy_price as capital_gain_loss  from sell_data s inner join buy_data b on s.stock_name = b.stock_name;