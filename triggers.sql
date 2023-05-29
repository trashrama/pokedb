-- limitar a 6 pokemons e se for maior joga pra box
create sequence seq_idpoke
start with 1
increment by 1
minvalue 1
cache 20;
create type poke as (
  	      id integer,
		  id_treinador int,
          id_pokemon int,
          lvl_pokemon varchar(30),
          -- como varchar pra ficar mais facil de registrar ao inves do id
          lugar varchar (50),
          hab varchar(30),
          slot int,
          life integer,
          max_life integer,
          id_item integer, -- pode estar segurando um item
          mov1 varchar(30),
          mov2 varchar(30),
          mov3 varchar(30),
          mov4 varchar(30),
  		hp_ev int,
        atk_ev int,
        def_ev int,
        spatk_ev int,
        spdef_ev int,
        speed_ev int,
          attack int,
          defense int, 
          sp_atk int, 
          sp_def int,
          nature varchar(20),
          speed int
);

--passa: id do treinador, id do pokemon, lugar e o lvl do pkmon
create or REPLACE PROCEDURE	capturado(integer, integer, varchar, varchar) AS $$
	declare 
    	intervalo INTEGER default 3;
        repetidos varchar[];
        qtde_hab integer;
        naturezas varchar[] := Array['Adamant', 'Bashful', 'Bold', 'Brave', 'Calm', 'Careful', 'Docile', 'Gentle', 'Hardy', 'Hasty', 'Impish', 'Jolly', 'Lax', 'Lonely', 'Mild', 'Modest', 'Naive', 'Naughty', 'Quiet', 'Quirky', 'Rash', 'Relaxed', 'Sassy', 'Serious', 'Timid'];
        val integer := floor((random() * 10000))+1;
        aux poke;
       
    begin
          aux.id := nextval('seq_idpoke');
          aux.id_treinador := $1;
          aux.id_pokemon := $2;
          aux.lugar := $3;
          aux.lvl_pokemon := $4;
          aux.life := (select pokemon.hp from pokemon where pokemon.id = $2);
          aux.max_life := (select pokemon.hp from pokemon where pokemon.id = $2);
          
          aux.hp_ev := (select pokemon.hp_ev from pokemon where pokemon.id = $2);
          aux.atk_ev := (select pokemon.atk_ev from pokemon where pokemon.id = $2);
          aux.def_ev := (select pokemon.def_ev from pokemon where pokemon.id = $2);
          aux.spatk_ev := (select pokemon.spatk_ev from pokemon where pokemon.id = $2);
          aux.spdef_ev := (select pokemon.spdef_ev from pokemon where pokemon.id = $2);
          aux.speed_ev := (select pokemon.speed_ev from pokemon where pokemon.id = $2);
          
        if val > 7000 THEN
        	AUX.id_item := floor(random()* (select count(*) from item) ) + 1;        	
        end if;
    	if (select hab_2 from pokemon where aux.id_pokemon = pokemon.id) is null then
        	intervalo := intervalo-2;
        end if;
    	AUX.slot := floor(random() * intervalo);
        IF AUX.slot = 1 THEN
            SELECT hab_1 INTO AUX.hab FROM pokemon WHERE id = AUX.id_pokemon;
        ELSIF AUX.slot = 2 THEN
            SELECT hab_2 INTO AUX.hab FROM pokemon WHERE id = AUX.id_pokemon;
        END IF;
        
