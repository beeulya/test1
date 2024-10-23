# TODO Найдите количество книг, которое можно разместить на дискете
books=0
Inform_vol_Mb=1.44
Inform_vol_Kb=Inform_vol_Mb*1024
Inform_vol_b=Inform_vol_Kb*1024
num_pages=100
num_strings=50
num_symbols=25
bytes_for_one_symbol=4
num_symbols_in_the_book=num_pages*num_strings*num_symbols
bytes_for_one_book=num_symbols_in_the_book*bytes_for_one_symbol
books=Inform_vol_b/bytes_for_one_book
print("Количество книг, помещающихся на дискету:", int(books))
