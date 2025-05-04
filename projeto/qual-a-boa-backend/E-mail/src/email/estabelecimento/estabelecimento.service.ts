import { Injectable } from '@nestjs/common';
import { MailerService } from '@nestjs-modules/mailer';

@Injectable() 
export class EstabelecimentoService {
  constructor(private readonly mailerService: MailerService) {}

  async cadastrarEstabelecimento(dados: any) {
    console.log('Estabelecimento cadastrado:', dados);

    if (!dados.email) {
      console.error('Erro: E-mail do destinatário não foi informado.');
      return { success: false, message: 'O campo "email" é obrigatório.' };
    }

    try {
      await this.mailerService.sendMail({
        to: dados.email, 
        subject: 'Novo Estabelecimento Cadastrado!',
        text: `Um novo estabelecimento foi cadastrado: ${dados.nome}`,
        html: `<p><strong>Nome:</strong> ${dados.nome}</p>
               <p><strong>Endereço:</strong> ${dados.endereco}</p>`,
      });

      console.log('E-mail enviado com sucesso!');
      return { success: true, message: 'E-mail enviado com sucesso!' };
    } catch (error) {
      console.error('Erro ao enviar e-mail:', error);
      return { success: false, message: 'Falha ao enviar e-mail.' };
    }
  }
}
