package prova.servicos;

import java.util.List;

import prova.modelos.Passagem;

public interface IPassagemService {
	
	void salvaPassagem(Integer id, float preco, String localChegada, String localEmbarque, String dataChegada, String dataEmbarque);
	void atualizaPassagem(Integer id,float preco, String dataChegada, String dataEmbarque);
	Passagem encontraPassagem(Integer id);
	List<Passagem> filtraPorDataDeEmbarque(String data);

}
