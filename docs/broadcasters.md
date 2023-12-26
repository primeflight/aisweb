# Broadcasters

The data was collected from the official page of [Radiodifusoras Espaço Aéreo](https://aisweb.decea.mil.br/?i=espaco-aereo&p=radiod) 

```python
from aisweb import AISWEB

broadcasters = AISWEB().broadcasters()

print(broadcasters)
```