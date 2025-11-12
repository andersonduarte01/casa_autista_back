from rest_framework import permissions

class IsAdministrador(permissions.BasePermission):
    """
    Permite acesso apenas a usuários que são administradores.
    Considera que o usuário logado vem de outro modelo (ex: Usuario).
    """

    def has_permission(self, request, view):
        user = request.user

        # Garante que o usuário está autenticado
        if not user or not user.is_authenticated:
            return False

        # Verifica se o campo is_administrator existe no objeto
        # (isso evita erro se o campo não estiver no modelo)
        return getattr(user, "is_administrator", False)
