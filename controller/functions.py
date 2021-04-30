from google.protobuf.timestamp_pb2 import Timestamp

def PtimeToPBtime(Ptime):
    PBtime = Timestamp()
    PBtime.FromDatetime(Ptime)
    return PBtime

def PBtimeToPtime(PBtime):
    return PBtime.ToDatetime()

