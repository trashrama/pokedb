drop table if exists demo CASCADE;
drop table if exists movimento cascade;
drop table if exists pokemon_movimento cascade;
drop table if exists habilidade cascade;
drop table if exists item CASCADE;
drop table if exists key_item CASCADE;
drop table if exists liga CASCADE;
drop table if exists pokemon_lugar CASCADE;
drop table if exists lugar CASCADE;
drop table if exists pokemon cascade;
drop table if exists efetividade_ATQ cascade;
drop table if exists efetividade_DEF cascade;
drop table if exists evolucaonormal cascade;
drop table if exists evolucao cascade;
drop table if exists evolucaopedras cascade;
drop table if exists ginasio cascade;
drop table if exists treinador cascade;
drop table if exists treinador_inv cascade;
drop table if exists captura cascade;
drop table if exists troca cascade;
drop table if exists batalha cascade;
drop table if exists batalha_ginasio cascade;
drop table if exists batalha_liga cascade;
drop table if exists treinador_insignias cascade;

CREATE OR REPLACE FUNCTION pegarHab()
RETURNS TRIGGER AS $$
DECLARE
    hab VARCHAR(30);
BEGIN
    IF NEW.slot = 1 THEN
        SELECT hab_1 INTO hab FROM pokemon WHERE id = NEW.id_pokemon;
    ELSIF NEW.slot = 2 THEN
        SELECT hab_2 INTO hab FROM pokemon WHERE id = NEW.id_pokemon;
    ELSIF NEW.slot = 3 THEN
        SELECT hab_3 INTO hab FROM pokemon WHERE id = NEW.id_pokemon;
    END IF;

    NEW.hab := hab;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


create table lugar(id int unique not null, 
                    nome varchar(50) not null unique,
                  	regiao varchar(50) not null check (regiao in ('Kanto', 'Johto', 'Hoenn')),
                   	primary key (id, nome)
                  	);

CREATE TABLE item(id_item serial not NULL unique, 
                   nome_item varchar(150) not NULL UNIQUE, 
                   categoria varchar(50),
                   efeito varchar(300),
                   primary key(id_item, nome_item));
create table habilidade (nome varchar(30) primary key unique not null, 
                         descricao varchar(200));
                         
create table movimento(nome varchar(50) primary key unique not null,
                       tipo varchar(50) check(tipo in ('Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy'))not null, 
                       cat varchar(30) check (cat in ('PHYSICAL', 'SPECIAL', 'STATUS')) not null, 
                       poder int,
                       precisao int,
                       pp int,
                       ger int not null check(ger in (1, 2, 3)),
                       efeito varchar(100)
                       );
CREATE TABLE pokemon(id serial not null unique check (id >= 1 and id <= 386),
                   nome varchar(50) not null,
                   tipo1 varchar(50) not null check(tipo1 in ('Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy')),
                   tipo2 varchar(50) check(tipo2 in ('Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy')),
                   hp int not null, 
                   attack int not NULL,
                   defense int not null, 
                   sp_atk int not null, 
                   sp_def int not null, 
                   especie varchar(30) not null,
                   speed int not null,
                   altura float not null, 
                   peso float not null,
                   hab_1 varchar(30) not null,
                   hab_2 varchar(30),
                   hab_3 varchar(30),
                     hp_ev int,
                     atk_ev int,
                     def_ev int,
                     spatk_ev int,
                     spdef_ev int,
                     speed_ev int,

                   PRIMARY KEY (id),
                   FOREIGN KEY (hab_1) REFERENCES habilidade(nome),
                   FOREIGN KEY (hab_2) REFERENCES habilidade(nome),
                   FOREIGN KEY (hab_3) REFERENCES habilidade(nome)

                    );
create table pokemon_movimento(id_pokemon int NOT NULL,
                                nome_mov varchar(50) NOT NULL,
                                level_poke varchar(30),
                               	aprendidoPor varchar(30) not NULL,
                                primary key (id_pokemon, level_poke, nome_mov, aprendidoPor),
                                foreign key (id_pokemon) references pokemon(id),
								foreign key (nome_mov) references movimento(nome)
);
create table pokemon_lugar(
  				  id_poke int not null,
                  jogo varchar(10) not null check(jogo in ('RED', 'BLUE', 'YELLOW', 'RUBY', 'SAPPHIRE', 'EMERALD', 'GOLD', 'CRYSTAL', 'SILVER')), 
                  id_lugar int not null,
  				  primary key (id_poke, jogo, id_lugar),
                  foreign key(id_poke) REFERENCES pokemon (id),
                  foreign key(id_lugar) references lugar(id)
                  );
