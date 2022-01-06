import sys
import itertools
from collections import defaultdict, Counter, deque
import heapq

class ParseState:
  def __init__(self, ab):
        self.b = ab
        self.i = 0

def take(n, s):
  #print("take(" + str(s.i) + ', ' + str(s.i+n) + ')')
  value = s.b[s.i:s.i+n]
  s.i += n
  # #print("value", value)
  return value


def parseLiteral(s, start):
  literal = []

  while take(1, s) == '1':
    literal.append(take(4, s))

  literal.append(take(4, s))

  # if (s.i-start) % 4 != 0:
  #   s.i += 4 - ((s.i-start) % 4)

  return "".join(literal)

# convert hex->binary
# Header: 
#   3 bits pkt version
#   3 bits pkt ID (numbers)
#      4 -> Literal value (single binary number, mult of 4 bits with a leading bit for each 4 that goes 1,1...1,0, then ignore pad bits to next hex letter)
#      others -> operators, mode defined in bit after pkt header: 
#        0 - next 15 bits are a number reps # bits in packet
#        1 - next 11 bits number of sub-packets contained by this packet

def doMaths(o1 : int, o2 : int, operator : int):
    if o1 == None:
        return o2
    if operator == 0: 
        return o1 + o2
    elif operator == 1: 
        return o1 * o2
    elif operator == 2: 
        return min(o1,o2)
    elif operator == 3: 
        return max(o1,o2)
    elif operator == 5: 
        return 1 if o1 > o2 else 0
    elif operator == 6: 
        return 1 if o1 < o2 else 0
    elif operator == 7: 
        return 1 if o1 == o2 else 0


def parsePacket(s, indent = ''):
  start = s.i
  version = int(take(3, s),2)
  id = int(take(3,s),2)
  print(indent + "ver",version, "id",id, "type", s.b[s.i])
  if id == 4:
    literal = parseLiteral(s, start)
    return int(literal,2)
  elif take(1,s) == '0':
    size_len = int(take(15,s),2)
    asdf = s.i
    value = None
    while s.i - asdf < size_len:
      value = doMaths(value, parsePacket(s, " " * s.i), id)
  else:
    value = None
    sub_packets = int(take(11,s),2)
    for i in range(sub_packets):
      value = doMaths(value,  parsePacket(s, " " * s.i), id)
  print(indent + str(s.b[start:s.i]))
  return value


def hexStrToBinaryStr(h):
  b = []
  for c in h:
    b.extend(bin(int(c,16))[2:].rjust(4,'0'))
  b = ("".join(b))
  return b


def parsePacketStream(h):
  i=0
  v = 0
  b = hexStrToBinaryStr(h)
  s = ParseState(b)

  # i=0
  # 000-0000
  # s.i = 3
  # 0000
  # str[s.i:s.i+1]

  # id = 3, ver = 3, min = [4, 1+11, 1+15]
  # therefore, remainder processing [go|no-go] needs to be decided....
  #  --- if we are at the end, it will certainly be all zeroes (padding as described by the problem statement)
  # is modus tollons correct?
  #  --- 


  # s.i = 51
  # #print(s.b[51:])
  # #print("--------------------------")
  # #print(len(s.b))
  # #print(s.b[58:69])
  # #print("--------------------------")
  # ver = parsePacket(s)
  # exit()

  #while s.i<len(s.b)-4: #or (s.i<len(s.b)-15 and int(s.b[s.i:],2) != 0):
  #print("s.i:", s.i)
  #print("len(s.b):", len(s.b))
  #print("tail: ", s.b[s.i:], len(s.b[s.i:]))
  ver = parsePacket(s)
  print("tail: ", s.b[s.i:], len(s.b[s.i:]))
  #return ver
  v += ver
  print(v)
  return v


