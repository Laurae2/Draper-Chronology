import caffe
import lmdb

lmdb_env = lmdb.open('/home/laurae-linux/Documents/Data_Science/Caffe/train')
lmdb_txn = lmdb_env.begin()
lmdb_cursor = lmdb_txn.cursor()
datum = caffe.proto.caffe_pb2.Datum()

for key, value in lmdb_cursor:
    datum.ParseFromString(value)
    label = datum.label
    data = caffe.io.datum_to_array(datum)
    print(data)
    for l, d in zip(label, data):
            print l, d
    sys.exit()