create table treinador(id_treinador serial not null primary key unique, 
                      nome varchar(30) not null,
                      data_nasc DATE not null,
                      sexo char(1) not null check (sexo in ('M', 'F')),
                      cor_olhos varchar(10) not null,
                      altura float not null, 
                      cidade_natal varchar(30) not null,
                      -- como varchar pra ficar mais facil de registrar ao inves do id
                      -- troquei de varchar pra int pq tem cidades em kanto
                      -- que se repetem em johto entao o ideal é uma coluna + cidade pra validar o canto
                       foreign key (cidade_natal) references lugar(nome)
                       );

                           
create table captura(id integer primary key,
				id_treinador int not null,
                               id_pokemon int not null,
                               lvl_pokemon varchar(30) not null default 1,
                                -- como varchar pra ficar mais facil de registrar ao inves do id
                               lugar varchar (50) ,
                               hab varchar(30),
                               slot int,
                               life integer default 100,
                               max_life integer default 100,
                               xp integer default 0,
                               nec_xp integer default 100,
                               id_item integer, -- pode estar segurando um item
                               mov1 varchar(30) default null,
                               mov2 varchar(30) default null,
                               mov3 varchar(30)	default null,
                               mov4 varchar(30) default null,
                               fainted boolean default false, 
                               attack int,
                               defense int, 
                               sp_atk int, 
                               sp_def int,
                               nature varchar(20),
                               speed int,
                               pp integer default 30,
                     		   hp_ev int,
                               atk_ev int,
                     		   def_ev int,
                     		   spatk_ev int,
                     		   spdef_ev int,
                     		   speed_ev int,
							   iv int, 
                               foreign key (id_treinador) references treinador(id_treinador),
                               foreign key (lugar) references lugar(nome),
                               foreign key (hab) references habilidade(nome)

                               );

create table box(
  				id serial primary key,
  				id_captura int,
  				foreign key (id_captura) references captura(id)
                               );

alter table treinador add column slot_1 integer;
ALTER TABLE treinador add CONSTRAINT distfk1 foreign key (slot_1) references captura(id);
alter table treinador add column slot_2 integer;
ALTER TABLE treinador add CONSTRAINT distfk2 foreign key (slot_2) references captura(id);
alter table treinador add column slot_3 integer;
ALTER TABLE treinador add CONSTRAINT distfk3 foreign key (slot_3) references captura(id);
alter table treinador add column slot_4 integer;
ALTER TABLE treinador add CONSTRAINT distfk4 foreign key (slot_4) references captura(id);
alter table treinador add column slot_5 integer;
ALTER TABLE treinador add CONSTRAINT distfk5 foreign key (slot_5) references captura(id);
alter table treinador add column slot_6 integer;
ALTER TABLE treinador add CONSTRAINT distfk6 foreign key (slot_6) references captura(id);



create TABLE troca(
    			   id serial primary key not null unique,
  				   id_treinador1 int not null,
                   id_treinador2 int not null,
                   id_cap1 int not null,
                   id_cap2 int not null,
                   
                   foreign key (id_treinador1) references treinador(id_treinador),
                   foreign key (id_treinador2) references treinador(id_treinador),
  -- aqui ele pegara o ID da linha, entao vai transferir o pokemon da forma certa
  -- pois vai transferir o nivel, e o lugar junto.
                   foreign key (id_cap1) references captura(id),
                   foreign key (id_cap2) references captura(id)
                  );

create TABLE batalha(
  				id serial primary key not null unique,
  				id_treinador1 int not null,
                id_treinador2 int not null,
                id_vencedor int not null,

                   
                   foreign key (id_treinador1) references treinador(id_treinador),
                   foreign key (id_treinador2) references treinador(id_treinador),
                   foreign key (id_vencedor) references treinador(id_treinador)
					-- fazer uma restricao tipo um if pra verificar se o id desse
  					-- treinador é == a todos os id_lideres de todos os ginasios 
  					-- e se for add a insginia do ginasio para o treinador de id_vencedor
                  );

create table ginasio (id_ginasio serial not null unique, 
                     id_lider int not null,
                     id_lider_sec int default null,
                     insignia varchar(30) not null unique,
                     cidade varchar(50) not null unique,
                     tipo varchar(50) not null check(tipo in ('Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy')),
                     primary key (id_ginasio, id_lider, insignia, cidade),
                     foreign key (cidade) references lugar(nome),
                     foreign key (id_lider) references treinador(id_treinador)
                     );
