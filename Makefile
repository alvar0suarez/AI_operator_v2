# Curso CX + IA — tareas de construcción.
.DEFAULT_GOAL := ayuda
PY := python3

.PHONY: ayuda instalar dataset verificar validar glosario tutor sitio sitio-build todo limpiar

ayuda:  ## Muestra esta ayuda
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'

instalar:  ## Instala las dependencias de construcción
	$(PY) -m pip install -r requirements.txt

dataset:  ## Genera el gemelo sintético (semilla fija, reproducible)
	$(PY) scripts/generar-dataset.py

verificar:  ## Comprueba que las 5 verdades escondidas siguen siendo derivables
	$(PY) scripts/verificar-verdades.py

validar:  ## Valida el grafo de nodos: ciclos, referencias, alcanzabilidad
	$(PY) scripts/validar-grafo.py

glosario:  ## Regenera el glosario navegable desde glosario.yml
	$(PY) scripts/generar-glosario.py

sitio:  ## Ensambla y levanta el sitio en local con recarga automática
	$(PY) scripts/construir-sitio.py
	cd sitio && mkdocs serve

sitio-build:  ## Construye el sitio estático y comprueba que SOLUCIONES/ no entra
	$(PY) scripts/construir-sitio.py
	cd sitio && mkdocs build --strict
	@$(PY) scripts/comprobar-build.py

tutor:  ## Reempaqueta el contexto del tutor y pasa sus pruebas
	$(PY) scripts/empaquetar-tutor.py
	cd tutor/serverless && node --test "pruebas/*.test.mjs"

todo: validar verificar glosario tutor sitio-build  ## Todas las comprobaciones

limpiar:  ## Borra artefactos de build
	rm -rf sitio/build .cache
	find . -name '__pycache__' -type d -prune -exec rm -rf {} +