select nome_mov into AUX.mov1 from pokemon_movimento pm where AUX.id_pokemon = pm.id_pokemon and split_part(pm.level_poke,' ', 2)::integer <= split_part(aux.lvl_pokemon, ' ',2)::integer and pm.aprendidopor = 'LEVEL UP' or pm.aprendidopor = 'PRE-EVOLUTION' ORDER BY random() limit 1; 
	    if not found then
        	AUX.mov1 := NULL;
       	else
        	repetidos := array_append(repetidos, AUX.mov1); 

        end if;
        
          
        select nome_mov into AUX.mov2 from pokemon_movimento pm where AUX.id_pokemon = pm.id_pokemon and split_part(pm.level_poke,' ', 2)::integer <= split_part(aux.lvl_pokemon, ' ',2)::integer and pm.aprendidopor = 'LEVEL UP' or pm.aprendidopor = 'PRE-EVOLUTION' and nome_mov not in (select unnest (repetidos)) ORDER BY random() limit 1; 
	    if not found THEN
        	AUX.mov2 := NULL;
        ELSE
        	repetidos := array_append(repetidos, AUX.mov2); 
        end if;
        
        select nome_mov into AUX.mov3 from pokemon_movimento pm where AUX.id_pokemon = pm.id_pokemon and (split_part(pm.level_poke,' ', 2)::integer <= split_part(aux.lvl_pokemon, ' ',2)::integer) and pm.aprendidopor = 'LEVEL UP' or pm.aprendidopor = 'PRE-EVOLUTION' and nome_mov not in (select unnest (repetidos)) ORDER BY random() limit 1; 
	    if not found THEN
        	AUX.mov3 := NULL;
        ELSE
        	repetidos := array_append(repetidos, AUX.mov3); 
        end if;
        
        select nome_mov into AUX.mov4 from pokemon_movimento pm where AUX.id_pokemon = pm.id_pokemon and split_part(pm.level_poke,' ', 2)::integer <= split_part(aux.lvl_pokemon, ' ',2)::integer and pm.aprendidopor = 'LEVEL UP' or pm.aprendidopor = 'PRE-EVOLUTION' and nome_mov not in (select unnest (repetidos)) ORDER BY random() limit 1; 
	    if not found THEN
        	AUX.mov4 := NULL;
        ELSE
        	repetidos := array_append(repetidos, AUX.mov4); 
        end if;
        
        select pk.attack, pk.defense, pk.speed, pk.sp_atk, pk.sp_def into AUX.attack, AUX.defense, AUX.speed, AUX.sp_atk, AUX.sp_def from pokemon pk where AUX.id_pokemon = pk.id; 

		select unnest(naturezas) into AUX.nature order by random() limit 1;
      	
        case (AUX.nature)
        	WHEN 'Adamant' THEN 
              AUX.attack := AUX.attack * 1.1;
              AUX.sp_atk := AUX.sp_atk * 0.9;


			WHEN 'Bashful' THEN 
              AUX.sp_atk := AUX.sp_atk * 1.1;
              AUX.sp_atk := AUX.sp_atk * 0.9;


			WHEN 'Bold' THEN 
              AUX.defense := AUX.defense * 1.1;
              AUX.attack := AUX.attack * 0.9;


            WHEN 'Brave' THEN 
              AUX.attack := AUX.attack * 1.1;
              AUX.speed := AUX.speed * 0.9;


            WHEN 'Calm' THEN 
              AUX.sp_def := AUX.sp_def * 1.1;
              AUX.attack := AUX.attack * 0.9;


            WHEN 'Careful' THEN 
              AUX.sp_def := AUX.sp_def * 1.1;
              AUX.sp_atk := AUX.sp_atk * 0.9;


            WHEN 'Docile' THEN 
              AUX.defense := AUX.defense * 1.1;
              AUX.defense := AUX.defense * 0.9;


            WHEN 'Gentle' THEN 
              AUX.sp_def := AUX.sp_def * 1.1;
              AUX.defense := AUX.defense * 0.9;


            WHEN 'Hardy' THEN 
              AUX.attack := AUX.attack * 1.1;
              AUX.attack := AUX.attack * 0.9;


            WHEN 'Hasty' THEN 
              AUX.speed := AUX.speed * 1.1;
              AUX.defense := AUX.defense * 0.9;


            WHEN 'Impish' THEN 
              AUX.defense := AUX.defense * 1.1;
              AUX.sp_atk := AUX.sp_atk * 0.9;


            WHEN 'Jolly' THEN 
              AUX.speed := AUX.speed * 1.1;
              AUX.sp_atk := AUX.sp_atk * 0.9;


            WHEN 'Lax' THEN 
              AUX.defense := AUX.defense * 1.1;
              AUX.sp_def := AUX.sp_def * 0.9;


            WHEN 'Lonely' THEN 
              AUX.attack := AUX.attack * 1.1;
              AUX.defense := AUX.defense * 0.9;


            WHEN 'Mild' THEN 
              AUX.sp_atk := AUX.sp_atk * 1.1;
              AUX.defense := AUX.defense * 0.9;


            WHEN 'Modest' THEN 
              AUX.sp_atk := AUX.sp_atk * 1.1;
              AUX.attack := AUX.attack * 0.9;


            WHEN 'Naive' THEN 
              AUX.speed := AUX.speed * 1.1;
              AUX.sp_def := AUX.sp_def * 0.9;


            WHEN 'Naughty' THEN 
              AUX.attack := AUX.attack * 1.1;
              AUX.sp_def := AUX.sp_def * 0.9;


            WHEN 'Quiet' THEN 
              AUX.sp_atk := AUX.sp_atk * 1.1;
              AUX.speed := AUX.speed * 0.9;


            WHEN 'Quirky' THEN 
              AUX.sp_def := AUX.sp_def * 1.1;
              AUX.sp_def := AUX.sp_def * 0.9;


              WHEN 'Rash' THEN 
              AUX.sp_atk := AUX.sp_atk * 1.1;
              AUX.sp_def := AUX.sp_def * 0.9;


            WHEN 'Relaxed' THEN 
              AUX.defense := AUX.defense * 1.1;
              AUX.speed := AUX.speed * 0.9;


            WHEN 'Sassy' THEN 
              AUX.sp_def := AUX.sp_def * 1.1;
              AUX.speed := AUX.speed * 0.9;


            WHEN 'Serious' THEN 
              AUX.speed := AUX.speed * 1.1;
              AUX.speed := AUX.speed * 0.9;


            ELSE
              AUX.speed := AUX.speed * 1.1;
              AUX.attack := AUX.attack * 0.9;

			end case;
            
            INSERT INTO captura (id, id_treinador, id_pokemon, lvl_pokemon, lugar, hab, slot, life, max_life, id_item, mov1, mov2, mov3, mov4, attack, defense, sp_atk, sp_def, nature, speed, iv) VALUES (aux.id, AUX.id_treinador, AUX.id_pokemon, AUX.lvl_pokemon, AUX.lugar, AUX.hab, AUX.slot, AUX.life, AUX.max_life, AUX.id_item, AUX.mov1, AUX.mov2, AUX.mov3, AUX.mov4, AUX.attack, AUX.defense, AUX.sp_atk, AUX.sp_def, AUX.nature, AUX.speed, (floor(random() * 32)+1));

            
            if (select slot_1 from treinador where treinador.id_treinador = aux.id_treinador) is null THEN
            	update treinador set slot_1 = aux.id where treinador.id_treinador = aux.id_treinador;
            elsif (select slot_2 from treinador where treinador.id_treinador = aux.id_treinador) is null THEN
            	update treinador set slot_2 = aux.id where treinador.id_treinador = aux.id_treinador;
            elsif (select slot_3 from treinador where treinador.id_treinador = aux.id_treinador) is null THEN
            	update treinador set slot_3 = aux.id where treinador.id_treinador = aux.id_treinador;
            elsif (select slot_4 from treinador where treinador.id_treinador = aux.id_treinador) is null THEN
            	update treinador set slot_4 = aux.id where treinador.id_treinador = aux.id_treinador;
            elsif (select slot_5 from treinador where treinador.id_treinador = aux.id_treinador) is null THEN
            	update treinador set slot_5 = aux.id where treinador.id_treinador = aux.id_treinador;
             elsif (select slot_6 from treinador where treinador.id_treinador = aux.id_treinador) is null THEN
            	update treinador set slot_6 = aux.id where treinador.id_treinador = aux.id_treinador;
			ELSE
            	insert into box values(aux.id);
            end if;
                
           

	end;