if __name__ == "__main__":
  #assert hexStrToBinaryStr('D2FE28') == '110100101111111000101000'
  # assert parsePacket(ParseState('110100101111111000101000')) == 6
  # assert parsePacketStream('D2FE28') == 6

  #assert hexStrToBinaryStr('38006F45291200') == '00111000000000000110111101000101001010010001001000000000'
  # assert parsePacket(ParseState('00111000000000000110111101000101001010010001001000000000')) == 1
  # assert parsePacketStream('38006F45291200') == 1
  
  #assert hexStrToBinaryStr('EE00D40C823060') == '11101110000000001101010000001100100000100011000001100000'
  # assert parsePacket(ParseState('11101110000000001101010000001100100000100011000001100000')) == 7
  #parsePacketStream('EE00D40C823060')

  
  assert parsePacketStream('C200B40A82') == 3 # finds the sum of 1 and 2, resulting in the value 3.
  assert parsePacketStream('04005AC33890') == 54 # finds the product of 6 and 9, resulting in the value 54.
  assert parsePacketStream('880086C3E88112') == 7 # finds the minimum of 7, 8, and 9, resulting in the value 7.
  assert parsePacketStream('CE00C43D881120') == 9 # finds the maximum of 7, 8, and 9, resulting in the value 9.
  assert parsePacketStream('D8005AC2A8F0') == 1 # produces 1, because 5 is less than 15.
  assert parsePacketStream('F600BC2D8F') == 0 # produces 0, because 5 is not greater than 15.
  assert parsePacketStream('9C005AC2F8F0') == 0 # produces 0, because 5 is not equal to 15.
  assert parsePacketStream('9C0141080250320F1802104A08') == 1 # produces 1, because 1 + 3 = 2 * 2.

  
  print(parsePacketStream('420D50000B318100415919B24E72D6509AE67F87195A3CCC518CC01197D538C3E00BC9A349A09802D258CC16FC016100660DC4283200087C6485F1C8C015A00A5A5FB19C363F2FD8CE1B1B99DE81D00C9D3002100B58002AB5400D50038008DA2020A9C00F300248065A4016B4C00810028003D9600CA4C0084007B8400A0002AA6F68440274080331D20C4300004323CC32830200D42A85D1BE4F1C1440072E4630F2CCD624206008CC5B3E3AB00580010E8710862F0803D06E10C65000946442A631EC2EC30926A600D2A583653BE2D98BFE3820975787C600A680252AC9354FFE8CD23BE1E180253548D057002429794BD4759794BD4709AEDAFF0530043003511006E24C4685A00087C428811EE7FD8BBC1805D28C73C93262526CB36AC600DCB9649334A23900AA9257963FEF17D8028200DC608A71B80010A8D50C23E9802B37AA40EA801CD96EDA25B39593BB002A33F72D9AD959802525BCD6D36CC00D580010A86D1761F080311AE32C73500224E3BCD6D0AE5600024F92F654E5F6132B49979802129DC6593401591389CA62A4840101C9064A34499E4A1B180276008CDEFA0D37BE834F6F11B13900923E008CF6611BC65BCB2CB46B3A779D4C998A848DED30F0014288010A8451062B980311C21BC7C20042A2846782A400834916CFA5B8013374F6A33973C532F071000B565F47F15A526273BB129B6D9985680680111C728FD339BDBD8F03980230A6C0119774999A09001093E34600A60052B2B1D7EF60C958EBF7B074D7AF4928CD6BA5A40208E002F935E855AE68EE56F3ED271E6B44460084AB55002572F3289B78600A6647D1E5F6871BE5E598099006512207600BCDCBCFD23CE463678100467680D27BAE920804119DBFA96E05F00431269D255DDA528D83A577285B91BCCB4802AB95A5C9B001299793FCD24C5D600BC652523D82D3FCB56EF737F045008E0FCDC7DAE40B64F7F799F3981F2490'))
  #print(parsePacketStream('005473C9244483004B001F79A9CE75FF9065446725685F1223600542661B7A9F4D001428C01D8C30C61210021F0663043A20042616C75868800BAC9CB59F4BC3A40232680220008542D89B114401886F1EA2DCF16CFE3BE6281060104B00C9994B83C13200AD3C0169B85FA7D3BE0A91356004824A32E6C94803A1D005E6701B2B49D76A1257EC7310C2015E7C0151006E0843F8D000086C4284910A47518CF7DD04380553C2F2D4BFEE67350DE2C9331FEFAFAD24CB282004F328C73F4E8B49C34AF094802B2B004E76762F9D9D8BA500653EEA4016CD802126B72D8F004C5F9975200C924B5065C00686467E58919F960C017F00466BB3B6B4B135D9DB5A5A93C2210050B32A9400A9497D524BEA660084EEA8EF600849E21EFB7C9F07E5C34C014C009067794BCC527794BCC424F12A67DCBC905C01B97BF8DE5ED9F7C865A4051F50024F9B9EAFA93ECE1A49A2C2E20128E4CA30037100042612C6F8B600084C1C8850BC400B8DAA01547197D6370BC8422C4A72051291E2A0803B0E2094D4BB5FDBEF6A0094F3CCC9A0002FD38E1350E7500C01A1006E3CC24884200C46389312C401F8551C63D4CC9D08035293FD6FCAFF1468B0056780A45D0C01498FBED0039925B82CCDCA7F4E20021A692CC012B00440010B8691761E0002190E21244C98EE0B0C0139297660B401A80002150E20A43C1006A0E44582A400C04A81CD994B9A1004BB1625D0648CE440E49DC402D8612BB6C9F5E97A5AC193F589A100505800ABCF5205138BD2EB527EA130008611167331AEA9B8BDCC4752B78165B39DAA1004C906740139EB0148D3CEC80662B801E60041015EE6006801364E007B801C003F1A801880350100BEC002A3000920E0079801CA00500046A800C0A001A73DFE9830059D29B5E8A51865777DCA1A2820040E4C7A49F88028B9F92DF80292E592B6B840'))

  