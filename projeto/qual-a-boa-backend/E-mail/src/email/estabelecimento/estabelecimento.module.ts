import { Module } from '@nestjs/common';
import { EstabelecimentoService } from './estabelecimento.service';
import { EstabelecimentoController } from './estabelecimento.controller';
import { MailerModule } from '@nestjs-modules/mailer';

@Module({
  imports: [MailerModule],
  controllers: [EstabelecimentoController], 
  providers: [EstabelecimentoService], 
})
export class EstabelecimentoModule {}