$$ language plpgsql;

-- passa o id dos dois treinadores, e o INDICE dos slots (respectivas a cada treinador)
CREATE OR REPLACE FUNCTION transferencia(integer, integer, integer, integer) RETURNS void AS $$
DECLARE 
  evId integer;
BEGIN
  CASE $3
    WHEN 1 THEN
      UPDATE captura SET id_treinador = $2 WHERE id = (SELECT slot_1 FROM treinador WHERE id_treinador = $1) AND id_treinador = $1; 
      UPDATE treinador SET slot_1 = (SELECT slot_1 FROM treinador WHERE id_treinador = $1) WHERE id_treinador = $2;

      SELECT evolucao.id_evo INTO evId FROM evolucao WHERE tipo_ev = 'TRADE' AND evolucao.id_atual = (SELECT slot_1 FROM treinador WHERE id_treinador = $2);
      IF evId IS NOT NULL THEN
        UPDATE captura SET id_pokemon = evId WHERE id_pokemon = (SELECT slot_1 FROM treinador WHERE id_treinador = $2);
      END IF;

    WHEN 2 THEN
      UPDATE captura SET id_treinador = $2 WHERE id = (SELECT slot_2 FROM treinador WHERE id_treinador = $1) AND id_treinador = $1; 
      UPDATE treinador SET slot_2 = (SELECT slot_2 FROM treinador WHERE id_treinador = $1) WHERE id_treinador = $2;

      SELECT evolucao.id_evo INTO evId FROM evolucao WHERE tipo_ev = 'TRADE' AND evolucao.id_atual = (SELECT slot_2 FROM treinador WHERE id_treinador = $2);
      IF evId IS NOT NULL THEN
        UPDATE captura SET id_pokemon = evId WHERE id_pokemon = (SELECT slot_2 FROM treinador WHERE id_treinador = $2);
      END IF;

    WHEN 3 THEN
      UPDATE captura SET id_treinador = $2 WHERE id = (SELECT slot_3 FROM treinador WHERE id_treinador = $1) AND id_treinador = $1; 
      UPDATE treinador SET slot_3 = (SELECT slot_3 FROM treinador WHERE id_treinador = $1) WHERE id_treinador = $2;

      SELECT evolucao.id_evo INTO evId FROM evolucao WHERE tipo_ev = 'TRADE' AND evolucao.id_atual = (SELECT slot_3 FROM treinador WHERE id_treinador = $2);
      IF evId IS NOT NULL THEN
        UPDATE captura SET id_pokemon = evId WHERE id_pokemon = (SELECT slot_3 FROM treinador WHERE id_treinador = $2);
      END IF;

    ELSE
      UPDATE captura SET id_treinador = $2 WHERE id = (SELECT slot_4 FROM treinador WHERE id_treinador = $1) AND id_treinador = $1; 
      UPDATE treinador SET slot_4 = (SELECT slot_4 FROM treinador WHERE id_treinador = $2) WHERE id_treinador = $1;

      SELECT evolucao.id_evo INTO evId FROM evolucao WHERE tipo_ev = 'TRADE' AND evolucao.id_atual = (SELECT slot_4 FROM treinador WHERE id_treinador = $1);
      IF evId IS NOT NULL THEN
        UPDATE captura SET id_pokemon = evId WHERE id_pokemon = (SELECT slot_4 FROM treinador WHERE id_treinador = $1);
      END IF;

  END CASE;
  
  CASE $4
    WHEN 1 THEN
      UPDATE captura SET id_treinador = $1 WHERE id = (SELECT slot_1 FROM treinador WHERE id_treinador = $2) AND id_treinador = $2; 
      UPDATE treinador SET slot_1 = (SELECT slot_1 FROM treinador WHERE id_treinador = $2) WHERE id_treinador = $1;

      SELECT evolucao.id_evo INTO evId FROM evolucao WHERE tipo_ev = 'TRADE' AND evolucao.id_atual = (SELECT slot_1 FROM treinador WHERE id_treinador = $1);
      IF evId IS NOT NULL THEN
        UPDATE captura SET id_pokemon = evId WHERE id_pokemon = (SELECT slot_1 FROM treinador WHERE id_treinador = $1);
      END IF;

    WHEN 2 THEN
      UPDATE captura SET id_treinador = $1 WHERE id = (SELECT slot_2 FROM treinador WHERE id_treinador = $2) AND id_treinador = $2; 
      UPDATE treinador SET slot_2 = (SELECT slot_2 FROM treinador WHERE id_treinador = $2) WHERE id_treinador = $1;

      SELECT evolucao.id_evo INTO evId FROM evolucao WHERE tipo_ev = 'TRADE' AND evolucao.id_atual = (SELECT slot_2 FROM treinador WHERE id_treinador = $1);
      IF evId IS NOT NULL THEN
        UPDATE captura SET id_pokemon = evId WHERE id_pokemon = (SELECT slot_2 FROM treinador WHERE id_treinador = $1);
      END IF;

    WHEN 3 THEN
      UPDATE captura SET id_treinador = $1 WHERE id = (SELECT slot_3 FROM treinador WHERE id_treinador = $2) AND id_treinador = $2; 
      UPDATE treinador SET slot_3 = (SELECT slot_3 FROM treinador WHERE id_treinador = $2) WHERE id_treinador = $1;

      SELECT evolucao.id_evo INTO evId FROM evolucao WHERE tipo_ev = 'TRADE' AND evolucao.id_atual = (SELECT slot_3 FROM treinador WHERE id_treinador = $1);
      IF evId IS NOT NULL THEN
        UPDATE captura SET id_pokemon = evId WHERE id_pokemon = (SELECT slot_3 FROM treinador WHERE id_treinador = $1);
      END IF;

    ELSE
      UPDATE captura SET id_treinador = $1 WHERE id = (SELECT slot_4 FROM treinador WHERE id_treinador = $2) AND id_treinador = $2; 
      UPDATE treinador SET slot_4 = (SELECT slot_4 FROM treinador WHERE id_treinador = $2) WHERE id_treinador = $1;
      
      SELECT evolucao.id_evo INTO evId FROM evolucao WHERE tipo_ev = 'TRADE' AND evolucao.id_atual = (SELECT slot_4 FROM treinador WHERE id_treinador = $1);
      IF evId IS NOT NULL THEN
        UPDATE captura SET id_pokemon = evId WHERE id_pokemon = (SELECT slot_4 FROM treinador WHERE id_treinador = $1);
      END IF;

  END CASE;
