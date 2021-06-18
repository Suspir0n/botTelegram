from flask import current_app, jsonify
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

def get_all(model, schemas, name_model):
    logging.info('\033[1;34mGetting all the data...\033[m')
    data = model.query.all()
    if data:
        logging.info('\033[1;34mGot something...\033[m')
        result = schemas.dump(data)
        logging.info('\033[1;34mSuccessfully obtained!\033[m')
        return jsonify({'message': 'successfully fetched', 'data': result}), 200
    logging.info('\033[1;31mThere is no data!\033[m')
    return jsonify({'message': f'{name_model} dont exist', 'data': {}}), 404


def get_one(uid, model, schema, name_model):
    logging.info('\033[1;34mGetting one data...\033[m')
    data = model.query.get(uid)
    if data:
        logging.info('\033[1;34mGot something...\033[m')
        result = schema.dump(data)
        logging.info('\033[1;34mSuccessfully obtained!\033[m')
        return jsonify({'message': 'successfully fetched', 'data': result}), 201
    logging.info('\033[1;31mThere is no data!\033[m')
    return jsonify({'message': f'{name_model} dont exist', 'data': {}}), 404


def delete(uid, model, schema, name_model):
    logging.info('\033[1;34mDeleting one data...\033[m')
    data = model.query.get(uid)
    if not data:
        logging.info('\033[1;31mThere is no data!\033[m')
        return jsonify({'message': f'{name_model} dont exist', 'data': {}}), 404
    if data:
        logging.info('\033[1;34mDeleting...\033[m')
        try:
            current_app.db.session.delete(data)
            current_app.db.session.commit()
            result = schema.dump(data)
            logging.info('\033[1;34mSuccessfully deleted!\033[m')
            return jsonify({'message': 'successfully deleted', 'data': result}), 200
        except Exception as error:
            logging.info('\033[1;31mUnable to delete!\033[m')
            return jsonify({'message': 'unable to delete', 'data': {}}), 404


def update(schema, data, name_model):
    logging.info('\033[1;34mUpdating one data...\033[m')
    if not data:
        logging.info('\033[1;31mThere is no data!\033[m')
        return jsonify({'message': f"{name_model} don't exist", 'data': {}}), 404
    if data:
        logging.info('\033[1;34mUpdating...\033[m')
        try:
            current_app.db.session.commit()
            result = schema.dump(data)
            logging.info('\033[1;34mSuccessfully updated!\033[m')
            return jsonify({'message': 'successfully updated', 'data': result}), 201
        except:
            logging.info('\033[1;31mUnable to update!\033[m')
            return jsonify({'message': 'unable to update', 'data': {}}), 404


def post(schema, data):
    logging.info('\033[1;34mSaving one data...\033[m')
    try:
        logging.info('\033[1;34mSaving...\033[m')
        current_app.db.session.add(data)
        current_app.db.session.commit()
        result = schema.dump(data)
        logging.info('\033[1;34mSuccessfully registered!\033[m')
        return jsonify({'message': 'successfully registered', 'data': result}), 201
    except Exception as error:
        logging.info('\033[1;31mUnable to create!\033[m')
        return jsonify({'message': 'unable to create', 'data': {}, 'error': error}), 500