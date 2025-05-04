import { Controller, Post, Body } from '@nestjs/common';
import { EstabelecimentoService } from './estabelecimento.service';

@Controller('estabelecimento')
export class EstabelecimentoController {
  constructor(private readonly estabelecimentoService: EstabelecimentoService) {}

  @Post() 
  async cadastrar(@Body() dados: any) {
    return this.estabelecimentoService.cadastrarEstabelecimento(dados);
  }
}