END;
$$ LANGUAGE plpgsql;

-- passa o id do pokemon q vai ser curado
create or replace function centroPokemon(integer) returns void as $$
	begin
    	update captura set 
    	life = max_life,
        fainted = false
        where id = $1;
    end;
$$ language plpgsql;

CREATE or replace FUNCTION add_insignia() returns trigger as $$
    BEGIN
    	if new.id_vencedor = new.id_treinador1 then
        	insert into treinador_insignias (select gin.id_ginasio, gin.insignia from ginasio gin where gin.id_ginasio = new.id_ginasio);
        end if;
        return new;
    end;
$$ language plpgsql;

-- passa o id de uma captura e uma qtde de XP
create or replace function addXp(integer, integer) returns void AS $$
    update captura set xp = xp + $2 where id_pokemon = $1;
$$ language sql;

create or replace function evolucaoPoke() returns trigger as $$
	declare
    level_evol integer;
    id_nEvo integer;
    evolui boolean := FALSE;
    repetidos varchar[];

	BEGIN
        
        if new.xp >= new.nec_xp then
        
        	new.lvl_pokemon := FORMAT ('Level %',  ((split_part(new.lvl_pokemon, ' ', 2)::integer + 1)));
            new.xp = new.xp - new.nec_xp;
            new.nec_xp := floor((split_part(new.lvl_pokemon, ' ', 2)::integer * 3.5 + 100));
       
          
          --1º: pegar o nivel da evolucao 
          select evolucao.tipo_ev, evolucao.id_evo into level_evol, id_nEvo from evolucao 
          where (tipo_ev like 'Level%' 
          and evolucao.id_atual = new.id_pokemon
          and new.lvl_pokemon = evolucao.tipo_ev);
          
	      if found then          
              new.id_pokemon = id_nEvo;
              evolui := TRUE;
          end if;
       
      	end if;
        
        select evolucao.id_evo into id_nEvo from evolucao
        where tipo_ev = 'STONE' and evolucao.id_atual = new.id_pokemon
        and ((select upper(item.nome_item) from item where item.id_item = new.id_item) = upper(evolucao.item));
        
        if FOUND THEN
        	new.id_pokemon = id_nEvo;
            evolui := TRUE;
        end if;
        
        if evolui = TRUE THEN
            select pk.attack, pk.defense, pk.speed, pk.sp_atk, pk.sp_def, pk.max_life, pk.hp_ev, pk.def_ev, pk.spatk_ev, pk.spdef_ev, pk.speed_ev
            into new.attack, new.defense, new.speed, new.sp_atk, new.sp_def, new.max_life, new.hp_ev, new.def_ev, new.spatk_ev, new.spdef_ev, new.speed_ev
            from pokemon pk where NEW.id_pokemon = pk.id; 
            
            case (NEW.nature)
        	WHEN 'Adamant' THEN 
              NEW.attack := NEW.attack * 1.1;
              NEW.sp_atk := NEW.sp_atk * 0.9;


	 		WHEN 'Bashful' THEN 
              NEW.sp_atk := NEW.sp_atk * 1.1;
              NEW.sp_atk := NEW.sp_atk * 0.9;


			WHEN 'Bold' THEN 
              NEW.defense := NEW.defense * 1.1;
              NEW.attack := NEW.attack * 0.9;


            WHEN 'Brave' THEN 
              NEW.attack := NEW.attack * 1.1;
              NEW.speed := NEW.speed * 0.9;


            WHEN 'Calm' THEN 
              NEW.sp_def := NEW.sp_def * 1.1;
              NEW.attack := NEW.attack * 0.9;


            WHEN 'Careful' THEN 
              NEW.sp_def := NEW.sp_def * 1.1;
              NEW.sp_atk := NEW.sp_atk * 0.9;


            WHEN 'Docile' THEN 
              NEW.defense := NEW.defense * 1.1;
              NEW.defense := NEW.defense * 0.9;


            WHEN 'Gentle' THEN 
              NEW.sp_def := NEW.sp_def * 1.1;
              NEW.defense := NEW.defense * 0.9;


            WHEN 'Hardy' THEN 
              NEW.attack := NEW.attack * 1.1;
              NEW.attack := NEW.attack * 0.9;


            WHEN 'Hasty' THEN 
              NEW.speed := NEW.speed * 1.1;
              NEW.defense := NEW.defense * 0.9;


            WHEN 'Impish' THEN 
              NEW.defense := NEW.defense * 1.1;
              NEW.sp_atk := NEW.sp_atk * 0.9;


            WHEN 'Jolly' THEN 
              NEW.speed := NEW.speed * 1.1;
              NEW.sp_atk := NEW.sp_atk * 0.9;


            WHEN 'Lax' THEN 
              NEW.defense := NEW.defense * 1.1;
              NEW.sp_def := NEW.sp_def * 0.9;


            WHEN 'Lonely' THEN 
              NEW.attack := NEW.attack * 1.1;
              NEW.defense := NEW.defense * 0.9;


            WHEN 'Mild' THEN 
              NEW.sp_atk := NEW.sp_atk * 1.1;
              NEW.defense := NEW.defense * 0.9;


            WHEN 'Modest' THEN 
              NEW.sp_atk := NEW.sp_atk * 1.1;
              NEW.attack := NEW.attack * 0.9;


            WHEN 'Naive' THEN 
              NEW.speed := NEW.speed * 1.1;
              NEW.sp_def := NEW.sp_def * 0.9;


            WHEN 'Naughty' THEN 
              NEW.attack := NEW.attack * 1.1;
              NEW.sp_def := NEW.sp_def * 0.9;


            WHEN 'Quiet' THEN 
              NEW.sp_atk := NEW.sp_atk * 1.1;
              NEW.speed := NEW.speed * 0.9;


            WHEN 'Quirky' THEN 
              NEW.sp_def := NEW.sp_def * 1.1;
              NEW.sp_def := NEW.sp_def * 0.9;


              WHEN 'Rash' THEN 
              NEW.sp_atk := NEW.sp_atk * 1.1;
              NEW.sp_def := NEW.sp_def * 0.9;


            WHEN 'Relaxed' THEN 
              NEW.defense := NEW.defense * 1.1;
              NEW.speed := NEW.speed * 0.9;


            WHEN 'Sassy' THEN 
              NEW.sp_def := NEW.sp_def * 1.1;
              NEW.speed := NEW.speed * 0.9;


            WHEN 'Serious' THEN 
              NEW.speed := NEW.speed * 1.1;
              NEW.speed := NEW.speed * 0.9;


            ELSE
              NEW.speed := NEW.speed * 1.1;
              NEW.attack := NEW.attack * 0.9;
              
        
			end case;
                 
             if new.mov1 = NULL THEN
             	select nome_mov into new.mov1 from pokemon_movimento pm where NEW.id_pokemon = pm.id_pokemon and split_part(pm.level_poke,' ', 2)::integer <= split_part(NEW.lvl_pokemon, ' ',2)::integer and pm.aprendidopor = 'LEVEL UP' ORDER BY random() limit 1; 
                repetidos := array_append(repetidos, new.mov1); 
             end if;
             
              if new.mov2 = NULL THEN
             	select nome_mov into new.mov1 from pokemon_movimento pm where NEW.id_pokemon = pm.id_pokemon and split_part(pm.level_poke,' ', 2)::integer <= split_part(NEW.lvl_pokemon, ' ',2)::integer and pm.aprendidopor = 'LEVEL UP' ORDER BY random() limit 1; 
                repetidos := array_append(repetidos, new.mov2); 
             end if;
             
              if new.mov3 = NULL THEN
             	select nome_mov into new.mov3 from pokemon_movimento pm where NEW.id_pokemon = pm.id_pokemon and split_part(pm.level_poke,' ', 2)::integer <= split_part(NEW.lvl_pokemon, ' ',2)::integer and pm.aprendidopor = 'LEVEL UP' ORDER BY random() limit 1; 
                repetidos := array_append(repetidos, new.mov3); 
             end if;
             
              if new.mov4 = NULL THEN
             	select nome_mov into new.mov4 from pokemon_movimento pm where NEW.id_pokemon = pm.id_pokemon and split_part(pm.level_poke,' ', 2)::integer <= split_part(NEW.lvl_pokemon, ' ',2)::integer and pm.aprendidopor = 'LEVEL UP' ORDER BY random() limit 1; 
                repetidos := array_append(repetidos, new.mov4); 
             end if;
             

        end if;
        
        return new;
        
        end;
