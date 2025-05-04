import { Module } from '@nestjs/common';
import { MailerModule } from '@nestjs-modules/mailer';
import { ConfigModule, ConfigService } from '@nestjs/config';
import { EstabelecimentoModule } from './email/estabelecimento/estabelecimento.module';

@Module({
  imports: [
    ConfigModule.forRoot(), 
    MailerModule.forRootAsync({
      imports: [ConfigModule],
      inject: [ConfigService],
      useFactory: async (configService: ConfigService) => ({
        transport: {
          host: configService.get<string>('MAIL_HOST'),
          port: configService.get<number>('MAIL_PORT'),
          secure: false, // true para SSL/TLS
          auth: {
            user: configService.get<string>('MAIL_USER'),
            pass: configService.get<string>('MAIL_PASS'),
          },
        },
        defaults: {
          from: '"Meu Projeto" <seuemail@gmail.com>',
        },
      }),
    }),
    EstabelecimentoModule,
  ],
})
export class AppModule {}
