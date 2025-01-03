#
# Autogenerated by Thrift Compiler (0.18.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import alirosll.ttypes

from thrift.transport import TTransport
all_structs = []


class MetricData(object):
    """
    Attributes:
     - value

    """


    def __init__(self, value=None,):
        self.value = value

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.DOUBLE:
                    self.value = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('MetricData')
        if self.value is not None:
            oprot.writeFieldBegin('value', TType.DOUBLE, 1)
            oprot.writeDouble(self.value)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class MetricMetadata(object):
    """
    Attributes:
     - metricType
     - metricLabels

    """


    def __init__(self, metricType=None, metricLabels=None,):
        self.metricType = metricType
        self.metricLabels = metricLabels

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I16:
                    self.metricType = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.MAP:
                    self.metricLabels = {}
                    (_ktype1, _vtype2, _size0) = iprot.readMapBegin()
                    for _i4 in range(_size0):
                        _key5 = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                        _val6 = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                        self.metricLabels[_key5] = _val6
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('MetricMetadata')
        if self.metricType is not None:
            oprot.writeFieldBegin('metricType', TType.I16, 1)
            oprot.writeI16(self.metricType)
            oprot.writeFieldEnd()
        if self.metricLabels is not None:
            oprot.writeFieldBegin('metricLabels', TType.MAP, 2)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.metricLabels))
            for kiter7, viter8 in self.metricLabels.items():
                oprot.writeString(kiter7.encode('utf-8') if sys.version_info[0] == 2 else kiter7)
                oprot.writeString(viter8.encode('utf-8') if sys.version_info[0] == 2 else viter8)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class MetricQuery(object):
    """
    Attributes:
     - categoryName
     - metricName

    """


    def __init__(self, categoryName=None, metricName=None,):
        self.categoryName = categoryName
        self.metricName = metricName

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.categoryName = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.metricName = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('MetricQuery')
        if self.categoryName is not None:
            oprot.writeFieldBegin('categoryName', TType.STRING, 1)
            oprot.writeString(self.categoryName.encode('utf-8') if sys.version_info[0] == 2 else self.categoryName)
            oprot.writeFieldEnd()
        if self.metricName is not None:
            oprot.writeFieldBegin('metricName', TType.STRING, 2)
            oprot.writeString(self.metricName.encode('utf-8') if sys.version_info[0] == 2 else self.metricName)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class MetricQueryReq(object):
    """
    Attributes:
     - query

    """


    def __init__(self, query=None,):
        self.query = query

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.query = MetricQuery()
                    self.query.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('MetricQueryReq')
        if self.query is not None:
            oprot.writeFieldBegin('query', TType.STRUCT, 1)
            self.query.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class MetricQueryReply(object):
    """
    Attributes:
     - status
     - metricData

    """


    def __init__(self, status=None, metricData=None,):
        self.status = status
        self.metricData = metricData

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.metricData = MetricData()
                    self.metricData.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('MetricQueryReply')
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.I32, 1)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        if self.metricData is not None:
            oprot.writeFieldBegin('metricData', TType.STRUCT, 2)
            self.metricData.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class MetricCategoriesQueryReply(object):
    """
    Attributes:
     - status
     - categoryNames

    """


    def __init__(self, status=None, categoryNames=None,):
        self.status = status
        self.categoryNames = categoryNames

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.categoryNames = []
                    (_etype12, _size9) = iprot.readListBegin()
                    for _i13 in range(_size9):
                        _elem14 = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                        self.categoryNames.append(_elem14)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('MetricCategoriesQueryReply')
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.I32, 1)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        if self.categoryNames is not None:
            oprot.writeFieldBegin('categoryNames', TType.LIST, 2)
            oprot.writeListBegin(TType.STRING, len(self.categoryNames))
            for iter15 in self.categoryNames:
                oprot.writeString(iter15.encode('utf-8') if sys.version_info[0] == 2 else iter15)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class MetricNamesQueryReq(object):
    """
    Attributes:
     - categoryName

    """


    def __init__(self, categoryName=None,):
        self.categoryName = categoryName

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.categoryName = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('MetricNamesQueryReq')
        if self.categoryName is not None:
            oprot.writeFieldBegin('categoryName', TType.STRING, 1)
            oprot.writeString(self.categoryName.encode('utf-8') if sys.version_info[0] == 2 else self.categoryName)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class MetricNamesQueryReply(object):
    """
    Attributes:
     - status
     - metricNames

    """


    def __init__(self, status=None, metricNames=None,):
        self.status = status
        self.metricNames = metricNames

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.metricNames = []
                    (_etype19, _size16) = iprot.readListBegin()
                    for _i20 in range(_size16):
                        _elem21 = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                        self.metricNames.append(_elem21)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('MetricNamesQueryReply')
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.I32, 1)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        if self.metricNames is not None:
            oprot.writeFieldBegin('metricNames', TType.LIST, 2)
            oprot.writeListBegin(TType.STRING, len(self.metricNames))
            for iter22 in self.metricNames:
                oprot.writeString(iter22.encode('utf-8') if sys.version_info[0] == 2 else iter22)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class MetricMetadataQueryReq(object):
    """
    Attributes:
     - categoryName
     - metricName

    """


    def __init__(self, categoryName=None, metricName=None,):
        self.categoryName = categoryName
        self.metricName = metricName

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.categoryName = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.metricName = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('MetricMetadataQueryReq')
        if self.categoryName is not None:
            oprot.writeFieldBegin('categoryName', TType.STRING, 1)
            oprot.writeString(self.categoryName.encode('utf-8') if sys.version_info[0] == 2 else self.categoryName)
            oprot.writeFieldEnd()
        if self.metricName is not None:
            oprot.writeFieldBegin('metricName', TType.STRING, 2)
            oprot.writeString(self.metricName.encode('utf-8') if sys.version_info[0] == 2 else self.metricName)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class MetricMetadataQueryReply(object):
    """
    Attributes:
     - status
     - metadata

    """


    def __init__(self, status=None, metadata=None,):
        self.status = status
        self.metadata = metadata

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.metadata = MetricMetadata()
                    self.metadata.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('MetricMetadataQueryReply')
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.I32, 1)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        if self.metadata is not None:
            oprot.writeFieldBegin('metadata', TType.STRUCT, 2)
            self.metadata.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class MetricLabelsQueryReq(object):
    """
    Attributes:
     - categoryName
     - metricName

    """


    def __init__(self, categoryName=None, metricName=None,):
        self.categoryName = categoryName
        self.metricName = metricName

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.categoryName = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.metricName = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('MetricLabelsQueryReq')
        if self.categoryName is not None:
            oprot.writeFieldBegin('categoryName', TType.STRING, 1)
            oprot.writeString(self.categoryName.encode('utf-8') if sys.version_info[0] == 2 else self.categoryName)
            oprot.writeFieldEnd()
        if self.metricName is not None:
            oprot.writeFieldBegin('metricName', TType.STRING, 2)
            oprot.writeString(self.metricName.encode('utf-8') if sys.version_info[0] == 2 else self.metricName)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class MetricLabelsQueryReply(object):
    """
    Attributes:
     - status
     - metricLabels

    """


    def __init__(self, status=None, metricLabels=None,):
        self.status = status
        self.metricLabels = metricLabels

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.MAP:
                    self.metricLabels = {}
                    (_ktype24, _vtype25, _size23) = iprot.readMapBegin()
                    for _i27 in range(_size23):
                        _key28 = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                        _val29 = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                        self.metricLabels[_key28] = _val29
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('MetricLabelsQueryReply')
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.I32, 1)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        if self.metricLabels is not None:
            oprot.writeFieldBegin('metricLabels', TType.MAP, 2)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.metricLabels))
            for kiter30, viter31 in self.metricLabels.items():
                oprot.writeString(kiter30.encode('utf-8') if sys.version_info[0] == 2 else kiter30)
                oprot.writeString(viter31.encode('utf-8') if sys.version_info[0] == 2 else viter31)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class MetricTypeQueryReq(object):
    """
    Attributes:
     - categoryName
     - metricName

    """


    def __init__(self, categoryName=None, metricName=None,):
        self.categoryName = categoryName
        self.metricName = metricName

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.categoryName = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.metricName = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('MetricTypeQueryReq')
        if self.categoryName is not None:
            oprot.writeFieldBegin('categoryName', TType.STRING, 1)
            oprot.writeString(self.categoryName.encode('utf-8') if sys.version_info[0] == 2 else self.categoryName)
            oprot.writeFieldEnd()
        if self.metricName is not None:
            oprot.writeFieldBegin('metricName', TType.STRING, 2)
            oprot.writeString(self.metricName.encode('utf-8') if sys.version_info[0] == 2 else self.metricName)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class MetricTypeQueryReply(object):
    """
    Attributes:
     - status
     - metricType

    """


    def __init__(self, status=None, metricType=None,):
        self.status = status
        self.metricType = metricType

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.metricType = iprot.readI16()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('MetricTypeQueryReply')
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.I32, 1)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        if self.metricType is not None:
            oprot.writeFieldBegin('metricType', TType.I16, 2)
            oprot.writeI16(self.metricType)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(MetricData)