$$ language plpgsql;

-- passa o ID da captura, o nome do movimento para aprender, id e o slot do movimento para substituir
create OR REPLACE FUNCTION aprenderGolpe(integer, varchar, integer) returns void as $$
    DECLARE
    	mov varchar;
    begin
        select nome_mov into mov from pokemon_movimento where nome_mov = $2 AND id_pokemon = (select captura.id_pokemon from captura where captura.id = $1) and ( pokemon_movimento.aprendidopor = 'TM' or pokemon_movimento.aprendidopor = 'HM') ;
    	if mov is null then
        	raise EXCEPTION 'NÃO EXISTE O MOVIMENTO!';
        ELSE
        	if (select mov1 from captura where captura.id = $1 ) is null then
            	update captura set mov1 = mov where id = $1; 
            ELSif (select mov2 from captura where captura.id = $1 ) is null then
            	update captura set mov2 = mov where id = $1; 
            ELSif (select mov3 from captura where captura.id = $1 ) is null then
            	update captura set mov3 = mov where id = $1; 
            ELSif (select mov4 from captura where captura.id = $1 ) is null then
            	update captura set mov4 = mov where id = $1; 
            ELSE
            	CASE($4)
                
                  WHEN 1 THEN update captura set mov1 = mov where id = $1; 
                  WHEN 2 THEN update captura set mov2 = mov where id = $1; 
                  WHEN 3 THEN update captura set mov3 = mov where id = $1; 
                  WHEN 4 THEN update captura set mov4 = mov where id = $1; 

                END CASE;
            end if;
        end if;
    end;

