all: quimica

quimica: 
	chmod +x quimica.py
teste:
	./quimica.py < ./exemplos/1.in
	./quimica.py < ./exemplos/2.in
	./quimica.py < ./exemplos/3.in
	./quimica.py < ./exemplos/4.in
	./quimica.py < ./exemplos/5.in
	./quimica.py < ./exemplos/1valor10-2.in
	./quimica.py < ./exemplos/2valor101-2-7.in
	./quimica.py < ./exemplos/3valor11-2-3-4-5.in
	./quimica.py < ./exemplos/4valor18-6-12-15.in	
clean:
	rm -r build/
	rm -r dist/
	rm quimica.spec
	rm quimica
