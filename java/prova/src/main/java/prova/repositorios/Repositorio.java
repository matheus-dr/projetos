package prova.repositorios;

import java.util.List;

import javax.persistence.EntityManager;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public abstract class Repositorio<T,U> {
	
	protected EntityManager em;
	
	public abstract Class<T> getMyClass();
	
	public void save(T obj) {
		em.getTransaction().begin();
		em.persist(obj);
		em.getTransaction().commit();
	}
	
	public void update(T obj) {
		em.getTransaction().begin();
		em.merge(obj);
		em.getTransaction().commit();
	}
	
	public List<T> findAll(){
		return em.createQuery("select t from " + getMyClass().getSimpleName() + " t ", getMyClass() ).getResultList();
	}
	
	public T findById(U id) {
		return em.find(getMyClass(), id);
	}

}
