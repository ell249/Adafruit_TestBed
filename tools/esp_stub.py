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
        "text": "CAAAYBwAAGAAAABgrCv+PxAAAGA2QQAh+v/AIAA4AkH5/8AgACgEICCUnOIGBQAAAEH1/4H2/8AgAKgEiAigoHTgCAALImYC54b0/yHx/8AgADkCHfAAAFQgQD9UMEA/NkEAkf3/wCAAiAmAgCRWSP+R+v/AIACICYCAJFZI/x3wAAAALCBAPwAgQD8AAAAINkEA5fz/Ifv/DAjAIACJApH7/4H5/8AgAJJoAMAgAJgIVnn/wCAAiAJ88oAiMCAgBB3wAAAAAEA2QQBl/P8Wmv+B7f+R/P/AIACZCMAgAJgIVnn/HfAAAAAAgAAAAAABmAD+P////wAEIEA/NkEAIfz/OEIWIwal+P8WygWIQgz5DAOHqQyIIpCIEAwZgDmDMDB0Zfr/pfP/iCKR8v9AiBGHOR+R7f/ME5Hs/6Hv/8AgAIkKgdH/wCAAmQjAIACYCFZ5/xwJDBgwiZM9CIhCMIjAiUKIIjo4OSId8JAA/j8IgP0/gIAAAISAAABAQAAASMD9P5QA/j82QQCx+P8goHSl4wCW6gWB9v+R9v+goHSQmIDAIACyKQCR8/+QiIDAIACSGACQkPQbycDA9MAgAMJYAJqbwCAAokkAwCAAkhgAger/kJD0gID0h5lGgeT/keX/oej/mpjAIADICbHk/4ecGUYCAHzohxrhRgkAAADAIACJCsAgALkJRgIAwCAAuQrAIACJCZHY/5qIDAnAIACSWAAd8AAAYC8BQDZBAIH+/+AIACIKGAwZIsL+DAggiYMtCB3wAAD4/P8/hDIBQLTxAECQMgFAwPEAQDZBAOX8/xbKAjH4/xYCAaIjAIH3/+AIAKKiAMYGAAAAoqIAgfT/4AgAqAOB8//gCABGBQAAACwKjIKB8P/gCACGAQAAgez/4AgAHfDwK/4/sCv+P4wxAUA2QQAh/P+B4//IAqgIsfr/gfv/4AgADAiJAh3wQCsBQDZBAGX1/xaqAIHy/4IoAIwY5fz/DAqB+f/gCAAd8AAAKCsBQDZBACXz/xZKA5Hp/4IpAKLIAakJkej/DAqKmSJJAILIwQwZgKmDoIB0zIiir0CqIiCJg4z4Zfj/hgIAAAAArQKB7//gCAAd8DZBAIKgwK0Ch5INoqDbpfr/oqDcRgMAAACCoNuHkgWl+f+ioN0l+f8d8AAANkEAOjIGAgAAogIAGyJl/P83kvQd8AAANkEAoqDA5fb/HfAAqCv+P6Qr/j8AMgFA7DEBQDAzAUA2YQB8yK0Ch5MrMab/xgUAAKgDDBy9AYH3/+AIAIES/6IBAIgI4AgAqAOB8//gCADmGt1GCgBmAyYMA80BsqACOQGB7v/gCACYAYHo/zeZDagIZhoIMeb/wCAAokMAmQgd8AAAzHEBQDZBAEE4/1g0UDNjFvMDWBRaU1BcQYYAAGXN/4hEphgEiCSHpfLlxf8Wmv+oFM0DvQKB8v/gCACgoHSMOiKgxClUKBQ6IikUKDQwMsA5NB3wcOL6PwggQD8AAEAAhGIBQKRiAUA2YQDlvv8x+f8QsSAwoyCB+v/gCABNCgwS7LqIAZKiAJCIEIkBJcP/kfL/ofL/wCAAiAmgiCDAIACJCbgBrQOB7//gCACgJIMd8AAA/w8AADZBAIEL/5KgAZJIADCcQZJoApH6/zJoASk4MDC0miIqMzA8QQwCKVg5SGX4/y0KjBoioMUd8AAAABAAAFgQAABsUgBAjHIBQIxSAEAMUwBANiEhotEQgfr/4AgAhgoAAABR9f+9AVBDY80ErQKB9f/gCACgoHT8Ks0EvQGi0RCB8v/gCABKIkAzwFYz/aHr/7LREBqqge3/4AgAoej/HAsaqqXg/y0DBgEAAAAioGMd8AAAAGwQAABoEAAAcBAAAHQQAAB4EAAA8CsBQDZBIWH7/4H7/xBmgEJmAEKgABqIYtEQrQRZCEJmGiXL/1Hz/4HS/xpVWAVXuAIGOACtBoHQ/+AIAIHv/3Hr/xqIelFZCMYmAIHq/0BzwBqIiAi9AXB4Y80HrQKBx//gCACgoHSMynHh/wwFUmYWenHGDAAAJdj/cLcgrQEl1v+l1//NBxCxIGCmIIG8/+AIAHoiekQ3tM6B1/9QdMAaiIgIhzejhu//DAqiRmyB0/8QiICiKACB0f/gCABW2v6xrP+iBmwQu4CllwD36g72RQtat6JLABtVBvP/AAB867eaxWZFCFImGje1Ale0pqGg/2C2IBCqgIGi/+AIAKXP/6Gc/7KgEBqqpc3/5c7/DBolvP8d8AAA/T9PSEFJ9Cv+P4iBAkBIPAFApIMCQAgACGAUgAJADAAAYDhAQD///wAAAAABABAnAAAogUA/AAAAgIyAAAAQQAAAAEAAAAAA/T8EAP0/FAAAYPD//wD0K/4/CAD9P7AA/j9c8gBA0PEAQKTxAEDUMgFAWDIBQKDkAEAEcAFAAHUBQIjYAECASQFA6DUBQOw7AUCAAAFAmCABQOxwAUBscQFADHEBQIQpAUB4dgFA4HcBQJR2AUAAMABAaAABQDbBACHQ/wwKImEKQqAAgeX/4AgAIcv/Mcz/xgAASQJLIjcy+OW//wxLosEo5b3/Zb//QXf+IXf+McX/KiTAIABJAiEa/jkCZaj/FioGIab+wfj+qAIMK4H6/uAIAAycPAsMCoHR/+AIALG5/wwMDJqBz//gCACiogCBn/7gCACxtf+oAgwVgcr/4AgAqAKBl/7gCACoAoHH/+AIADGv/8AgACgDUCIgwCAAKQMGCgAAsav/zQoMWoG9/+AIADGo/1KhAcAgACgDLApQIiDAIAApA4GJ/uAIAIG4/+AIACGh/8AgACgCzLocwzAiECLC+AwTIKODDAuBsf/gCADxmv/RJv/Bmv+xIf7ioQAMCoGs/+AIACGa/1Ee/ipEYtUrRhYAAAAAgcP+wCAAMggAMDB0FnMEoqIAwCAAIkgAgWz+4AgAoYv/gZ//4AgAgZ//4AgAcYj/fOjAIAA4B6GH/4AzEMAgADkHgZn/4AgAgZj/4AgAIKIggZf/4AgAwCAAKAQWAvoMB8AgADgEDBLAIAB5BCJBHCIDAQwoeYEiQR2CUQ8cN3cSIhxHdxIjZpIlIgMDcgMCgCIRcCIgZkIWKCPAIAAoAimBhgIAHCKGAAAADMIiUQ/lpP8Mi6LBHOWi/7IDA4IDAiFm/4C7EYCLICAg9IeyEqKgwGWe/6Kg7iWe/yWi/wbd/wAiAwEM13eSAobAACc3VWZiAkb5APZyIGYyAoaQAPZCCGYiAkZ0AEYqAGZCAkakAGZSAgbVAIYmAAyXd5ICxrgAJzcOZnICxtYAZoICRiMABiAAZpICxsgADLd3kgLGoADGGwAAHEd3kgJGKgAnNzAcF3eSAgZ6ACc3EQz3d5IChlEAZrICBmcAxhEAABwnd5ICBosAHDd3kgJGUQDGDAAAcqDSd5IChkwAJzcUcqDQd5ICxiAAcqDRd5IChiMARgQAcqDTd5ICRmUBcqDUd5ICBmMADAcioP8G0AAAACxJDAcioMCXGAJGzAAtB3mBDHcgoiBljv8goiDljf/lkf/lkf+yoAiiwRwLd6WP/1b3/QYwAAAAACKgAVbYL8LBEIC4IICoIIEq/+AIAFa6LgzLosEQJY3/hpkADBJWuC2J4YEl/+AIAIjhhkMAAAAmiAQMEgaxACIjAnIjA3CCIICAtFa4/iWa/3AigJwaBvj/AKCsQYEZ/+AIAFY6/XLX8HCiwMwXBoYAoID0Vij+RgQAoKD1gRL/4AgAVjr7gfL+gHfAgfD+cKLAdzjkBgQAAACgrEGBCf/gCABWOvly1/BwosBWp/7GdQAADAcioMAmiALGkQAMBy0HBpAAACa49MZnACKgASa4AoaLALIjA6IjAmWb/4YIAAAioAEmuAIGhgCR3v6CIwRyoAAioMKHuQIGggC4U6gjJZT/DBcMAqAnk0Z9AAAioAEmuALGegCCIwSR0v5yoAAioMKHuQLGdgAoM7hTqCMgKILlkP9xT/0MCIlnctcrKScMEqAog0ZuAJFK/QwHogkAIqDGd5oChmoAKFmYI7LI8LCZwIKgwJAok5Kg74YCAAB6g4IIGBt3gJkwtyfycgMFggMEgHcRgHcgggMGAIgRcHggggMHgIgBcIgggJnAgqDBDAeQKJOGVgCBMf0ioMaSCAB9CRbJFJg4DAcioMh3GQLGTwCSSAAoWEZNAByJDAcMEpcYAsZKAPhz6GPYU8hDuDOoI4Gv/uAIAH0KDApwKoPGQwAAAAwSJkgCxkAAqCMMC4Gm/uAIAAYfAACAoDQMByKgwHcaAkY6AICEQYuTfQp8+8YNAKg5ieGZ0bnBgZ3+4AgAmNGI4SgpqBnICaCiELjBJgINwCAA2AwgKzDQIhAgqiDAIACpDBt3kskQhzfExpX/ZkgCRpT/DAcioMBGJAAMEia4AsYhACF7/ohTeCOJAiF6/nkCDAIGHQDBdv4MB9gMssjwDBKNB7CCk9AnkyCIECKgxneYWZFw/iKgyegJtz5OsKAUIqDAd5pFLQoMH0YCACpzeGdLInkKjQ8gfsAqrbcy7RYY3qkMeQmGdv8ADBJmiBpxYf4oBxYiACKgyAwKqQdxXP6pBwwXIKeTLQoMByCgdKVb/3CgdCVb/yVf/1ZStHIDAYKgD4cXP3c4FWZHAgZ6AGZnAsZ/ACY3AsbJ/gYgAAAcIieXAgZ0AHcyDBwSJ5cCBj0ARsP+AAAioNInF08ioNQnF3MGv/54MzgjpUT/ViqvoTn+gU7+4AgAgT/+kT/+wCAAiAggoiCAtDXAiBGQiBCAiyBwuIIwu8KBTf7gCACio+iBQv7gCADGrf4AANIjBcIjBLIjA6gjpXX/Bqn+ALIDAyIDAoC7ESC7ILLL8KLDGCVc/8ai/iIDA3IDAoAiEXAiIIE8/uAIAHGj/CLC8Ig3gCJjFrKmiBeKgoCMQYYBAInh5Sf/iOGSJwSmGQSYJ5eo7SUg/xaa/6InASDCILLDGIEt/uAIABZKADKgxDlXOBcqMzkXODcgI8ApN4En/uAIAAaH/gByAwOCAwKAdxGAdyAiwxhyx/AMGQYhAACBCP4xpfziKAByYQngM8AyYQQ4JgwZN7cBDDmJ4ZnR6cElIP+Y0TH//ejBof/9vQKZAcLBJPLBEN0DgRH+4AgAnQq4JqiRiOGgu8C5JqB3wLgIqiKoQQwcqrsMCpCsg7kIoKB0MLvAzHrS24DQrIMWGgEwoyCCYQ6SYQ2lS/+I4ZjROQg4NYynkI8xkIjA1igAVrP21okAIqDHKVWGAAAAjEmMswZX/gAioMjMU8ZU/gAioMkpVYZS/igjVlKU5TP/oc39geL94AgAge794AgABkz+AAAAKDMWgpIlMv+io+iB2v3gCADgAgCGRf4AAAAd8AAANkEAnQKCoMAoA4eZD8wyDBKGBwAMAikDfOKGDgAmEgcmIhaGAwAAAIKg24ApI4eZJgwiKQN88kYHACKg3CeZCAwSKQMtCIYDAIKg3Xzyh5kGDBIpAyKg2x3wAAA=",
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
    },
    'esp8266': {
        "entry": 1074843652,
        "text": "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",
        "text_start": 1074843648,
        "data": "CIH+PwUFBAACAwcAAwMLALnXEEDv1xBAHdgQQLrYEEBo5xBAHtkQQHTZEEDA2RBAaOcQQILaEED/2hBAwNsQQGjnEEBo5xBAWNwQQGjnEEA33xBAAOAQQDvgEEBo5xBAaOcQQNfgEEBo5xBAv+EQQGXiEECj4xBAY+QQQDTlEEBo5xBAaOcQQGjnEEBo5xBAYuYQQGjnEEBX5xBAkN0QQI/YEECm5RBAq9oQQPzZEEBo5xBA7OYQQDHnEEBo5xBAaOcQQGjnEEBo5xBAaOcQQGjnEEBo5xBAaOcQQCLaEEBf2hBAvuUQQAEAAAACAAAAAwAAAAQAAAAFAAAABwAAAAkAAAANAAAAEQAAABkAAAAhAAAAMQAAAEEAAABhAAAAgQAAAMEAAAABAQAAgQEAAAECAAABAwAAAQQAAAEGAAABCAAAAQwAAAEQAAABGAAAASAAAAEwAAABQAAAAWAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAABAAAAAgAAAAIAAAADAAAAAwAAAAQAAAAEAAAABQAAAAUAAAAGAAAABgAAAAcAAAAHAAAACAAAAAgAAAAJAAAACQAAAAoAAAAKAAAACwAAAAsAAAAMAAAADAAAAA0AAAANAAAAAAAAAAAAAAADAAAABAAAAAUAAAAGAAAABwAAAAgAAAAJAAAACgAAAAsAAAANAAAADwAAABEAAAATAAAAFwAAABsAAAAfAAAAIwAAACsAAAAzAAAAOwAAAEMAAABTAAAAYwAAAHMAAACDAAAAowAAAMMAAADjAAAAAgEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAQAAAAEAAAABAAAAAgAAAAIAAAACAAAAAgAAAAMAAAADAAAAAwAAAAMAAAAEAAAABAAAAAQAAAAEAAAABQAAAAUAAAAFAAAABQAAAAAAAAAAAAAAAAAAABAREgAIBwkGCgULBAwDDQIOAQ8AAQEAAAEAAAAEAAAA",
        "data_start": 1073720488
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


# print list of stubs first
for k in stub.keys():
    print("// const esp32_stub_loader_t stub_%s" % k)
print()

# print stubs
for k in stub.keys():
    print_stub(k)
