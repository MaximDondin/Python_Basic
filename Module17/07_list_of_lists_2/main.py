nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = [j_numb[k_numb]
            for i_numb in nice_list
            for j_numb in i_numb
            for k_numb in range(len(nice_list[0][0]))]
print('Ответ:', new_list)