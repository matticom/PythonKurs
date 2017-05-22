d={"OS":("Linux","Open Solaris",["Free BSD","Open BSD"],{"Minix":["V2","V3"]})}
print(d["OS"][3]) #Dict mit Minix Key
print(d["OS"][2][-1:][0][-3]) # B von Open BSD
print(d.keys()) # dict_keys['OS']
print(d.values()) # dict_values([('Linux',..., ...'V3']})])
print(d.items()) # dict_items([('OS', ('Linux', .. 'V3']}))])
