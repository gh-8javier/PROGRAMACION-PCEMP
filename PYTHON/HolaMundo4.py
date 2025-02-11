# EXCEPCIONES
print('EXCEPCIONES')
print('\n')

'''
Comentar varias líneas
'''

# print(5 + '2') #Genera una excepción

# Para ver el tipo de error, hay que generar el error en consola
try:
    print(5 + '2') # Excepción del tipo TypeError
    #print(adfdfa) # Excepción del tipo NameError 
    print(5 + 2) # No hay excepción
except TypeError as error: # Excepción TypeError / con as error almacenamos en la variable error el error producido                
    print('¡Error TypeError!','\n')
    print(error)
except: # No se define el tipo de excepción por tanto aplica para cualquier tipo de excepción si no se ha definido antes
    print('¡Error!','\n')
else:
    print('¡No hay error','\n')
finally:
    print('Siempre se ejecuta','\n')
    
    
# MÓDULOS
print('MÓDULOS O ARCHIVOS DEL PROYECTO')
print('\n')    