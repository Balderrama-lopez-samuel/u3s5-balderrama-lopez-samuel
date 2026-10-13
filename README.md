# Proyecto Django — Balderrama López Samuel

Proyecto Django conectado a MySQL en Aiven y desplegado en Render.

## Semana 5 (Unidad 3): CRUD completo con ModelForms
Pantallas propias para crear, listar, editar y eliminar servicios sin entrar a `/admin`:
- `ServicioForm` (ModelForm) en `core/forms.py`, con validación personalizada `clean_precio` (el precio debe ser mayor a 0).
- Vistas `crear_servicio`, `editar_servicio` y `eliminar_servicio` protegidas con `@login_required`; el propietario se asigna con `request.user`.
- Plantillas `base.html`, `servicio_form.html` (crear y editar) y `servicio_confirm_delete.html` (confirmación antes de borrar).
- Mientras llega el login propio (Semana 6), el inicio de sesión usa `/admin/login/`.

## Producción
https://u3s5-balderrama-lopez-samuel.onrender.com

- Servicios: https://u3s5-balderrama-lopez-samuel.onrender.com/servicios/
- Panel de administración: https://u3s5-balderrama-lopez-samuel.onrender.com/admin/

## Rutas
| URL | Vista | name |
|---|---|---|
| `/` | `inicio` | `inicio` |
| `/servicios/` | `servicios` | `servicios` |
| `/servicios/nuevo/` | `crear_servicio` | `crear_servicio` |
| `/servicios/<pk>/editar/` | `editar_servicio` | `editar_servicio` |
| `/servicios/<pk>/eliminar/` | `eliminar_servicio` | `eliminar_servicio` |

## Cómo correrlo localmente
1. Crear y activar un entorno virtual
2. pip install -r requirements.txt
3. Copiar .env.example a .env y completar con credenciales propias de Aiven, un SECRET_KEY y DEBUG=True
4. python manage.py migrate
5. python manage.py createsuperuser
6. python manage.py runserver

## Despliegue en Render
- **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
- **Start Command:** `gunicorn miproyecto.wsgi`
- **Variables de entorno:** `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS=u3s5-balderrama-lopez-samuel.onrender.com`, `CSRF_TRUSTED_ORIGINS=https://u3s5-balderrama-lopez-samuel.onrender.com`

## Evidencia
- Semana 3 (Django + MySQL en Aiven): capturas de `migrate`, tablas en Aiven y vistas locales en la carpeta [/evidencia](evidencia).
- Semana 4 (modelo Servicio + Render): capturas del panel /admin, /servicios/ en producción y el Web Service en Render en la carpeta [/evidencia/unidad2_Django_OnRender](evidencia/unidad2_Django_OnRender).
