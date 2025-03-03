def loginUsuario(perfil):
    if perfil.lower() == 'admin':  # Converte o valor para minúsculas antes de comparar
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

# Chamadas da função com diferentes valores
loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')
loginUsuario('ADMIN')
loginUsuario('cliente')