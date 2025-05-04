import { Injectable } from '@nestjs/common';
import { MailerService } from '@nestjs-modules/mailer';

@Injectable()
export class EmailService {
  constructor(private readonly mailerService: MailerService) {}

  async sendEmail(to: string, subject: string, text: string) {
    try {
      await this.mailerService.sendMail({
        to,
        subject,
        text,
        html: `<p>${text}</p>`,
      });
      return { success: true, message: 'E-mail enviado com sucesso!' };
    } catch (error) {
      console.error('Erro ao enviar e-mail:', error);
      return { success: false, message: 'Falha ao enviar e-mail.' };
    }
  }
}
