vip_box = ('Monica', 'Fibi', 'Leo')
not_vip_box = ['Riri', 'Kira', None, 'Tom', None, 'Jim', 'Kate', None]
new_guests = ['Leyla', 'Gerry', 'Peter']
print(f'VIP guests: {vip_box}')
counter_place = 0
counter_guests = 0
for guest in not_vip_box:
    if not guest:
        for new_guest in new_guests:
            if len(new_guests) > counter_guests >= 0:
                not_vip_box[counter_place] = new_guests[counter_guests]
        counter_guests += 1
    counter_place += 1
print(f'Other guests: {not_vip_box}')
