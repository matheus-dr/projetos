package prova.servicos;

import java.util.List;
import java.util.stream.Collectors;

import javax.persistence.EntityManager;

import prova.modelos.Passagem;
import prova.repositorios.PassagemRepositorio;

public class PassagemService extends PassagemRepositorio implements IPassagemService {
	
	public PassagemService(EntityManager em) {
		super(em);
	}

	PassagemRepositorio passagemRep;
	
	@Override
	public void salvaPassagem(Integer id, float preco, String localChegada, String localEmbarque, String dataChegada,
			String dataEmbarque) {
		Passagem passagem = new Passagem(id, preco, localChegada, localEmbarque, dataChegada, dataEmbarque);
		passagemRep.save(passagem);
	}
	
	@Override
	public void atualizaPassagem(Integer id, float preco, String dataChegada, String dataEmbarque) {
		Passagem passagem = new Passagem(id, preco, null, null, dataChegada, dataEmbarque);
		passagemRep.update(passagem);
	}

	@Override
	public Passagem encontraPassagem(Integer id) {
		return passagemRep.findById(id);
	}

	@Override
	public List<Passagem> filtraPorDataDeEmbarque(String data) {
		List<Passagem> passagens = passagemRep.findAll(); 
		return passagens.stream().filter(p -> p.equals(data)).collect(Collectors.toList());
	}

}