$$ language plpgsql;

-- id da captura, slot da habilidade e pokemon de defesa
-- vou utilizar a formula da geracao 1
create or replace function calcEfetividade(integer, integer, integer) returns varchar as $$
	DECLARE
      pk1_tp1 varchar;
      pk1_tp2 varchar;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
      
      pk2_tp1 varchar;
      pk2_tp2 varchar;
      
      mov varchar;
      
      dano float;
      stab float;
      
      ef_Um float;
      ef_Dois float;
    begin
    	-- 1) pegar o tipo do 1º e o tipo do 2º
        select pk.tipo1 into pk1_tp1 from pokemon pk where pk.id = (select captura.id_pokemon from captura where captura.id = $1 LIMIT 1);
        select pk.tipo2 into pk1_tp2 from pokemon pk where pk.id = (select captura.id_pokemon from captura where captura.id = $1 LIMIT 1);
		

        select pk.tipo1 into pk2_tp1 from pokemon pk where pk.id = (select captura.id_pokemon from captura where captura.id = $3 LIMIT 1);
        select pk.tipo2 into pk2_tp2 from pokemon pk where pk.id = (select captura.id_pokemon from captura where captura.id = $3 LIMIT 1);

          
      	case $2
        when 1 then 
          begin
            select movimento.nome into mov from movimento where movimento.nome = (select captura.mov1 FROM captura where captura.id = $1);
            IF NOT FOUND THEN
                raise EXCEPTION 'O ATAQUE NÃO FOI DESFERIDO POIS NÃO ELE NÃO EXISTE';
            end if;
        end;
        when 2 then 
        begin    
            select movimento.nome into mov from movimento where movimento.nome = (select captura.mov2 FROM captura where captura.id = $1);
		    IF NOT FOUND THEN
            	raise EXCEPTION 'O ATAQUE NÃO FOI DESFERIDO POIS NÃO ELE NÃO EXISTE';
            end if;
        end;
        when 3 then 
        begin
            select movimento.nome into mov from movimento where movimento.nome = (select captura.mov3 FROM captura where captura.id = $1);
		    IF NOT FOUND THEN
            	raise EXCEPTION 'O ATAQUE NÃO FOI DESFERIDO POIS NÃO ELE NÃO EXISTE';
            end if;
        end;
        when 4 then 
        begin
            select movimento.nome into mov from movimento where movimento.nome = (select captura.mov4 FROM captura where captura.id = $1);
		    IF NOT FOUND THEN
            	raise EXCEPTION 'O ATAQUE NÃO FOI DESFERIDO POIS NÃO ELE NÃO EXISTE';
            end if;
        end;
       ELSE 
       	raise EXCEPTION 'FORA DO RANGE';
        end case;
        
        
        if (SELECT tipo from movimento where mov = movimento.nome) = pk1_tp1 or (SELECT tipo from movimento where mov = movimento.nome) = pk1_tp2 THEN
        	stab := 1.5;
        ELSE 
        	stab := 1;
        end if;
        
        
        case (pk2_tp1)
          when 'Normal' then select normal into ef_Um from efetividade_atq where efetividade_atq.tipo = pk1_tp1;
          when 'Fire' then select fire into ef_Um from efetividade_atq where efetividade_atq.tipo = pk1_tp1;
          when 'Water' then select water into ef_Um from efetividade_atq where efetividade_atq.tipo = pk1_tp1;
          when 'Electric' then select electric into ef_Um from efetividade_atq where efetividade_atq.tipo = pk1_tp1;
          when 'Grass' then select grass into ef_Um from efetividade_atq where efetividade_atq.tipo = pk1_tp1;
          when 'Ice' then select ice into ef_Um from efetividade_atq where efetividade_atq.tipo = pk1_tp1;
          when 'Fighting' then select fighting into ef_Um from efetividade_atq where efetividade_atq.tipo = pk1_tp1;
          when 'Poison' then select poison into ef_Um from efetividade_atq where efetividade_atq.tipo = pk1_tp1;
          when 'Ground' then select ground into ef_Um from efetividade_atq where efetividade_atq.tipo = pk1_tp1;
          when 'Flying' then select flying into ef_Um from efetividade_atq where efetividade_atq.tipo = pk1_tp1;
          when 'Psychic' then select psychic into ef_Um from efetividade_atq where efetividade_atq.tipo = pk1_tp1;
          when 'Bug' then select bug into ef_Um from efetividade_atq where efetividade_atq.tipo = pk1_tp1;
          when 'Rock' then select rock into ef_Um from efetividade_atq where efetividade_atq.tipo = pk1_tp1;
          when 'Ghost' then select ghost into ef_Um from efetividade_atq where efetividade_atq.tipo = pk1_tp1;
          when 'Dragon' then select dragon into ef_Um from efetividade_atq where efetividade_atq.tipo = pk1_tp1;
          when 'Dark' then select dark into ef_Um from efetividade_atq where efetividade_atq.tipo = pk1_tp1;
          when 'Steel' then select steel into ef_Um from efetividade_atq where efetividade_atq.tipo = pk1_tp1;
          ELSE select fairy into ef_Um from efetividade_atq where efetividade_atq.tipo = pk1_tp1;

        end case;
        
        case (pk2_tp2)
            when 'Normal' then select normal into ef_Dois from efetividade_atq where efetividade_atq.tipo = pk1_tp2;
            when 'Fire' then select fire into ef_Dois from efetividade_atq where efetividade_atq.tipo = pk1_tp2;
            when 'Water' then select water into ef_Dois from efetividade_atq where efetividade_atq.tipo = pk1_tp2;
            when 'Electric' then select electric into ef_Dois from efetividade_atq where efetividade_atq.tipo = pk1_tp2;
            when 'Grass' then select grass into ef_Dois from efetividade_atq where efetividade_atq.tipo = pk1_tp2;
            when 'Ice' then select ice into ef_Dois from efetividade_atq where efetividade_atq.tipo = pk1_tp2;
            when 'Fighting' then select fighting into ef_Dois from efetividade_atq where efetividade_atq.tipo = pk1_tp2;
            when 'Poison' then select poison into ef_Dois from efetividade_atq where efetividade_atq.tipo = pk1_tp2;
            when 'Ground' then select ground into ef_Dois from efetividade_atq where efetividade_atq.tipo = pk1_tp2;
            when 'Flying' then select flying into ef_Dois from efetividade_atq where efetividade_atq.tipo = pk1_tp2;
            when 'Psychic' then select psychic into ef_Dois from efetividade_atq where efetividade_atq.tipo = pk1_tp2;
            when 'Bug' then select bug into ef_Dois from efetividade_atq where efetividade_atq.tipo = pk1_tp2;
            when 'Rock' then select rock into ef_Dois from efetividade_atq where efetividade_atq.tipo = pk1_tp2;
            when 'Ghost' then select ghost into ef_Dois from efetividade_atq where efetividade_atq.tipo = pk1_tp2;
            when 'Dragon' then select dragon into ef_Dois from efetividade_atq where efetividade_atq.tipo = pk1_tp2;
            when 'Dark' then select dark into ef_Dois from efetividade_atq where efetividade_atq.tipo = pk1_tp2;
            when 'Steel' then select steel into ef_Dois from efetividade_atq where efetividade_atq.tipo = pk1_tp2;
            Else select fairy into ef_Dois from efetividade_atq where efetividade_atq.tipo = pk1_tp2;
        end case;

       if (select movimento.cat from movimento where movimento.nome = mov) = 'PHYSICAL' then
        
            dano :=  (((((2 * split_part((SELECT captura.lvl_pokemon FROM captura WHERE id = $1), ' ', 2)::integer * floor(random() * 2 + 1)) / 5) + 2)
        * (SELECT movimento.poder FROM movimento WHERE movimento.nome = mov) * ( (SELECT captura.attack FROM captura WHERE captura.id = $1) / (SELECT captura.defense FROM captura WHERE captura.id = $1)) ) / 50 + 2)
        * stab * ef_Um * ef_Dois * ((floor(random() * (255 - 217 + 1) + 217)::integer) / 255);
    

        elsif (select movimento.cat from movimento where movimento.nome = mov) = 'SPECIAL' then
            dano :=  (((((2 * split_part((SELECT captura.lvl_pokemon FROM captura WHERE id = $1), ' ', 2)::integer * floor(random() * 2 + 1)) / 5) + 2)
        * (SELECT movimento.poder FROM movimento WHERE movimento.nome = mov) * ( (SELECT captura.sp_atk FROM captura WHERE captura.id = $1) / (SELECT captura.sp_def FROM captura WHERE captura.id = $1))) / 50 + 2)
        * stab * ef_Um * ef_Dois * ((floor(random() * (255 - 217 + 1) + 217)::integer) / 255);

        else dano := NULL; 
        end if;
    	return format('DANO: %s',dano::varchar);

    end;
