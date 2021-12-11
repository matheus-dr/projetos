package prova.repositorios;

import javax.persistence.EntityManager;

import prova.modelos.Passagem;

public class PassagemRepositorio extends Repositorio<Passagem, Integer> {
	
	public PassagemRepositorio(EntityManager em) {
		super(em);
	}
	
	@Override
	public Class<Passagem> getMyClass() {
		return Passagem.class;
	}

}
