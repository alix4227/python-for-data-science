#!/usr/bin/env python3.10

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#ft_list
ft_list[1] = "World!"

#ft_tuple
cast_tuple = list(ft_tuple)
cast_tuple[1] = "France!"
ft_tuple = tuple(cast_tuple)

#ft_set
ft_set.remove("tutu!")
ft_set.add("Paris!")

#ft_dict
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

