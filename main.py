import json
from fastapi import Depends, FastAPI, HTTPException, status

with open("pesanan.json", "r") as read_file:
    data = json.load(read_file)
app = FastAPI()

@app.get('/pesanan/{item_id}')                                                  #melihat status pesanan
async def read_pesanan(item_id: int): 
    for menu_item in data['pesanan']:
        if menu_item['id_pesanan'] == item_id:
            return menu_item
    raise HTTPException(
        status_code=404, detail=f'Pesanan tidak ditemukan!'
        )

@app.post('/add-pesanan/{item_id}')                                              #menambahkan pesanan
async def write_pesanan(jumlah: int)):
    item_id = len(data['pesanan'])+1
    newdata = {'id': item_id, 'kuantitas' : jumlah}
    if(item_id > 1):
        data['pesanan'].append(newdata)
        with open("pesanan.json", "w") as write_file:
            json.dump(data, write_file)
        write_file.close()
        return data
        
@app.put('/change-status/{item_id}')                                           #mengubah status pesanan
async def update_status(item_id: int, new_stat: str):
    for menu_item in data['menu']:
        if menu_item['id'] == item_id:
            menu_item['status'] = new_stat 
        read_file.close()    
        with open("menu.json", "w") as write_file:
            json.dump(data, write_file,indent=4)
        write_file.close()
    return {'message':'Data changed successfully'}