create TABLE batalha_ginasio(
  				id serial primary key not null unique,
  				id_treinador1 int not null,
                id_ginasio int not null,
                id_vencedor int not null,

                   
                   foreign key (id_treinador1) references treinador(id_treinador),
                   foreign key (id_ginasio) references ginasio(id_ginasio)
  					-- treinador batalha contra o lider q esta em um ginasio
					-- fazer uma restricao tipo um if pra verificar se o id desse
  					-- treinador é == a todos os id_lideres de todos os ginasios 
  					-- e se for add a insginia do ginasio para o treinador de id_vencedor
                  );
create table liga (id serial not null unique,
                     lugar varchar(30) unique not null,
                     id_elite4_1 int not null,
                     tipo_elite4_1 varchar(30) check(tipo_elite4_1 in ('Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy')),
                     id_elite4_2 int not null,
                     tipo_elite4_2 varchar(30) check(tipo_elite4_2 in ('Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy')),
                     id_elite4_3 int not null,
                     tipo_elite4_3 varchar(30) check(tipo_elite4_3 in ('Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy')),
                     id_elite4_4 int not null,
                     tipo_elite4_4 varchar(30) check(tipo_elite4_4 in ('Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy')),
                     id_campeao int not null,
                     tipo_campeao varchar(30) check(tipo_campeao in ('Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy')),
                   
                   	 primary key (id,lugar),
                   
                   	 foreign key (lugar) references lugar(nome),
                   	 foreign key (id_elite4_1) references treinador(id_treinador),
                     foreign key (id_elite4_2) references treinador(id_treinador),
                   	 foreign key (id_elite4_3) references treinador(id_treinador),
                   	 foreign key (id_elite4_4) references treinador(id_treinador)

                   );
create TABLE batalha_liga(
  				id serial primary key not null unique,
  				id_treinador int not null,
                id_liga int not null,
                id_vencedor int not null,

  --             treinador batalha contra o campeao q esta em uma liga. 
                   foreign key (id_treinador) references treinador(id_treinador),
                   foreign key (id_liga) references liga(id)
					-- fazer uma restricao tipo um if pra verificar se o id desse
  					-- treinador é == a todos os id_lideres de todos os ginasios 
  					-- e se for add a insginia do ginasio para o treinador de id_vencedor
                  );
                             
--madanicos de shibuya (sant, sant & sant)

create table treinador_inv(id_item int not null unique,
                          qtde_item int not null default 1 check (qtde_item>0),
                           -- como varchar pra ficar mais facil de registrar ao inves do id
                          lugar varchar(50) not null,
                          primary key(id_item),
                          foreign key (id_item) references item(id_item),
                          foreign key (lugar) references lugar(nome));  

create table treinador_insignias(
  						  id_ginasio integer,
  						  insignia varchar(50),
                          primary key(id_ginasio, insignia),
                          foreign key (id_ginasio) references ginasio(id_ginasio),
                          foreign key (insignia) references ginasio(insignia));



                  
create table evolucao(
  					  id_atual int not null,
                      id_evo int not null UNIQUE,
                      tipo_ev varchar(20) not null,
                      item varchar(50),
  					  primary key (id_atual, id_evo),
                      FOREIGN key (id_atual) REFERENCES pokemon (id),
                      FOREIGN key (id_evo) REFERENCES pokemon (id),
  					  FOREIGN KEY (item) references item(nome_item)
                      );
                      
                      
CREATE TABLE efetividade_atq(tipo varchar(10) primary key not null unique,  
                             Normal float not null,
Fire float not null,
Water float not null,
Electric float not null,
Grass float not null,
Ice float not null,
Fighting float not null,
Poison float not null,
Ground float not null,
Flying float not null,
Psychic float not null,
Bug float not null,
Rock float not null,
Ghost float not null,
Dragon float not null,
Dark float not null,
Steel float not null,
Fairy float not null);

CREATE TABLE efetividade_def(tipo varchar(10) primary key null unique, 
                             Normal float,
Fire float not null,
Water float not null,
Electric float not null,
Grass float not null,
Ice float not null,
Fighting float not null,
Poison float not null,
Ground float not null,
Flying float not null,
Psychic float not null,
Bug float not null,
Rock float not null,
Ghost float not null,
Dragon float not null,
Dark float not null,
Steel float not null,
Fairy float not null);


alter table pokemon add total int;
update pokemon set total = hp + attack + defense + sp_atk + speed + sp_def;