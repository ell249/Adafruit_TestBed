import base64
import string
from samba.dcerpc.dcerpc import payload

# from esptool.py v4.4
stub = {
    'esp32': {
        "entry": 1074521516,
        "text": "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",
        "text_start": 1074520064,
        "data": "CMD8Pw==",
        "data_start": 1073605544
    },
    'esp32s2': {
        "entry": 1073907552,
        "text": "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",
        "text_start": 1073905664,
        "data": "CAD9Pw==",
        "data_start": 1073622004
    },
    'esp32s3': {
        "entry": 1077381512,
        "text": "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",
        "text_start": 1077379072,
        "data": "CADKPw==",
        "data_start": 1070279668
    }
}


def print_array(payload):
    while len(payload) > 0:
        print('    ' + ', '.join('0x{:02x}'.format(x) for x in payload[0:16]) + ',')
        payload = payload[16:]


def print_stub(mcu):
    data = base64.b64decode(stub[mcu]["data"])
    text = base64.b64decode(stub[mcu]["text"])
    
    print("//------------- {} -------------//".format(mcu))
    print ("const uint8_t _stub_%s_data[%d] = {" % (mcu, len(data)))
    print_array(data)
    print("};");
    print()

    print ("const uint8_t _stub_%s_text[%d] = {" % (mcu, len(text)))
    print_array(text)
    print("};");
    print()

    print("const esp32_stub_loader_t stub_%s = {" % mcu)
    print("  .entry = 0x%08x," % stub[mcu]["entry"])

    print("  .text_start = 0x%08x," % stub[mcu]["text_start"])
    print("  .text_length = %d," % len(text))
    print("  .text = _stub_%s_text," % mcu)

    print("  .data_start = 0x%08x," % stub[mcu]["data_start"])
    print("  .data_length = %d," % len(data))
    print("  .data = _stub_%s_data," % mcu)
    print("};")
    print()


# print stubs
print_stub('esp32')
print_stub('esp32s2')
#print_stub('esp32s3')
