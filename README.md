# Admin Codeflix


> ## Repositório do curso Full Cycle 3.0

Microsserviço: Administração do Catálogo de vídeos com Python ( Back-end )

Com DDD e Clean Architecture

> ## Metodologias e Designs

* DDD
* Code Review
* PR Request Template
* Conventional Commits
* CI
* Observabilidade


> ## Bibliotecas e Ferramentas

* Autopep8
* Pylint
* pytest
* Django
* DRF (Django Rest Framework)
* Git
* Github Actions
* Docker
* SonarCloud
* ELK Stack
* Prometheus
* Grafana
* OpenTelemetry



Documentação em andamento...


(obs): documentar docker extra.host

> ## Instação

Rodar o docker-compose
``` 
docker-compose up -d
```

> ## Testes

```
python -m unittest core.category.tests.unit.domain.test_unit_entities
```

```
python -m unittest core.__seedwork.tests.unit.domain.test_unit_repository
```
