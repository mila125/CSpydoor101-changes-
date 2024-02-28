import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body):
    # Configura los datos de autenticación
    gmail_user = 'sistema.planificacion@mpco.cl'  # Cambia esto por tu dirección de correo electrónico de Gmail
    gmail_password = 'Practica123'  # Cambia esto por tu contraseña de Gmail

    # Crea el mensaje
    message = MIMEMultipart()
    message["From"] = gmail_user
    message["To"] = 'hydral0k4@gmail.com'  # Cambia esto por la dirección de correo electrónico del destinatario
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        # Establece la conexión con el servidor SMTP de Gmail
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        # Inicia sesión en el servidor SMTP
        server.login(gmail_user, gmail_password)
        # Envía el correo electrónico
        server.sendmail(gmail_user, message["To"], message.as_string())
        # Cierra la conexión
        server.close()
        print("Correo electrónico enviado correctamente!")
    except Exception as e:
        print("Error al enviar el correo electrónico:", str(e))

# Llama a la función send_email con el asunto y el cuerpo del correo electrónico
send_email("Prueba de correo electrónico", "Este es un correo electrónico de prueba enviado desde Python utilizando una cuenta de Gmail.")
