#tiles = 10
#row = 3  # 3 pieces per row

#Dictionary
tilecolor = {'red' : 100, 'blue' :200, 'yellow' :300, 'black' :400, 'orange':500, 'green': 600}

#Show color and price
print('----สีและราคากระเบื้อง----')
for c,p in tilecolor.items():
        print(f'สี: {c} ราคา: {p}')




#User input 
    #Try - Except
try:
        tiles = int(input('คุณต้องการปูกระเบื้องทั้งหมดกี่แผ่น : '))
        row = int(input('ใน 1 แถว ต้องปูกระเบื้องกี่แผ่น : '))
        color = input('ต้องการกระเบื้องสีอะไร [red, blue, yellow, black, orange, green]: ')
except:
         print('กรอกข้อมูลเฉพาะตัวเลขเท่านั้น')
         tiles = int(input('คุณต้องการปูกระเบื้องทั้งหมดกี่แผ่น : '))
         row = int(input('ใน 1 แถว ต้องปูกระเบื้องกี่แผ่น : '))
         color = input('ต้องการกระเบื้องสีอะไร [red, blue, yellow, black, orange, green]: ')

#Calculation          
total_row = tiles // row
remain_tiles = tiles % row
buy_more = row - remain_tiles
total_cost = (buy_more * tilecolor[color])

print(f'มีกระเบื้องทั้งหมด : {tiles} แผ่น')
print(f'1 แถว ปูกระเบื้องได้ทั้งหมด {row} แผ่น')
print('----- Calculation -----')
print(f'ปูกระเบื้องได้ทั้งหมด {total_row} แถว')
print(f'เหลือกระเบื้องที่ไม่ได้ปูเต็มแถว {remain_tiles} แผ่น')
print(f'ลูกค้าต้องซื้อกระเบื้องเพิ่ม {buy_more} แผ่น')
print(f'รวมค่าใช้จ่ายสำหรับสั่งซื้อกระเบื้องเพิ่ม : {total_cost}')

print('-----------End of code-----------\n\n')