MetricData.thrift_spec = (
    None,  # 0
    (1, TType.DOUBLE, 'value', None, None, ),  # 1
)
all_structs.append(MetricMetadata)
MetricMetadata.thrift_spec = (
    None,  # 0
    (1, TType.I16, 'metricType', None, None, ),  # 1
    (2, TType.MAP, 'metricLabels', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 2
)
all_structs.append(MetricQuery)
MetricQuery.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'categoryName', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'metricName', 'UTF8', None, ),  # 2
)
all_structs.append(MetricQueryReq)
MetricQueryReq.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'query', [MetricQuery, None], None, ),  # 1
)
all_structs.append(MetricQueryReply)
MetricQueryReply.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'status', None, None, ),  # 1
    (2, TType.STRUCT, 'metricData', [MetricData, None], None, ),  # 2
)
all_structs.append(MetricCategoriesQueryReply)
MetricCategoriesQueryReply.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'status', None, None, ),  # 1
    (2, TType.LIST, 'categoryNames', (TType.STRING, 'UTF8', False), None, ),  # 2
)
all_structs.append(MetricNamesQueryReq)
MetricNamesQueryReq.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'categoryName', 'UTF8', None, ),  # 1
)
all_structs.append(MetricNamesQueryReply)
MetricNamesQueryReply.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'status', None, None, ),  # 1
    (2, TType.LIST, 'metricNames', (TType.STRING, 'UTF8', False), None, ),  # 2
)
all_structs.append(MetricMetadataQueryReq)
MetricMetadataQueryReq.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'categoryName', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'metricName', 'UTF8', None, ),  # 2
)
all_structs.append(MetricMetadataQueryReply)
MetricMetadataQueryReply.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'status', None, None, ),  # 1
    (2, TType.STRUCT, 'metadata', [MetricMetadata, None], None, ),  # 2
)
all_structs.append(MetricLabelsQueryReq)
MetricLabelsQueryReq.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'categoryName', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'metricName', 'UTF8', None, ),  # 2
)
all_structs.append(MetricLabelsQueryReply)
MetricLabelsQueryReply.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'status', None, None, ),  # 1
    (2, TType.MAP, 'metricLabels', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 2
)
all_structs.append(MetricTypeQueryReq)
MetricTypeQueryReq.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'categoryName', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'metricName', 'UTF8', None, ),  # 2
)
all_structs.append(MetricTypeQueryReply)
MetricTypeQueryReply.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'status', None, None, ),  # 1
    (2, TType.I16, 'metricType', None, None, ),  # 2
)
fix_spec(all_structs)
del all_structs
