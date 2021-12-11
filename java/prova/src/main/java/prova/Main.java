package prova;

import java.io.IOException;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;

import prova.modelos.Passagem;
import prova.servicos.AuthService;
import prova.servicos.IAuthService;
import prova.servicos.IPassagemService;
import prova.servicos.PassagemService;

public class Main {
	
	private static final EntityManagerFactory emFactoryObj;
    private static final String PERSISTENCE_UNIT_NAME = "revisao";  
 
    static {
        emFactoryObj = Persistence.createEntityManagerFactory(PERSISTENCE_UNIT_NAME);
    }
 
    // This Method Is Used To Retrieve The 'EntityManager' Object
    public static EntityManager getEntityManager() {
        return emFactoryObj.createEntityManager();
    }



	
	public static void main(String[] args) throws SQLException, IOException {
		EntityManager entityMgr = getEntityManager();
		
		// IAuthService authService = null;
		AuthService authService = new AuthService();
		// IPassagemService passagemService = null;
		PassagemService passagemService = new PassagemService(entityMgr);
		List<String> loggedUsers = new ArrayList<String>();
				
		
		Scanner scanner = new Scanner(System.in);
		int opcao = scanner.nextInt();
		while(opcao != 0) {
			if(opcao > 2 && loggedUsers.isEmpty()) {
				opcao = scanner.nextInt();
				continue;
			}
			if(opcao == 1) {
				System.out.println("Entre com email");
				String email = scanner.next();
				System.out.println("Entre com password");
				String password = scanner.next();				
				authService.createUser(email, password);
			} else if(opcao == 2) {
				System.out.println("Entre com email");
				String email = scanner.next();
				System.out.println("Entre com password");
				String password = scanner.next();
				authService.login(email, password, loggedUsers);
			}  else if(opcao == 3) {
				System.out.println("Entre com id");
				Integer id = scanner.nextInt();
				System.out.println("Entre com preco");
				float preco = scanner.nextFloat();
				System.out.println("Entre com localChegada");
				String localChegada = scanner.next();
				System.out.println("Entre com localEmbarque");
				String localEmbarque = scanner.next();
				System.out.println("Entre com dataChegada");
				String dataChegada = scanner.next();
				System.out.println("Entre com dataEmbarque");
				String dataEmbarque = scanner.next();
				passagemService.salvaPassagem(id, preco, localChegada, localEmbarque, dataChegada, dataEmbarque);
			} else if(opcao == 4) {
				System.out.println("Entre com id");
				Integer id = scanner.nextInt();
				System.out.println("Entre com preco");
				float preco = scanner.nextFloat();
				System.out.println("Entre com dataChegada");
				String dataChegada = scanner.next();
				System.out.println("Entre com dataEmbarque");
				String dataEmbarque = scanner.next();
				passagemService.atualizaPassagem(id, preco, dataChegada, dataEmbarque);
			} else if(opcao == 5) {
				System.out.println("Entre com id");
				Integer id = scanner.nextInt();
				Passagem passagem = passagemService.encontraPassagem(id);
				System.out.println(passagem);
			} else if(opcao == 6) {
				System.out.println("Entre com dataEmbarque");
				String dataEmbarque = scanner.next();
				
				List<Passagem> passagens = passagemService.filtraPorDataDeEmbarque(dataEmbarque);
				for(Passagem passagem : passagens) {
					System.out.println(passagem);
				}
			}
			
			opcao = scanner.nextInt();
			
		}
				
		
	}

}