$$ LANGUAGE PLPGSQL;




-- passa o id do pokemon, e o id do item
CREATE or replace FUNCTION treinaEvItem(integer, integer) RETURNS void as $$
	BEGIN
    
      case (select item.nome_item from item where item.id_item = $2)
          when 'HP Up' THEN
              update captura set hp_ev = hp_ev + 10 where captura.id = $1;
          when 'Carbos' THEN
              update captura set speed_ev = speed_ev + 10 where captura.id = $1;
          when 'Protein' THEN
              update captura set atk_ev = atk_ev + 10 where captura.id = $1;
          when 'Iron' THEN
              update captura set def_ev = def_ev + 10 where captura.id = $1;
          when 'Calcium' THEN
              update captura set sp_atk = sp_atk + 10 where captura.id = $1;
          when 'Zinc' THEN
              update captura set sp_def = sp_def + 10 where captura.id = $1;
          when 'Iron' THEN
              update captura set def_ev = def_ev + 10 where captura.id = $1;
          else
              raise EXCEPTION 'O ITEM INSERIDO NÃO É EFETIVO PARA EV...';
          end case;
    end;
$$ LANGUAGE PLPGSQL;

-- passa o id dos dois pokemons, basicamente dizendo q o 1 ganhou do 2
CREATE or replace FUNCTION treinarEvVersus(integer, integer) RETURNS void as $$
	declare
    	aux1 float;
    	aux2 float;
    	aux3 float;
    	aux4 float;
    	aux5 float;
    	aux6 float;
    begin 
    	if $1 <> $2 then
          select captura.hp_ev, captura.atk_ev, captura.def_ev, captura.spatk_ev,
          captura.spdef_ev, captura.speed_ev into aux1, aux2, aux3, aux4, aux5, aux6 from captura where captura.id = $2;

          update captura set hp_ev = hp_ev + aux1 where id = $1;
          update captura set atk_ev = atk_ev + aux2 where id = $1;
          update captura set def_ev = def_ev + aux3 where id = $1;
          update captura set spatk_ev = spatk_ev + aux4 where id = $1;
          update captura set spdef_ev = spdef_ev + aux5 where id = $1;
          update captura set speed_ev = speed_ev + aux6 where id = $1;
      	else raise EXCEPTION 'SEU JUMENTO 1 pokemon nao pode lutar contra si mesmo BURRO seu imbecil meu deus voce e mto burrooooooooooorrrrrrrrr';
        end if;

    end;
	
