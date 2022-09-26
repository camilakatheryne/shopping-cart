
async def create_address(address_collection, address):
    try:
        address = await address_collection.insert_one(address)

        if address.inserted_id:
            address = await get_address(address_collection, address.inserted_id)
            return address

    except Exception as e:
        print(f'create_address.error: {e}')

async def get_address(address_collection, address_id):
    try:
        data = await address_collection.find_one({'_id': address_id})
        if data:
            return data
    except Exception as e:
        print(f'get_address.error: {e}')

async def get_addresses(address_collection, skip, limit):
    try:
        address_cursor = address_collection.find().skip(int(skip)).limit(int(limit))
        addresses = await address_cursor.to_list(length=int(limit))
        return addresses

    except Exception as e:
        print(f'get_addresses.error: {e}')

async def update_address(address_collection, address_id, address_data):
    try:
        data = {k: v for k, v in address_data.items() if v is not None}

        address = await address_collection.update_one(
            {'_id': address_id},
            {'$set': data}
        )

        if address.modified_count:
            return True, address.modified_count

        return False, 0
    except Exception as e:
        print(f'update_address.error: {e}')

async def delete_address(address_collection, address_id):
    try:
        address = await address_collection.delete_one(
            {'_id': address_id}
        )
        if address.deleted_count:
            return {'status': 'Address deleted'}
    except Exception as e:
        print(f'delete_address.error: {e}')
