package prova.modelos;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Table(name = "passagens")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class Passagem {
	@Id
	Integer id;
	float preco;
	String localChegada;
	String localEmbarque;
	String dataChegada;
	String dataEmbarque;
}