$$ LANGUAGE PLPGSQL;

create or replace function updateEv() returns trigger as $$
	BEGIN
    	  IF (New.hp_ev) >= 255 THEN New.hp_ev := 255; end if;
          IF (New.atk_ev) >= 255 THEN New.atk_ev := 255; end if;
    	  IF (New.def_ev) >= 255 THEN New.def_ev := 255; end if;
    	  IF (New.spatk_ev) >= 255 THEN New.spatk_ev := 255; end if;
    	  IF (New.spdef_ev) >= 255 THEN New.spdef_ev := 255; end if;
    	  IF (New.speed_ev) >= 255 THEN New.speed_ev := 255; end if;
          
          return new;
          
    
    end;
$$ language plpgsql;


-- troca um elemento que ta no lugar x pra um lugar y
create or replace function lugarNaBox(integer, integer) returns void as $$
	BEGIN
    	if exists(select box.id from box where box.id = $1) and exists(select box.id from box where box.id = $2) then
    		update box set id = $2 where box.id = $1;
            update box set id = $1 where box.id = $2;

        	
        end if;
    end;
$$ language plpgsql;

-- passa o id do treinador, passa o slot e id da box
CREATE or replace FUNCTION trocabox(integer, integer, integer, char(1)) RETURNS void as $$ 
	BEGIN
   		case $2
        
        when 1 then 
          if (EXISTS(select treinador.slot_1 from treinador where id_treinador = $1 and slot_1 <> NULL) and upper($4) = 'Y') or (select treinador.slot_1 from treinador where id_treinador = $1 and slot_1 <> NULL) = NULL then
            insert into box(id_captura) select treinador.slot_1 from treinador where id_treinador = $1 and slot_1 <> NULL;
            update treinador set slot_1 = (select box.id_captura from box where box.id = $3) where treinador.id_treinador = $1;
          ELSE RAISE EXCEPTION 'SUBSTUIÇÃO NÃO PERMITIDA';
          end if;
        when 2 then 
          if (EXISTS(select treinador.slot_2 from treinador where id_treinador = $1 and slot_2 <> NULL) and $4 = 'Y') or (select treinador.slot_2 from treinador where id_treinador = $1 and slot_2 <> NULL) = NULL then
            insert into box(id_captura) select treinador.slot_2 from treinador where id_treinador = $1 and slot_2 <> NULL;
            update treinador set slot_2 = (select box.id_captura from box where box.id = $3) where treinador.id_treinador = $1;
            ELSE RAISE EXCEPTION 'SUBSTUIÇÃO NÃO PERMITIDA';
          end if;
        when 3 then 
        if (EXISTS(select treinador.slot_3 from treinador where id_treinador = $1 and slot_3 <> NULL) and $4 = 'Y') or (select treinador.slot_3 from treinador where id_treinador = $1 and slot_3 <> NULL) = NULL then
          insert into box(id_captura) select treinador.slot_3 from treinador where id_treinador = $1 and slot_3 <> NULL;
          update treinador set slot_3 = (select box.id_captura from box where box.id = $3) where treinador.id_treinador = $1;
          ELSE RAISE EXCEPTION 'SUBSTUIÇÃO NÃO PERMITIDA';

        end if;
        when 4 then 
        	if (EXISTS(select treinador.slot_4 from treinador where id_treinador = $1 and slot_4 <> NULL) and $4 = 'Y' ) or (select treinador.slot_4 from treinador where id_treinador = $1 and slot_4 <> NULL) = NULL  then
              insert into box(id_captura) select treinador.slot_4 from treinador where id_treinador = $1 and slot_4 <> NULL;
              update treinador set slot_4 = (select box.id_captura from box where box.id = $3) where treinador.id_treinador = $1;
              ELSE RAISE EXCEPTION 'SUBSTUIÇÃO NÃO PERMITIDA';
           	end if;
        end case;
   end;
$$ Language plpgsql;

-- exclui 1 pokemon com o id x da box
CREATE or replace FUNCTION soltabox(integer) RETURNS void as $$
	delete from box where box.id = $1;        
$$ LANGUAGE sql;


-- numero do slot, numero do treinador
CREATE or replace FUNCTION addbox(integer, integer) RETURNS void as $$
	BEGIN
   		case $2
        
        when 1 then 
        insert into box(id_captura) select treinador.slot_1 from treinador where id_treinador = $1;
        update treinador set slot_1 = NULL where treinador.id_treinador = $1;
        when 2 then 
        insert into box(id_captura) select treinador.slot_2 from treinador where id_treinador = $1;
        update treinador set slot_2 = NULL where treinador.id_treinador = $1;
        when 3 then 
        insert into box(id_captura) select treinador.slot_3 from treinador where id_treinador = $1;
        update treinador set slot_3 = NULL where treinador.id_treinador = $1;
        when 4 then 
        insert into box(id_captura) select treinador.slot_4 from treinador where id_treinador = $1;
        update treinador set slot_4 = NULL where treinador.id_treinador = $1;
        end case;
   end;
$$ LANGUAGE PLPGSQL;


CREATE or replace FUNCTION atualizastatus() RETURNS trigger AS $$
	begin
    	if new.life = 0 then
        	new.fainted = true;
        end if;
        return new;
    end;
$$ LANGUAGE PLPGSQL;

create or replace trigger tg1 AFTER update on captura for each ROW
execute procedure updateev();

create or replace trigger tg2 AFTER update on captura for each ROW
execute procedure atualizastatus();

create or replace trigger tg3 before update on captura for each ROW
execute procedure evolucaoPoke();

create or replace trigger tg4 AFTER INSERT on batalha_ginasio for each ROW
execute procedure add_insignia();



